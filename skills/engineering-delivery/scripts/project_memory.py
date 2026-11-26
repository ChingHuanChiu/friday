#!/usr/bin/env python3
"""Resolve project-scoped role memory; initialize only when explicitly requested."""

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path


ROLES = ("architect", "developer", "reviewer", "verifier")


def project_state(repository, root):
    repository = Path(repository).expanduser().resolve(strict=True)
    if not repository.is_dir():
        raise ValueError("repository must be a directory")
    identity = repository
    try:
        result = subprocess.run(
            ["git", "-C", str(repository), "rev-parse", "--path-format=absolute", "--git-common-dir"],
            capture_output=True, text=True, check=False,
        )
    except FileNotFoundError:
        result = None
    if result is not None and result.returncode == 0:
        identity = Path(result.stdout.strip()).resolve(strict=True)
    project = identity.parent if identity.name == ".git" else identity
    slug = re.sub(r"[^a-z0-9-]+", "-", project.name.lower()).strip("-")[:48] or "project"
    digest = hashlib.sha256(str(identity).encode()).hexdigest()[:16]
    project_id = f"{slug}-{digest}"
    root = Path(root).expanduser()
    if not root.is_absolute():
        raise ValueError("projects root must be absolute")
    directory = root.resolve() / project_id
    return {
        "project_id": project_id,
        "identity": str(identity),
        "directory": str(directory),
        "memory": {role: str(directory / "memory" / f"{role}.md") for role in ROLES},
        "tasks": str(directory / "tasks"),
    }


def initialize(state):
    Path(state["tasks"]).mkdir(parents=True, exist_ok=True)
    for role, name in state["memory"].items():
        path = Path(name)
        path.parent.mkdir(parents=True, exist_ok=True)
        try:
            with path.open("x", encoding="utf-8") as memory:
                memory.write(f"# {role.capitalize()} memory\n\nProject: {state['project_id']}\n")
        except FileExistsError:
            pass


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository")
    parser.add_argument("--root", default=str(Path.home() / ".config/friday/projects"))
    parser.add_argument("--init", action="store_true", help="create missing memory files without overwriting")
    args = parser.parse_args()
    try:
        state = project_state(args.repository, args.root)
        if args.init:
            initialize(state)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Project memory unavailable: {error}\n")
    print(json.dumps(state, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
