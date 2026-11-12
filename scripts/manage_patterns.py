"""Search, validate and package the generator's offline pattern references."""

import argparse
from collections import Counter
from datetime import date
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlparse
import zipfile


ROOT = Path(__file__).resolve().parent.parent
LIBRARY = Path("references") / "pattern-library" / "patterns.json"
TEXT_FIELDS = (
    "id", "name", "source_family", "source_url", "reviewed_on", "evidence",
    "evidence_note", "mechanism", "input", "response", "layout", "motion",
    "accessibility", "offline", "avoid", "licensing",
)
LIST_FIELDS = ("user_goals", "tags")
EVIDENCE = {"documentation", "source-inspection", "rendered-observation"}
FAMILIES = {"codrops", "react-bits"}


def validate_records(data, minimum=30):
    if not isinstance(data, dict) or type(data.get("schema_version")) is not int:
        raise ValueError("Library requires an integer schema_version.")
    if data["schema_version"] != 1 or not isinstance(data.get("patterns"), list):
        raise ValueError("Expected schema_version 1 and a patterns array.")
    records = data["patterns"]
    if len(records) < minimum:
        raise ValueError(f"Expected at least {minimum} patterns, found {len(records)}.")
    seen = set()
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("Each pattern must be an object.")
        for field in TEXT_FIELDS:
            if not isinstance(record.get(field), str) or not record[field].strip():
                raise ValueError(f"{record.get('id', '<unknown>')}: missing text field {field}.")
        for field in LIST_FIELDS:
            values = record.get(field)
            if not isinstance(values, list) or not values:
                raise ValueError(f"{record['id']}: {field} must be a nonempty array.")
            if any(not isinstance(value, str) or not value.strip() for value in values):
                raise ValueError(f"{record['id']}: invalid value in {field}.")
        identifier = record["id"]
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", identifier) or identifier in seen:
            raise ValueError(f"Invalid or duplicate pattern ID: {identifier}.")
        seen.add(identifier)
        if record["source_family"] not in FAMILIES or record["evidence"] not in EVIDENCE:
            raise ValueError(f"{identifier}: invalid source family or evidence label.")
        try:
            reviewed = date.fromisoformat(record["reviewed_on"])
        except ValueError as error:
            raise ValueError(f"{identifier}: invalid review date.") from error
        if reviewed.isoformat() != record["reviewed_on"] or reviewed > date.today():
            raise ValueError(f"{identifier}: review date must be ISO and not in the future.")
        url = urlparse(record["source_url"])
        if url.scheme != "https" or not url.hostname or url.username or url.password:
            raise ValueError(f"{identifier}: source must be an HTTPS URL without credentials.")
    return records


def read_library(root):
    data = json.loads((root / LIBRARY).read_text(encoding="utf-8"))
    return validate_records(data)


def search_records(records, query):
    terms = set(re.findall(r"[\w-]+", query.casefold()))
    if not terms:
        raise ValueError("Search requires at least one word.")
    results = []
    for record in records:
        text = " ".join(
            [record[field] for field in ("id", "name", "mechanism", "input", "response")]
            + record["user_goals"] + record["tags"]
        ).casefold()
        words = set(re.findall(r"[\w-]+", text))
        score = len(terms & words)
        if score:
            results.append((score, record))
    return [record for _, record in sorted(results, key=lambda item: (-item[0], item[1]["id"]))]


def package_files(root):
    files = [root / "SKILL.md", root / "NOTICE.md"]
    for folder in ("references", "licenses"):
        files.extend(path for path in (root / folder).rglob("*") if path.is_file())
    files.append(root / "scripts" / "manage_patterns.py")
    if any(not path.is_file() or path.is_symlink() for path in files):
        raise ValueError("Package inputs must be existing regular files, not symbolic links.")
    return sorted(files, key=lambda path: path.relative_to(root).as_posix())


