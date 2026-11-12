#!/usr/bin/env python3
"""
fix_all_issues.py
=================
Comprehensive fix for Savelanded website:
1. Fix all garbled UTF-8 characters (â€" → –, â€™ → ', etc.) across all HTML files
2. Improve the CSS for the 6-column comparison table on desktop
3. Add tablet breakpoint for the table (880px–1200px range)
4. Fix rate table mobile display on shipping.html
"""

import re
import os

# ------------------------------------------------------------------
# 1. UTF-8 garbled character repair map (latin-1 misread of UTF-8)
# ------------------------------------------------------------------
ENCODING_FIXES = [
    # Em dash (—) → U+2014
    ('â€"', '&mdash;'),
    # En dash (–) → U+2013
    ('â€"', '&ndash;'),  # sometimes same bytes
    # Right single quotation mark (') → U+2019
    ('â€™', '&rsquo;'),
    # Left double quotation mark (") → U+201C
    ('â€œ', '&ldquo;'),
    # Right double quotation mark (") → U+201D
    ('â€\x9d', '&rdquo;'),
    # Ellipsis (…) → U+2026
    ('â€¦', '&hellip;'),
    # Non-breaking space (Â ) — just remove the Â
    ('Â ', ' '),
    # Bullet (•) garbled
    ('â€¢', '&bull;'),
    # Trade mark ™
    ('â„¢', '&trade;'),
    # Copyright ©
    ('Â©', '&copy;'),
    # Registered ®
    ('Â®', '&reg;'),
    # Degree °
    ('Â°', '&deg;'),
    # Fraction ½
    ('Â½', '&frac12;'),
    # Euro €
    ('â‚¬', '&euro;'),
    # Left angle quote «
    ('Â«', '&laquo;'),
    # Right angle quote »
    ('Â»', '&raquo;'),
    # Acute accent accented chars
    ('Ã©', '&eacute;'),
    ('Ã¨', '&egrave;'),
    ('Ã ', '&agrave;'),
    ('Ã¢', '&acirc;'),
    ('Ã®', '&icirc;'),
    ('Ã´', '&ocirc;'),
    ('Ã»', '&ucirc;'),
    ('Ã¼', '&uuml;'),
    ('Ã¶', '&ouml;'),
    ('Ã¤', '&auml;'),
    ('Ã±', '&ntilde;'),
    # Chinese dash used in badge: Chinaâ€"Nigeria → China&mdash;Nigeria
    # Already covered above with â€"
]

# A second pass: direct byte-sequence replacement using the actual
# Windows-1252 / Latin-1 misread of UTF-8 sequences
RAW_FIXES = [
    (b'\xe2\x80\x93', '&ndash;'),   # – (en dash)
    (b'\xe2\x80\x94', '&mdash;'),   # — (em dash)
    (b'\xe2\x80\x99', '&rsquo;'),   # ' (right single quote)
    (b'\xe2\x80\x9c', '&ldquo;'),   # " (left double quote)
    (b'\xe2\x80\x9d', '&rdquo;'),   # " (right double quote)
    (b'\xe2\x80\xa6', '&hellip;'),  # … (ellipsis)
    (b'\xe2\x80\xa2', '&bull;'),    # • (bullet)
    (b'\xc2\xa0', ' '),             # Non-breaking space
    (b'\xc2\xa9', '&copy;'),        # ©
    (b'\xc2\xae', '&reg;'),         # ®
    (b'\xc2\xb0', '&deg;'),         # °
    (b'\xe2\x84\xa2', '&trade;'),   # ™
    (b'\xe2\x82\xac', '&euro;'),    # €
]


def fix_encoding_in_file(filepath):
    """Read file as bytes, fix UTF-8 sequences that were saved as latin-1 garbles."""
    try:
        # Read as bytes first
        with open(filepath, 'rb') as f:
            raw = f.read()

        # Try to detect if the file is actually valid UTF-8
        try:
            text = raw.decode('utf-8')
            # It's valid UTF-8 — but may have garbled visible text from previous save
            # Apply string-level fixes for garbled patterns
            original = text
            for broken, fixed in ENCODING_FIXES:
                text = text.replace(broken, fixed)
            if text != original:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(text)
                return True, 'string-level fixes applied'
            return False, 'no changes needed (already clean UTF-8)'
        except UnicodeDecodeError:
            # File is latin-1/windows-1252 — fix at byte level
            fixed_parts = []
            i = 0
            changed = False
            while i < len(raw):
                replaced = False
                for seq, replacement in RAW_FIXES:
                    if raw[i:i+len(seq)] == seq:
                        fixed_parts.append(replacement.encode('ascii'))
                        i += len(seq)
                        replaced = True
                        changed = True
                        break
                if not replaced:
                    fixed_parts.append(raw[i:i+1])
                    i += 1
            if changed:
                result = b''.join(fixed_parts)
                with open(filepath, 'wb') as f:
                    f.write(result)
                return True, 'byte-level fixes applied'
            return False, 'no changes needed'
    except Exception as e:
        return False, f'ERROR: {e}'


