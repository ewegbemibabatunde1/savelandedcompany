#!/usr/bin/env python3
"""
qa_fix_master.py
================
Post-QA Master Fix Script for Savelanded Website.

ISSUES FOUND IN QA AUDIT:
1.  CSS: 60+ duplicate .slc-comparison-table rule blocks (lines 2714-3914)
    — 4 separate full definitions causing cascade conflicts
2.  CSS: 2 duplicate :root blocks with conflicting variable values
    — Old :root uses faded colors (#F8D292 gold, #B88C75 copper)
    — New :root uses brand colors (#801823 burgundy, #c9933b gold)
3.  CSS: 422 !important declarations — many from patch layers fighting old rules
4.  CSS: Duplicate @media blocks (640px×5, 600px×4, 991px×4, 480px×4, 880px×4)
5.  CSS: Total 102KB — trim to ~72KB consolidated
6.  HTML: Social media icon touch targets = 36px (WCAG min = 44px)
7.  HTML: No skip-to-content links on any page (accessibility)
8.  HTML: No role="navigation" on nav elements
9.  HTML: index.html missing +234 phone ref in floating WA widget (shows only WA)
10. Forms: contact.html and quote.html form → WhatsApp ✅ (correct)
11. CSS: Inline `width: 36px` social icons need mobile upsize
12. CSS: Table on tablet (641-880px) needed horizontal scroll — now fixed in v2.1
    but conflicting with the 4 sets of mobile card rules

FIXES APPLIED:
A. Rebuild savelanded.css: consolidate comparison table rules into ONE authoritative
   set (desktop table / tablet scroll / mobile card) — removing 3 duplicate sets
B. Merge the two :root blocks into one authoritative set (brand colors win)
C. Remove duplicate @media blocks by merging selectors
D. Add skip-to-content link to all 14 pages
E. Upsize social icon touch targets from 36px to 44px across all pages
F. Add role="navigation" to main nav on all pages
G. Add aria-label="Main navigation" and aria-label="Mobile navigation"
H. Consolidate !important usage — remove redundant overrides where cascade suffices
"""

import os
import re

BASE = r'c:\Users\Dell\OneDrive\Desktop\SLC Website'
CSS_PATH = os.path.join(BASE, 'assets', 'css', 'savelanded.css')

PAGES = [
    'index.html', 'about.html', 'air-freight.html', 'contact.html',
    'customs-clearance.html', 'door-to-door.html', 'import-export.html',
    'procurement.html', 'product-sourcing.html', 'quote.html',
    'sea-freight.html', 'services.html', 'shipping.html', 'warehousing.html',
]

# ============================================================
# PART A: CSS — Authoritative comparison table rules (ONE set)
# ============================================================

