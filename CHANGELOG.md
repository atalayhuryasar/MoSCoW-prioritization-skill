# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.0] - 2026-10-09

### Added
- **Core Agent Skill:** Initial release of `moscow-prioritization` skill specification (`skills/moscow-prioritization/SKILL.md`) complying with Agent Skills standards.
- **Methodology References:**
  - `skills/moscow-prioritization/references/moscow-method.md`: Exhaustive guide covering Must, Should, Could, Won't categories, test questions, and common pitfalls.
  - `skills/moscow-prioritization/references/60-20-20-rule.md`: Mathematical principles of delivery buffers and the 60% hard cap rule.
- **Validation Engine:** `scripts/validate_moscow.py` zero-dependency CLI validator enforcing the 60/20/20 capacity breakdown with rich console reporting and error codes.
- **Reference Examples:**
  - `examples/input.json`: 13-item Coffee Shop Mobile App MVP backlog with relative effort estimations.
  - `examples/output.md`: Complete prioritization report including Executive Summary, MoSCoW Matrix, Decision Log, and Scope Boundary.
- **Multi-Platform Support:** Setup guides and adapters for Claude Code, Cursor, Gemini CLI, OpenAI Codex, and GitHub Copilot.
- **Automated Installer:** `install.sh` shell script to install the skill across multiple agent environments with a single command.
- **Open Source Infrastructure:** Added `.gitignore`, `LICENSE` (MIT), `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, GitHub Issue Templates (`bug_report.md`, `feature_request.md`), and Pull Request Template.