def check(root):
    records = read_library(root)
    if {record["source_family"] for record in records} != FAMILIES:
        raise ValueError("Library must retain both Codrops and React Bits coverage.")
    for relative in (
        "references/pattern-library/INDEX.md",
        "references/pattern-library/MAINTENANCE.md",
        "scripts/manage_patterns.py",
    ):
        if not (root / relative).is_file():
            raise ValueError(f"Missing library resource: {relative}.")
    index = (root / "references" / "pattern-library" / "INDEX.md").read_text(encoding="utf-8")
    directory_ids = re.findall(r"^\| `([a-z0-9-]+)` \|", index, re.MULTILINE)
    if len(directory_ids) != len(set(directory_ids)) or set(directory_ids) != {
        record["id"] for record in records
    }:
        raise ValueError("Pattern index directory must list each stored ID exactly once.")
    for path in [root / "SKILL.md", *list((root / "references").rglob("*.md"))]:
        for link in re.findall(
            r"`((?:references/|licenses/|scripts/)[^`\n]+)`",
            path.read_text(encoding="utf-8"),
        ):
            if not (root / link).exists():
                raise ValueError(f"{path.name}: missing local reference {link}.")
    return records


def rebuild(root):
    records = check(root)
    readme_path = root / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    evaluations = json.loads((root / "evals" / "evals.json").read_text(encoding="utf-8"))
    files = package_files(root)
    replacements = (
        (r"ZIP containing \d+ files", f"ZIP containing {len(files)} files"),
        (r"contains \d+ evaluation prompts", f"contains {len(evaluations['evals'])} evaluation prompts"),
        (r"\*\*\d+ curated patterns\*\*", f"**{len(records)} curated patterns**"),
    )
    for expression, replacement in replacements:
        readme, count = re.subn(expression, replacement, readme)
        if count != 1:
            raise ValueError(f"README requires exactly one count marker: {expression}.")
    if len(re.findall(r"(?m)^[0-9a-f]{64}$", readme)) != 1:
        raise ValueError("README requires exactly one SHA-256 marker.")
    archive = root / "dist" / "interactive-experience-generator.skill"
    archive.parent.mkdir(parents=True, exist_ok=True)
    temporary = archive.with_suffix(".skill.tmp")
    try:
        with zipfile.ZipFile(temporary, "w", compression=zipfile.ZIP_DEFLATED) as output:
            for path in files:
                entry = zipfile.ZipInfo(
                    "interactive-experience-generator/" + path.relative_to(root).as_posix(),
                    date_time=(2026, 11, 12, 0, 0, 0),
                )
                entry.compress_type = zipfile.ZIP_DEFLATED
                entry.external_attr = 0o644 << 16
                output.writestr(entry, path.read_bytes())
        with zipfile.ZipFile(temporary) as output:
            if output.testzip() is not None or len(output.namelist()) != len(files):
                raise ValueError("Archive integrity or file-count check failed.")
            for path in files:
                name = "interactive-experience-generator/" + path.relative_to(root).as_posix()
                if output.read(name) != path.read_bytes():
                    raise ValueError(f"Archive differs from source: {name}.")
        digest = hashlib.sha256(temporary.read_bytes()).hexdigest()
        readme = re.sub(r"(?m)^[0-9a-f]{64}$", digest, readme)
        temporary.replace(archive)
        with readme_path.open("w", encoding="utf-8", newline="\n") as output:
            output.write(readme)
    finally:
        if temporary.exists():
            temporary.unlink()
    print(f"Packaged and byte-verified {len(files)} files; SHA-256 {digest}.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--check", action="store_true", help="Validate local library records and references.")
    action.add_argument("--search", metavar="WORDS", help="Search stored pattern mechanisms and visitor needs.")
    action.add_argument("--package", action="store_true", help="Validate, rebuild the archive and update README metadata.")
    args = parser.parse_args()
    try:
        if args.package:
            rebuild(ROOT)
        else:
            records = check(ROOT)
            if args.search is not None:
                results = search_records(records, args.search)
                if not results:
                    print("No stored match. Choose another query or design an original mechanism.")
                for record in results[:8]:
                    print(f"{record['id']}: {record['name']}")
                    print(f"  {record['mechanism']}")
                    print(f"  {record['source_url']} ({record['evidence']}, {record['reviewed_on']})")
            else:
                print(f"Validated {len(records)} patterns: {dict(Counter(r['source_family'] for r in records))}.")
    except (ValueError, OSError, zipfile.BadZipFile) as error:
        print(f"Pattern library error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
