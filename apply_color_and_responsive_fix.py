# -*- coding: utf-8 -*-
"""
Theme Color Restoration & Unification Script
Upgrades dull/washed-out copper (#B88C75) and pale gold (#F8D292) to
luxurious, vibrant deep burgundy (#801823 / #6a1a24) and radiant warm amber-gold (#d4a359).
Ensures strong contrast, high-end corporate feel, and perfect desktop & mobile responsive table layout.
"""

with open('responsive_table_styles.css', 'r', encoding='utf-8') as f:
    table_css = f.read()

COLOR_AND_RESPONSIVE_OVERHAUL_CSS = f"""
/* ==========================================================================
   SAVELANDED LUXURY CORPORATE BRAND COLOR & RESPONSIVENESS RESTORATION
   ========================================================================== */

:root {{
  /* Vibrant, non-faded brand colors */
  --slc-burgundy: #801823;
  --slc-burgundy-dark: #5c141c;
  --slc-burgundy-light: #9e2330;
  
  --slc-gold-rich: #c9933b;
  --slc-gold-glow: #e8b86d;
  --slc-gold-dark: #a67424;

  /* Re-energize base brand variables */
  --slc-copper: #801823 !important; /* Replaces faded dusty pink/brown with rich signature wine */
  --slc-copper-light: #9e2330 !important;
  --slc-gold: #c9933b !important; /* Replaces pale washed-out cream with warm metallic gold */
  --slc-gold-hover: #b88228 !important;
  --slc-border-subtle: rgba(201, 147, 59, 0.35) !important;
}}

/* Ensure high contrast and rich brand accents */
.slc-pill-badge--light {{
  background: rgba(128, 24, 35, 0.08) !important;
  color: #801823 !important;
  border: 1px solid rgba(128, 24, 35, 0.22) !important;
  box-shadow: 0 2px 8px rgba(128, 24, 35, 0.04) !important;
}}

.slc-pill-badge--dark {{
  background: rgba(201, 147, 59, 0.15) !important;
  color: #fce7c8 !important;
  border: 1px solid rgba(201, 147, 59, 0.35) !important;
}}

.slc-pill-dot {{
  background: #801823 !important;
}}

.slc-pill-badge--dark .slc-pill-dot {{
  background: #c9933b !important;
}}

.slc-btn-copper {{
  background-color: #801823 !important;
  border-color: #801823 !important;
  color: #ffffff !important;
  box-shadow: 0 4px 14px rgba(128, 24, 35, 0.25) !important;
}}

.slc-btn-copper:hover {{
  background-color: #5c141c !important;
  border-color: #5c141c !important;
  color: #ffffff !important;
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(128, 24, 35, 0.35) !important;
}}

.slc-btn-gold {{
  background-color: #c9933b !important;
  border-color: #c9933b !important;
  color: #ffffff !important;
  font-weight: 700 !important;
  box-shadow: 0 4px 14px rgba(201, 147, 59, 0.3) !important;
}}

.slc-btn-gold:hover {{
  background-color: #a67424 !important;
  border-color: #a67424 !important;
  color: #ffffff !important;
  transform: translateY(-2px);
}}

.slc-section-desc em, .slc-lead em, em {{
  color: #801823 !important;
  font-style: italic;
  font-weight: 600;
}}

/* Desktop Table View Refinements */
@media (min-width: 881px) {{
  .slc-comparison-table-wrapper {{
    max-width: 1140px;
    margin-left: auto;
    margin-right: auto;
  }}
  .slc-comparison-table td:first-child {{
    width: 22%;
    font-weight: 700;
  }}
  .slc-comparison-table td:last-child {{
    text-align: center;
    width: 14%;
  }}
}}

{table_css}
"""

# Append to assets/css/savelanded.css
with open('assets/css/savelanded.css', 'r', encoding='utf-8') as f:
    main_css = f.read()

# Replace or append
if 'SAVELANDED LUXURY CORPORATE BRAND COLOR' in main_css:
    idx = main_css.find('SAVELANDED LUXURY CORPORATE BRAND COLOR')
    main_css = main_css[:idx-4] # Remove old section
main_css += '\n' + COLOR_AND_RESPONSIVE_OVERHAUL_CSS

with open('assets/css/savelanded.css', 'w', encoding='utf-8') as f:
    f.write(main_css)

print("Updated assets/css/savelanded.css with brand color restoration and mobile card view.")

# Also ensure index.html links to assets/css/savelanded.css so it gets the exact styles
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

if 'assets/css/savelanded.css' not in index_html:
    target = '</head>'
    link_tag = '  <link rel="stylesheet" href="assets/css/savelanded.css">\n</head>'
    index_html = index_html.replace(target, link_tag, 1)

# Also ensure index.html internal <style> block gets the updated root color values
index_html = index_html.replace('--slc-copper: #B88C75;', '--slc-copper: #801823;')
index_html = index_html.replace('--slc-gold: #F8D292;', '--slc-gold: #c9933b;')
index_html = index_html.replace('--slc-copper-light: #d6a892;', '--slc-copper-light: #9e2330;')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print("Updated index.html: Linked assets/css/savelanded.css and energized color variables.")

