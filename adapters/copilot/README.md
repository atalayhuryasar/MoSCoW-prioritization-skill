# GitHub Copilot Adapter: MoSCoW Prioritization

This adapter configures the **MoSCoW Prioritization Skill** for **GitHub Copilot Chat** in VS Code, JetBrains, and GitHub.com.

---

## Target Files & Directories

- **Copilot Custom Instructions:** `.github/copilot-instructions.md`
- **Agent Skill Path:** `.agents/skills/moscow-prioritization/`

---

## Installation

### Standard Installation
```bash
COPILOT_INSTRUCTIONS=1 bash install.sh
```
This command copies the skill directory into `.agents/skills/` and generates `.github/copilot-instructions.md` so Copilot Chat always applies MoSCoW principles when requested.

### Manual Installation
1. Copy skill folder:
   ```bash
   mkdir -p .agents/skills
   cp -R skills/moscow-prioritization .agents/skills/
   ```
2. Add instructions to `.github/copilot-instructions.md`:
   ```markdown
   When asked to prioritize requirements or define an MVP:
   - Use the MoSCoW methodology (Must, Should, Could, Won't Have).
   - Enforce the 60/20/20 capacity allocation rule (Must Have <= 60%).
   - See skills/moscow-prioritization/SKILL.md for details.
   ```

---

## Trigger Phrases

In Copilot Chat (`@workspace` or inline chat):
- *"@workspace Prioritize our pending user stories using MoSCoW."*
- *"@workspace Help me define what to build first for the upcoming milestone."*
- *"@workspace Apply 60/20/20 MoSCoW triage to our product backlog."*

---

## Platform-Specific Notes

- **GitHub Copilot Workspace:** When prompted in Copilot Workspace or pull request reviews, Copilot will respect the boundaries defined in `.github/copilot-instructions.md`.
- **Scope Boundary Enforcement:** Copilot will warn users when suggested new features threaten to push Must Have effort above the 60% threshold.

---

## Example Usage Session

```text
User: @workspace How should we prioritize the features in our roadmap?

GitHub Copilot:
Based on the MoSCoW Prioritization Skill in .agents/skills/moscow-prioritization:
1. Core authentication and order processing are Must Haves (<= 60% of capacity).
2. Saved filters and reorder are Should Haves (~20%).
3. Dark mode and notifications are Could Haves (~20% contingency buffer).
4. AI recommendations are Won't Have for this sprint.
Here is the structured prioritization table...
```