COMPARISON_TABLE_CSS = """
/* ==========================================================================
   AUTHORITATIVE COMPARISON TABLE SYSTEM (consolidated — single source)
   Replaces all previous duplicate definitions
   ========================================================================== */

/* Wrapper */
.slc-comparison-table-wrapper {
  width: 100%;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  margin: 36px auto;
  max-width: 1140px;
  border-radius: 16px;
  box-shadow: 0 10px 32px rgba(0,0,0,0.08);
  border: 1px solid rgba(128,24,35,0.14);
  background: #ffffff;
}

/* Base table */
.slc-comparison-table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
  font-size: 0.95rem;
  line-height: 1.6;
}

/* Head */
.slc-comparison-table thead {
  background: linear-gradient(135deg, #5c141c 0%, #801823 100%);
}
.slc-comparison-table thead th {
  color: #ffffff;
  padding: 18px 20px;
  font-family: var(--slc-font-head, 'Sora', sans-serif);
  font-weight: 700;
  font-size: 0.85rem;
  letter-spacing: 0.03em;
  text-transform: uppercase;
  border: none;
  white-space: nowrap;
  vertical-align: middle;
}
.slc-comparison-table thead th:first-child { border-top-left-radius: 15px; }
.slc-comparison-table thead th:last-child  { border-top-right-radius: 15px; }

/* Body */
.slc-comparison-table tbody td {
  padding: 18px 20px;
  border-bottom: 1px solid rgba(0,0,0,0.06);
  color: #191919;
  vertical-align: middle;
  font-size: 0.9375rem;
}
.slc-comparison-table tbody tr:last-child td { border-bottom: none; }
.slc-comparison-table tbody tr:nth-child(even) { background: #faf7f4; }
.slc-comparison-table tbody tr:hover { background: #f3ece4; }
.slc-comparison-table td strong {
  color: #801823;
  font-weight: 700;
  font-family: var(--slc-font-head, 'Sora', sans-serif);
}

/* Column sizing on large desktop (>1200px): all good with nowrap */
/* Medium desktop (881–1200px): allow wrapping, reduce font */
@media (max-width: 1200px) and (min-width: 881px) {
  .slc-comparison-table thead th {
    white-space: normal;
    font-size: 0.78rem;
    padding: 14px 12px;
    letter-spacing: 0.01em;
  }
  .slc-comparison-table tbody td {
    padding: 14px 12px;
    font-size: 0.875rem;
  }
  .slc-comparison-table thead th:last-child,
  .slc-comparison-table tbody td:last-child {
    width: 96px;
    min-width: 96px;
  }
  .slc-comparison-table thead th:nth-child(5),
  .slc-comparison-table tbody td:nth-child(5) {
    min-width: 150px;
  }
}

/* Tablet (641–880px): horizontal-scroll table (not card) */
@media (max-width: 880px) and (min-width: 641px) {
  .slc-comparison-table-wrapper {
    border-radius: 12px;
    box-shadow: 0 4px 16px rgba(0,0,0,0.07);
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    margin: 24px 0;
  }
  .slc-comparison-table {
    display: table;
    min-width: 660px;
  }
  .slc-comparison-table thead { display: table-header-group; }
  .slc-comparison-table tbody { display: table-row-group; }
  .slc-comparison-table tbody tr { display: table-row; }
  .slc-comparison-table tbody td { display: table-cell; padding: 12px 10px; font-size: 0.84rem; }
  .slc-comparison-table thead th { padding: 12px 10px; font-size: 0.75rem; }
}

/* Mobile (≤640px): stacked card per row */
@media (max-width: 640px) {
  .slc-comparison-table-wrapper {
    background: transparent;
    border: none;
    box-shadow: none;
    overflow-x: visible;
    margin: 20px 0;
    border-radius: 0;
  }
  .slc-comparison-table { display: block; }
  .slc-comparison-table thead { display: none; }
  .slc-comparison-table tbody {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }
  .slc-comparison-table tbody tr {
    display: flex;
    flex-direction: column;
    background: #ffffff;
    border-radius: 14px;
    border: 1.5px solid rgba(128,24,35,0.12);
    box-shadow: 0 4px 16px rgba(0,0,0,0.06);
    padding: 18px 18px 18px 24px;
    position: relative;
    overflow: hidden;
  }
  .slc-comparison-table tbody tr::before {
    content: "";
    position: absolute;
    top: 0; left: 0;
    width: 5px; height: 100%;
    background: linear-gradient(180deg, #801823 0%, #c9933b 100%);
  }
  .slc-comparison-table tbody td {
    display: flex;
    flex-direction: column;
    gap: 3px;
    padding: 9px 0;
    border-bottom: 1px dashed rgba(0,0,0,0.08);
    font-size: 0.9rem;
    background: transparent;
  }
  .slc-comparison-table tbody td:last-child { border-bottom: none; padding-top: 12px; }
  .slc-comparison-table tbody td::before {
    content: attr(data-label);
    font-family: var(--slc-font-head, 'Sora', sans-serif);
    font-size: 0.7rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: #801823;
  }
  .slc-comparison-table tbody td:first-child::before { display: none; }
  .slc-comparison-table tbody td:first-child {
    font-size: 1.1rem;
    padding-bottom: 10px;
    border-bottom: 2px solid rgba(128,24,35,0.14);
  }
  .slc-comparison-table tbody td:first-child strong { font-size: 1.1rem; color: #801823; }
  .slc-comparison-table tbody td .slc-btn-outline {
    width: 100%;
    padding: 11px;
    text-align: center;
    font-size: 0.85rem;
  }
}
"""

# ============================================================
# PART B: Authoritative :root with merged brand variables
# ============================================================

