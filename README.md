<!-- Written by Alexander Holman 19/08/2019 -->
<!--
This file is simply a welcom page and should offer only a little information, further information should be added to 
either to the relevant markdown files included or to a wiki. It is written to be used with most internal projects, but 
as per the other documents feel free to adapt it to fit your needs, adding, modifying and removing as necessary.
-->

# AgentFactory
A structured repository for managing AI agents with flat file architecture and comprehensive documentation standards.

<!-- All badges representing the current status of the application below should they exist -->

## What is AgentFactory
AgentFactory is a framework for defining, documenting, and managing AI agents using a simple flat-file structure. It enforces standards for agent documentation, maintains append-only logs for specifications and decisions, and provides validation tools to ensure consistency.

### Key Features
- **Flat File Structure**: Simple, navigable file organization
- **Standardized Documentation**: Required headings and formatting for all agents
- **Append-Only Logs**: Historical record of specs, runs, and decisions
- **Validation Tools**: Automated tests for all MUST requirements
- **No Fabrication Policy**: All citations and results must be verifiable

For detailed specifications, see [specs.md](/specs.md).

## Getting started

### Quick Start
1. Review the [agents.md](/agents.md) for rules and guidelines
2. Check [agents.yaml](/agents.yaml) for agent configuration structure
3. Read [specs.md](/specs.md) for detailed specifications
4. Review [decisions.md](/decisions.md) to understand design choices

### Adding a New Agent
1. Define the agent in `agents.yaml` with all required fields
2. Create the agent markdown file following the template in `agents.md`
3. Ensure all required headings are present
4. Run `./validate_agents.sh` to verify compliance
5. Document the addition in `decisions.md`

### Validation
Run the validation script to check compliance:
```bash
./validate_agents.sh
```

For more details, see [INSTALL](/INSTALL.md).

## Agent Definitions

The `agents/` directory contains agent definition files that describe roles and behaviors for the agent factory system:

**Core Agents:**
- **Architect.md** - Spec Author + System Designer
- **Builder.md** - Implementer / Artifact Producer
- **Skeptic.md** - Adversarial Reviewer / Breaker
- **Editor.md** - Clarity + Structure Editor
- **ProjectManager.md** - Packaging + Orchestration
- **CitationOfficer.md** - Evidence Auditor + Claim Tracker
- **ChatGPT.md** - Generalist Execution Agent

**Specialisms** (in `specialisms/` directory):
- **Researcher.md** - Research work standards
- **Coder.md** - Code artifact standards
- **CitationManager.md** - Citation handling standards

## Getting involved
If for any reason you wish or need to get involved, please start by reading our [CODE OF CONDUCT](/CODE_OF_CONDUCT.md) 
and the [CONTRIBUTING](/.github/CONTRIBUTING.md) guide.

## Need support
Should you need further support not covered above, please take a look at the [SUPPORT](/.github/SUPPORT.md) guide.

Further documentation:
- [agents.md](/agents.md) - Agent documentation rules and templates
- [agents.yaml](/agents.yaml) - Agent configuration schema
- [specs.md](/specs.md) - Technical specifications (append-only)
- [agent_runs.md](/agent_runs.md) - Agent execution log (append-only)
- [decisions.md](/decisions.md) - Design decisions (append-only)

## Legal
Unless otherwise stated, or where written permission has been given by the copyright holder, this software is for use 
by the copyright holder only. Public availability of this repository or any of it's contents does grant anyone licence 
or rights of any kind. Further information can be found in the [LICENSE](/LICENSE) document.