def fix_all_html_files(base_dir):
    html_files = [f for f in os.listdir(base_dir) if f.endswith('.html') and f != 'google6d0656f586d536b2.html']
    results = []
    for fname in sorted(html_files):
        fpath = os.path.join(base_dir, fname)
        changed, msg = fix_encoding_in_file(fpath)
        results.append((fname, changed, msg))
    return results


# ------------------------------------------------------------------
# 2. CSS Improvements for the 6-column comparison table
# ------------------------------------------------------------------
CSS_ADDITION = """

/* ==========================================================================
   COMPARISON TABLE — DESKTOP TABLET REFINEMENT (fix 6-column overflow)
   Added by fix_all_issues.py
   ========================================================================== */

/* Medium screens: allow wrapping in table header cells */
@media (max-width: 1200px) and (min-width: 881px) {
  .slc-comparison-table thead th {
    white-space: normal !important;
    font-size: 0.8rem !important;
    padding: 14px 14px !important;
    letter-spacing: 0.02em !important;
  }
  .slc-comparison-table tbody td {
    padding: 14px 14px !important;
    font-size: 0.88rem !important;
  }
  /* Slim the Action column */
  .slc-comparison-table tbody td:last-child,
  .slc-comparison-table thead th:last-child {
    width: 90px !important;
    min-width: 90px !important;
  }
  /* Give the cargo description column more room */
  .slc-comparison-table tbody td:nth-child(5),
  .slc-comparison-table thead th:nth-child(5) {
    min-width: 160px !important;
  }
}

/* Large desktop: enforce nowrap only on first 2 columns */
@media (min-width: 1201px) {
  .slc-comparison-table thead th {
    white-space: nowrap !important;
  }
  .slc-comparison-table tbody td {
    padding: 18px 20px !important;
  }
}

/* Tablet portrait (641px–880px): switch to compact horizontal scroll */
@media (max-width: 880px) and (min-width: 641px) {
  .slc-comparison-table-wrapper {
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
    border-radius: 12px !important;
    border: 1px solid rgba(128,24,35,0.14) !important;
    background: #ffffff !important;
    box-shadow: 0 4px 16px rgba(0,0,0,0.06) !important;
  }
  .slc-comparison-table {
    display: table !important;
    min-width: 640px !important;
  }
  .slc-comparison-table thead {
    display: table-header-group !important;
  }
  .slc-comparison-table tbody {
    display: table-row-group !important;
    flex-direction: unset !important;
    gap: unset !important;
  }
  .slc-comparison-table tbody tr {
    display: table-row !important;
    padding: 0 !important;
    border-radius: 0 !important;
    border: none !important;
    box-shadow: none !important;
  }
  .slc-comparison-table tbody tr::before {
    display: none !important;
  }
  .slc-comparison-table tbody td {
    display: table-cell !important;
    padding: 12px 14px !important;
    border-bottom: 1px solid rgba(0,0,0,0.06) !important;
    font-size: 0.85rem !important;
    flex-direction: unset !important;
  }
  .slc-comparison-table tbody td::before {
    display: none !important;
  }
}

/* Rate table (pricing tables on /shipping): improved mobile display */
@media (max-width: 880px) {
  .slc-rate-table-wrapper {
    border: none !important;
    box-shadow: none !important;
    background: transparent !important;
    overflow-x: visible !important;
    padding: 0 !important;
  }
  .slc-rate-table {
    display: block !important;
  }
  .slc-rate-table thead {
    display: none !important;
  }
  .slc-rate-table tbody,
  .slc-rate-table tr,
  .slc-rate-table td {
    display: block !important;
    width: 100% !important;
  }
  .slc-rate-table tr {
    margin-bottom: 16px !important;
    background: #ffffff !important;
    border: 1.5px solid rgba(128,24,35,0.12) !important;
    border-radius: 12px !important;
    padding: 14px 16px !important;
    box-shadow: 0 4px 14px rgba(0,0,0,0.05) !important;
  }
  .slc-rate-table td {
    display: flex !important;
    justify-content: space-between !important;
    align-items: flex-start !important;
    gap: 12px !important;
    padding: 8px 0 !important;
    border-bottom: 1px dashed rgba(0,0,0,0.08) !important;
    font-size: 0.9rem !important;
    text-align: right !important;
  }
  .slc-rate-table td:last-child {
    border-bottom: none !important;
  }
  .slc-rate-table td::before {
    content: attr(data-label) !important;
    font-weight: 700 !important;
    color: #801823 !important;
    font-size: 0.8rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.04em !important;
    text-align: left !important;
    flex: 1 !important;
    white-space: nowrap !important;
  }
}

/* Hero section fix: prevent text overflow on small screens */
@media (max-width: 480px) {
  .slc-hero__title,
  .slc-page-hero__title,
  h1 {
    font-size: clamp(1.6rem, 7vw, 2.2rem) !important;
    line-height: 1.2 !important;
  }
  h2, .slc-section-title {
    font-size: clamp(1.25rem, 5.5vw, 1.8rem) !important;
  }
  .slc-container {
    padding-left: 14px !important;
    padding-right: 14px !important;
  }
}

/* Stats / counters row: prevent overflow on mobile */
@media (max-width: 600px) {
  .slc-stats-grid,
  .slc-stats-row {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 16px !important;
  }
  .slc-stat-value {
    font-size: clamp(1.6rem, 7vw, 2.4rem) !important;
  }
}

/* Nav drawer fix: ensure full-width on mobile */
@media (max-width: 991px) {
  .slc-drawer {
    width: 100% !important;
    max-width: 340px !important;
  }
  .slc-drawer__nav {
    padding: 20px 0 !important;
  }
  .slc-drawer__nav a {
    font-size: 1.1rem !important;
    padding: 14px 24px !important;
    display: block !important;
  }
}

/* Footer grid: single column on mobile */
@media (max-width: 640px) {
  .slc-footer__grid {
    grid-template-columns: 1fr !important;
    gap: 32px !important;
  }
  .slc-footer__bottom {
    flex-direction: column !important;
    text-align: center !important;
    gap: 12px !important;
  }
}

/* TOC (table of contents on /shipping): wraps on mobile */
@media (max-width: 640px) {
  .slc-toc__list {
    columns: 1 !important;
  }
  .slc-toc {
    padding: 18px 16px !important;
  }
}

/* Calculator card: full width on mobile */
@media (max-width: 640px) {
  .slc-calc-card {
    padding: 20px 16px !important;
  }
  .slc-calc-tabs {
    flex-direction: column !important;
    gap: 8px !important;
  }
  .slc-calc-tab-btn {
    width: 100% !important;
    text-align: center !important;
  }
}

/* Pricing notice: stack icon and text on tiny screens */
@media (max-width: 480px) {
  .slc-pricing-notice {
    flex-direction: column !important;
    gap: 8px !important;
  }
}

/* Hub cards: single column on very small phones */
@media (max-width: 480px) {
  .slc-hub-grid,
  .slc-case-grid,
  .slc-step-grid,
  .slc-feature-grid-3,
  .slc-feature-grid-2 {
    grid-template-columns: 1fr !important;
  }
}

/* AEO snippet / fact chips: wrap on mobile */
@media (max-width: 600px) {
  .slc-aeo-chips,
  .slc-fact-chips {
    flex-direction: column !important;
    align-items: flex-start !important;
  }
}

/* Page hero actions: stack vertically on mobile */
@media (max-width: 480px) {
  .slc-page-hero__actions {
    flex-direction: column !important;
    gap: 10px !important;
    width: 100% !important;
  }
  .slc-page-hero__actions .slc-btn,
  .slc-page-hero__actions a {
    width: 100% !important;
    text-align: center !important;
    justify-content: center !important;
  }
}
"""