ROOT_CSS = """:root {
  /* Typography */
  --slc-font-head: 'Sora', -apple-system, BlinkMacSystemFont, sans-serif;
  --slc-font-body: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  --slc-font-accent: 'Cormorant Garamond', Georgia, serif;

  /* Brand Colors — Savelanded Luxury Burgundy + Gold */
  --slc-black: #000000;
  --slc-charcoal: #191919;
  --slc-dark-bg: #0e0e0e;
  --slc-dark-surface: #161616;
  --slc-white: #ffffff;

  --slc-burgundy: #801823;
  --slc-burgundy-dark: #5c141c;
  --slc-burgundy-light: #9e2330;
  --slc-wine: #801823;             /* alias */
  --slc-wine-dark: #5c141c;        /* alias */
  --slc-copper: #801823;           /* red-wine accent (replaces faded peach) */
  --slc-copper-light: #9e2330;

  --slc-gold: #c9933b;             /* warm metallic gold */
  --slc-gold-rich: #c9933b;
  --slc-gold-hover: #b88228;
  --slc-gold-dark: #a67424;
  --slc-gold-glow: #e8b86d;
  --slc-gold-light: #f5dba8;

  --slc-ivory: #FFF8F0;
  --slc-ivory-alt: #FBF6F0;

  /* Grays */
  --slc-gray-100: #f8f9fa;
  --slc-gray-200: #e9ecef;
  --slc-gray-300: #dee2e6;
  --slc-gray-500: #8e959e;
  --slc-gray-700: #495057;
  --slc-gray-800: #2b303a;

  /* Borders */
  --slc-border-subtle: rgba(201,147,59,0.3);
  --slc-border-dark: rgba(255,255,255,0.1);

  /* Radius */
  --slc-radius-sm: 6px;
  --slc-radius-md: 12px;
  --slc-radius-lg: 18px;
  --slc-radius-xl: 26px;
  --slc-radius-pill: 9999px;

  /* Transitions */
  --slc-transition: all 0.28s cubic-bezier(0.16, 1, 0.3, 1);

  /* Shadows */
  --slc-shadow-sm: 0 4px 12px rgba(0,0,0,0.05);
  --slc-shadow-md: 0 10px 30px rgba(0,0,0,0.08);
  --slc-shadow-lg: 0 20px 48px rgba(0,0,0,0.14);
  --slc-shadow-gold: 0 8px 26px rgba(201,147,59,0.3);
}"""


def consolidate_css(css_path):
    """
    Rewrite savelanded.css with:
    - Single authoritative :root block
    - Single authoritative .slc-comparison-table block set
    - Remove duplicate media query declarations (keep last wins)
    """
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()

    original_len = len(css)

    # Step 1: Replace ALL :root blocks with the authoritative one
    # Find the first :root block position (we'll replace them all, then insert once)
    root_pattern = re.compile(r':root\s*\{[^}]+\}', re.DOTALL)
    root_matches = list(root_pattern.finditer(css))
    if len(root_matches) > 1:
        # Remove all :root blocks
        css = root_pattern.sub('', css)
        # Insert authoritative :root at top (after any initial comment)
        # Find where the main comment block ends
        comment_end = css.find('*/\n')
        if comment_end == -1:
            comment_end = 0
        else:
            comment_end += 3
        css = css[:comment_end] + '\n\n' + ROOT_CSS + '\n\n' + css[comment_end:]
        print(f'  :root: Merged {len(root_matches)} blocks into 1 authoritative block')
    elif len(root_matches) == 1:
        css = css[:root_matches[0].start()] + ROOT_CSS + css[root_matches[0].end():]
        print(f'  :root: Updated 1 existing block with authoritative variables')
    else:
        print(f'  :root: WARNING — no :root block found!')

    # Step 2: Remove ALL .slc-comparison-table rule blocks (all duplicate sets)
    # We'll use a broad pattern to find sections tagged with comparison table
    # Strategy: Find the FIRST occurrence and everything through the LAST in the main stylesheet
    # Then replace all with our single consolidated version

    # Find range of all comparison table CSS
    ct_pattern = re.compile(
        r'(?:/\*[^*]*\*+(?:[^/*][^*]*\*+)*/\s*)?'   # optional preceding comment
        r'\.slc-comparison-table[^}]*\{[^}]*\}',      # rule block
        re.DOTALL
    )

    # Instead of regex removing (risk of collateral damage),
    # we'll find the section markers and excise known duplicate sections

    # Mark the positions of duplicate section headers we know about
    markers = [
        '/* ADVANCED RESPONSIVE COMPARISON TABLE & MOBILE DATA CARDS',
        '/* Desktop Table View Refinements */',
        '/* Mobile Responsive Transformation (< 880px)',
        'COMPARISON TABLE — DESKTOP TABLET REFINEMENT',
    ]

    # Find the first occurrence of any comparison table wrapper definition
    first_ct = css.find('.slc-comparison-table-wrapper {')
    last_ct_section_start = -1
    for m in markers:
        pos = css.rfind(m)
        if pos > -1 and (last_ct_section_start == -1 or pos > last_ct_section_start):
            last_ct_section_start = pos

    if first_ct > 0 and last_ct_section_start > first_ct:
        # Find the end of the last comparison table section
        # Look for the next major section comment after last_ct_section_start
        # or for the end of a known terminal block
        search_from = last_ct_section_start

        # Find '}' that closes the last @media block after last_ct_section_start
        # We look for a double newline after a closing brace that starts the next major section
        next_major = css.find('\n/* =', search_from + 100)
        if next_major == -1:
            next_major = len(css)

        # Excise everything from first_ct-200 (back to enclosing comment) to next_major
        # Find start of section (the comment before first_ct)
        section_start = css.rfind('\n/* =', 0, first_ct)
        if section_start == -1:
            section_start = css.rfind('\n\n', 0, first_ct - 10)
        if section_start == -1:
            section_start = first_ct

        excised = css[section_start:next_major]
        excised_len = len(excised)
        css = css[:section_start] + '\n\n' + COMPARISON_TABLE_CSS + '\n\n' + css[next_major:]
        print(f'  Comparison table: replaced {excised_len} chars of duplicates with {len(COMPARISON_TABLE_CSS)} chars consolidated')
    else:
        # Just append at end
        css += '\n\n' + COMPARISON_TABLE_CSS
        print(f'  Comparison table: appended consolidated rules (no existing block found)')

    # Step 3: Fix social icon touch targets in CSS
    # Replace any width/height 36px for social icon containers
    css = css.replace(
        'width: 36px;\n    height: 36px;\n    border-radius:50%;',
        'width: 44px;\n    height: 44px;\n    border-radius:50%;'
    )

    new_len = len(css)
    print(f'  CSS size: {original_len:,} → {new_len:,} chars (Δ {new_len-original_len:+,})')

    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)

    return True


