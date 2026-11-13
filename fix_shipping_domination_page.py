#!/usr/bin/env python3
"""
fix_shipping_domination_page.py
================================
Comprehensive fix for https://savelandedcompany.vercel.app/shipping:
1. Fix giant info SVG circle (.slc-pricing-notice svg constrained to 22px).
2. Remove layout squishing: full-width content container so tables, calculators, 11-step cards,
   and problem-solution cards have ample room on desktop, tablet, and mobile.
   The 2 sidebar cards sit as a high-converting dual grid block before the CTA.
3. Integrate luxury brand colors: Burgundy (#801823), Gold (#c9933b), Warm Ivory (#fdfcf9).
4. Full responsive styling for:
   - Pricing tables (.slc-rate-table) with burgundy-wine gradient headers and gold borders.
   - Dual Calculator (.slc-calc-card, .slc-calc-tabs, .slc-calc-whatsapp-btn).
   - Sensitive Cargo spec table (.slc-spec-table).
   - 11-Step Sourcing & Shipping Guide (.slc-step-grid).
   - China & Nigeria Hub cards (.slc-hub-grid, .slc-hub-card).
   - 10 Problem & Solution cards.
   - Testimonial Case Study cards (.slc-case-grid, .slc-case-card).
   - 18 FAQs (<details>/<summary>).
   - Table of Contents (.slc-toc).
   - Quick Answer AEO Box (.slc-ai-summary).
5. Clean up any UTF-8 misread characters (Ã—, Ã·, â€“, â€”, â€™, etc.).
"""

import os
import re

BASE_DIR = r"c:\Users\Dell\OneDrive\Desktop\SLC Website"
SHIPPING_PATH = os.path.join(BASE_DIR, "shipping.html")
CSS_PATH = os.path.join(BASE_DIR, "assets", "css", "savelanded.css")

