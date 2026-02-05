# GitHub Copilot Agent Integration Guide

## Overview
This document explains how AgentFactory integrates with GitHub Copilot and GitHub Copilot Workspace to provide enhanced AI agent capabilities.

## What is AgentFactory?
AgentFactory is a framework for defining, documenting, and managing AI agents using a flexible flat-file structure. It provides:
- Standardized agent definitions with required documentation
- Validation tools to ensure consistency
- Append-only logs for specifications and decisions
- A proven pattern for AI agent collaboration

## GitHub Copilot Integration

### Workspace Agent Integration
GitHub Copilot Workspace can leverage AgentFactory's agent definitions to:

1. **Understand Agent Roles and Capabilities**
   - Read agent definitions from the `agents/` directory
   - Understand the purpose, inputs, outputs, behavior, and constraints of each agent
   - Apply agent-specific patterns when working on related tasks

2. **Follow Established Patterns**
   - Respect the flexible file structure constraint (agents/ may be nested)
   - Maintain append-only logs (specs.md, decisions.md, agent_runs.md)
   - Use proper tagging conventions ([SPEC], [ASSUMPTION], [RISK], etc.)
   - Enforce required headings in agent documentation

3. **Automated Validation**
   - GitHub Actions automatically validate agent definitions on PRs
   - The `validate_agents.sh` script ensures compliance with standards
   - All 22 validation tests must pass before merging

### Copilot Instructions File
The `.github/copilot-instructions.md` file provides context to GitHub Copilot Workspace about:
- Repository architecture and key principles
- Required agent file format and structure
- Development workflow and constraints
- What Copilot must/must not do when working with this repository

## Using Copilot with AgentFactory

### Creating New Agents with Copilot
When asking Copilot to create a new agent:

1. **Specify the agent's purpose clearly**
   ```
   "Create a new agent called DataValidator that validates data schemas"
   ```

2. **Copilot will automatically:**
   - Create the agent file with all required headings (Purpose, Inputs, Outputs, Behavior, Constraints)
   - Add an entry to `agents.yaml` with proper metadata
   - Use appropriate tags from the allowed list
   - Follow the flexible file structure
   - Generate a unique agent ID

3. **Verify the result:**
   ```bash
   ./validate_agents.sh
   ```

### Modifying Existing Agents with Copilot
When asking Copilot to modify an agent:

1. **Be specific about what to change**
   ```
   "Update the Builder agent to add support for Python packaging"
   ```

2. **Copilot will:**
   - Preserve the required heading structure
   - Update the relevant sections only
   - Maintain the existing format and style
   - Document the change appropriately

3. **Add a decision entry:**
   ```
   "Add a decision entry to decisions.md explaining why we added Python packaging support"
   ```

### Working with Append-Only Files
Copilot understands that certain files are append-only:

**Correct Usage:**
```
"Add a new specification to specs.md for data validation requirements"
```
- Copilot will append the new spec at the end of the file
- Existing specs will remain unchanged

**Incorrect Usage (will be prevented):**
```
"Modify the existing SPEC-001 in specs.md"  ❌
```
- Copilot will refuse to modify existing append-only content
- It will suggest appending an updated version instead

## Agent Collaboration Patterns

### The Agent Factory Workflow
AgentFactory defines several agents that work together:

1. **Architect** - Converts user goals into testable specs
2. **Builder** - Implements artifacts from specs
3. **Skeptic** - Reviews and finds edge cases
4. **Editor** - Improves clarity and structure
5. **ProjectManager** - Coordinates and packages work
6. **CitationOfficer** - Audits evidence and claims
7. **ChatGPT** - Generalist execution agent

### Using Copilot to Orchestrate Agents
You can ask Copilot to simulate the agent workflow:

```
"Act as the Architect agent and create a spec for a user authentication system"
```

