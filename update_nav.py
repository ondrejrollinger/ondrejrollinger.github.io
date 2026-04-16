#!/usr/bin/env python3
"""Replace ## Quick Navigation blocks with new table-based ## Navigation blocks."""

import re
import os

BASE = "/home/user/ondrejrollinger.github.io/secplus/objectives"

# ── Domain 4 data ─────────────────────────────────────────────────────────────
D4_OBJECTIVES = [
    ("4.1", "4-1", "Given a scenario, apply common security techniques to computing resources."),
    ("4.2", "4-2", "Explain the security implications of proper hardware, software, and data asset management."),
    ("4.3", "4-3", "Explain various activities associated with vulnerability management."),
    ("4.4", "4-4", "Explain security alerting and monitoring concepts and tools."),
    ("4.5", "4-5", "Given a scenario, modify enterprise capabilities to enhance security."),
    ("4.6", "4-6", "Given a scenario, implement and maintain identity and access management."),
    ("4.7", "4-7", "Explain the importance of automation and orchestration related to secure operations."),
    ("4.8", "4-8", "Explain appropriate incident response activities."),
    ("4.9", "4-9", "Given a scenario, use data sources to support an investigation."),
]

# ── Domain 5 data ─────────────────────────────────────────────────────────────
D5_OBJECTIVES = [
    ("5.1", "5-1", "Summarize elements of effective security governance."),
    ("5.2", "5-2", "Explain elements of the risk management process."),
    ("5.3", "5-3", "Explain the processes associated with third-party risk assessment and management."),
    ("5.4", "5-4", "Summarize elements of effective security compliance."),
    ("5.5", "5-5", "Explain types and purposes of audits and assessments."),
    ("5.6", "5-6", "Given a scenario, implement security awareness practices."),
]


def make_nav_block(domain_label, domain_name, objectives, current_slug, status, footer_line):
    """Build the full ## Navigation replacement block."""
    lines = []
    lines.append("## Navigation")
    lines.append("")
    lines.append(f"**{domain_label}: {domain_name}**")
    lines.append("")
    lines.append("| Objective | Title | Status |")
    lines.append("|---|---|---|")
    for obj_num, obj_slug, obj_title in objectives:
        url = "{{% raw %}}{{ '/secplus/objectives/{slug}/' | relative_url }}{{% endraw %}}".format(slug=obj_slug)
        # Use raw Jekyll syntax (no escaping needed in the actual file)
        url = "{{{{ '/secplus/objectives/{slug}/' | relative_url }}}}".format(slug=obj_slug)
        if obj_slug == current_slug:
            lines.append(f"| **{obj_num}** | {obj_title} (current) | {status} |")
        else:
            lines.append(f"| [{obj_num}]({url}) | {obj_title} | {status} |")
    lines.append("")
    lines.append(footer_line)
    return "\n".join(lines)


def url(slug):
    return "{{{{ '/secplus/objectives/{slug}/' | relative_url }}}}".format(slug=slug)


def dashboard_url():
    return "{{ '/secplus/' | relative_url }}"


def make_footer_d4(slug):
    idx = [s for _, s, _ in D4_OBJECTIVES].index(slug)
    dash = "{{ '/secplus/' | relative_url }}"
    if slug == "4-1":
        return (
            f"[← Previous: Domain 3]({url('3-4')}) | "
            f"[Back to Dashboard]({dash}) | "
            f"[Next: Objective 4.2 →]({url('4-2')})"
        )
    elif slug == "4-9":
        return (
            f"[← Previous: Objective 4.8]({url('4-8')}) | "
            f"[Back to Dashboard]({dash}) | "
            f"[Next: Domain 5 →]({url('5-1')})"
        )
    else:
        prev_slug = D4_OBJECTIVES[idx - 1][1]
        next_slug = D4_OBJECTIVES[idx + 1][1]
        prev_num = D4_OBJECTIVES[idx - 1][0]
        next_num = D4_OBJECTIVES[idx + 1][0]
        return (
            f"[← Previous: Objective {prev_num}]({url(prev_slug)}) | "
            f"[Back to Dashboard]({dash}) | "
            f"[Next: Objective {next_num} →]({url(next_slug)})"
        )


def make_footer_d5(slug):
    idx = [s for _, s, _ in D5_OBJECTIVES].index(slug)
    dash = "{{ '/secplus/' | relative_url }}"
    if slug == "5-1":
        return (
            f"[← Previous: Domain 4]({url('4-9')}) | "
            f"[Back to Dashboard]({dash}) | "
            f"[Next: Objective 5.2 →]({url('5-2')})"
        )
    elif slug == "5-6":
        return (
            f"[← Previous: Objective 5.5]({url('5-5')}) | "
            f"[Back to Dashboard]({dash}) | "
            f"[Next: Dashboard →]({dash})"
        )
    else:
        prev_slug = D5_OBJECTIVES[idx - 1][1]
        next_slug = D5_OBJECTIVES[idx + 1][1]
        prev_num = D5_OBJECTIVES[idx - 1][0]
        next_num = D5_OBJECTIVES[idx + 1][0]
        return (
            f"[← Previous: Objective {prev_num}]({url(prev_slug)}) | "
            f"[Back to Dashboard]({dash}) | "
            f"[Next: Objective {next_num} →]({url(next_slug)})"
        )


def get_status(content):
    m = re.search(r'^status:\s*["\']?(\w[\w-]*)["\']?', content, re.MULTILINE)
    return m.group(1) if m else "pending"


# Regex to match the entire ## Quick Navigation or ## Navigation section
# (from the heading to end of file, including any leading ---)
NAV_PATTERN = re.compile(
    r'\n---\n\n## (?:Quick Navigation|Navigation).*$',
    re.DOTALL
)

results = []

all_files = (
    [(slug, "4") for _, slug, _ in D4_OBJECTIVES] +
    [(slug, "5") for _, slug, _ in D5_OBJECTIVES]
)

for slug, domain in all_files:
    filepath = os.path.join(BASE, slug, "index.md")
    with open(filepath, "r") as fh:
        content = fh.read()

    old_found = bool(re.search(r'## (?:Quick Navigation|Navigation)', content))
    status = get_status(content)

    if domain == "4":
        footer = make_footer_d4(slug)
        nav_block = make_nav_block(
            "Domain 4.0", "Security Operations",
            D4_OBJECTIVES, slug, status, footer
        )
    else:
        footer = make_footer_d5(slug)
        nav_block = make_nav_block(
            "Domain 5.0", "Security Program Management and Oversight",
            D5_OBJECTIVES, slug, status, footer
        )

    new_section = f"\n---\n\n{nav_block}"
    new_content, n_subs = NAV_PATTERN.subn(new_section, content)

    replaced = n_subs > 0
    if replaced:
        with open(filepath, "w") as fh:
            fh.write(new_content)

    results.append((filepath.replace(BASE + "/", ""), old_found, replaced))

# Print summary table
print(f"{'File':<30} {'Old nav found':>14} {'Replaced':>10}")
print("-" * 58)
for fname, found, replaced in results:
    print(f"{fname:<30} {'yes' if found else 'no':>14} {'yes' if replaced else 'no':>10}")
