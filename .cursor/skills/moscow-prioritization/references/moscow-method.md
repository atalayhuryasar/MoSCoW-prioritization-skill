# MoSCoW Methodology Guide

The **MoSCoW method** is a battle-tested prioritization technique originating from the Dynamic Systems Development Method (DSDM) in 1994. It helps teams reach clear consensus on what must be delivered, what should be delivered if possible, what can be deferred, and what is explicitly out of scope for a given release or timebox.

---

## The Four Categories

```text
+--------------------------------------------------------------+
|                          TOTAL SCOPE                         |
+------------------------------+---------------+---------------+
|          MUST HAVE           |  SHOULD HAVE  |  COULD HAVE   |
|         (Max <=60%)          |  (Target ~20%)|  (Target ~20%)|
|     Non-negotiable Core      | Vital Workar. | Buffer & Wins |
+------------------------------+---------------+---------------+
|                    WON'T HAVE THIS TIME                      |
|                (0% - Explicitly Out of Scope)                 |
+--------------------------------------------------------------+
```

### 1. Must Have (M) — Non-Negotiable
- **Definition:** The fundamental requirements without which the product cannot launch, is illegal or unsafe, or provides zero viable utility to users.
- **Test Question:** *"If this single item is missing on launch day, does the release fail completely or become illegal/unviable?"*
  - If **Yes** $\rightarrow$ Must Have.
  - If there is any viable manual or operational workaround $\rightarrow$ Demote to **Should Have**.
- **Key Characteristic:** Non-negotiable. If a Must Have slips, the release date must slip.

### 2. Should Have (S) — Important but Not Vital
- **Definition:** High-impact, painful-to-omit features that are critical for long-term satisfaction or standard workflows, but a temporary workaround exists for Day 1.
- **Test Question:** *"Is this feature painful to omit, but can users still complete their core job via an alternative or manual workaround?"*
  - If **Yes** $\rightarrow$ Should Have.
- **Key Characteristic:** Highly desirable, but omitting it does not break core functionality or legal compliance.

### 3. Could Have (C) — Desirable Nice-to-Haves
- **Definition:** Valuable enhancements, quality-of-life improvements, or minor features that will only be tackled if remaining time and effort allow.
- **Test Question:** *"If we don't build this, will the user experience remain fundamentally sound with only minor inconvenience?"*
  - If **Yes** $\rightarrow$ Could Have.
- **Key Characteristic:** This acts as the **delivery contingency buffer**. When unexpected delays occur, Could Have items are the first to be descheduled.

### 4. Won't Have (W) — Out of Scope (For Now)
- **Definition:** Ideas and features agreed to be out of scope for the current delivery window, preserved for future releases or iterations.
- **Test Question:** *"Is this something we agree not to work on during this specific timebox to protect the deadline and budget?"*
  - If **Yes** $\rightarrow$ Won't Have.
- **Key Characteristic:** Explicitly prevents scope creep and sets clear stakeholder expectations.

---

## The 60/20/20 Effort Rule Summary

To ensure release safety in Agile and fixed-time delivery:
- **Must Have:** $\le 60\%$ of total active capacity.
- **Should Have:** $\sim 20\%$ of total active capacity ($15\% - 25\%$).
- **Could Have:** $\sim 20\%$ of total active capacity ($15\% - 25\%$).
- **Won't Have:** $0\%$ of current capacity (deferred).

Having more than 60% of capacity tied to "Must Haves" removes all contingency margin, creating extreme risk of missed deadlines, quality degradation, and team burnout.

---

## Common Pitfalls & How to Avoid Them

| Pitfall | Why It Happens | Solution |
|---|---|---|
| **"Everything is a Must"** | Stakeholders fear omitted items will never be built. | Enforce the hard 60% cap. Explain that labelling everything a Must removes agility and guarantees delivery delays. |
| **Hiding Won't Have** | Teams avoid uncomfortable scope cuts. | Celebrate Won't Have as a sign of strategic focus. Document items in the release scope boundary. |
| **No Clear Workaround Analysis** | Should Haves are promoted to Must without testing alternatives. | Force the question: *"Can customer service or a spreadsheet temporarily fill this gap?"* |
| **Treating Could Haves as Guarantees** | Promising Could Haves to executive sponsors. | Clearly message Could Haves as contingency buffers: they only ship if capacity permits. |
| **Missing Effort Values** | Categorizing solely by emotional importance. | Pair every requirement with an effort estimate (story points or hours) before calculating percentages. |
