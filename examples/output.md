# MoSCoW Prioritization Report: Coffee Shop Mobile App MVP

## 1. Executive Summary & 60/20/20 Budget Check

This prioritization analysis evaluates the Minimum Viable Product (MVP) scope for the Coffee Shop Mobile App. The release boundary enforces the **60/20/20 rule** to ensure release certainty within the fixed launch window.

- **Total Evaluated Backlog:** 76.0 pts (13 features)
- **Active In-Scope Effort:** 50.0 pts (10 features)
- **Deferred Scope (Won't Have):** 26.0 pts (3 features)

### Capacity Allocation Breakdown

| Category | Item Count | Total Effort | Capacity Share | Target Guideline | Compliance Status |
|---|---|---|---|---|---|
| **Must Have** | 4 | 28.0 pts | **56.0%** | $\le 60.0\%$ | **[PASS] ✅** |
| **Should Have** | 3 | 11.0 pts | **22.0%** | $15.0\% - 25.0\%$ | **[PASS] ✅** |
| **Could Have** | 3 | 11.0 pts | **22.0%** | $15.0\% - 25.0\%$ | **[PASS] ✅** |
| **Won't Have** | 3 | 26.0 pts | *Deferred (0%)* | Excluded from Active | **[DEFERRED] 📦** |

> **Automated Validation Result:**  
> Verified via `scripts/validate_moscow.py examples/input.json` $\rightarrow$ **PASS** (Zero rule violations).

---

## 2. MoSCoW Prioritization Matrix

| ID | Feature / User Story | Category | Effort (pts) | Primary Rationale |
|---|---|---|---|---|
| **CS-01** | User Account & Authentication | **Must** | 7.0 | Core security prerequisite; required to save user payments and bind mobile order history legally and securely. |
| **CS-02** | Menu Browsing & Item Customization | **Must** | 8.0 | Fundamental commercial capability. Customers must be able to specify beverages (milk, size, syrups). Without this, there is no digital transaction. |
| **CS-03** | Order Placement & In-App Payment | **Must** | 8.0 | Primary monetization gateway. Customers cannot complete an advance order without integrated payment processing. |
| **CS-04** | Real-time Order Status & Pickup Tracking | **Must** | 5.0 | Essential pickup loop. Prevents crowds at physical pickup counters by notifying customers when the order is ready. |
| **CS-05** | Saved Favorite Orders & Quick Reorder | **Should** | 4.0 | High-value UX booster during morning peak rushes. Users can still navigate standard menus, making this a painful omission but viable without it on Day 1. |
| **CS-06** | Store Locator with Live Hours & Directions | **Should** | 4.0 | Crucial for multi-branch orders, but customers can alternatively rely on external maps (Google/Apple Maps) if needed. |
| **CS-07** | Digital Receipt via In-App View & Email | **Should** | 3.0 | Required for financial clarity, though credit card notification provides a temporary proof-of-purchase fallback. |
| **CS-08** | Loyalty Points & Rewards Tracker | **Could** | 5.0 | High marketing appeal, but not required to complete purchases. Acts as prime contingency buffer if engineering velocity drops. |
| **CS-09** | Custom Tip Amount for Barista | **Could** | 3.0 | Desirable staff support feature, but orders execute smoothly without tip processing on Day 1. |
| **CS-10** | Dark Mode & Accessibility Font Scaling | **Could** | 3.0 | Significant polish and accessibility enhancement, safe to deliver in a fast-follow update. |
| **CS-11** | Curbside Geofenced Vehicle Pickup Detection | **Won't** | 8.0 | Complex GPS integration and external hardware monitoring; deferred to Phase 2 to safeguard deadline. |
| **CS-12** | Social Beverage Gifting via Messaging Links | **Won't** | 5.0 | Viral growth channel; not part of core individual mobile ordering utility. Deferred to post-launch marketing sprint. |
| **CS-13** | AI Barista Flavor Recommender | **Won't** | 13.0 | High technical complexity with external LLM latency and prompt evaluation; deferred to future innovation roadmap. |

---

## 3. Scope Boundary (Won't Have — Explicitly Deferred)

The following items are **strictly excluded** from the current MVP release. Teams and contractors must not allocate sprint capacity or design time to these items during this release cycle:

1. **CS-11: Curbside Geofenced Vehicle Pickup Detection (8.0 pts):**
   - *Reason for deferral:* Requires branch hardware upgrades and geofencing testing across diverse parking layouts.
2. **CS-12: Social Beverage Gifting via Messaging Links (5.0 pts):**
   - *Reason for deferral:* Dependent on third-party link unwrapping and fraud prevention systems.
3. **CS-13: AI Barista Flavor Recommender (13.0 pts):**
   - *Reason for deferral:* Consumes 26% of total engineering capacity on speculative engagement.

---

## 4. Decision Log & Rebalancing Notes

- **Initial State:** Early stakeholder discussions proposed including *Loyalty Points (CS-08)* and *Saved Favorites (CS-05)* as Must Haves.
- **Rebalancing Action:** Moving CS-08 and CS-05 to Must would have pushed the Must Have tier to **37.0 pts (74.0%)**, directly violating the 60% cap and removing delivery contingency.
- **Resolution:**
  - *CS-05* was categorized as **Should Have** because users can manually pick items from the menu.
  - *CS-08* was categorized as **Could Have** (buffer), preserving a healthy 22% buffer that protects the launch date against backend API delays.

---

## 5. Next Steps

1. **Sprint 1 Commitment:** Lock the 4 **Must Have** items (28 pts) into Sprint 1 & Sprint 2 backlogs.
2. **Buffer Management:** Monitor velocity after Sprint 2; if velocity falls behind $\ge 15\%$, immediately deschedule **CS-10 (Dark Mode)** and **CS-09 (Barista Tips)**.
3. **Roadmap Archival:** Transfer CS-11, CS-12, and CS-13 to the Jira/Linear Phase 2 product backlog with documentation of rationale.
