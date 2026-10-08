# Claude Code Adapter: MoSCoW Prioritization

This adapter configures the **MoSCoW Prioritization Skill** for **Claude Code** (Anthropic's agentic CLI).

---

## Target Directory

- **Project-Level:** `.claude/skills/moscow-prioritization/`
- **Global / Personal:** `~/.claude/skills/moscow-prioritization/`

---

## Installation

### Project-Level Installation
From the root of this repository:
```bash
bash install.sh
```
Or manually:
```bash
mkdir -p .claude/skills
cp -R skills/moscow-prioritization .claude/skills/
```

### Global Installation (Available across all Claude Code projects)
```bash
mkdir -p ~/.claude/skills
cp -R skills/moscow-prioritization ~/.claude/skills/
```

---

## Trigger Phrases

Claude Code automatically matches task prompts against the skill's description:
- *"Prioritize our sprint backlog using MoSCoW."*
- *"Help me triage these feature requests and calculate the 60/20/20 distribution."*
- *"Define the MVP scope for this project; what should we build first?"*
- *"Can we run MoSCoW prioritization on this list of user stories?"*

---

## Platform-Specific Notes

- **Skill Discovery:** Claude Code discovers skills located in `.claude/skills/` at workspace startup.
- **Reference Files:** When Claude Code loads `SKILL.md`, it can dynamically read `references/moscow-method.md` and `references/60-20-20-rule.md` on demand without consuming initial context tokens.
- **Subagent Execution:** Claude Code will execute `python3 scripts/validate_moscow.py` via bash commands to ensure the final table strictly satisfies the 60% Must Have rule.

---

## Example Usage Session

```text
> user: "Here are 10 features for our photo editor MVP. Let's do a MoSCoW triage with effort estimates."

> Claude Code:
  Loading skill: moscow-prioritization
  Analyzing requirements and estimating relative effort (pts)...
  Applying 60/20/20 capacity rule:
  - Must Have: 24 pts (57%) [PASS]
  - Should Have: 9 pts (21%) [PASS]
  - Could Have: 9 pts (21%) [PASS]
  - Won't Have: 18 pts (Deferred)
  Generating MoSCoW Matrix and Decision Log...
```
