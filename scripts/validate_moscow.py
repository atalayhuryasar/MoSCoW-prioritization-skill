#!/usr/bin/env python3
"""
MoSCoW Prioritization & 60/20/20 Rule Validator
Validates requirement effort distribution against Agile MoSCoW budgeting rules.
Zero external dependencies (uses standard library only).
"""

import sys
import json
import os

VALID_CATEGORIES = {
    "must": "Must Have",
    "must have": "Must Have",
    "should": "Should Have",
    "should have": "Should Have",
    "could": "Could Have",
    "could have": "Could Have",
    "wont": "Won't Have",
    "won't": "Won't Have",
    "won't have": "Won't Have",
    "wont have": "Won't Have"
}

def print_usage():
    print("Usage: python validate_moscow.py <path/to/input.json>")
    print("\nExpected JSON format:")
    print(json.dumps({
        "project": "Project Name (optional)",
        "items": [
            {"name": "Feature A", "category": "must", "effort": 5},
            {"name": "Feature B", "category": "should", "effort": 3},
            {"name": "Feature C", "category": "could", "effort": 2},
            {"name": "Feature D", "category": "wont", "effort": 8}
        ]
    }, indent=2))

def normalize_category(cat_str):
    if not isinstance(cat_str, str):
        return None
    cleaned = cat_str.strip().lower()
    return VALID_CATEGORIES.get(cleaned)

def main():
    if len(sys.argv) < 2:
        print("❌ Error: Missing input JSON file path.\n")
        print_usage()
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print(f"❌ Error: File not found at '{file_path}'.")
        sys.exit(1)

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON syntax in '{file_path}': {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error reading file '{file_path}': {e}")
        sys.exit(1)

    project_name = data.get("project", "MoSCoW Prioritization Analysis") if isinstance(data, dict) else "MoSCoW Prioritization Analysis"
    items = data.get("items") if isinstance(data, dict) else data

    if not isinstance(items, list):
        print("❌ Error: Input JSON must contain an 'items' array.")
        sys.exit(1)

    if len(items) == 0:
        print("ℹ️ Info: The 'items' list is empty. Nothing to validate.")
        sys.exit(0)

    category_efforts = {
        "Must Have": 0.0,
        "Should Have": 0.0,
        "Could Have": 0.0,
        "Won't Have": 0.0
    }

    category_counts = {
        "Must Have": 0,
        "Should Have": 0,
        "Could Have": 0,
        "Won't Have": 0
    }

    warnings = []
    unrecognized_items = []

    for index, item in enumerate(items, start=1):
        if not isinstance(item, dict):
            warnings.append(f"Item #{index} is not a valid dictionary object. Skipped.")
            continue

        name = item.get("name", f"Item #{index}")
        raw_category = item.get("category", "")
        raw_effort = item.get("effort", 0)

        try:
            effort = float(raw_effort)
            if effort < 0:
                warnings.append(f"Item '{name}' has negative effort ({effort}). Treated as 0.")
                effort = 0.0
        except (ValueError, TypeError):
            warnings.append(f"Item '{name}' has invalid effort '{raw_effort}'. Treated as 0.")
            effort = 0.0

        normalized = normalize_category(raw_category)
        if normalized:
            category_efforts[normalized] += effort
            category_counts[normalized] += 1
        else:
            unrecognized_items.append((name, raw_category, effort))
            warnings.append(f"Item '{name}' has unrecognized category '{raw_category}'. Excluded from calculation.")

    active_effort = (
        category_efforts["Must Have"]
        + category_efforts["Should Have"]
        + category_efforts["Could Have"]
    )
    deferred_effort = category_efforts["Won't Have"]
    total_effort = active_effort + deferred_effort

    if active_effort == 0:
        print("\n============================================================")
        print("ℹ️ Info: Total active effort (Must + Should + Could) is 0.")
        print(f"Deferred (Won't Have) effort: {deferred_effort:.1f}")
        print("Nothing to evaluate for the active release.")
        print("============================================================\n")
        sys.exit(0)

    must_pct = (category_efforts["Must Have"] / active_effort) * 100
    should_pct = (category_efforts["Should Have"] / active_effort) * 100
    could_pct = (category_efforts["Could Have"] / active_effort) * 100

    # Rule Validations
    must_pass = must_pct <= 60.0
    should_pass = 15.0 <= should_pct <= 25.0
    could_pass = 15.0 <= could_pct <= 25.0

    print("\n" + "=" * 66)
    print(f"            MoSCoW 60/20/20 Validation Report")
    print("=" * 66)
    print(f"Project:               {project_name}")
    print(f"Total Evaluated Items: {len(items)}")
    print(f"Active Release Effort: {active_effort:.1f} pts (Excludes deferred Won't Have)")
    wont_count = category_counts["Won't Have"]
    print(f"Deferred Scope Effort: {deferred_effort:.1f} pts ({wont_count} items)")
    print("-" * 66)
    print(f"{'Category':<14} {'Count':<7} {'Effort':<9} {'Share':<9} {'Target':<12} {'Status'}")
    print("-" * 66)

    # Must Have
    must_status = "[PASS] ✅" if must_pass else f"[FAIL] ❌ (>60%)"
    print(f"{'Must Have':<14} {category_counts['Must Have']:<7} {category_efforts['Must Have']:<9.1f} {must_pct:<8.1f}% {'<= 60.0%':<12} {must_status}")

    # Should Have
    should_status = "[PASS] ✅" if should_pass else f"[WARN] ⚠️"
    print(f"{'Should Have':<14} {category_counts['Should Have']:<7} {category_efforts['Should Have']:<9.1f} {should_pct:<8.1f}% {'15% - 25%':<12} {should_status}")

    # Could Have
    could_status = "[PASS] ✅" if could_pass else f"[WARN] ⚠️"
    print(f"{'Could Have':<14} {category_counts['Could Have']:<7} {category_efforts['Could Have']:<9.1f} {could_pct:<8.1f}% {'15% - 25%':<12} {could_status}")

    # Won't Have
    wont_label = "Won't Have"
    print(f"{wont_label:<14} {wont_count:<7} {deferred_effort:<9.1f} {'0.0% (def.)':<9} {'Deferred':<12} {'[DEFERRED] 📦'}")
    print("-" * 66)

    # Output Warnings if any
    if warnings:
        print("\n⚠️ Warnings & Notices:")
        for w in warnings:
            print(f"  • {w}")

    # Final Verdict
    print("\n" + "=" * 66)
    if not must_pass:
        print("❌ VERDICT: FAIL — Must Have budget exceeds the 60% hard limit!")
        print(f"   Current Must Have is {must_pct:.1f}% ({category_efforts['Must Have']:.1f}/{active_effort:.1f} pts).")
        print("   Recommendation: Demote lower-urgency Must Have items to Should Have.")
        print("=" * 66 + "\n")
        sys.exit(1)
    elif not (should_pass and could_pass):
        print("⚠️ VERDICT: PASS WITH WARNINGS — 60% Must Have rule satisfied,")
        print("   but Should Have or Could Have ratios deviate from the 15–25% guideline.")
        print("=" * 66 + "\n")
        sys.exit(0)
    else:
        print("✅ VERDICT: PASS — Perfect compliance with the 60/20/20 rule!")
        print("============================================================\n")
        sys.exit(0)

if __name__ == "__main__":
    main()
