<!-- Written by Alexander Holman 19/08/2019 -->
<!--
This file contains a list of all changes made to a system since it's introduction. It is written to be used with most 
internal projects, but as per the other documents feel free to adapt it to fit your needs, adding, modifying and 
removing as necessary.
In the event that it is added to an existing repository, (unless a full desscription is feasable) simply start with the 
current version.
-->

# Changelog
A rough overview of changes to over time.

<!-- EXAMPLE START -->
## [v1.1.0] 2026-01-28
GitHub Copilot Agent Readiness Release
* [Added] - `.github/copilot-instructions.md` - Comprehensive workspace instructions for GitHub Copilot
* [Added] - `COPILOT_INTEGRATION.md` - Complete guide for using AgentFactory with GitHub Copilot
* [Added] - `.github/workflows/validate-agents.yml` - Automated validation workflow for CI/CD
* [Fixed] - Updated all 7 core agent files (Architect, Builder, Skeptic, Editor, ProjectManager, CitationOfficer, ChatGPT) to include required heading structure
* [Fixed] - All agents now have proper Purpose, Inputs, Outputs, Behavior, and Constraints sections in correct order
* [Updated] - README.md with GitHub Copilot integration information and validation details
* [Validated] - All 22 validation tests now pass successfully
* [Enhanced] - Repository is now fully ready for GitHub Copilot Workspace integration

## [v1.0.0](https://github.com/alexanderholman/AgentFactory/releases/tag/v1.0.0) 2026-01-28
Initial release of AgentFactory - a framework for defining, documenting, and managing AI agents.
* [Added] - Core agent definitions (Architect, Builder, Skeptic, Editor, ProjectManager, CitationOfficer, ChatGPT)
* [Added] - Specialism definitions (Researcher, Coder, CitationManager)
* [Added] - Agent documentation framework with standardized headings and YAML frontmatter
* [Added] - Validation tools (validate_agents.sh) for MUST requirements
* [Added] - Append-only logs for specs, runs, and decisions
* [Added] - Project structure and configuration files (agents.yaml, repo.yaml)
* [Added] - Initial project documentation templates
* [Added] - Issue templates for bugs, tasks, features, questions, and brainstorming
* [Added] - Contributing guidelines and code of conduct
* [Added] - Support documentation and installation instructions
<!--  EXAMPLE END -->