# Agent Factory Expansion - Quick Reference

**Status**: Proposed | **Date**: 2026-01-28 | **Full Details**: [agent_recommendations.md](agent_recommendations.md)

## Current System (7 Agents + 3 Specialisms)

### Agents
1. **Architect** - Spec Author + System Designer
2. **Builder** - Implementer / Artifact Producer
3. **Skeptic** - Adversarial Reviewer / Breaker
4. **Editor** - Clarity + Structure Editor
5. **ProjectManager** - Packaging + Orchestration
6. **CitationOfficer** - Evidence Auditor + Claim Tracker
7. **ChatGPT** - Generalist Execution Agent

### Specialisms
1. **Researcher** - Research work standards
2. **Coder** - Code artifact standards
3. **CitationManager** - Citation handling standards

## Recommended Additions

### 🔴 High Priority (Phase 1 - Immediate)

#### New Agents
- **Tester** - Test Creator + Quality Validator
  - Creates test plans, test suites, validates coverage
  - Fills gap: Systematic testing currently missing
  
- **SecurityReviewer** - Security Analyst + Compliance Auditor
  - Security threat modeling, vulnerability assessment
  - Fills gap: Dedicated security expertise needed

#### New Specialisms
- **Security** - Security standards and best practices
- **Testing** - Testing standards and methodologies

### 🟡 Medium Priority (Phase 2 - Next Quarter)

#### New Agents
- **Deployer** - Deployment Engineer + Operations Specialist
  - Deployment guides, CI/CD, operational documentation
  - Fills gap: Deployment readiness not systematically addressed
  
- **DocWriter** - Technical Writer + UX Documentation Specialist
  - User guides, tutorials, API documentation
  - Fills gap: User-facing docs need specialized attention
  
- **Integrator** - Integration Architect + API Designer
  - API specs, integration patterns, interface definitions
  - Fills gap: Integration concerns span multiple artifacts
  
- **DataModeler** - Data Architect + Schema Designer
  - Data models, schemas, migration strategies
  - Fills gap: Data design needs specialized expertise

#### New Specialisms
- **API Design** - API and interface design standards
- **Deployment** - Deployment and operational standards
- **Documentation** - User documentation standards

### 🟢 Low Priority (Phase 3 - As Needed)

#### New Agents
- **Optimizer** - Performance Engineer + Efficiency Analyst
  - Performance analysis, bottleneck identification
  - Fills gap: Performance optimization

#### New Specialisms
- **Data** - Data modeling and management standards
- **Performance** - Performance and optimization standards

## Key Gaps Addressed

| Gap | Priority | Solution |
|-----|----------|----------|
| Testing & QA | High | Tester Agent + Testing Specialism |
| Security & Compliance | High | SecurityReviewer Agent + Security Specialism |
| Deployment & Operations | Medium | Deployer Agent + Deployment Specialism |
| User Documentation | Medium | DocWriter Agent + Documentation Specialism |
| Integration & APIs | Medium | Integrator Agent + API Design Specialism |
| Data Architecture | Medium | DataModeler Agent + Data Specialism |
| Performance Optimization | Low | Optimizer Agent + Performance Specialism |

## Phased Implementation

```
Phase 1 (Immediate)          Phase 2 (Q2)              Phase 3 (As Needed)
├─ Tester                    ├─ Deployer               ├─ Optimizer
├─ SecurityReviewer          ├─ DocWriter              ├─ Data Specialism
├─ Security Specialism       ├─ Integrator             └─ Performance Specialism
└─ Testing Specialism        ├─ DataModeler
                             ├─ API Design Specialism
                             ├─ Deployment Specialism
                             └─ Documentation Specialism
```

## Enhanced Workflow

**Current:**
```
Architect → Builder → Skeptic → Editor → ProjectManager
```

**Enhanced:**
```
Architect → Builder → Tester → SecurityReviewer → Skeptic → Editor → DocWriter → Deployer → ProjectManager
              ↓         ↓              ↓                                   ↓
         Integrator  DataModeler   CitationOfficer                    Optimizer
```

## New Tags Required

Add to `allowed_tags` in agents.yaml:
- `security` - for SecurityReviewer
- `quality` - for Tester
- `performance` - for Optimizer
- `data` - for DataModeler
- `api` - for Integrator

## Benefits Summary

✅ **Quality**: Systematic testing and validation  
✅ **Security**: Dedicated security analysis  
✅ **Production Ready**: Deployment and operational support  
✅ **User Focused**: Better documentation for end users  
✅ **Integrated**: Better API and integration patterns  
✅ **Scalable**: Data and performance considerations  

## Implementation Checklist

For each new agent:
- [ ] Create agent file in `agents/` directory
- [ ] Add entry to `agents.yaml` with unique ID
- [ ] Include all required headings (Purpose, Inputs, Outputs, Behavior, Constraints)
- [ ] Add appropriate tags
- [ ] Run `./validate_agents.sh`
- [ ] Update `decisions.md` with implementation decision
- [ ] Update `agent_runs.md` with run log

## References

- **Full Analysis**: [agent_recommendations.md](agent_recommendations.md)
- **Decision Record**: [decisions.md](decisions.md) - DEC-009
- **Run Log**: [agent_runs.md](agent_runs.md) - Run #002
- **Configuration**: [agents.yaml](agents.yaml)
- **Guidelines**: [agents.md](agents.md)

---

**Next Actions:**
1. Review recommendations with stakeholders
2. Approve Phase 1 agents for implementation
3. Create detailed specs for approved agents
4. Implement Tester agent (highest priority)
5. Implement SecurityReviewer agent
6. Update tags in agents.yaml
7. Update documentation

---

*Generated: 2026-01-28*
