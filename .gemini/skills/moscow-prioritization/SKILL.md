---
name: moscow-prioritization
description: Use when you need to prioritize product requirements, perform backlog triage, define an MVP scope, apply the MoSCoW methodology, or decide what to build first.
version: 0.1.0
license: MIT
tags:
  - product-management
  - prioritization
  - mvp
  - moscow
---

# MoSCoW Prioritization Skill

## Purpose

The **MoSCoW Prioritization Skill** guides AI agents and product teams to categorize requirements into Must Have, Should Have, Could Have, and Won't Have (this time). It strictly enforces the **60/20/20 effort allocation rule** to safeguard sprint and release feasibility while creating a transparent audit trail of decisions.

---

## When to Use This Skill

Activate this skill when:
- Defining or refining an MVP (Minimum Viable Product) scope.
- Triaging a feature backlog under constrained engineering capacity or fixed deadlines.
- Planning sprint milestones or release increments.
- Stakeholders disagree on priorities and need objective justification.
- The user asks: *"What should we build first?"*, *"Help me prioritize these features"*, or *"Apply MoSCoW to this list"*.

**When NOT to use:**
- Pure bug triage without effort estimations (use standard defect severity matrix).
- Granular daily task scheduling.

---

## Inputs

The skill expects:
1. **Requirements / Features List:** Titles and descriptions of features or user stories.
2. **Effort Estimates (Story points, t-shirt size, or person-days):** If missing, the agent will prompt or estimate relative weights (1 to 8).
3. **Target Release Goal / Constraints:** Timebox, budget, team size, or core business objective.

---

## Procedure (7 Steps)

Follow these steps sequentially:

### Step 1: Validate Input
- Verify that requirements have names and discernible scopes.
- Check if effort values exist. If missing, assign relative baseline efforts (e.g., Fibonacci scale: 1, 2, 3, 5, 8) and confirm with the user.

### Step 2: Collect Business Context
- Identify the primary release objective (e.g., "Launch core ordering experience in 6 weeks").
- Note regulatory, legal, security, or foundational technical constraints.

### Step 3: Categorize Features
Evaluate each item using the standard test questions:
- **Must Have (M):** Without this, does the release fail, become unsafe, or provide zero functional utility? If yes $\rightarrow$ **Must**.
- **Should Have (S):** Is it critical for good UX or operational efficiency, but has a viable workaround if omitted? If yes $\rightarrow$ **Should**.
- **Could Have (C):** Is it a high-value enhancement that only ships if time and resources permit? If yes $\rightarrow$ **Could**.
- **Won't Have (W):** Is it explicitly deferred to a future milestone to protect focus? If yes $\rightarrow$ **Won't**.

### Step 4: Document Rationale
- For every categorized item, write a 1–2 sentence justification explaining why it belongs in that tier.
- Reject subjective labels ("nice to have" or "crucial") without specific business/user impact reasoning.

### Step 5: Enforce the 60/20/20 Rule
Calculate the percentage of total estimated effort (excluding Won't Have):
$$\text{Allocation \%} = \frac{\text{Effort of Category}}{\text{Total Active Effort (M + S + C)}} \times 100$$

- **Must Have:** $\le 60\%$ (❌ **VIOLATION** if $> 60\%$: Demote items to Should Have until $\le 60\%$).
- **Should Have:** Target $\sim 20\%$ (Guideline: $15\% - 25\%$).
- **Could Have:** Target $\sim 20\%$ (Guideline: $15\% - 25\%$; serves as schedule buffer).
- **Won't Have:** $0\%$ of active release capacity (deferred).

Run `python scripts/validate_moscow.py <input.json>` whenever structured JSON is available to verify constraints programmatically.

### Step 6: Produce Output
Generate the structured MoSCoW Prioritization Matrix in clean Markdown.

### Step 7: Generate Decision Log & Scope Boundaries
- Document explicit trade-offs and demotions made during the 60/20/20 balancing.
- Highlight the **Won't Have boundary** so stakeholders know what is out of scope.

---

## Output Format

Outputs must follow this standard Markdown structure:

```markdown
# MoSCoW Prioritization Report: [Project Name]

## 1. Executive Summary & 60/20/20 Budget Check
- **Total In-Scope Effort:** [X] pts
- **Must Have:** [X] pts ([M%]%) — [✅ Pass / ❌ Over Budget]
- **Should Have:** [X] pts ([S%]%) — [✅ Pass / ⚠️ Review]
- **Could Have:** [X] pts ([C%]%) — [✅ Pass / ⚠️ Review]
- **Won't Have (Deferred):** [X] pts ([W] items)

## 2. Prioritization Matrix

| ID | Feature / User Story | Category | Effort | Rationale |
|---|---|---|---|---|
| F-01 | User Authentication | Must | 5 | Core security and access prerequisite |
| F-02 | Push Notifications | Should | 3 | Key retention driver, manual email workaround exists |
| F-03 | Dark Mode | Could | 2 | Enhances UI experience, non-essential for initial launch |
| F-04 | AI Recommendation Engine | Won't | 8 | High complexity; deferred to Phase 2 |

## 3. Scope Boundary (Won't Have - Deferred)
- Features explicitly excluded from this release to safeguard timeline.

## 4. Decision Log & Rebalancing Notes
- Detail any items demoted from Must to Should to satisfy the 60% cap.
```

---

## Rules and Guardrails

1. **The 60% Hard Cap:** Under no circumstance should `Must Have` exceed 60% of active capacity. If a stakeholder insists everything is a Must, explain that 100% Must guarantees schedule slippage or failure.
2. **Buffer Protection:** `Could Have` items represent the 20% contingency buffer. They are the first to be dropped if delivery velocity slows.
3. **Every Item Needs Rationale:** No category assignment without documented reasoning.
4. **Scope Integrity:** Won't Have is an agreement of focus, not a rejection bin. It protects team attention.

---

## Related Skills & Tools

- **Validator Tool:** `scripts/validate_moscow.py` (CLI validation of effort budgets)
- **Methodology Guide:** `references/moscow-method.md`
- **Budgeting Mechanics:** `references/60-20-20-rule.md`

---

## References

- Clegg, Dai; Barker, Richard (1994). *Case Method Fast-Track: A Radically New Approach to Software Engineering*.
- DSDM Agile Project Framework (Dynamic Systems Development Method).
