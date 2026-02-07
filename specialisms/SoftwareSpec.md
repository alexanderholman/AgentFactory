<!-- filename: SoftwareSpec.md -->

## [SPEC] Specialism Addendum - SoftwareSpec (v1.0)

### Purpose
Defines standards for specifying software systems that are implementable, testable, and reproducible.

### Operating Rules
- Translate goals into explicit requirements (MUST/SHOULD/MAY).
- Define interfaces first: CLI/API, config schema, and file contracts.
- Include validation gates: unit/integration checks, reproducibility checks, and failure handling.
- Keep runtime portability explicit across local, Colab, Docker, OpenCode, and HPC contexts.
- Record assumptions and unresolved risks.

### Outputs (typical)
- architecture spec
- task breakdown with dependencies
- interface contracts
- test/validation plan
- migration plan for legacy assets

### Quality Gates (SoftwareSpec)
- Requirements are unambiguous and testable.
- Inputs/outputs and paths are explicit.
- Execution path from raw inputs to final artifacts is reproducible.
- Security baseline is included (auth, secret handling, backup posture).

### [TEST] Acceptance Checks
- A builder can implement without follow-up clarification.
- A tester can verify pass/fail against stated criteria.
