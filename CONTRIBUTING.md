# Contributing to MoSCoW Prioritization Skill

Thank you for your interest in improving the **MoSCoW Prioritization Skill**! We welcome contributions from developers, product managers, agile coaches, and AI enthusiasts.

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before participating in this project.

---

## What We Look For in Contributions

We actively encourage contributions in the following areas:
- **New Platform Adapters:** Support for emerging AI IDEs and agent orchestration frameworks (e.g., Windsurf, Continue.dev, Roo Code, LangChain agents).
- **Translations:** Localization of `SKILL.md` and reference guides into Turkish, Spanish, German, Japanese, etc.
- **Validator Enhancements:** Adding CSV/Markdown table parsing to `scripts/validate_moscow.py` (while maintaining the zero-dependency stdlib rule).
- **Edge-Case Documentation:** Case studies, real-world examples, and comparisons with RICE/ICE scoring models.
- **CI/CD Automation:** GitHub Actions workflows for automated validator testing across Python versions.

---

## Development & Contribution Workflow

We follow standard GitHub Flow:

### 1. Fork & Clone
Fork the repository on GitHub, then clone your local copy:
```bash
git clone https://github.com/<your-username>/moscow-prioritization-skill.git
cd moscow-prioritization-skill
```

### 2. Create a Feature Branch
Use a descriptive branch name:
```bash
git checkout -b feature/add-windsurf-adapter
# or
git checkout -b fix/validator-rounding-edgecase
```

### 3. Make Your Changes
- Ensure any modifications to `SKILL.md` stay under **500 lines** and adhere to the Agent Skills specification.
- If modifying `scripts/validate_moscow.py`, **do not introduce external Python package dependencies**. It must run with Python 3.8+ stdlib only.
- Preserve UTF-8 encoding and LF (Unix) line endings across all files.

### 4. Run Local Validations (Mandatory)
Before committing, you **must run the validator** and test any modified examples:
```bash
# Validate sample input
python3 scripts/validate_moscow.py examples/input.json

# Test execution permissions
bash install.sh
```

Ensure all status indicators show `[PASS] ✅` without unhandled errors.

### 5. Commit & Push
Write clear, conventional commit messages:
```bash
git commit -m "feat(adapters): add Windsurf configuration guide"
git push origin feature/add-windsurf-adapter
```

### 6. Submit a Pull Request
- Open a Pull Request against the `main` branch.
- Fill out the provided [PR Template](.github/PULL_REQUEST_TEMPLATE.md).
- Link any related issues (e.g., `Fixes #12`).

---

## Code of Conduct
All contributors and maintainers are expected to adhere to the [Contributor Covenant](CODE_OF_CONDUCT.md). Please report any unacceptable behavior to the project maintainers.
