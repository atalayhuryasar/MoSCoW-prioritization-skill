# MoSCoW Prioritization Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python: 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Status: Active](https://img.shields.io/badge/Status-v0.1.0-green.svg)](CHANGELOG.md)

An open-source **AI Agent Skill** that brings rigor, mathematical discipline, and speed to product requirement prioritization using the **MoSCoW methodology** and the **60/20/20 effort allocation rule**.

Works seamlessly across **Claude Code**, **Cursor**, **Gemini CLI**, **Codex**, **GitHub Copilot**, and any Agent Skills-compatible runtime.

---

## Why This Skill?

Prioritizing backlogs is notoriously vulnerable to political compromises and wishful thinking:
- **"Everything is a Must":** Without constraints, stakeholders often label 80–90% of features as "Must Have", eliminating buffer and guaranteeing delivery slippage.
- **Subjective Debates:** Arguments erupt over vague terms like "nice-to-have" instead of systematic trade-off analysis.
- **Untracked Scope Exclusions:** Rejected or deferred items get forgotten instead of documented as deliberate release boundaries.

The **MoSCoW Prioritization Skill** solves this by:
1. **Enforcing the 60/20/20 Rule:** Hard-capping Must Haves at $\le 60\%$ of capacity while guarding a $20\%$ Could Have buffer.
2. **Standardizing Rationale:** Demanding objective justification and workaround analysis for every tier assignment.
3. **Automated Verification:** Providing a zero-dependency CLI validator (`scripts/validate_moscow.py`) to check mathematical integrity.

---

## Quick Start (3 Steps)

### Step 1: Install the Skill
Run the automated installer into your favorite AI coding assistant environment:
```bash
bash install.sh
```
*Installs by default to `.claude/skills/`, `.cursor/skills/`, `.gemini/skills/`, and `.agents/skills/`.*

### Step 2: Prompt Your Agent
Invoke the skill naturally in conversation using any trigger phrase:
> *"Help me prioritize our mobile checkout features using MoSCoW for an MVP launch in 4 weeks."*

Your agent will load the skill, analyze constraints, estimate/weigh efforts, apply the test questions, and generate a balanced matrix.

### Step 3: Validate the Allocation
If you export your backlog to JSON, verify the distribution against the 60/20/20 rule:
```bash
python scripts/validate_moscow.py examples/input.json
```

---

## Repository Structure

```text
moscow-prioritization-skill/
├── README.md                              # Project overview, quick start, usage
├── LICENSE                                # MIT license
├── CONTRIBUTING.md                        # Contribution guidelines & PR flow
├── CODE_OF_CONDUCT.md                     # Contributor Covenant v2.1
├── CHANGELOG.md                           # Keep a Changelog history
├── .gitignore                             # Ignored runtime & build files
├── install.sh                             # Multi-platform installer script
├── skills/
│   └── moscow-prioritization/
│       ├── SKILL.md                       # Standard Agent Skill specification
│       └── references/
│           ├── moscow-method.md           # MoSCoW category guide & test questions
│           └── 60-20-20-rule.md           # Mathematical justification & buffer mechanics
├── scripts/
│   └── validate_moscow.py                 # Zero-dependency CLI budget validator
├── examples/
│   ├── input.json                         # Coffee Shop App backlog scenario (13 items)
│   └── output.md                          # Sample prioritized report & decision log
├── adapters/                              # Platform-specific configuration guides
│   ├── claude-code/README.md
│   ├── cursor/README.md
│   ├── gemini-cli/README.md
│   ├── codex/README.md
│   └── copilot/README.md
└── .github/
    ├── ISSUE_TEMPLATE/
    │   ├── bug_report.md
    │   └── feature_request.md
    └── PULL_REQUEST_TEMPLATE.md
```

---

## Usage & Trigger Phrases

Your AI assistant will automatically activate this skill when you prompt with phrases such as:
- *"Prioritize these requirements using MoSCoW"*
- *"What should we build first for our MVP?"*
- *"Help me triage our feature backlog"*
- *"Define our MVP scope with 60/20/20 budget"*
- *"Run MoSCoW prioritization on this user story list"*

---

## Contributing

We welcome community contributions, platform adapters, translations, and benchmarking tools! Please review [CONTRIBUTING.md](CONTRIBUTING.md) and our [Code of Conduct](CODE_OF_CONDUCT.md) before submitting pull requests.

---

## License

This project is open-source software licensed under the [MIT License](LICENSE).  
Copyright (c) 2026 The MoSCoW Prioritization Skill Contributors.