Copilot will:
- Follow the Architect agent's defined behavior
- Use the specified inputs and outputs format
- Respect the constraints defined in Architect.md
- Produce a spec following the proper format

## Best Practices with Copilot

### Do's ✓
- **Use Copilot to create new agent definitions** following the template
- **Ask Copilot to validate** changes before committing
- **Let Copilot help** with documentation and spec writing
- **Use Copilot to run** validation scripts and interpret results
- **Ask Copilot to explain** existing agent definitions and their purpose

### Don'ts ✗
- **Don't ask Copilot to circumvent** the flat-file structure
- **Don't ask Copilot to modify** append-only files (it will append instead)
- **Don't ask Copilot to fabricate** citations or test results
- **Don't ask Copilot to remove** required headings from agent files
- **Don't ask Copilot to create** agent files outside `agents/`

## Example Copilot Prompts

### Creating a New Agent
```
"Create a new agent called SecurityAuditor in the agents/ directory. 
It should audit code for security vulnerabilities.
Follow the required heading structure from agents.md."
```

### Adding a Specification
```
"Add a new specification to specs.md (append-only) for 
implementing two-factor authentication. Follow the spec format 
from existing entries."
```

### Validating Changes
```
"Run the validation script and explain any failures"
```

### Understanding an Agent
```
"Explain what the Builder agent does and how it differs from the Architect agent"
```

### Documenting a Decision
```
"Add an entry to decisions.md explaining why we chose to use 
flat file structure instead of a database"
```

## Validation and Quality Assurance

### Automated Validation
GitHub Actions automatically runs validation on:
- All PRs that modify agent files
- Pushes to main/develop branches
- Manual workflow dispatch

The workflow validates:
- File structure (agents/ path correctness)
- Required headings in agent files
- Unique agent IDs
- Proper tag usage
- File existence and format

### Manual Validation
Run validation locally:
```bash
./validate_agents.sh
```

Expected output:
```
======================================
Agent Factory Validation Suite
======================================

=== SPEC-001: File Structure ===
✓ PASS: TEST-001-1

=== SPEC-002: Agent File Format ===
✓ PASS: TEST-002-1 (all agents)

=== SPEC-003: Tags and Metadata ===
✓ PASS: TEST-003-1
✓ PASS: TEST-003-2
✓ PASS: TEST-003-3

======================================
Total tests run: 22
Passed: 22
All tests passed!
======================================
```

## Troubleshooting

### Common Issues

**Issue: Validation fails on heading order**
```
✗ FAIL: TEST-002-1: Verify required headings in MyAgent.md
```
**Solution:** Ensure headings appear in this exact order:
1. ## Purpose
2. ## Inputs
3. ## Outputs
4. ## Behavior
5. ## Constraints

**Issue: Missing agent file**
```
✗ FAIL: Missing file: agents/quality/Tester.md
```
**Solution:** Ensure the file exists at the path defined in agents.yaml (subdirectories allowed).

**Issue: Duplicate agent ID**
```
✗ FAIL: Duplicate IDs found in agents.yaml
```
**Solution:** Ensure each agent has a unique ID in the format `agent-name-###`.

## Contributing

When contributing agent definitions or modifications:

1. Read [CONTRIBUTING.md](/.github/CONTRIBUTING.md)
2. Follow the [CODE_OF_CONDUCT.md](/CODE_OF_CONDUCT.md)
3. Use Copilot to help create well-structured contributions
4. Run validation before submitting PR
5. Document decisions in `decisions.md`

## Resources

- [agents.md](/agents.md) - Agent documentation rules and templates
- [agents.yaml](/agents.yaml) - Agent configuration schema
- [specs.md](/specs.md) - Technical specifications (append-only)
- [decisions.md](/decisions.md) - Design decisions (append-only)
- [.github/copilot-instructions.md](/.github/copilot-instructions.md) - Copilot workspace context

## License
See [LICENSE](/LICENSE) for usage rights and restrictions.
