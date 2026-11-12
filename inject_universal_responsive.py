# -*- coding: utf-8 -*-
"""
Universal Mobile & Desktop Responsive Engine for Savelanded
Resolves all viewport issues:
1. Tables: Turns all tables (.slc-comparison-table, .slc-spec-table) into cards on screens < 880px
2. Overflow prevention: Ensures all tables, pre, code, and grids have max-width: 100% and break-word
3. Sidebar Layouts: Switches from 2fr 1fr to 1fr on tablets and mobile with optimal ordering
4. Hero Banners: Uses fluid responsive typography and fluid padding on mobile and desktop
5. Touch Targets: Ensures navigation, drawers, buttons, and floating icons are accessible on touch devices
"""

UNIVERSAL_RESPONSIVE_OVERHAUL_CSS = """
/* ==========================================================================
   SAVELANDED 100% UNIVERSAL RESPONSIVE ENGINE (MOBILE + TABLET + DESKTOP)
   ========================================================================== */

/* 1. Universal Layout & Box Sizing Protection */
html, body {
  width: 100% !important;
  max-width: 100vw !important;
  overflow-x: hidden !important;
  position: relative !important;
  margin: 0 !important;
  padding: 0 !important;
  -webkit-text-size-adjust: 100% !important;
}

*, *::before, *::after {
  box-sizing: border-box !important;
}

img, video, iframe, svg, canvas {
  max-width: 100% !important;
  height: auto !important;
}

/* 2. Fluid Containers */
.slc-container {
  width: 100% !important;
  max-width: 1240px !important;
  margin-left: auto !important;
  margin-right: auto !important;
  padding-left: clamp(16px, 4vw, 32px) !important;
  padding-right: clamp(16px, 4vw, 32px) !important;
}

/* 3. Fluid Responsive Typography */
h1, .slc-hero__title, .slc-page-hero__title {
  font-size: clamp(1.85rem, 5vw, 3.4rem) !important;
  line-height: 1.15 !important;
  word-wrap: break-word !important;
  overflow-wrap: break-word !important;
}

h2, .slc-section-title, .slc-prose h2 {
  font-size: clamp(1.45rem, 3.8vw, 2.3rem) !important;
  line-height: 1.25 !important;
  word-wrap: break-word !important;
}

h3, .slc-feature-box__title, .slc-prose h3 {
  font-size: clamp(1.15rem, 2.6vw, 1.45rem) !important;
  line-height: 1.35 !important;
}

p, .slc-prose p, .slc-section-desc {
  word-wrap: break-word !important;
  overflow-wrap: break-word !important;
}

/* 4. Complete Mobile Card Transformation for ALL Tables (< 880px) */
@media (max-width: 880px) {
  .slc-table-wrap,
  .slc-comparison-table-wrapper {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    overflow-x: visible !important;
    margin: 24px 0 !important;
    width: 100% !important;
  }

  .slc-spec-table,
  .slc-comparison-table {
    display: block !important;
    width: 100% !important;
    border: none !important;
  }

  .slc-spec-table thead,
  .slc-comparison-table thead {
    display: none !important; /* Hide rigid tabular header on mobile */
  }

  .slc-spec-table tbody,
  .slc-comparison-table tbody {
    display: flex !important;
    flex-direction: column !important;
    gap: 16px !important;
    width: 100% !important;
  }

  .slc-spec-table tbody tr,
  .slc-comparison-table tbody tr {
    display: flex !important;
    flex-direction: column !important;
    background: #ffffff !important;
    border-radius: 14px !important;
    border: 1.5px solid rgba(128, 24, 35, 0.15) !important;
    box-shadow: 0 4px 18px rgba(0, 0, 0, 0.06) !important;
    padding: 16px 18px !important;
    position: relative !important;
    overflow: hidden !important;
  }

  .slc-spec-table tbody tr::before,
  .slc-comparison-table tbody tr::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 5px;
    height: 100%;
    background: linear-gradient(180deg, #801823 0%, #c9933b 100%);
  }

  .slc-spec-table tbody td,
  .slc-comparison-table tbody td {
    display: flex !important;
    flex-direction: column !important;
    gap: 4px !important;
    padding: 8px 0 !important;
    border: none !important;
    border-bottom: 1px dashed rgba(0, 0, 0, 0.08) !important;
    text-align: left !important;
    font-size: 0.92rem !important;
    background: transparent !important;
  }

  .slc-spec-table tbody td:last-child,
  .slc-comparison-table tbody td:last-child {
    border-bottom: none !important;
    padding-top: 12px !important;
  }

  .slc-spec-table tbody td::before,
  .slc-comparison-table tbody td::before {
    content: attr(data-label);
    font-family: var(--slc-font-head, 'Sora', sans-serif);
    font-size: 0.72rem !important;
    font-weight: 800 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.06em !important;
    color: #801823 !important;
  }

  .slc-spec-table tbody td:first-child,
  .slc-comparison-table tbody td:first-child {
    padding-bottom: 10px !important;
    border-bottom: 2px solid rgba(128, 24, 35, 0.15) !important;
  }

  .slc-spec-table tbody td:first-child strong,
  .slc-comparison-table tbody td:first-child strong {
    font-size: 1.1rem !important;
    color: #801823 !important;
  }
}

/* 5. Desktop Table View Perfect Alignment (>= 881px) */
@media (min-width: 881px) {
  .slc-table-wrap,
  .slc-comparison-table-wrapper {
    width: 100% !important;
    max-width: 1140px !important;
    margin: 32px auto !important;
    border-radius: 14px !important;
    overflow: hidden !important;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.06) !important;
    border: 1px solid rgba(128, 24, 35, 0.14) !important;
  }

  .slc-spec-table,
  .slc-comparison-table {
    width: 100% !important;
    border-collapse: collapse !important;
    display: table !important;
  }

  .slc-spec-table thead,
  .slc-comparison-table thead {
    display: table-header-group !important;
    background: linear-gradient(135deg, #5c141c 0%, #801823 100%) !important;
  }

  .slc-spec-table th,
  .slc-comparison-table thead th {
    color: #ffffff !important;
    padding: 16px 20px !important;
    font-family: var(--slc-font-head, 'Sora', sans-serif) !important;
    font-weight: 700 !important;
    font-size: 0.85rem !important;
    letter-spacing: 0.04em !important;
    text-transform: uppercase !important;
    border: none !important;
  }

  .slc-spec-table tbody,
  .slc-comparison-table tbody {
    display: table-row-group !important;
  }

  .slc-spec-table tbody tr,
  .slc-comparison-table tbody tr {
    display: table-row !important;
  }

  .slc-spec-table tbody td,
  .slc-comparison-table tbody td {
    display: table-cell !important;
    padding: 16px 20px !important;
    border-bottom: 1px solid rgba(0, 0, 0, 0.06) !important;
    vertical-align: middle !important;
  }
}

/* 6. Layout With Sidebar Responsive Rules */
.slc-layout-with-sidebar {
  display: grid !important;
  grid-template-columns: 2fr 1fr !important;
  gap: 40px !important;
  align-items: start !important;
}

@media (max-width: 991px) {
  .slc-layout-with-sidebar {
    grid-template-columns: 1fr !important;
    gap: 36px !important;
  }
  
  .slc-layout-with-sidebar > aside {
    order: 2 !important;
    width: 100% !important;
  }

  .slc-layout-with-sidebar > .slc-prose,
  .slc-layout-with-sidebar > div:first-child {
    order: 1 !important;
    width: 100% !important;
  }
}

/* 7. Feature Grids, Step Grids & Cards */
.slc-step-grid {
  display: grid !important;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)) !important;
  gap: 20px !important;
  margin: 28px 0 !important;
}

.slc-feature-grid-3 {
  display: grid !important;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)) !important;
  gap: 24px !important;
  margin: 32px 0 !important;
}

.slc-feature-grid-2 {
  display: grid !important;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)) !important;
  gap: 24px !important;
  margin: 32px 0 !important;
}

/* 8. Mobile Buttons & Touch Targets */
@media (max-width: 640px) {
  .slc-hero__actions,
  .slc-page-hero__actions,
  .slc-cta__actions {
    flex-direction: column !important;
    width: 100% !important;
    gap: 12px !important;
  }

  .slc-hero__actions .slc-btn,
  .slc-page-hero__actions .slc-btn,
  .slc-cta__actions .slc-btn {
    width: 100% !important;
    justify-content: center !important;
    padding: 14px 20px !important;
  }

  .slc-form-grid {
    grid-template-columns: 1fr !important;
    gap: 14px !important;
  }

  .slc-calc-card,
  .slc-form-card,
  .slc-ai-summary,
  .slc-toc {
    padding: 20px 16px !important;
  }
}

/* 9. Header & Drawer Responsiveness */
@media (max-width: 991px) {
  .slc-nav,
  .slc-nav-wrap,
  .slc-header__cta {
    display: none !important;
  }

  .slc-menu-toggle {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    width: 44px !important;
    height: 44px !important;
    background: #f7fafc !important;
    border: 1.5px solid #cbd5e0 !important;
    border-radius: 8px !important;
    cursor: pointer !important;
  }

  .slc-header__inner {
    height: 72px !important;
  }
}

/* 10. Word Break & Code Blocks */
code, pre {
  max-width: 100% !important;
  word-break: break-all !important;
  white-space: pre-wrap !important;
}
"""

with open('assets/css/savelanded.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace or append
if 'SAVELANDED 100% UNIVERSAL RESPONSIVE ENGINE' in css:
    idx = css.find('SAVELANDED 100% UNIVERSAL RESPONSIVE ENGINE')
    css = css[:idx-4]

css += '\n' + UNIVERSAL_RESPONSIVE_OVERHAUL_CSS

with open('assets/css/savelanded.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("SUCCESS: Injected UNIVERSAL_RESPONSIVE_OVERHAUL_CSS into assets/css/savelanded.css")

