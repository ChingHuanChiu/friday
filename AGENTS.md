# Development workflow

1. Inspect the working tree and preserve existing changes. Before editing, create a branch with `git switch -c <type>/<short-description>`. Do not initialize a repository or discard changes without a request.
2. Make the smallest change that meets the request. Edit role instructions in `agents/` and workflow behavior in `skills/<skill-name>/` directly. Both hosts use `skills/friday/SKILL.md` as the coordination entry point. Keep `skills/friday/` focused on coordination. Put role ownership and restrictions in `agents/`, reusable procedures in workflow skills, and conditional detail in their references. Edit source directly. Runtime data stays outside installed plugin caches.
3. Update `README.md` and `CHANGELOG.md` with each change. Keep documentation concise and in English. Keep installation, usage, and workflow instructions accurate.
4. Add each changelog entry at the top under exactly `## YYYY-MM-DD-index`, with no version suffix. Use the Asia/Taipei date. Start `index` at `1` each day and increment it for each new entry that day (for example, `2026-11-17-1`, then `2026-11-17-2`). Do not zero-pad the index or renumber existing correctly formatted entries.
5. Treat version `0.0` as the initial baseline. Do not reconstruct changes from before this baseline. When changing the plugin version, keep `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json`, and `skills/friday/team.json` in sync.
6. Check JSON syntax, documentation links, registry paths, and version consistency. Validate Claude manifests with:

   ```sh
   claude plugin validate .claude-plugin/plugin.json
   claude plugin validate --strict .claude-plugin/marketplace.json
   ```

7. For script changes, run the README test command. Never bundle credentials, virtual environments, or employer-specific hosts, repositories, or data.
8. Report the changes, checks run, and remaining limitations. Commit, publish, or update installed plugins only within the user's authorization.

`CLAUDE.md` imports this file for Claude Code. Keep all development instructions in `AGENTS.md`; do not add a separate `AGENT.md`. These are checkout development instructions, not installed-plugin runtime context. Plugin validation may warn that root `CLAUDE.md` is not runtime context; this is expected.
