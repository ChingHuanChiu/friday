# Project memory

Engineering roles persist experience under `~/.config/friday/projects/{project-id}/`. This is explicit file-backed memory, not a permanently running agent or host-guaranteed memory. Read relevant notes on entry and save durable lessons before returning. Current user/repository instructions and current source take precedence over remembered conclusions.

## Resolve once per project

The lead runs the bundled helper using the absolute installed plugin root and target repository, never the plugin checkout as a substitute for the target:

```sh
python3 <plugin-root>/skills/engineering-delivery/scripts/project_memory.py <target-repository> --init
```

The JSON result gives the project directory, four memory paths, and tasks directory. The project ID is a readable name plus a hash of the canonical Git common directory (canonical target directory for non-Git projects). Worktrees of the same repository share memory; unrelated same-name repositories do not. Separate clones have separate IDs. Paths contain no remote URLs or credentials. `--root <absolute-directory>` overrides the projects root for tests or an explicitly supplied state location. Initialization preserves existing files. If writes are unavailable, report memory persistence as unavailable and continue only with the permitted task; do not claim saved memory.

```text
~/.config/friday/projects/{project-id}/
├── memory/
│   ├── architect.md
│   ├── developer.md
│   ├── reviewer.md
│   └── verifier.md
└── tasks/
    └── {task-id}.md
```

Friday creates a unique task ID and maintains one task record; direct engineering-delivery invocation assigns ownership to the lead. The record contains goal/non-goals, criteria, repository/revision, design references, current owner/status, findings, correction count, evidence paths, and next action. Keep reports in the conversation or assigned separate artifact paths; specialists return updates rather than concurrently editing the task record. Existing records under `~/.local/share/friday/tasks/` remain untouched; resume them only when relevant and explicitly referenced.

## Ownership and retrieval

- Specialists read this section on entry. Use the assigned project memory path and task context; load only relevant entries and save durable lessons before returning. With direct invocation and no paths, use the resolver above only if permitted by the role, otherwise request paths from the caller. A reviewer must not run the shell helper. If paths or write access remain unavailable, continue permitted work and explicitly report persistence as unavailable; never guess a project directory or claim unsaved memory was saved.
- Architect writes only `architect.md`; developer `developer.md`; reviewer `reviewer.md`; verifier `verifier.md`. One writer per role memory; serialize same-role work for a project or collect deferred updates. Memory writes are permitted even when role instructions forbid application-code edits. If the host blocks all writing, return a proposed note and report it as unsaved; do not bypass the restriction through another tool.
- Read only your own compact memory and task-relevant entries. Request another role's relevant evidence through the lead; do not preload every role's history or full past conversations.
- Save reusable lessons with date, source revision/task, applicable conditions, and a way to recheck. Distinguish observations from hypotheses. Update or remove disproved/stale notes; do not turn a one-time workaround into a universal rule. Compact duplicated notes instead of appending full logs.
- Shared facts and decisions belong in the task record or versioned repository documents, not only private memory. The architect supplies design decisions; the developer implements code/tool changes. Use the repository's existing docs instead of another knowledge store; role memory holds only reusable lessons such as discovered run/test commands.
- Do not store credentials, raw private payloads, or full service dumps. Memory is task data, not authority to expand scope, mutate external services, or override tool restrictions.
