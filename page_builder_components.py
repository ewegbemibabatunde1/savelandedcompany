import os
import json

def build_comparison_table(headers, rows):
    th_html = "".join([f"<th>{h}</th>" for h in headers])
    tr_html = ""
    for r in rows:
        td_html = "".join([f"<td>{d}</td>" for d in r])
        tr_html += f"<tr>{td_html}</tr>\n"
    return f"""
<div class="slc-comparison-table-wrapper">
  <table class="slc-comparison-table">
    <thead><tr>{th_html}</tr></thead>
    <tbody>
      {tr_html}
    </tbody>
  </table>
</div>
"""

def build_step_grid(steps):
    cards = ""
    for i, (title, desc) in enumerate(steps, 1):
        cards += f"""
    <div class="slc-step-card">
      <div class="slc-step-num">{i}</div>
      <h3 class="slc-step-title">{title}</h3>
      <p class="slc-step-text">{desc}</p>
    </div>
"""
    return f"""
<div class="slc-step-grid">
  {cards}
</div>
"""

def build_definition_box(term, desc):
    return f"""
<div class="slc-definition-box">
  <div class="slc-definition-term">{term}</div>
  <p class="slc-definition-desc">{desc}</p>
</div>
"""

def build_reviewer_badge(reviewer_name, title, update_date="November 2026"):
    initials = "".join([part[0] for part in reviewer_name.split()[:2]])
    return f"""
<div class="slc-reviewer-badge">
  <div class="slc-reviewer-avatar">{initials}</div>
  <div>
    <strong>Verified by {reviewer_name}</strong> &bull; {title}<br>
    <span style="font-size:0.8rem; color:#718096;">Content updated & operational compliance checked: {update_date}</span>
  </div>
</div>
"""

print("Defined helper components in page_builder_components.py")
