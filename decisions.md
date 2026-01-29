# Architectural and Design Decisions

**NOTE: This file is append-only. Do not modify or remove existing entries. Only add new decisions at the end.**

---

## Decision Record Format

Each decision entry MUST follow this format:

```
## [DEC-XXX] Decision Title
**Date**: YYYY-MM-DD
**Status**: Proposed | Accepted | Implemented | Superseded | Deprecated
**Decision Maker**: Name/Role

### Context
What is the situation and why do we need to make a decision?

### Decision
What did we decide to do and why?

### Alternatives Considered
- Alternative 1: Why it was not chosen
- Alternative 2: Why it was not chosen

### Consequences
- Positive consequence 1
- Positive consequence 2
- Negative consequence 1
- Trade-off 1

### Implementation Notes
How should this decision be implemented?

### Related Decisions
- Links to related decisions

### Related Specs
- Links to related specifications

---
```

## Purpose

This file maintains a record of all significant architectural and design decisions made in the Agent Factory project. This helps with:
- Understanding the rationale behind current design
- Avoiding revisiting settled questions
- Onboarding new team members
- Learning from past decisions

## Initial Decisions

---

## [DEC-001] Use Flat File Structure for Agent Repository
**Date**: 2026-01-28
**Status**: Accepted
**Decision Maker**: System Architect

### Context
The Agent Factory needs a file organization structure that is simple, maintainable, and easy to navigate. We must decide between a flat file structure vs. a hierarchical directory structure.

### Decision
Use a flat file structure where all agent files are stored at the root level or in a single `agents/` directory with no nested subdirectories.

### Alternatives Considered
- **Hierarchical Structure**: Organize agents in nested directories by category/type
  - Not chosen because it adds complexity and makes navigation harder
  - Can lead to debates about proper categorization
  - Makes file paths longer and more brittle
