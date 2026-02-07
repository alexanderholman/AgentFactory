# Workflow: OpenCode Agent Memory

## Workflow ID
opencode-agent-memory-001

## Purpose
Standardize how OpenCode sessions initialize continuity memory, validate wiring, and maintain linked memory events during execution.

## Sequence
1. Install AgentMemory CLI (`memlog`) and verify `PATH` availability.
2. Run `memlog doctor` to validate environment wiring.
3. Run `memlog validate` before and after substantial runs.
4. During action-phase, log events with `memlog log` using `agent_id`, `session_id`, and `event_type`.
5. At handoff/review, load recent memory context with `memlog load` and include links in output.

## Inputs/Outputs
- Inputs: workspace root, session id, agent id, action context, tool output summaries
- Outputs: linked markdown continuity graph in `memory/` and `actions/`, plus validation status

## Validation
- `memlog doctor --root ~/opencode --strict` returns success
- `memlog validate --root ~/opencode --strict` returns success
- Logged events include action links and memory_uuid references
