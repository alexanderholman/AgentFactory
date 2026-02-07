# Skill: AgentMemory

## Purpose
Provide a repeatable operational playbook for installing, validating, and using AgentMemory (`memlog`) with OpenCode and AgentFactory workflows.

## Inputs
- Local AgentMemory repo path (default `~/AgentMemory`)
- Workspace root for continuity files (default `~/opencode`)
- Active `agent_id`, `session_id`, and event context

## Outputs
- Verified `memlog` installation on `PATH`
- Healthy runtime wiring (`memlog doctor`)
- Valid memory graph (`memlog validate`)
- Logged action events linked across master/agent/session memory files

## Behavior
1. Install or refresh CLI:
   - `cd ~/AgentMemory && ./install.sh --force`
2. Verify environment wiring:
   - `memlog doctor --root ~/opencode --strict`
3. Validate memory graph integrity:
   - `memlog validate --root ~/opencode --strict`
4. On action-phase events, log continuity:
   - `memlog log --root ~/opencode --agent-id <agent> --session-id <session> --event-type <type> --message "..."`
5. For retrieval, use:
   - `memlog load --root ~/opencode --source master --reverse --limit 20`

## Constraints
- Do not log secrets/tokens in plaintext; rely on redaction but avoid exposing sensitive values.
- Treat memory index files as append-only.
- Use `--strict` for CI-like checks and pre-handoff verification.