- **Database Storage**: Store agent data in a database
  - Not chosen because it requires additional infrastructure
  - Reduces transparency (can't easily browse in GitHub)
  - Makes version control more complex

### Consequences
- **Positive**: Simpler navigation and file discovery
- **Positive**: Easier to enforce naming conventions
- **Positive**: Works well with version control
- **Positive**: Reduces cognitive overhead
- **Negative**: May have many files in one directory as system grows
- **Trade-off**: Less organizational hierarchy, but compensated by tags and metadata

### Implementation Notes
- Store agent markdown files in flat `agents/` directory or root
- Use clear naming conventions for files
- Rely on tags in agents.yaml for categorization
- Enforce with validation tests

### Related Decisions
- DEC-002 (YAML Configuration)

### Related Specs
- SPEC-001 (File Structure)

---

## [DEC-002] Use agents.yaml for Agent Configuration
**Date**: 2026-01-28
**Status**: Accepted
**Decision Maker**: System Architect

### Context
We need a way to define agent metadata, configuration, and relationships. Options include YAML, JSON, TOML, or embedding in markdown frontmatter.

### Decision
Use a centralized `agents.yaml` file to define all agent metadata and configuration.

### Alternatives Considered
- **JSON Configuration**: Use agents.json
  - Not chosen because YAML is more human-readable
  - JSON doesn't support comments as easily
- **TOML Configuration**: Use agents.toml
  - Not chosen because YAML is more widely adopted in similar contexts
  - Team has more familiarity with YAML
- **Markdown Frontmatter**: Embed metadata in each agent file
  - Not chosen because it's harder to get a system-wide view
  - Makes validation and queries more complex

### Consequences
- **Positive**: Single source of truth for agent metadata
- **Positive**: Easy to validate schema
- **Positive**: Human-readable and editable
- **Positive**: Supports comments for documentation
- **Negative**: Requires keeping YAML in sync with markdown files
- **Trade-off**: Centralized vs. distributed metadata (chose centralized)

### Implementation Notes
- Define clear schema in agents.yaml
- Include validation rules in the file
- Reference agent markdown files via file_path
- Use YAML comments for inline documentation

### Related Decisions
- DEC-001 (Flat File Structure)
- DEC-003 (Required Headings)

### Related Specs
- SPEC-003 (Tags and Metadata)

---

## [DEC-003] Require Standardized Headings in Agent Files
**Date**: 2026-01-28
**Status**: Accepted
**Decision Maker**: System Architect

### Context
Agent documentation files need a consistent structure so users know what to expect and can find information easily.

### Decision
Require all agent files to include five specific headings in a defined order: Purpose, Inputs, Outputs, Behavior, and Constraints.

### Alternatives Considered
- **Freeform Documentation**: Let each agent define its own structure
  - Not chosen because it leads to inconsistency
  - Makes it harder to find information
  - Difficult to validate completeness
- **Minimal Requirements**: Only require one or two headings
  - Not chosen because it doesn't ensure sufficient documentation
  - Leaves too much ambiguity
- **More Extensive Requirements**: Require 10+ headings
  - Not chosen because it's too rigid
  - Creates unnecessary overhead for simple agents

### Consequences
- **Positive**: Consistent documentation structure
- **Positive**: Easy to validate
- **Positive**: Users know where to find information
- **Positive**: Forces thinking about key aspects of agent design
- **Negative**: May feel constraining for very simple agents
- **Trade-off**: Consistency vs. flexibility (chose consistency)

### Implementation Notes
- Document required headings in agents.md
- Create validation tests to check for headings
- Provide template in agents.md
- Allow additional headings beyond required ones

### Related Decisions
- DEC-002 (YAML Configuration)
- DEC-006 (Markdown Output)

### Related Specs
- SPEC-002 (Agent File Format)

---

## [DEC-004] Make specs.md, agent_runs.md, and decisions.md Append-Only
**Date**: 2026-01-28
**Status**: Accepted
**Decision Maker**: System Architect

### Context
Some files in the system need to maintain a complete historical record. We must decide whether to allow editing/deletion or enforce append-only behavior.

### Decision
Make specs.md, agent_runs.md, and decisions.md append-only files where content can only be added at the end, never modified or deleted.

### Alternatives Considered
- **Fully Editable Files**: Allow any modifications
  - Not chosen because it can lose historical context
  - Makes it harder to track what changed and why
  - Can lead to "rewriting history"
- **Version-Controlled Only**: Rely only on Git history
  - Not chosen because Git history can be complex to navigate
  - Having explicit append-only makes intent clearer
  - Provides an easy-to-read historical record
- **Separate Dated Files**: Create new files for each time period
  - Not chosen because it fragments information
  - Makes searching across time periods harder

### Consequences
- **Positive**: Preserves complete historical record
- **Positive**: Clear audit trail
- **Positive**: Prevents accidental loss of information
- **Positive**: Makes evolution of thinking visible
- **Negative**: Files will grow over time
- **Negative**: Can't fix typos in old entries
- **Trade-off**: Historical completeness vs. editability (chose history)

### Implementation Notes
- Add clear warnings at top of each append-only file
- Create validation tests to check git diffs
- Use horizontal rules to separate entries
- Include timestamps with each entry

### Related Decisions
- DEC-005 (No Fabrication)

### Related Specs
- SPEC-004 (Append-Only Files)

---

## [DEC-005] Enforce No Fabrication Rule
**Date**: 2026-01-28
**Status**: Accepted
**Decision Maker**: System Architect

### Context
Documentation and agent outputs must be trustworthy. We need to establish whether fabricated data or citations are acceptable.

### Decision
Prohibit fabrication of citations, results, or data. All information must be verifiable and accurate.

### Alternatives Considered
- **Allow Placeholders**: Permit example/dummy data
  - Partially accepted: placeholders OK if clearly marked as such
  - Not allowed for actual results or citations
- **Relaxed Policy**: Don't explicitly prohibit fabrication
  - Not chosen because it undermines trust
  - Can lead to confusion about what's real
  - Makes documentation less valuable

### Consequences
- **Positive**: Builds trust in documentation
- **Positive**: Ensures accuracy and reliability
- **Positive**: Makes information verifiable
- **Negative**: Requires more work to find real sources
- **Negative**: Can't use hypothetical examples as easily
- **Trade-off**: Convenience vs. accuracy (chose accuracy)

### Implementation Notes
- Document rule clearly in agents.md
- Include in validation requirements
- Manual review process for citations
- Mark placeholder data explicitly

### Related Decisions
- DEC-004 (Append-Only Files)

### Related Specs
- SPEC-005 (No Fabrication)

---

## [DEC-006] Prefer Markdown for All Output
**Date**: 2026-01-28
**Status**: Accepted
**Decision Maker**: System Architect

### Context
Agent outputs and documentation can use various formats. We need to standardize on a preferred format.

### Decision
Prefer Markdown format for all agent outputs, documentation, and reports.

### Alternatives Considered
- **Plain Text**: Use simple .txt files
  - Not chosen because it lacks formatting capabilities
  - Harder to structure complex information
- **HTML**: Use HTML for rich formatting
  - Not chosen because it's less human-readable in source form
  - More complex to write and maintain
- **Mixed Formats**: Allow each agent to choose format
  - Not chosen because it reduces consistency
  - Makes tooling more complex

### Consequences
- **Positive**: Consistent, readable format
- **Positive**: Great version control (text-based)
- **Positive**: Renders nicely on GitHub
- **Positive**: Wide tool support
- **Negative**: Limited formatting compared to rich formats
- **Trade-off**: Simplicity vs. rich formatting (chose simplicity)

### Implementation Notes
- Use .md extension for all documentation
- Follow CommonMark or GitHub Flavored Markdown
- Use code blocks with language specifiers
- Include examples in agents.md

### Related Decisions
- DEC-003 (Required Headings)

### Related Specs
- SPEC-006 (Markdown Preference)

---

## [DEC-007] Use MUST/SHOULD/MAY RFC 2119 Keywords
**Date**: 2026-01-28
**Status**: Accepted
**Decision Maker**: System Architect

### Context
Specifications need clear language to indicate requirement levels. We need a standard way to express mandatory vs. optional requirements.

### Decision
Use RFC 2119 keywords (MUST, SHOULD, MAY) to indicate requirement levels in all specifications and documentation.

### Alternatives Considered
- **Custom Keywords**: Create our own requirement levels
  - Not chosen because RFC 2119 is a well-known standard
  - Reinventing the wheel adds confusion
- **Natural Language Only**: Write requirements in plain English
  - Not chosen because it can be ambiguous
  - Harder to parse programmatically
- **Numeric Priorities**: Use P0, P1, P2 priority levels
  - Not chosen because it doesn't convey nature of requirement
  - Less intuitive for requirement specifications

### Consequences
- **Positive**: Clear, unambiguous requirement levels
- **Positive**: Industry-standard terminology
- **Positive**: Easy to parse and validate
- **Positive**: Well-understood by developers
- **Negative**: Requires familiarity with RFC 2119
- **Trade-off**: Precision vs. natural language (chose precision)

### Implementation Notes
- Use MUST for mandatory requirements
- Use SHOULD for recommended but not mandatory
- Use MAY for optional features
- Document usage in specs.md
- Create tests for all MUST requirements

### Related Decisions
- DEC-008 (Test Requirements)

### Related Specs
- SPEC-001 through SPEC-006 (all use MUST/SHOULD/MAY)

---

## [DEC-008] Require Pass/Fail Tests for All MUST Requirements
**Date**: 2026-01-28
**Status**: Accepted
**Decision Maker**: System Architect

### Context
MUST requirements need to be verifiable. We need to decide how to ensure requirements are actually met.

### Decision
Require every MUST requirement to have at least one associated pass/fail test with clear criteria.

### Alternatives Considered
- **Manual Verification Only**: Check requirements manually
  - Not chosen because it's not scalable
  - Prone to human error
  - Hard to maintain consistency
- **Optional Tests**: Make tests recommended but not required
  - Not chosen because requirements without tests are often ignored
  - Can't verify compliance
- **Integration Tests Only**: Use end-to-end tests
  - Not chosen because they don't test individual requirements clearly
  - Harder to debug when failures occur

### Consequences
- **Positive**: Requirements are verifiable
- **Positive**: Clear acceptance criteria
- **Positive**: Can automate validation
- **Positive**: Reduces ambiguity
- **Negative**: Requires effort to write tests
- **Negative**: Some requirements may be hard to test automatically
- **Trade-off**: Effort vs. verifiability (chose verifiability)

### Implementation Notes
- Include test definition with each MUST requirement in specs.md
- Define clear pass and fail criteria
- Document test ID for tracking
- Automate tests where possible
- Manual tests OK if automation isn't feasible

### Related Decisions
- DEC-007 (MUST/SHOULD/MAY keywords)

### Related Specs
- All specs include test definitions

---

## [DEC-009] Agent Analysis and Expansion Recommendations
**Date**: 2026-01-28
**Status**: Proposed
**Decision Maker**: System Analysis / GitHub Copilot Agent

### Context
The initial Agent Factory system was established with 7 core agents and 3 specialisms. After analyzing the system's coverage, gaps were identified in critical areas including testing, security, deployment, documentation, integration, data modeling, and performance optimization. A comprehensive analysis was needed to recommend additions that would enhance the system's capability without over-complicating it.

### Decision
Recommend a phased approach to expanding the agent system with 7 new agents and 7 new specialisms, prioritized by impact and necessity:

**Phase 1 (High Priority - Immediate):**
- Tester Agent - for systematic test creation and validation
- SecurityReviewer Agent - for security analysis and compliance
- Security Specialism - security standards
- Testing Specialism - testing standards

**Phase 2 (Medium Priority - Next Quarter):**
- Deployer Agent - for deployment readiness
- DocWriter Agent - for user-facing documentation
- Integrator Agent - for API and integration design
- DataModeler Agent - for data architecture
- API Design Specialism
- Deployment Specialism
- Documentation Specialism

**Phase 3 (Low Priority - As Needed):**
- Optimizer Agent - for performance optimization
- Data Specialism
- Performance Specialism

### Alternatives Considered
- **Expand Existing Agents**: Add responsibilities to current agents
  - Not chosen because it would violate single responsibility principle
  - Would make agents too complex and harder to use
  - Each specialty requires dedicated focus

- **Create Mega-Agent**: Create one "Quality" agent to handle testing, security, performance
  - Not chosen because specialization is more effective
  - Would be too broad and lack deep expertise
  - Goes against the factory pattern philosophy

- **Minimal Expansion**: Only add 1-2 most critical agents
  - Not chosen because it leaves too many gaps
  - Would require revisiting expansion soon
  - Better to have comprehensive plan even if phased

- **Maximum Expansion**: Add 15+ agents covering every niche
  - Not chosen because it adds unnecessary complexity
  - Many niches don't have sufficient use cases yet
  - Can lead to confusion about which agent to use

### Consequences
**Positive:**
- Comprehensive coverage of software development lifecycle
- Specialized expertise in critical areas (testing, security)
- Better quality outputs with systematic validation
- Clearer separation of concerns
- Production-ready artifacts
- Enhanced security posture
- Better deployment support

**Negative:**
- More agents to learn and understand
- Increased coordination complexity
- More maintenance burden
- Steeper learning curve for new users
- Need to update documentation and tooling

**Trade-offs:**
- Completeness vs. Simplicity (chose completeness with phased approach)
- Specialization vs. Generalization (chose specialization)
- Immediate implementation vs. Phased rollout (chose phased)

### Implementation Notes

**For Each New Agent:**
1. Create agent definition file in agents/ directory
2. Follow required structure (Purpose, Inputs, Outputs, Behavior, Constraints)
3. Add entry to agents.yaml with unique ID
4. Tag appropriately with existing or new tags
5. Run validation: ./validate_agents.sh
6. Update integration documentation

**For Each New Specialism:**
1. Create specialism file in specialisms/ directory
2. Define purpose, operating rules, outputs, quality gates
3. Include test acceptance checks
4. Reference from appropriate agent definitions

**New Tags to Add:**
- security (for SecurityReviewer)
- quality (for Tester)
- performance (for Optimizer)
- data (for DataModeler)
- api (for Integrator)

**Workflow Integration:**
Update orchestration to support optional agent invocation based on artifact type and requirements.

**Documentation Updates:**
- Update agents.md with new agent patterns
- Update README.md with expanded agent list
- Create workflow diagrams showing agent interactions
- Update COPILOT_INTEGRATION.md with new agent capabilities

### Phased Rollout Strategy

**Phase 1 Success Criteria:**
- Tester and SecurityReviewer agents created and validated
- At least 2 test cases using new agents successfully completed
- Security and Testing specialisms documented
- No regression in existing agent functionality

**Phase 2 Entry Criteria:**
- Phase 1 agents proven valuable in practice
- User feedback incorporated
- Clear use cases for Phase 2 agents identified

**Phase 3 Entry Criteria:**
- Performance or data-heavy projects emerge
- Demonstrated need for optimization or data modeling

### Benefits and Mitigation

**Key Benefits:**
- **Quality**: Systematic testing and security review
- **Completeness**: All lifecycle stages covered
- **Scalability**: Can handle more complex projects
- **Trust**: Better validation and security

**Complexity Mitigation:**
- Phased rollout reduces learning curve
- Clear documentation of when to use each agent
- ProjectManager orchestrates, users don't need to know all agents
- Optional agents - only invoke what's needed

### Related Decisions
- DEC-001 (Flat File Structure) - New agents follow same pattern
- DEC-002 (YAML Configuration) - New agents defined in agents.yaml
- DEC-003 (Required Headings) - New agents use standard structure
- DEC-008 (Test Requirements) - Tester agent enhances this capability

### Related Specs
- SPEC-001 (File Structure) - New agents maintain flat structure
- SPEC-002 (Agent File Format) - New agents follow format
- SPEC-003 (Tags and Metadata) - New agents properly tagged

### Output Reference
- Detailed analysis: agent_recommendations.md
- Run log: agent_runs.md #002

---

## [DEC-010] Phase 1 Agent Implementation - Tester and SecurityReviewer
**Date**: 2026-01-29
**Status**: Implemented
**Decision Maker**: GitHub Copilot Agent / User Request

### Context
Following DEC-009 (Agent Expansion Recommendations), the user requested implementation of the recommendations starting with Phase 1 high-priority agents. Phase 1 focused on addressing critical gaps in testing and security that are currently handled ad-hoc by existing agents.

### Decision
Implement Phase 1 agents and specialisms as specified in agent_recommendations.md:
1. **Tester Agent** - Systematic test creation and validation
2. **SecurityReviewer Agent** - Security analysis and compliance
3. **Testing Specialism** - Testing standards and best practices
4. **Security Specialism** - Security standards and OWASP compliance

### Alternatives Considered
- **Implement All Phases at Once**: Create all 7 recommended agents
  - Not chosen because phased approach allows for validation and feedback
  - Too many changes at once increases risk
  
- **Extend Existing Agents**: Add testing and security to Skeptic/Builder
  - Not chosen because violates single responsibility principle
  - Specialized agents provide deeper expertise
  - Would make existing agents too complex

- **Wait for More Feedback**: Delay implementation pending additional review
  - Not chosen because user explicitly requested implementation
  - Phase 1 agents address critical, well-understood gaps

### Consequences
**Positive:**
- Systematic testing now available (was ad-hoc before)
- Dedicated security expertise (was scattered across Skeptic)
- Clear quality gates for testing and security
- Testing specialism provides standards for test creation
- Security specialism provides OWASP Top 10 compliance framework
- Agents follow established patterns and conventions
- All validation requirements met (except known script bug)

**Negative:**
- Increased system complexity (9 agents vs 7)
- More files to maintain
- Users need to learn new agent capabilities
- Validation script bug discovered (TEST-003-2)

**Trade-offs:**
- Specialization vs. Simplicity (chose specialization)
- Immediate implementation vs. Extended review (chose immediate)
- Complete coverage vs. Focused delivery (chose focused Phase 1)

### Implementation Notes

**Agent Design:**
- Both agents follow required 5-heading structure
- Clear separation of concerns:
  - Tester: Validation that requirements are met
  - SecurityReviewer: Security vulnerabilities and compliance
  - Skeptic: Adversarial breaking and edge cases (unchanged)
- Agents integrate into workflow between Builder and Skeptic
- Both agents reference their respective specialisms

**Specialisms Created:**
- Testing.md: AAA pattern, test types, coverage metrics, naming conventions
- Security.md: OWASP Top 10, secure coding practices, severity classification

**Configuration Changes:**
- Added tags: security, quality
- Added 2 agent entries to agents.yaml
- Maintained flat file structure
- All files in appropriate directories (agents/, specialisms/)

**Validation:**
- Python YAML validation: All checks pass
- Agent files: All required headings present
- File structure: Flat structure maintained
- Tags: All from allowed list
- Known issue: Validation script TEST-003-2 bug (extracts "id:" literal instead of values)

**Workflow Integration:**
Enhanced workflow:
```
Architect → Builder → Tester → SecurityReviewer → Skeptic → Editor → ProjectManager
```

Tester validates requirements are met, SecurityReviewer checks security compliance, Skeptic finds edge cases.

### Future Considerations
- Phase 2 agents can build on this foundation
- Tester and SecurityReviewer can be referenced by Phase 2 agents
- Validation script bug should be fixed (use awk $3 instead of $2)
- Consider adding example test and security reports

### Related Decisions
- DEC-009 (Agent Expansion Recommendations) - parent decision
- DEC-003 (Required Headings) - followed
- DEC-001 (Flat File Structure) - maintained

### Related Specs
- SPEC-001 (File Structure) - compliant
- SPEC-002 (Agent File Format) - compliant
- SPEC-003 (Tags and Metadata) - compliant
- SPEC-004 (Append-Only Files) - followed for this entry

### Output References
- Agent: agents/Tester.md
- Agent: agents/SecurityReviewer.md
- Specialism: specialisms/Testing.md
- Specialism: specialisms/Security.md
- Configuration: agents.yaml (updated)
- Run log: agent_runs.md #003

---

