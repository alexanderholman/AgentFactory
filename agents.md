# Agents Documentation

## Overview
This document defines the rules and structure for agent files in the Agent Factory repository. All agents MUST follow these rules to ensure consistency and maintainability.

## Rules for Agent Files

### MUST Requirements
1. **Flat File Structure**: All agent files MUST be stored as flat files in the repository root or a single-level `agents/` directory. No nested subdirectories are allowed.
   - **Test**: Verify no agent files exist in nested directories (depth > 1)
   - **Pass**: All agent files are at root or one level deep
   - **Fail**: Any agent file found in nested directories

2. **Required Headings**: All agent files MUST include the following headings in order:
   - `## Purpose` - What the agent does
   - `## Inputs` - What data/parameters the agent requires
   - `## Outputs` - What the agent produces
   - `## Behavior` - How the agent operates
   - `## Constraints` - Limitations and boundaries
   - **Test**: Parse markdown files and verify all headings are present
   - **Pass**: All required headings exist in the correct order
   - **Fail**: Any required heading is missing or out of order

3. **Tags**: All agent files MUST have at least one tag defined in the agents.yaml file
   - **Test**: Verify each agent in agents.yaml has tags array with at least one entry
   - **Pass**: All agents have 1+ tags
   - **Fail**: Any agent has zero tags

4. **Unique IDs**: All agents MUST have a unique identifier in agents.yaml
   - **Test**: Check for duplicate IDs in agents.yaml
   - **Pass**: All IDs are unique
   - **Fail**: Duplicate IDs found

5. **File Path Validation**: All agent file_path values in agents.yaml MUST point to existing files
   - **Test**: Check that all referenced files exist
   - **Pass**: All files exist
   - **Fail**: Any referenced file is missing

6. **No Fabrication**: Agent documentation MUST NOT fabricate citations, results, or data. All references MUST be verifiable.
   - **Test**: Manual review or citation validation
   - **Pass**: All citations are verifiable
   - **Fail**: Fabricated or unverifiable citations found

### SHOULD Requirements
1. **Descriptive Names**: Agent names SHOULD be descriptive and clearly indicate their purpose
2. **Version Control**: Agents SHOULD include semantic version numbers
3. **Examples**: Agent documentation SHOULD include usage examples
4. **Change History**: Changes to agents SHOULD be documented in CHANGELOG.md

### MAY Requirements
1. **Additional Metadata**: Agents MAY include additional custom metadata fields
2. **External Resources**: Agents MAY reference external documentation or resources
3. **Diagrams**: Agent documentation MAY include diagrams or flowcharts
4. **Performance Notes**: Agents MAY document performance characteristics

## Agent File Template

```markdown
# Agent Name

## Purpose
Describe what this agent does and why it exists.

## Inputs
- Input 1: Description and format
- Input 2: Description and format

## Outputs
- Output 1: Description and format
- Output 2: Description and format

## Behavior
Describe how the agent processes inputs to produce outputs.

1. Step 1
2. Step 2
3. Step 3

## Constraints
- Constraint 1: Description
- Constraint 2: Description

## Tags
Tags are defined in agents.yaml and help categorize this agent.

## Version History
- v1.0.0 (2026-01-28): Initial version
```

## Validation Process

To validate agent files, run the following checks:

1. **Structure Check**: Verify flat file structure
   ```bash
   find agents/ -mindepth 2 -type f && echo "FAIL: Nested files found" || echo "PASS"
   ```

2. **Heading Check**: Verify required headings exist in correct order
   ```bash
   for file in agents/*.md; do
     # Check presence of all required headings
     grep -q "## Purpose" "$file" && 
     grep -q "## Inputs" "$file" && 
     grep -q "## Outputs" "$file" && 
     grep -q "## Behavior" "$file" && 
     grep -q "## Constraints" "$file" || 
     echo "FAIL: Missing headings in $file"
     
     # Check heading order (Purpose < Inputs < Outputs < Behavior < Constraints)
     purpose_line=$(grep -n "^## Purpose" "$file" | cut -d: -f1)
     inputs_line=$(grep -n "^## Inputs" "$file" | cut -d: -f1)
     outputs_line=$(grep -n "^## Outputs" "$file" | cut -d: -f1)
     behavior_line=$(grep -n "^## Behavior" "$file" | cut -d: -f1)
     constraints_line=$(grep -n "^## Constraints" "$file" | cut -d: -f1)
     
     [ "$purpose_line" -lt "$inputs_line" ] && 
     [ "$inputs_line" -lt "$outputs_line" ] && 
     [ "$outputs_line" -lt "$behavior_line" ] && 
     [ "$behavior_line" -lt "$constraints_line" ] || 
     echo "FAIL: Headings out of order in $file"
   done
   ```

3. **YAML Validation**: Validate agents.yaml structure
   ```bash
   # Requires yq or similar YAML parser
   yq eval '.agents[].id' agents.yaml | sort | uniq -d | grep . && echo "FAIL: Duplicate IDs" || echo "PASS"
   ```

## Adding New Agents

To add a new agent:

1. Define the agent in `agents.yaml` with all required fields
2. Create the agent markdown file in the flat file structure
3. Ensure all required headings are present
4. Add appropriate tags from the allowed list
5. Run validation tests
6. Document the addition in `decisions.md`

## Modifying Existing Agents

When modifying agents:

1. Update the agent definition in `agents.yaml` if metadata changes
2. Update the markdown file with changes
3. Increment the version number
4. Document changes in the agent's version history
5. Record the decision in `decisions.md`

## Append-Only Files

The following files are **append-only** and MUST NOT have content removed or modified (only additions at the end):
- `specs.md` - Technical specifications and requirements
- `agent_runs.md` - Log of agent execution runs
- `decisions.md` - Architectural and design decisions

## Markdown Output Preference

All agent outputs and documentation SHOULD be in Markdown format for consistency and readability.