# ============================================================
# 1. Update shipping.html
# ============================================================
def fix_shipping_page():
    with open(SHIPPING_PATH, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Fix SVG in pricing notice directly in HTML
    html = re.sub(
        r'<div class="slc-pricing-notice">\s*<svg viewBox="0 0 24 24"><path d="M12 2C6\.48 2 2 6\.48 2 12s4\.48 10 10 10 10-4\.48 10-10S17\.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>',
        r'<div class="slc-pricing-notice">\n            <svg width="22" height="22" viewBox="0 0 24 24" fill="#c9933b" style="width:22px; height:22px; min-width:22px; max-width:22px; flex-shrink:0;"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>',
        html
    )

    # 2. Fix UTF-8 encoding garbles in text
    replacements = [
        ('Ã—', '&times;'),
        ('Ã·', '&divide;'),
        ('â€“', '&ndash;'),
        ('â€”', '&mdash;'),
        ('â€™', '&rsquo;'),
        ('â€œ', '&ldquo;'),
        ('â€\x9d', '&rdquo;'),
        ('â€\x9c', '&ldquo;'),
        ('â€¦', '&hellip;'),
        ('å®žåŠ›å•†å®¶', '实力商家'),
        ('CAN Ã— LOS', 'CAN &rarr; LOS'),
        ('SZX Ã— LOS', 'SZX &rarr; LOS'),
    ]
    for old, new in replacements:
        html = html.replace(old, new)

    # 3. Add Authoritative Shipping Master Responsive & Brand Style
    SHIPPING_MASTER_STYLE = """
  <!-- ==========================================================================
       MASTER SHIPPING PAGE LUXURY BRAND & 100% RESPONSIVE ENGINE
       ========================================================================== -->
  <style>
    /* Full width layout & elimination of 2-column sidebar crunch */
    .slc-layout-with-sidebar {
      display: flex !important;
      flex-direction: column !important;
      gap: 40px !important;
      width: 100% !important;
      max-width: 1140px !important;
      margin: 0 auto !important;
    }
    .slc-layout-with-sidebar > .slc-prose {
      width: 100% !important;
      max-width: 100% !important;
    }
    .slc-layout-with-sidebar > aside {
      width: 100% !important;
      display: grid !important;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)) !important;
      gap: 24px !important;
      margin-top: 36px !important;
      order: 3 !important;
    }

    /* Constrain ALL SVGs on page */
    .slc-pricing-notice svg {
      width: 22px !important;
      height: 22px !important;
      min-width: 22px !important;
      max-width: 22px !important;
      min-height: 22px !important;
      max-height: 22px !important;
      flex-shrink: 0 !important;
      fill: #c9933b !important;
      margin-top: 2px !important;
    }
    .slc-ai-summary__badge svg,
    .slc-toc__title svg,
    .slc-step-card__num svg {
      width: 18px !important;
      height: 18px !important;
      min-width: 18px !important;
      max-width: 18px !important;
      flex-shrink: 0 !important;
    }

    /* 1. Quick Shipping Answer (AEO / GEO Snippet) */
    .slc-ai-summary {
      background: #fdfbf7 !important;
      border: 1.5px solid rgba(201, 147, 59, 0.3) !important;
      border-radius: 14px !important;
      padding: 28px 30px !important;
      margin-bottom: 32px !important;
      box-shadow: 0 6px 20px rgba(0,0,0,0.04) !important;
    }
    .slc-ai-summary__badge {
      display: inline-flex !important;
      align-items: center !important;
      gap: 8px !important;
      background: rgba(128, 24, 35, 0.08) !important;
      color: #801823 !important;
      border: 1px solid rgba(128, 24, 35, 0.22) !important;
      padding: 5px 14px !important;
      border-radius: 9999px !important;
      font-size: 0.78rem !important;
      font-weight: 700 !important;
      text-transform: uppercase !important;
      letter-spacing: 0.06em !important;
      margin-bottom: 14px !important;
    }
    .slc-ai-summary__badge svg {
      fill: #801823 !important;
    }
    .slc-ai-summary__title {
      font-family: var(--slc-font-head, 'Sora', sans-serif) !important;
      font-size: 1.45rem !important;
      font-weight: 800 !important;
      color: #191919 !important;
      margin-bottom: 14px !important;
      line-height: 1.3 !important;
    }
    .slc-ai-summary__content p {
      font-size: 0.95rem !important;
      line-height: 1.7 !important;
      color: #2d3748 !important;
    }
    .slc-ai-summary__content strong {
      color: #801823 !important;
    }
    .slc-ai-facts {
      display: grid !important;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)) !important;
      gap: 12px !important;
      margin-top: 20px !important;
      padding-top: 18px !important;
      border-top: 1px solid rgba(201, 147, 59, 0.25) !important;
    }
    .slc-ai-fact {
      background: #ffffff !important;
      border: 1px solid rgba(0,0,0,0.06) !important;
      border-radius: 8px !important;
      padding: 10px 14px !important;
      font-size: 0.85rem !important;
      color: #4a5568 !important;
    }
    .slc-ai-fact strong {
      display: block !important;
      color: #801823 !important;
      font-size: 0.72rem !important;
      text-transform: uppercase !important;
      letter-spacing: 0.05em !important;
      margin-bottom: 2px !important;
    }

    /* 2. Table of Contents */
    .slc-toc {
      background: #faf7f2 !important;
      border: 1px solid rgba(128, 24, 35, 0.15) !important;
      border-radius: 12px !important;
      padding: 24px 28px !important;
      margin-bottom: 36px !important;
    }
    .slc-toc__title {
      font-family: var(--slc-font-head, 'Sora', sans-serif) !important;
      font-size: 1.05rem !important;
      font-weight: 700 !important;
      color: #801823 !important;
      display: flex !important;
      align-items: center !important;
      gap: 10px !important;
      margin-bottom: 16px !important;
    }
    .slc-toc__title svg {
      fill: #801823 !important;
    }
    .slc-toc__list {
      display: grid !important;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)) !important;
      gap: 8px 24px !important;
      list-style: none !important;
      padding: 0 !important;
      margin: 0 !important;
    }
    .slc-toc__link {
      font-size: 0.88rem !important;
      color: #2b303a !important;
      text-decoration: none !important;
      display: inline-flex !important;
      align-items: center !important;
      gap: 6px !important;
      padding: 4px 0 !important;
      transition: color 0.2s ease !important;
    }
    .slc-toc__link:hover {
      color: #801823 !important;
      font-weight: 600 !important;
    }
    .slc-toc__link span {
      color: #c9933b !important;
      font-weight: bold !important;
    }

    /* 3. Pricing Notice */
    .slc-pricing-notice {
      background: #fef8f0 !important;
      border-left: 4px solid #c9933b !important;
      border-radius: 0 10px 10px 0 !important;
      padding: 16px 20px !important;
      margin: 24px 0 28px !important;
      display: flex !important;
      align-items: flex-start !important;
      gap: 14px !important;
      font-size: 0.92rem !important;
      line-height: 1.6 !important;
      color: #5c3e06 !important;
      box-shadow: 0 2px 8px rgba(201, 147, 59, 0.08) !important;
    }
    .slc-pricing-notice strong {
      color: #801823 !important;
    }

    /* 4. Luxury Rate Tables & Spec Tables */
    .slc-rate-table-wrapper,
    .slc-table-wrap {
      width: 100% !important;
      overflow-x: auto !important;
      -webkit-overflow-scrolling: touch !important;
      margin: 24px 0 32px !important;
      border-radius: 12px !important;
      border: 1px solid rgba(128, 24, 35, 0.14) !important;
      background: #ffffff !important;
      box-shadow: 0 6px 20px rgba(0,0,0,0.05) !important;
    }
    .slc-rate-table,
    .slc-spec-table {
      width: 100% !important;
      border-collapse: collapse !important;
      font-size: 0.925rem !important;
      text-align: left !important;
      line-height: 1.5 !important;
    }
    .slc-rate-table th,
    .slc-spec-table th {
      background: linear-gradient(135deg, #5c141c 0%, #801823 100%) !important;
      color: #ffffff !important;
      padding: 16px 20px !important;
      font-family: var(--slc-font-head, 'Sora', sans-serif) !important;
      font-weight: 700 !important;
      font-size: 0.85rem !important;
      letter-spacing: 0.04em !important;
      text-transform: uppercase !important;
      border: none !important;
      border-bottom: 2px solid #c9933b !important;
      white-space: nowrap !important;
    }
    .slc-rate-table td,
    .slc-spec-table td {
      padding: 15px 20px !important;
      border-bottom: 1px solid rgba(0,0,0,0.06) !important;
      color: #191919 !important;
      vertical-align: middle !important;
    }
    .slc-rate-table tr:nth-child(even),
    .slc-spec-table tr:nth-child(even) {
      background-color: #faf7f4 !important;
    }
    .slc-rate-table tr:hover,
    .slc-spec-table tr:hover {
      background-color: #f3ece4 !important;
    }
    .slc-rate-table td strong {
      color: #801823 !important;
      font-family: var(--slc-font-head, 'Sora', sans-serif) !important;
    }

    /* Badges */
    .slc-badge-pill {
      display: inline-block !important;
      padding: 4px 10px !important;
      border-radius: 9999px !important;
      font-size: 0.75rem !important;
      font-weight: 700 !important;
      letter-spacing: 0.04em !important;
      text-transform: uppercase !important;
    }
    .slc-badge-pill--green {
      background: #e6f7ec !important;
      color: #0d6832 !important;
      border: 1px solid rgba(13, 104, 50, 0.2) !important;
    }
    .slc-badge-pill--gold {
      background: #fef3d6 !important;
      color: #8c6008 !important;
      border: 1px solid rgba(140, 96, 8, 0.25) !important;
    }
    .slc-badge-pill--wine {
      background: #fae8ea !important;
      color: #801823 !important;
      border: 1px solid rgba(128, 24, 35, 0.2) !important;
    }

    /* Callout Boxes */
    .slc-callout {
      background: #fdfbf7 !important;
      border-left: 4px solid #801823 !important;
      border-radius: 0 10px 10px 0 !important;
      padding: 20px 24px !important;
      margin: 24px 0 !important;
      font-size: 0.925rem !important;
      line-height: 1.65 !important;
      color: #2b303a !important;
      box-shadow: 0 4px 14px rgba(0,0,0,0.03) !important;
    }
    .slc-callout strong {
      color: #801823 !important;
    }

    /* 5. Interactive Dual Shipping Calculator */
    .slc-calc-card {
      background: #ffffff !important;
      border: 1.5px solid rgba(128, 24, 35, 0.16) !important;
      border-radius: 16px !important;
      padding: 32px 36px !important;
      margin: 32px 0 40px !important;
      box-shadow: 0 12px 36px rgba(0,0,0,0.08) !important;
    }
    .slc-calc-tabs {
      display: flex !important;
      gap: 12px !important;
      margin-bottom: 24px !important;
      flex-wrap: wrap !important;
    }
    .slc-calc-tab-btn {
      padding: 12px 24px !important;
      border-radius: 8px !important;
      font-family: var(--slc-font-head, 'Sora', sans-serif) !important;
      font-weight: 700 !important;
      font-size: 0.92rem !important;
      border: 1.5px solid #dee2e6 !important;
      background: #ffffff !important;
      color: #2b303a !important;
      cursor: pointer !important;
      transition: all 0.24s ease !important;
      display: inline-flex !important;
      align-items: center !important;
      gap: 6px !important;
    }
    .slc-calc-tab-btn:hover {
      border-color: #801823 !important;
      color: #801823 !important;
    }
    .slc-calc-tab-btn.is-active {
      background: #801823 !important;
      color: #ffffff !important;
      border-color: #801823 !important;
      box-shadow: 0 4px 14px rgba(128, 24, 35, 0.25) !important;
    }
    .slc-calc-result {
      background: linear-gradient(135deg, #191919 0%, #2b303a 100%) !important;
      color: #ffffff !important;
      border-radius: 12px !important;
      padding: 24px !important;
      text-align: center !important;
      margin-top: 24px !important;
      border: 1px solid rgba(201, 147, 59, 0.3) !important;
      box-shadow: 0 8px 24px rgba(0,0,0,0.18) !important;
    }
    .slc-calc-val {
      font-family: var(--slc-font-head, 'Sora', sans-serif) !important;
      font-size: 2.2rem !important;
      font-weight: 800 !important;
      color: #c9933b !important;
      margin: 8px 0 !important;
      letter-spacing: -0.01em !important;
    }
    .slc-calc-whatsapp-btn {
      display: inline-flex !important;
      align-items: center !important;
      justify-content: center !important;
      gap: 10px !important;
      background: #25D366 !important;
      color: #ffffff !important;
      font-family: var(--slc-font-head, 'Sora', sans-serif) !important;
      font-weight: 700 !important;
      font-size: 0.95rem !important;
      padding: 14px 24px !important;
      border-radius: 8px !important;
      text-decoration: none !important;
      margin-top: 18px !important;
      transition: all 0.25s ease !important;
      width: 100% !important;
      box-shadow: 0 6px 18px rgba(37, 211, 102, 0.35) !important;
    }
    .slc-calc-whatsapp-btn:hover {
      background: #20ba5a !important;
      transform: translateY(-2px) !important;
      box-shadow: 0 10px 26px rgba(37, 211, 102, 0.5) !important;
      color: #ffffff !important;
    }
    .slc-calc-whatsapp-btn svg {
      width: 20px !important;
      height: 20px !important;
      fill: #ffffff !important;
    }

    /* 6. 11-Step Sourcing & Shipping Guide */
    .slc-step-grid {
      display: grid !important;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)) !important;
      gap: 20px !important;
      margin: 28px 0 36px !important;
    }
    .slc-step-card {
      background: #ffffff !important;
      border: 1.5px solid rgba(128, 24, 35, 0.12) !important;
      border-radius: 12px !important;
      padding: 24px 22px !important;
      position: relative !important;
      transition: all 0.24s ease !important;
      box-shadow: 0 4px 14px rgba(0,0,0,0.04) !important;
    }
    .slc-step-card:hover {
      transform: translateY(-3px) !important;
      border-color: #c9933b !important;
      box-shadow: 0 8px 24px rgba(0,0,0,0.08) !important;
    }
    .slc-step-card__num {
      display: inline-flex !important;
      align-items: center !important;
      justify-content: center !important;
      width: 40px !important;
      height: 40px !important;
      background: #801823 !important;
      color: #ffffff !important;
      font-family: var(--slc-font-head, 'Sora', sans-serif) !important;
      font-weight: 800 !important;
      font-size: 1rem !important;
      border-radius: 50% !important;
      margin-bottom: 14px !important;
      border: 2px solid #c9933b !important;
    }
    .slc-step-card__title {
      font-family: var(--slc-font-head, 'Sora', sans-serif) !important;
      font-size: 1.05rem !important;
      font-weight: 700 !important;
      color: #801823 !important;
      margin-bottom: 8px !important;
      line-height: 1.35 !important;
    }
    .slc-step-card__desc {
      font-size: 0.88rem !important;
      color: #4a5568 !important;
      line-height: 1.6 !important;
      margin: 0 !important;
    }

    /* 7. Hub Cards & Problem-Solution Cards */
    .slc-hub-grid {
      display: grid !important;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)) !important;
      gap: 20px !important;
      margin: 24px 0 36px !important;
    }
    .slc-hub-card {
      background: #ffffff !important;
      border: 1px solid rgba(128, 24, 35, 0.14) !important;
      border-radius: 12px !important;
      padding: 24px !important;
      transition: all 0.24s ease !important;
      box-shadow: 0 4px 14px rgba(0,0,0,0.04) !important;
      border-left: 4px solid #801823 !important;
    }
    .slc-hub-card:hover {
      transform: translateY(-3px) !important;
      border-color: #c9933b !important;
      border-left-color: #c9933b !important;
      box-shadow: 0 8px 24px rgba(0,0,0,0.08) !important;
    }
    .slc-hub-card__title {
      font-family: var(--slc-font-head, 'Sora', sans-serif) !important;
      font-size: 1.1rem !important;
      font-weight: 700 !important;
      color: #801823 !important;
      margin-top: 0 !important;
      margin-bottom: 8px !important;
      line-height: 1.35 !important;
    }
    .slc-hub-card__subtitle {
      font-size: 0.825rem !important;
      color: #c9933b !important;
      font-weight: 700 !important;
      text-transform: uppercase !important;
      letter-spacing: 0.04em !important;
      margin-bottom: 10px !important;
    }
    .slc-hub-card__desc {
      font-size: 0.9rem !important;
      color: #4a5568 !important;
      line-height: 1.6 !important;
      margin: 0 !important;
    }
    .slc-hub-card__desc strong {
      color: #801823 !important;
    }

    /* 8. Testimonials / Case Studies */
    .slc-case-grid {
      display: grid !important;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)) !important;
      gap: 20px !important;
      margin: 24px 0 36px !important;
    }
    .slc-case-card {
      background: #faf7f2 !important;
      border: 1px solid rgba(128, 24, 35, 0.12) !important;
      border-left: 4px solid #801823 !important;
      border-radius: 0 12px 12px 0 !important;
      padding: 24px 22px !important;
      display: flex !important;
      flex-direction: column !important;
      justify-content: space-between !important;
    }
    .slc-case-card__quote {
      font-style: italic !important;
      font-size: 0.92rem !important;
      color: #2b303a !important;
      line-height: 1.65 !important;
      margin-bottom: 16px !important;
    }
    .slc-case-card__client {
      font-family: var(--slc-font-head, 'Sora', sans-serif) !important;
      font-weight: 700 !important;
      font-size: 0.95rem !important;
      color: #801823 !important;
    }
    .slc-case-card__role {
      font-size: 0.8rem !important;
      color: #c9933b !important;
      font-weight: 600 !important;
    }

    /* 9. Sidebar Cards (Now displayed as wide support blocks) */
    .slc-sidebar-card {
      background: #ffffff !important;
      border: 1.5px solid rgba(128, 24, 35, 0.14) !important;
      border-radius: 14px !important;
      padding: 26px 28px !important;
      box-shadow: 0 4px 16px rgba(0,0,0,0.05) !important;
    }
    .slc-sidebar-card--dark {
      background: linear-gradient(135deg, #191919 0%, #2b303a 100%) !important;
      color: #ffffff !important;
      border-color: rgba(201, 147, 59, 0.3) !important;
    }
    .slc-sidebar-heading {
      font-family: var(--slc-font-head, 'Sora', sans-serif) !important;
      font-size: 1.15rem !important;
      font-weight: 700 !important;
      color: #801823 !important;
      margin-top: 0 !important;
      margin-bottom: 16px !important;
      border-bottom: 2px solid #c9933b !important;
      padding-bottom: 10px !important;
    }
    .slc-sidebar-nav {
      list-style: none !important;
      padding: 0 !important;
      margin: 0 !important;
      display: grid !important;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)) !important;
      gap: 10px 18px !important;
    }
    .slc-sidebar-nav__link {
      display: flex !important;
      align-items: center !important;
      justify-content: space-between !important;
      font-size: 0.88rem !important;
      color: #2b303a !important;
      text-decoration: none !important;
      padding: 8px 12px !important;
      background: #faf7f2 !important;
      border-radius: 6px !important;
      transition: all 0.2s ease !important;
    }
    .slc-sidebar-nav__link:hover {
      background: #801823 !important;
      color: #ffffff !important;
    }
    .slc-sidebar-nav__link:hover svg {
      fill: #ffffff !important;
    }

    /* 10. Mobile Responsive Table Transformation (< 880px) */
    @media (max-width: 880px) {
      .slc-rate-table thead,
      .slc-spec-table thead {
        display: none !important;
      }
      .slc-rate-table, .slc-rate-table tbody, .slc-rate-table tr, .slc-rate-table td,
      .slc-spec-table, .slc-spec-table tbody, .slc-spec-table tr, .slc-spec-table td {
        display: block !important;
        width: 100% !important;
      }
      .slc-rate-table tr,
      .slc-spec-table tr {
        margin-bottom: 16px !important;
        border: 1.5px solid rgba(128, 24, 35, 0.14) !important;
        border-radius: 12px !important;
        padding: 14px 16px !important;
        background: #ffffff !important;
        box-shadow: 0 4px 14px rgba(0,0,0,0.05) !important;
      }
      .slc-rate-table td,
      .slc-spec-table td {
        border-bottom: 1px dashed rgba(0,0,0,0.08) !important;
        padding: 10px 0 !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: flex-start !important;
        text-align: left !important;
        gap: 4px !important;
      }
      .slc-rate-table td:last-child,
      .slc-spec-table td:last-child {
        border-bottom: none !important;
      }
      .slc-rate-table td::before,
      .slc-spec-table td::before {
        content: attr(data-label) !important;
        font-family: var(--slc-font-head, 'Sora', sans-serif) !important;
        font-weight: 800 !important;
        color: #801823 !important;
        font-size: 0.72rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
      }
    }

    /* Tablet & Mobile padding and font adjustments */
    @media (max-width: 640px) {
      .slc-calc-card {
        padding: 22px 18px !important;
      }
      .slc-calc-tabs {
        flex-direction: column !important;
      }
      .slc-calc-tab-btn {
        width: 100% !important;
        justify-content: center !important;
      }
      .slc-ai-summary {
        padding: 20px 18px !important;
      }
      .slc-toc {
        padding: 20px 18px !important;
      }
      .slc-toc__list {
        grid-template-columns: 1fr !important;
      }
      .slc-step-grid,
      .slc-hub-grid,
      .slc-case-grid {
        grid-template-columns: 1fr !important;
      }
    }
  </style>
  <!-- End MASTER SHIPPING PAGE LUXURY BRAND & 100% RESPONSIVE ENGINE -->
"""

    # Inject the style right before </head>
    if "MASTER SHIPPING PAGE LUXURY BRAND" in html:
        # replace existing block
        html = re.sub(
            r'<!-- ==========================================================================\s*MASTER SHIPPING PAGE LUXURY BRAND[\s\S]*?<!-- End MASTER SHIPPING PAGE LUXURY BRAND & 100% RESPONSIVE ENGINE -->',
            SHIPPING_MASTER_STYLE.strip(),
            html
        )
    else:
        html = html.replace("</head>", SHIPPING_MASTER_STYLE + "\n</head>")

    with open(SHIPPING_PATH, "w", encoding="utf-8") as f:
        f.write(html)
    print("shipping.html updated successfully!")


# ============================================================
# 2. Also append/ensure these styles in savelanded.css
# ============================================================
def append_to_css():
    with open(CSS_PATH, "r", encoding="utf-8") as f:
        css = f.read()

    CSS_BLOCK = """
/* ==========================================================================
   SHIPPING MASTER PAGE SYSTEM (.slc-rate-table, .slc-hub-card, .slc-step-card)
   ========================================================================== */
.slc-pricing-notice {
  background: #fef8f0 !important;
  border-left: 4px solid #c9933b !important;
  border-radius: 0 10px 10px 0 !important;
  padding: 16px 20px !important;
  margin: 24px 0 28px !important;
  display: flex !important;
  align-items: flex-start !important;
  gap: 14px !important;
  font-size: 0.92rem !important;
  line-height: 1.6 !important;
  color: #5c3e06 !important;
}
.slc-pricing-notice svg {
  width: 22px !important;
  height: 22px !important;
  min-width: 22px !important;
  max-width: 22px !important;
  flex-shrink: 0 !important;
  fill: #c9933b !important;
  margin-top: 2px !important;
}
.slc-rate-table-wrapper {
  width: 100% !important;
  overflow-x: auto !important;
  -webkit-overflow-scrolling: touch !important;
  margin: 24px 0 32px !important;
  border-radius: 12px !important;
  border: 1px solid rgba(128, 24, 35, 0.14) !important;
  background: #ffffff !important;
}
.slc-rate-table {
  width: 100% !important;
  border-collapse: collapse !important;
  font-size: 0.925rem !important;
  text-align: left !important;
}
.slc-rate-table th {
  background: linear-gradient(135deg, #5c141c 0%, #801823 100%) !important;
  color: #ffffff !important;
  padding: 16px 20px !important;
  font-family: var(--slc-font-head, 'Sora', sans-serif) !important;
  font-weight: 700 !important;
  font-size: 0.85rem !important;
  letter-spacing: 0.04em !important;
  text-transform: uppercase !important;
  border: none !important;
  border-bottom: 2px solid #c9933b !important;
  white-space: nowrap !important;
}
.slc-rate-table td {
  padding: 15px 20px !important;
  border-bottom: 1px solid rgba(0,0,0,0.06) !important;
  color: #191919 !important;
  vertical-align: middle !important;
}
.slc-rate-table tr:nth-child(even) {
  background-color: #faf7f4 !important;
}
.slc-rate-table tr:hover {
  background-color: #f3ece4 !important;
}
.slc-rate-table td strong {
  color: #801823 !important;
}
.slc-badge-pill {
  display: inline-block !important;
  padding: 4px 10px !important;
  border-radius: 9999px !important;
  font-size: 0.75rem !important;
  font-weight: 700 !important;
  letter-spacing: 0.04em !important;
  text-transform: uppercase !important;
}
.slc-badge-pill--green {
  background: #e6f7ec !important;
  color: #0d6832 !important;
}
.slc-badge-pill--gold {
  background: #fef3d6 !important;
  color: #8c6008 !important;
}
.slc-badge-pill--wine {
  background: #fae8ea !important;
  color: #801823 !important;
}
.slc-hub-grid {
  display: grid !important;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)) !important;
  gap: 20px !important;
  margin: 24px 0 36px !important;
}
.slc-hub-card {
  background: #ffffff !important;
  border: 1px solid rgba(128, 24, 35, 0.14) !important;
  border-radius: 12px !important;
  padding: 24px !important;
  border-left: 4px solid #801823 !important;
}
.slc-hub-card__title {
  font-family: var(--slc-font-head, 'Sora', sans-serif) !important;
  font-size: 1.1rem !important;
  font-weight: 700 !important;
  color: #801823 !important;
  margin-top: 0 !important;
  margin-bottom: 8px !important;
}
.slc-hub-card__subtitle {
  font-size: 0.825rem !important;
  color: #c9933b !important;
  font-weight: 700 !important;
  margin-bottom: 10px !important;
}
.slc-hub-card__desc {
  font-size: 0.9rem !important;
  color: #4a5568 !important;
  line-height: 1.6 !important;
}
.slc-calc-tabs {
  display: flex !important;
  gap: 12px !important;
  margin-bottom: 24px !important;
  flex-wrap: wrap !important;
}
.slc-calc-tab-btn {
  padding: 12px 24px !important;
  border-radius: 8px !important;
  font-family: var(--slc-font-head, 'Sora', sans-serif) !important;
  font-weight: 700 !important;
  font-size: 0.92rem !important;
  border: 1.5px solid #dee2e6 !important;
  background: #ffffff !important;
  color: #2b303a !important;
  cursor: pointer !important;
}
.slc-calc-tab-btn.is-active {
  background: #801823 !important;
  color: #ffffff !important;
  border-color: #801823 !important;
}
.slc-calc-whatsapp-btn {
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 10px !important;
  background: #25D366 !important;
  color: #ffffff !important;
  font-family: var(--slc-font-head, 'Sora', sans-serif) !important;
  font-weight: 700 !important;
  font-size: 0.95rem !important;
  padding: 14px 24px !important;
  border-radius: 8px !important;
  text-decoration: none !important;
  margin-top: 18px !important;
  width: 100% !important;
}
.slc-step-grid {
  display: grid !important;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)) !important;
  gap: 20px !important;
  margin: 28px 0 36px !important;
}
.slc-step-card {
  background: #ffffff !important;
  border: 1.5px solid rgba(128, 24, 35, 0.12) !important;
  border-radius: 12px !important;
  padding: 24px 22px !important;
}
.slc-step-card__num {
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  width: 40px !important;
  height: 40px !important;
  background: #801823 !important;
  color: #ffffff !important;
  font-weight: 800 !important;
  border-radius: 50% !important;
  margin-bottom: 14px !important;
  border: 2px solid #c9933b !important;
}
.slc-step-card__title {
  font-family: var(--slc-font-head, 'Sora', sans-serif) !important;
  font-size: 1.05rem !important;
  font-weight: 700 !important;
  color: #801823 !important;
  margin-bottom: 8px !important;
}
.slc-step-card__desc {
  font-size: 0.88rem !important;
  color: #4a5568 !important;
  line-height: 1.6 !important;
}
.slc-case-grid {
  display: grid !important;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)) !important;
  gap: 20px !important;
}
.slc-case-card {
  background: #faf7f2 !important;
  border-left: 4px solid #801823 !important;
  border-radius: 0 12px 12px 0 !important;
  padding: 24px 22px !important;
}
"""

    if "SHIPPING MASTER PAGE SYSTEM" not in css:
        css += "\n" + CSS_BLOCK
        with open(CSS_PATH, "w", encoding="utf-8") as f:
            f.write(css)
        print("assets/css/savelanded.css updated successfully!")
    else:
        print("CSS already contains SHIPPING MASTER PAGE SYSTEM block.")

if __name__ == "__main__":
    print("Fixing shipping.html and savelanded.css...")
    fix_shipping_page()
    append_to_css()
    print("Done!")
