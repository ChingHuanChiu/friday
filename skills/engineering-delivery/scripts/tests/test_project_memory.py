import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path


spec = importlib.util.spec_from_file_location(
    "project_memory", Path(__file__).resolve().parents[1] / "project_memory.py"
)
memory = importlib.util.module_from_spec(spec)
spec.loader.exec_module(memory)


class ProjectMemoryTests(unittest.TestCase):
    def test_project_isolation_and_non_destructive_initialization(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            first = base / "a" / "same-name"
            second = base / "b" / "same-name"
            first.mkdir(parents=True)
            second.mkdir(parents=True)
            root = base / "state"
            state = memory.project_state(first, root)
            self.assertNotEqual(state["project_id"], memory.project_state(second, root)["project_id"])
            self.assertFalse(root.exists())
            memory.initialize(state)
            saved = Path(state["memory"]["developer"])
            saved.write_text("Existing lesson\n")
            memory.initialize(state)
            self.assertEqual(saved.read_text(), "Existing lesson\n")
            self.assertTrue(all(Path(path).is_file() for path in state["memory"].values()))
            self.assertTrue(Path(state["tasks"]).is_dir())
            self.assertFalse(Path(memory.project_state(second, root)["directory"]).exists())

    def test_git_worktree_subdirectory_and_symlink_share_identity(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            repo, worktree, alias = base / "repo", base / "worktree", base / "alias"
            subprocess.run(["git", "init", "-q", str(repo)], check=True)
            subprocess.run(
                ["git", "-C", str(repo), "-c", "user.name=Test", "-c", "user.email=test@example.invalid",
                 "-c", "commit.gpgsign=false", "commit", "-q", "--allow-empty", "-m", "fixture"],
                check=True,
            )
            subprocess.run(["git", "-C", str(repo), "worktree", "add", "-q", "-b", "fixture", str(worktree)], check=True)
            (worktree / "subdir").mkdir()
            alias.symlink_to(repo, target_is_directory=True)
            expected = memory.project_state(repo, base / "state")
            for target in (worktree, worktree / "subdir", alias):
                self.assertEqual(memory.project_state(target, base / "state"), expected)

    def test_invalid_paths_do_not_initialize(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            with self.assertRaises(ValueError):
                memory.project_state(base, "relative-root")
            with self.assertRaises(FileNotFoundError):
                memory.project_state(base / "missing", base / "state")
            file = base / "file"
            file.touch()
            with self.assertRaises(ValueError):
                memory.project_state(file, base / "state")
            self.assertFalse((base / "state").exists())


if __name__ == "__main__":
    unittest.main()
