# OpenAI Codex & Cross-Agent Adapter: MoSCoW Prioritization

This adapter configures the **MoSCoW Prioritization Skill** for **OpenAI Codex CLI** and agents adhering to the cross-runtime `.agents/` standard.

---

## Target Directory

- **Project Root:** `.agents/skills/moscow-prioritization/`
- **Global / User Home:** `~/.agents/skills/moscow-prioritization/`

---

## Installation

### Project Setup
```bash
bash install.sh
```
Or manually:
```bash
mkdir -p .agents/skills
cp -R skills/moscow-prioritization .agents/skills/
```

### Global Setup
```bash
mkdir -p ~/.agents/skills
cp -R skills/moscow-prioritization ~/.agents/skills/
```

---

## Trigger Phrases

- *"Apply MoSCoW prioritization to our project requirements."*
- *"Backlog triage with 60/20/20 effort balancing."*
- *"Help us figure out what to build first for this release."*
- *"Define MVP scope for our new API endpoint collection."*

---

## Platform-Specific Notes

- **The `.agents/` Standard:** Modern agent runtimes (Codex, Copilot CLI, Gemini, Claude) recognize `~/.agents/skills/` as a unified, cross-runtime skill repository.
- **Strict Format Compliance:** The `SKILL.md` specification adheres strictly to `agentskills.io` standard schemas.

---

## Example Usage Session

```bash
$ codex "Prioritize features in features.md using MoSCoW"
# Output:
# Loaded .agents/skills/moscow-prioritization/SKILL.md
# Categorizing 10 items...
# Verifying 60/20/20 compliance...
# Generating output table...
```