def add_css_improvements(css_path):
    """Append CSS improvements if not already added."""
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()

    marker = 'COMPARISON TABLE — DESKTOP TABLET REFINEMENT'
    if marker in css:
        return False, 'CSS improvements already applied'

    with open(css_path, 'a', encoding='utf-8') as f:
        f.write(CSS_ADDITION)
    return True, 'CSS improvements appended'


# ------------------------------------------------------------------
# 3. Main execution
# ------------------------------------------------------------------
if __name__ == '__main__':
    base = r'c:\Users\Dell\OneDrive\Desktop\SLC Website'
    css_file = os.path.join(base, 'assets', 'css', 'savelanded.css')

    print('=' * 60)
    print('SAVELANDED — COMPREHENSIVE FIX SCRIPT')
    print('=' * 60)

    print('\n[1/2] Fixing garbled UTF-8 encoding in HTML files...\n')
    results = fix_all_html_files(base)
    for fname, changed, msg in results:
        status = '✅ FIXED' if changed else '—'
        print(f'  {status}  {fname}: {msg}')

    print(f'\n[2/2] Adding CSS responsive improvements...\n')
    changed, msg = add_css_improvements(css_file)
    status = '✅ DONE' if changed else '—'
    print(f'  {status}  savelanded.css: {msg}')

    print('\n' + '=' * 60)
    print('ALL FIXES COMPLETE')
    print('=' * 60)
    print('\nNext step: git add -A && git commit -m "Fix UTF-8 encoding and table responsiveness" && git push')

