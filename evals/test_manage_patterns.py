import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import zipfile


ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location(
    "manage_patterns", ROOT / "scripts" / "manage_patterns.py"
)
manager = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(manager)


class PatternLibraryTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / manager.LIBRARY).read_text(encoding="utf-8"))

    def test_incomplete_or_duplicate_records_cannot_be_packaged(self):
        broken = copy.deepcopy(self.data)
        broken["patterns"][1]["id"] = broken["patterns"][0]["id"]
        with self.assertRaisesRegex(ValueError, "duplicate pattern ID"):
            manager.validate_records(broken)
        broken = copy.deepcopy(self.data)
        del broken["patterns"][0]["licensing"]
        with self.assertRaisesRegex(ValueError, "missing text field licensing"):
            manager.validate_records(broken)

    def test_unrecognised_evidence_and_private_source_urls_are_rejected(self):
        broken = copy.deepcopy(self.data)
        broken["patterns"][0]["evidence"] = "looks-smooth"
        with self.assertRaisesRegex(ValueError, "evidence label"):
            manager.validate_records(broken)
        broken = copy.deepcopy(self.data)
        broken["patterns"][0]["source_url"] = "https://name:secret@example.com/demo"
        with self.assertRaisesRegex(ValueError, "without credentials"):
            manager.validate_records(broken)

    def test_search_retrieves_visitor_goals_without_network(self):
        record = copy.deepcopy(self.data["patterns"][0])
        record["user_goals"] = ["compare alternatives"]
        self.assertEqual(
            manager.search_records([record], "compare alternatives"), [record]
        )
        self.assertEqual(manager.search_records([record], "unmatched-visitor-goal"), [])
        with self.assertRaisesRegex(ValueError, "at least one word"):
            manager.search_records([record], "!?")

    def test_package_is_reproducible_source_exact_and_excludes_evaluations(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for path in manager.package_files(ROOT):
                target = root / path.relative_to(ROOT)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(path.read_bytes())
            (root / "evals").mkdir()
            (root / "evals" / "evals.json").write_text(
                json.dumps({"evals": []}), encoding="utf-8"
            )
            (root / "README.md").write_text(
                "ZIP containing 0 files\ncontains 0 evaluation prompts\n"
                "**0 curated patterns**\n" + "0" * 64 + "\n",
                encoding="utf-8",
            )
            manager.rebuild(root)
            archive = root / "dist" / "interactive-experience-generator.skill"
            first = archive.read_bytes()
            manager.rebuild(root)
            self.assertEqual(first, archive.read_bytes())
            with zipfile.ZipFile(archive) as output:
                self.assertFalse(any("/evals/" in name for name in output.namelist()))
                self.assertFalse(any(name.endswith("/README.md") for name in output.namelist()))
                for path in manager.package_files(root):
                    name = "interactive-experience-generator/" + path.relative_to(root).as_posix()
                    self.assertEqual(output.read(name), path.read_bytes())


if __name__ == "__main__":
    unittest.main()
