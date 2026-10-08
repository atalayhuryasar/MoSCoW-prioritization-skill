#!/usr/bin/env bash
# ==============================================================================
# MoSCoW Prioritization Skill — Multi-Platform Installer
# Installs the moscow-prioritization skill across modern AI Agent platforms:
# - Claude Code   (.claude/skills/)
# - Cursor        (.cursor/skills/)
# - Gemini CLI    (.gemini/skills/)
# - Codex/Copilot (.agents/skills/)
# ==============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_SKILL_DIR="${SCRIPT_DIR}/skills/moscow-prioritization"

if [ ! -d "${SOURCE_SKILL_DIR}" ]; then
  echo "❌ Error: Source skill directory not found at '${SOURCE_SKILL_DIR}'" >&2
  exit 1
fi

echo "============================================================"
echo "    Installing MoSCoW Prioritization Skill across Platforms"
echo "============================================================"

install_to() {
  local target_dir="$1"
  local platform_name="$2"

  mkdir -p "${target_dir}"
  rm -rf "${target_dir}/moscow-prioritization"
  cp -R "${SOURCE_SKILL_DIR}" "${target_dir}/"
  echo "✅ ${platform_name}: Installed to ${target_dir}/moscow-prioritization"
}

# 1. Claude Code
install_to "${SCRIPT_DIR}/.claude/skills" "Claude Code"

# 2. Cursor (Modern Agent Skills)
install_to "${SCRIPT_DIR}/.cursor/skills" "Cursor"

# 3. Gemini CLI / Antigravity
install_to "${SCRIPT_DIR}/.gemini/skills" "Gemini CLI"

# 4. Codex & Cross-Platform Agent Skills Standard
install_to "${SCRIPT_DIR}/.agents/skills" "Codex / Copilot (.agents)"

# Optional: Legacy Cursor (.cursorrules)
if [ "${LEGACY_CURSOR:-0}" = "1" ]; then
  CURSORRULES_FILE="${SCRIPT_DIR}/.cursorrules"
  cat <<'EOF' > "${CURSORRULES_FILE}"
# MoSCoW Prioritization Rules (Cursor Legacy)
When prioritizing features, defining MVP scope, or triaging backlogs:
1. Follow the MoSCoW methodology: Must Have, Should Have, Could Have, Won't Have.
2. Enforce the 60/20/20 rule: Must Have must NEVER exceed 60% of total active effort.
3. Reserve ~20% for Could Have items as a delivery contingency buffer.
4. For every categorized item, supply 1-2 sentences of objective justification and workaround analysis.
5. Refer to skills/moscow-prioritization/SKILL.md for the full 7-step procedure.
EOF
  echo "✅ Legacy Cursor: Generated .cursorrules"
fi

# Optional: GitHub Copilot Instructions (.github/copilot-instructions.md)
if [ "${COPILOT_INSTRUCTIONS:-0}" = "1" ]; then
  COPILOT_FILE="${SCRIPT_DIR}/.github/copilot-instructions.md"
  mkdir -p "${SCRIPT_DIR}/.github"
  cat <<'EOF' > "${COPILOT_FILE}"
# GitHub Copilot Custom Instructions: MoSCoW Prioritization

When the user asks to prioritize features, plan an MVP, or triage requirements:
- Apply the MoSCoW framework (Must Have, Should Have, Could Have, Won't Have).
- Enforce the 60/20/20 capacity rule: Must Have <= 60% of active effort; Should Have ~20%; Could Have ~20% (buffer).
- Explicitly exclude Won't Have items to protect scope boundaries.
- Provide clear rationale for each tier assignment.
- See skills/moscow-prioritization/SKILL.md for guidelines.
EOF
  echo "✅ GitHub Copilot: Generated .github/copilot-instructions.md"
fi

echo "============================================================"
echo "🎉 Installation complete! The MoSCoW skill is ready to use."
echo "============================================================"