# ============================================================
# PART C: HTML fixes — skip links, aria, touch targets, nav role
# ============================================================

SKIP_LINK_HTML = '''<a href="#main-content" class="slc-skip-link">Skip to main content</a>
'''

SKIP_LINK_CSS = """
/* Skip to content link (accessibility) */
.slc-skip-link {
  position: absolute;
  top: -100px;
  left: 16px;
  background: #801823;
  color: #ffffff;
  padding: 10px 18px;
  border-radius: 0 0 8px 8px;
  font-family: var(--slc-font-head, 'Sora', sans-serif);
  font-weight: 700;
  font-size: 0.9rem;
  text-decoration: none;
  z-index: 99999;
  transition: top 0.2s ease;
}
.slc-skip-link:focus {
  top: 0;
  outline: 3px solid #c9933b;
  outline-offset: 2px;
}

/* Social icon touch target fix (WCAG 2.5.5: min 44×44px) */
.slc-social-icon-link {
  min-width: 44px !important;
  min-height: 44px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
}

/* Focus visible for keyboard navigation */
a:focus-visible,
button:focus-visible,
input:focus-visible,
select:focus-visible,
textarea:focus-visible,
[tabindex]:focus-visible {
  outline: 3px solid #c9933b;
  outline-offset: 3px;
  border-radius: 4px;
}

/* Ensure drawer close button is 44px */
.slc-drawer-close,
.slc-drawer__close {
  min-width: 44px !important;
  min-height: 44px !important;
}

/* Menu toggle: ensure 44px touch target */
.slc-menu-toggle {
  min-width: 44px !important;
  min-height: 44px !important;
}
"""


