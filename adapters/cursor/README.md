# Cursor Adapter: MoSCoW Prioritization

This adapter configures the **MoSCoW Prioritization Skill** for the **Cursor AI** code editor.

---

## Target Directory

- **Modern Agent Skills:** `.cursor/skills/moscow-prioritization/`
- **Legacy Rules:** `.cursorrules` in repository root

---

## Installation

### Modern Agent Skills (Recommended)
From the root of this repository:
```bash
bash install.sh
```
Or manually:
```bash
mkdir -p .cursor/skills
cp -R skills/moscow-prioritization .cursor/skills/
```

### Legacy Cursor Setup (`.cursorrules`)
If using older Cursor versions that do not index `.cursor/skills/`:
```bash
LEGACY_CURSOR=1 bash install.sh
```
This generates a dedicated `.cursorrules` file containing MoSCoW and 60/20/20 behavioral guardrails.

---

## Trigger Phrases

Cursor Composer / Agent Mode triggers on:
- *"Prioritize our requirements with MoSCoW."*
- *"Help me define what to build first for this product."*
- *"Apply the 60/20/20 rule to our pending backlog."*
- *"Triage these features into Must, Should, Could, and Won't Have."*

---

## Platform-Specific Notes

- **Composer Mode:** Cursor Composer in Agent mode reads local skill files and can auto-run `python3 scripts/validate_moscow.py` in the terminal to verify generated output.
- **Context Pinning:** In Cursor Chat, you can explicitly reference `@SKILL.md` or `@60-20-20-rule.md` to ensure maximum adherence.

---

## Example Usage Session

```text
User: @input.json Review these features and prioritize them using MoSCoW.

Cursor:
Reading @SKILL.md...
Evaluating 13 backlog items against 60/20/20 capacity constraints.
Running `python3 scripts/validate_moscow.py examples/input.json`...
[PASS] Must Have: 56.0% <= 60%
Generating formatted MoSCoW Prioritization Matrix in Markdown...
```
