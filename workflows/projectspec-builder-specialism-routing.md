# Workflow: ProjectSpec Builder-Specialism Routing

## Workflow ID
projectspec-builder-routing-001

## Purpose
Run ProjectSpec orchestration with Builder-only sub-agent delegation while enforcing the correct specialism selection.

## Sequence
1. Startup check: read `tasks/wip.md` and `tasks/triage.md` to recover active state and blockers.
2. Intake task in `ProjectSpec` and classify workstream (`software` or `academic_submission`).
3. Build a clarification queue of missing information needed for complete specification.
4. Ask one clarification question at a time and integrate each answer before asking the next.
5. Run a read-only Planner pass when task scope/ambiguity warrants planning support.
6. Select sub-agent profile:
   - `Builder + SoftwareSpec` for software/infrastructure/code work.
   - `Builder + AcademicSubmission` for manuscript/submission work.
7. Delegate execution to Builder sub-agent with selected specialism context.
8. ProjectSpec validates output against acceptance checks.
9. Update `tasks/wip.md` and `tasks/triage.md` before returning final output.
10. ProjectSpec returns integrated result and residual risks.

## Planner Invocation Rubric (Read-Only)
Invoke Planner when any condition is true:

- 3 or more distinct deliverables or workstreams.
- Cross-system impact (repo + infra + data + docs coupling).
- Ambiguous requirements likely to change architecture.
- High-risk changes (security, backup, data loss, production/HPC impact).
- Migration/refactor with legacy compatibility constraints.

Skip Planner when all are true:

- Single, localized change.
- Clear acceptance criteria already present.
- Low-risk and no cross-system dependency.

## Inputs/Outputs
- Inputs: objective, constraints, repo context, selected specialism file.
- Outputs: execution result, validation summary, next actions.

## Validation
- Planner pass is read-only and produced no side effects.
- Startup state was read from `tasks/wip.md` and `tasks/triage.md`.
- Clarification queue is exhausted (or unresolved items are tagged `[ASSUMPTION]`).
- Builder delegation starts only after blocking clarifications are resolved.
- Correct specialism was selected and referenced in the run summary.
- Output satisfies objective-specific acceptance checks.
- Assumptions are tagged `[ASSUMPTION]`.
