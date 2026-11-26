---
name: engineering-delivery
description: Coordinate software delivery through an engineering lead, a design-only system architect, developer self-verification, independent review, and runtime acceptance.
---

# Engineering delivery

Read [team rules](../friday/references/team.md). Act as engineering lead in the current context; own scope, dispatch, handoffs, correction limits, and delivery evidence. The architect owns design and the developer owns code changes; do not do their work yourself when they are available. Confirm the target repository, existing changes, constraints, and observable acceptance criteria.

Read [engineering principles](references/engineering-principles.md) on entry and pass applicable numbered clauses through specialist handoffs and correction rounds. Other workflows do not load them; role memory cannot override them.

## Select specialists

Use [team.json](../friday/team.json) to locate independent role instructions. Claude uses registered agents; Codex uses separate generic contexts with the same files. Load only selected roles.

| Work | Default team |
|---|---|
| Low-risk docs/configuration | Developer and relevant checks; add independent checks when required. |
| Ordinary bug/feature | Developer + reviewer; add verifier for risk or incomplete actual-artifact evidence. |
| Architecture, cross-module, high-risk | All four specialists. |
| Advice-only | Architect; reviewer for feasibility assessment when needed. No implementation. |
| Code/project review | Reviewer only, at the given range or current HEAD. Split large repositories by module across at most three reviewers, each given only its module. No implementation unless requested. |

Use existing architecture for small changes. Do not duplicate specialist analysis or launch every role by default.

Pass the matching required steps in each handoff:

- **Bug:** reproduce first and add a failing check before fixing; list at least two candidate causes and rule them out with evidence.
- **Refactor:** behavior unchanged; the same checks pass before and after.
- **Performance:** measure before and after in the same environment.
- **Investigation:** developer for runtime causes or architect for design questions; read-only, return an evidenced explanation, no implementation.

## Delivery loop

1. **Design:** The [architect](../../agents/friday-system-architect.md) supplies an evidenced design, interfaces, tradeoffs, implementation scope, and acceptance checks for the assigned revision. It writes design documents/specifications only, never code/tests/tools. Advice-only work stops here unless assessment was requested.
2. **Build:** The [developer](../../agents/friday-developer.md) investigates causes, implements, and runs its own check/run/fix loop. It implements needed APIs, lint, tests, and tools, using the project's documented run/test commands (README, AGENTS.md, CI config) and recording newly found ones in role memory. Design blockers return to the lead; the developer does not redesign alone.
3. **Review:** Give the independent [reviewer](../../agents/friday-reviewer.md) a fixed patch/base or revision with paths (it reads source itself), design, criteria, and check results; pause shared-tree writers. It classifies issues: implementation to developer, confirmed design problems to architect, unclear requirements to lead/user. It does not implement fixes.
4. **Verify:** When required, the independent [verifier](../../agents/friday-verifier.md) checks requirements against the exact reviewed build with authorized environment/data. Failures return to the lead. Changed artifacts need affected review and acceptance rerun; old passes do not cover new revisions.
5. **Deliver:** Inspect the integrated patch and acceptance evidence. Report changes, exact checks/results, blockers, and pending checks. Distinguish local edits, reviewed revisions, installed/deployed versions, and verified post-release behavior. Missing checks are not passes; implementation alone does not authorize merge, deployment, publishing, or messages.

Classify developer blockers and verifier failures from their evidence: send clear implementation defects straight back to the developer and product questions to the user. Ask the reviewer only when the cause is unclear or a design flaw is suspected; send confirmed design issues to the architect.

Keep reviewer and verifier contexts independent of implementation; self-tests or design advice do not count as independent review. Stop after two unsuccessful correction rounds for the same issue by default: record evidence and reassess cause/design rather than cycling. Product decisions go to the user. Define rollout/rollback and post-release checks when shipping requires them; reported regressions re-enter this loop without implying background monitoring.

## Handoffs and memory

Resolve [project memory](references/memory.md) once. Friday owns the shared task record when coordinating; the lead owns it for direct invocation. Specialists write only their own memory and assigned artifacts within role limits.

Pass goal, revision/snapshot, absolute plugin/target paths, selected role instructions/tool restrictions, relevant preferences/team rules, design/criteria, applicable principles, owned files/worktree, authorization, report/memory paths, and stopping condition. Use compact evidence references rather than full conversations. Start sequentially; parallelize only independent work with isolated artifacts. Reuse the developer's context across correction rounds. Start reviewers and verifiers fresh each round with only the original brief, new revision, prior findings, and changed range, so they stay independent without rereading the whole task.

Use native agents, never another host's CLI. The lead runs in the main context and dispatches specialists directly; specialists never delegate. If delegation is unavailable, perform only permitted combined-role work, label it single-agent, and report required independent checks as pending; never impersonate separate workers. Collect results and release workers through supported controls.

## Improve the environment

For recurring defects, ask the architect whether API/module design can remove the mistake; have the developer implement agreed restrictions, regression checks, or verification tools and clean up relevant misleading examples within scope. Review/verify normally. Use formal/property checks when justified. Establish a reliable inner loop before adding parallelism or automated release/repair loops.
