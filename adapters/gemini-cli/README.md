# Gemini CLI & Antigravity Adapter: MoSCoW Prioritization

This adapter configures the **MoSCoW Prioritization Skill** for **Gemini CLI** and the **Google Antigravity IDE**.

---

## Target Directory

- **Workspace Customization:** `.gemini/skills/moscow-prioritization/`
- **Global Config Root:** `~/.gemini/config/skills/moscow-prioritization/`

---

## Installation

### Workspace Installation
From the root of this repository:
```bash
bash install.sh
```
Or manually:
```bash
mkdir -p .gemini/skills
cp -R skills/moscow-prioritization .gemini/skills/
```

### Global Installation
```bash
mkdir -p ~/.gemini/config/skills
cp -R skills/moscow-prioritization ~/.gemini/config/skills/
```

---

## Trigger Phrases

Gemini CLI and Antigravity auto-discover the skill on:
- *"Prioritize our user stories with MoSCoW"*
- *"MVP scope definition with 60/20/20 rule"*
- *"What should we build first in this release?"*
- *"Backlog triage and prioritization analysis"*

---

## Platform-Specific Notes

- **Antigravity Customizations:** Customizations placed in `.gemini/skills/` or `~/.gemini/config/skills/` are dynamically loaded into the agent system prompt when triggered.
- **Task Artifact Integration:** When running multi-step prioritization in Antigravity, the agent tracks its 7-step procedure using structured Markdown task artifacts.
- **CLI Commands:** The agent natively executes `python3 scripts/validate_moscow.py` via `run_command`.

---

## Example Usage Session

```text
User: "We have 8 features in our sprint. Run a MoSCoW prioritization with 60/20/20 verification."

Gemini CLI:
Activated skill: moscow-prioritization
Step 1: Validating inputs and effort weights...
Step 2: Checking business constraints...
Step 3-5: Categorizing items & enforcing 60% cap...
Step 6-7: Generating Markdown matrix and decision log...
Report successfully produced!
```
