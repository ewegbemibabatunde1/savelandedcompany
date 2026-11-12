#!/usr/bin/env python3
"""
fix_responsive_all_pages.py
============================
Inject a universal responsive <style> block into every page's <head>
to fix mobile + desktop rendering across all pages.
Targets:
  - Hero section mobile padding / font clamping
  - Inline stats rows wrapping  
  - Corridor bar wrapping
  - Service card grids
  - Contact form responsiveness
  - Page hero (subpage) padding
  - Table overflow on medium desktop (641-880px)
  - Drawer nav accessibility
  - Footer grid stacking
"""

import os
import re

PAGES = [
    'index.html',
    'about.html',
    'air-freight.html',
    'contact.html',
    'customs-clearance.html',
    'door-to-door.html',
    'import-export.html',
    'procurement.html',
    'product-sourcing.html',
    'quote.html',
    'sea-freight.html',
    'services.html',
    'shipping.html',
    'warehousing.html',
]

UNIVERSAL_RESPONSIVE_STYLE = """
  <!-- Universal Responsive Engine v2.1 (injected by fix_responsive_all_pages.py) -->
  <style>
    /* ======================================================
       SAVELANDED UNIVERSAL RESPONSIVE ENGINE v2.1
       Covers: mobile phones, tablets, desktops
       ====================================================== */

    /* 1. Base reset */
    *, *::before, *::after { box-sizing: border-box !important; }
    html, body {
      max-width: 100vw !important;
      overflow-x: hidden !important;
    }
    img, video, iframe, embed { max-width: 100% !important; height: auto !important; }

    /* 2. Container fluid */
    .slc-container {
      width: 100% !important;
      max-width: 1240px !important;
      margin-left: auto !important;
      margin-right: auto !important;
      padding-left: clamp(16px, 4vw, 32px) !important;
      padding-right: clamp(16px, 4vw, 32px) !important;
    }

    /* 3. Fluid typography */
    h1, .slc-hero__title, .slc-page-hero__title {
      font-size: clamp(1.75rem, 5.5vw, 3.8rem) !important;
      line-height: 1.18 !important;
      word-break: break-word !important;
      overflow-wrap: break-word !important;
    }
    h2, .slc-section-title {
      font-size: clamp(1.4rem, 4vw, 2.4rem) !important;
      line-height: 1.28 !important;
      word-break: break-word !important;
    }
    h3 { font-size: clamp(1.1rem, 2.8vw, 1.5rem) !important; }
    p, li { word-break: break-word !important; overflow-wrap: break-word !important; }

    /* 4. Navigation */
    @media (max-width: 991px) {
      .slc-nav, .slc-nav-wrap, .slc-header__cta { display: none !important; }
      .slc-menu-toggle {
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        width: 44px !important; height: 44px !important;
        background: rgba(255,255,255,0.1) !important;
        border: 1.5px solid rgba(255,255,255,0.3) !important;
        border-radius: 8px !important; cursor: pointer !important;
      }
      .slc-header__inner { height: 68px !important; }
      .slc-logo { max-height: 48px !important; width: auto !important; }
    }
    .slc-drawer {
      position: fixed !important; top: 0 !important; right: 0 !important;
      width: min(90vw, 320px) !important; height: 100vh !important;
      background: #fff !important; z-index: 10001 !important;
      transform: translateX(100%) !important;
      transition: transform 0.3s ease !important;
      overflow-y: auto !important; overflow-x: hidden !important;
      box-shadow: -4px 0 24px rgba(0,0,0,0.15) !important;
    }
    .slc-drawer.is-open { transform: translateX(0) !important; }
    .slc-drawer-overlay {
      position: fixed !important; inset: 0 !important; z-index: 10000 !important;
      background: rgba(0,0,0,0.5) !important; display: none !important;
    }
    .slc-drawer-overlay.is-open { display: block !important; }

    /* 5. Hero section */
    @media (max-width: 768px) {
      .slc-hero { padding: 80px 0 60px !important; min-height: 70vh !important; }
      .slc-hero__title { font-size: clamp(1.9rem, 7vw, 2.8rem) !important; }
      .slc-hero__desc { font-size: 1rem !important; margin-bottom: 28px !important; }
      .slc-hero__actions {
        flex-direction: column !important; gap: 12px !important; width: 100% !important;
      }
      .slc-hero__actions .slc-btn, .slc-hero__actions a.slc-btn {
        width: 100% !important; justify-content: center !important; padding: 14px 20px !important;
      }
      .slc-hero__corridor-bar {
        flex-direction: column !important; align-items: flex-start !important; gap: 14px !important;
      }
    }
    @media (max-width: 480px) {
      .slc-hero { padding: 72px 0 48px !important; }
      .slc-hero__cities { flex-wrap: wrap !important; font-size: 0.75rem !important; }
    }

    /* 6. Page hero (subpages) */
    @media (max-width: 768px) {
      .slc-page-hero { padding: 72px 0 56px !important; }
      .slc-page-hero__title { font-size: clamp(1.6rem, 6vw, 2.4rem) !important; }
      .slc-page-hero__desc { font-size: 0.95rem !important; }
      .slc-page-hero__actions {
        flex-direction: column !important; gap: 10px !important; width: 100% !important;
      }
      .slc-page-hero__actions a {
        width: 100% !important; text-align: center !important; justify-content: center !important;
      }
    }

    /* 7. Stats row */
    .slc-stats-row, .slc-stats-grid {
      display: flex !important; flex-wrap: wrap !important;
      gap: 20px !important; justify-content: center !important;
    }
    .slc-stat-item { min-width: 120px !important; flex: 1 1 120px !important; text-align: center !important; }
    @media (max-width: 480px) {
      .slc-stat-item { flex: 1 1 calc(50% - 20px) !important; }
      .slc-stat-value { font-size: clamp(1.6rem, 7vw, 2.4rem) !important; }
    }

    /* 8. Service / feature card grids */
    .slc-services-grid,
    .slc-feature-grid,
    .slc-service-cards,
    [class*="slc-grid-"] {
      display: grid !important;
      grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr)) !important;
      gap: 20px !important;
    }
    @media (max-width: 480px) {
      .slc-services-grid,
      .slc-feature-grid,
      .slc-service-cards {
        grid-template-columns: 1fr !important;
      }
    }

    /* 9. Comparison table: tablet horizontal scroll (641-880px) */
    @media (max-width: 880px) and (min-width: 641px) {
      .slc-comparison-table-wrapper {
        overflow-x: auto !important; -webkit-overflow-scrolling: touch !important;
        border-radius: 12px !important; border: 1px solid rgba(128,24,35,0.14) !important;
        background: #fff !important; box-shadow: 0 4px 16px rgba(0,0,0,0.06) !important;
      }
      .slc-comparison-table {
        display: table !important; min-width: 640px !important;
      }
      .slc-comparison-table thead { display: table-header-group !important; }
      .slc-comparison-table tbody {
        display: table-row-group !important; flex-direction: unset !important;
      }
      .slc-comparison-table tbody tr {
        display: table-row !important; padding: 0 !important;
        border-radius: 0 !important; box-shadow: none !important;
      }
      .slc-comparison-table tbody tr::before { display: none !important; }
      .slc-comparison-table tbody td {
        display: table-cell !important; padding: 12px 14px !important;
        font-size: 0.85rem !important;
      }
      .slc-comparison-table tbody td::before { display: none !important; }
    }

    /* 10. Comparison table desktop: allow wrapping on medium screens */
    @media (max-width: 1200px) and (min-width: 881px) {
      .slc-comparison-table thead th {
        white-space: normal !important; font-size: 0.8rem !important;
        padding: 14px !important;
      }
      .slc-comparison-table tbody td { padding: 14px !important; font-size: 0.88rem !important; }
      .slc-comparison-table td:last-child,
      .slc-comparison-table th:last-child { width: 100px !important; }
    }

    /* 11. Rate tables (pricing) */
    @media (max-width: 640px) {
      .slc-rate-table-wrapper {
        overflow-x: auto !important; -webkit-overflow-scrolling: touch !important;
      }
      .slc-rate-table { min-width: 480px !important; }
    }

    /* 12. Forms */
    .slc-form-grid {
      display: grid !important;
      grid-template-columns: repeat(auto-fit, minmax(min(100%, 240px), 1fr)) !important;
      gap: 16px !important;
    }
    @media (max-width: 600px) {
      .slc-form-grid { grid-template-columns: 1fr !important; }
      .slc-form-card, .slc-quote-form { padding: 20px 16px !important; }
      .slc-btn[type="submit"], button[type="submit"] { width: 100% !important; }
    }

    /* 13. CTA sections */
    @media (max-width: 640px) {
      .slc-cta__inner { padding: 40px 20px !important; }
      .slc-cta__actions {
        flex-direction: column !important; gap: 12px !important; width: 100% !important;
      }
      .slc-cta__actions .slc-btn, .slc-cta__actions a {
        width: 100% !important; justify-content: center !important;
      }
    }

    /* 14. Footer */
    @media (max-width: 768px) {
      .slc-footer__grid {
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)) !important;
        gap: 28px !important;
      }
    }
    @media (max-width: 480px) {
      .slc-footer__grid { grid-template-columns: 1fr !important; gap: 24px !important; }
      .slc-footer__bottom {
        flex-direction: column !important; text-align: center !important; gap: 10px !important;
      }
      .slc-footer { padding: 48px 0 24px !important; }
    }

    /* 15. Floating WhatsApp pill */
    @media (max-width: 600px) {
      .slc-float-whatsapp {
        bottom: 16px !important; right: 16px !important;
        padding: 12px !important; border-radius: 50% !important;
      }
      .slc-float-whatsapp span { display: none !important; }
    }

    /* 16. Scroll margin for anchor links (account for sticky header) */
    [id] { scroll-margin-top: 90px !important; }

    /* 17. Table of contents */
    @media (max-width: 640px) {
      .slc-toc { padding: 18px 14px !important; }
      .slc-toc__list { column-count: 1 !important; }
    }

    /* 18. Calculator */
    @media (max-width: 600px) {
      .slc-calc-card { padding: 18px 14px !important; }
      .slc-calc-tabs { flex-direction: column !important; }
      .slc-calc-tab-btn { width: 100% !important; }
    }

    /* 19. Hub / step / case grids */
    @media (max-width: 480px) {
      .slc-hub-grid, .slc-step-grid, .slc-case-grid {
        grid-template-columns: 1fr !important;
      }
    }

    /* 20. FAQ details elements */
    details summary {
      cursor: pointer !important;
      padding: 16px 20px !important;
      word-break: break-word !important;
    }
    @media (max-width: 600px) {
      details summary { padding: 14px 16px !important; font-size: 0.95rem !important; }
      details .slc-faq__answer { padding: 14px 16px !important; }
    }

    /* 21. Locations section */
    .slc-locations__grid {
      display: grid !important;
      grid-template-columns: repeat(auto-fit, minmax(min(100%, 300px), 1fr)) !important;
      gap: 24px !important;
    }
    @media (max-width: 480px) {
      .slc-locations__grid { grid-template-columns: 1fr !important; }
      .slc-location-card { padding: 20px 16px !important; }
    }

    /* 22. Process / timeline steps */
    .slc-process-grid {
      display: grid !important;
      grid-template-columns: repeat(auto-fit, minmax(min(100%, 220px), 1fr)) !important;
      gap: 20px !important;
    }

    /* 23. Testimonials */
    .slc-testimonials-grid {
      display: grid !important;
      grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)) !important;
      gap: 20px !important;
    }

    /* 24. Prevent fixed width inline styles breaking layout */
    @media (max-width: 600px) {
      [style*="width:"] { max-width: 100% !important; }
      [style*="min-width: 6"] { min-width: 0 !important; }
    }
  </style>
  <!-- End Universal Responsive Engine v2.1 -->
"""

MARKER = 'Universal Responsive Engine v2.1'

def inject_responsive_style(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if MARKER in content:
        return False, 'already injected'

    # Insert just before </head>
    if '</head>' not in content:
        return False, 'no </head> tag found'

    new_content = content.replace('</head>', UNIVERSAL_RESPONSIVE_STYLE + '\n</head>', 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True, 'responsive style injected'


if __name__ == '__main__':
    base = r'c:\Users\Dell\OneDrive\Desktop\SLC Website'
    print('=' * 60)
    print('INJECTING UNIVERSAL RESPONSIVE ENGINE v2.1')
    print('=' * 60)
    for page in PAGES:
        fpath = os.path.join(base, page)
        if os.path.exists(fpath):
            changed, msg = inject_responsive_style(fpath)
            status = '✅ DONE' if changed else '—'
            print(f'  {status}  {page}: {msg}')
        else:
            print(f'  ⚠️   {page}: FILE NOT FOUND')
    print('\nDone. All pages updated.')