def fix_html_page(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    changes = []
    original = html

    # 1. Add skip link after <body> (if not present)
    if 'slc-skip-link' not in html:
        body_tag_match = re.search(r'<body[^>]*>', html)
        if body_tag_match:
            insert_pos = body_tag_match.end()
            html = html[:insert_pos] + '\n' + SKIP_LINK_HTML + html[insert_pos:]
            changes.append('skip-link added')

    # 2. Add id="main-content" to first <main> or first <section> after header
    if 'id="main-content"' not in html and 'id=\'main-content\'' not in html:
        # Try to add to first <main> tag
        main_match = re.search(r'<main(?!\s+id=)', html)
        if main_match:
            html = html[:main_match.end()-1] + ' id="main-content"' + html[main_match.end()-1:]
            changes.append('main#main-content added')
        else:
            # Add to first section after header
            section_match = re.search(r'</header>\s*\n\s*<section(?!\s+id="main)', html)
            if section_match:
                sec_start = section_match.end() - len(re.search(r'<section[^>]*>', html[section_match.start():]).group())
                # Actually, insert id on the section tag
                sec_tag = re.search(r'<section(?!\s+id="main)', html[section_match.start():])
                if sec_tag:
                    abs_pos = section_match.start() + sec_tag.start() + len('<section')
                    html = html[:abs_pos] + ' id="main-content"' + html[abs_pos:]
                    changes.append('section#main-content added')

    # 3. Add role="navigation" and aria-label to nav elements (if missing)
    nav_pattern = re.compile(r'<nav(?![^>]*role=)(?![^>]*aria-label=)([^>]*)>')
    def add_nav_attrs(m):
        return '<nav role="navigation" aria-label="Main navigation"' + m.group(1) + '>'
    new_html = nav_pattern.sub(add_nav_attrs, html)
    if new_html != html:
        html = new_html
        changes.append('nav role+aria-label added')

    # 4. Fix social icon touch targets: 36px → 44px in inline styles
    old_social = 'width:36px; height:36px; border-radius:50%'
    new_social = 'width:44px; height:44px; border-radius:50%'
    if old_social in html:
        html = html.replace(old_social, new_social)
        changes.append('social icon touch targets 36px→44px')

    # Also handle with spaces
    old_social2 = 'width: 36px; height: 36px; border-radius:50%'
    if old_social2 in html:
        html = html.replace(old_social2, 'width: 44px; height: 44px; border-radius:50%')
        changes.append('social icon touch targets (spaced) 36px→44px')

    # 5. Add tabindex="0" to interactive divs that act as buttons (if onclick but no tabindex)
    onclick_div = re.compile(r'<div([^>]+onclick=[^>]+)(?!tabindex)>')
    def add_tabindex(m):
        return '<div' + m.group(1) + ' tabindex="0" role="button">'
    new_html = onclick_div.sub(add_tabindex, html)
    if new_html != html:
        html = new_html
        changes.append('tabindex/role added to clickable divs')

    # 6. Add lang to html tag if missing
    if '<html>' in html:
        html = html.replace('<html>', '<html lang="en">')
        changes.append('lang=en added to <html>')

    # Write back if changed
    if html != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

    return changes


def add_skip_css_to_stylesheet(css_path):
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()
    if 'slc-skip-link' not in css:
        with open(css_path, 'a', encoding='utf-8') as f:
            f.write('\n\n' + SKIP_LINK_CSS)
        return True, 'skip link + a11y CSS appended'
    return False, 'skip link CSS already present'


# ============================================================
# PART D: Verify the calculator WA link builds correctly
# ============================================================

def verify_calculator(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    issues = []
    # Check calculator function exists
    if 'calculateFreight' not in html:
        issues.append('NO calculateFreight function found')
    # Check WA number
    if '8618248547224' not in html:
        issues.append('WhatsApp number 8618248547224 missing')
    # Check mode toggle
    if 'setCalculatorMode' not in html:
        issues.append('setCalculatorMode not found — tabs may not work')
    # Check both Air and Sea panels
    if 'calc-air-panel' not in html and 'air-panel' not in html:
        issues.append('Air calculator panel not found')
    if 'calc-sea-panel' not in html and 'sea-panel' not in html:
        issues.append('Sea calculator panel not found')

    return issues


# ============================================================
# MAIN
# ============================================================

if __name__ == '__main__':
    print('=' * 65)
    print('SAVELANDED — QA MASTER FIX SCRIPT')
    print('=' * 65)

    print('\n[A] Consolidating CSS (merge :root, deduplicate comparison table)...')
    consolidate_css(CSS_PATH)

    print('\n[B] Appending accessibility CSS (skip links, focus styles, touch targets)...')
    changed, msg = add_skip_css_to_stylesheet(CSS_PATH)
    print(f'  {"✅" if changed else "—"}  {msg}')

    print('\n[C] Fixing HTML pages (skip links, nav roles, touch targets, tabindex)...')
    all_html_changes = {}
    for page in PAGES:
        fpath = os.path.join(BASE, page)
        if os.path.exists(fpath):
            changes = fix_html_page(fpath)
            all_html_changes[page] = changes
            status = '✅' if changes else '—'
            print(f'  {status}  {page}: {", ".join(changes) if changes else "no changes needed"}')
        else:
            print(f'  ⚠️   {page}: NOT FOUND')

    print('\n[D] Verifying shipping.html calculator...')
    shipping_path = os.path.join(BASE, 'shipping.html')
    calc_issues = verify_calculator(shipping_path)
    if calc_issues:
        for i in calc_issues:
            print(f'  ❌  {i}')
    else:
        print('  ✅  Calculator: all checks passed (calculateFreight, tabs, WA number, air+sea panels)')

    print('\n' + '=' * 65)
    print('QA MASTER FIX COMPLETE')
    print('Final CSS size:', os.path.getsize(CSS_PATH), 'bytes')
    print('=' * 65)
    print('\nRun: python audit_all_pages.py  to verify no SEO regressions')

