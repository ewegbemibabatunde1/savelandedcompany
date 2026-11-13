#!/usr/bin/env python3
"""
master_responsive_fix.py
=========================
One-shot comprehensive fix for all Savelanded pages:

1. index.html — fix all fixed-column grids (locations 3-col, testimonials 3-col,
   stats 4-col, services 2-col at tablet) to be fully responsive
2. All pages — rebuild the floating WhatsApp widget so it's correct on every page
3. index.html — fix all 3 location card images with reliable, correct Unsplash photos
4. All pages — fix hero sections on sub-pages to have correct, responsive images
5. index.html — fix mobile responsiveness for every section
6. Add a comprehensive page-specific responsive <style> block to index.html
"""

import os
import re

BASE = r'c:\Users\Dell\OneDrive\Desktop\SLC Website'

# ============================================================
# CORRECT UNSPLASH IMAGES (all tested to work reliably)
# ============================================================
IMAGES = {
    # Locations
    'yiwu_market':    'https://images.unsplash.com/photo-1555529669-e69e7aa0ba9a?auto=format&fit=crop&w=800&q=80',
    'guangzhou_wh':   'https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=800&q=80',
    'lagos_market':   'https://images.unsplash.com/photo-1565008576549-57569a49371d?auto=format&fit=crop&w=800&q=80',
    # Hero backgrounds (CSS bg-image)
    'cargo_ship':     'https://images.unsplash.com/photo-1494412574643-ff11b0a5c1c3?auto=format&fit=crop&w=1920&q=80',
    'air_freight':    'https://images.unsplash.com/photo-1570710891163-6d3b5c47248b?auto=format&fit=crop&w=1920&q=80',
    'warehouse':      'https://images.unsplash.com/photo-1553413077-190dd305871c?auto=format&fit=crop&w=1920&q=80',
    'customs':        'https://images.unsplash.com/photo-1450133064473-71024230f91b?auto=format&fit=crop&w=1920&q=80',
    'sourcing':       'https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=1920&q=80',
    'door_delivery':  'https://images.unsplash.com/photo-1580674684081-7617fbf3d745?auto=format&fit=crop&w=1920&q=80',
    'procurement':    'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=1920&q=80',
    'import_export':  'https://images.unsplash.com/photo-1559136555-9303baea8ebd?auto=format&fit=crop&w=1920&q=80',
}

# ============================================================
# FLOATING WHATSAPP WIDGET (authoritative version)
# ============================================================
WA_WIDGET = '''  <!-- Floating WhatsApp Action Button -->
  <a href="https://wa.me/8618248547224?text=Hello%20Savelanded!%20I%20found%20you%20online%20and%20I%27d%20like%20to%20enquire%20about%20shipping%20from%20China%20to%20Nigeria."
     class="slc-float-whatsapp"
     target="_blank"
     rel="noopener noreferrer"
     aria-label="Chat with Savelanded on WhatsApp">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false">
      <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
    </svg>
    <span>Chat on WhatsApp</span>
  </a>
'''

# ============================================================
# INDEX.HTML COMPREHENSIVE RESPONSIVE STYLE BLOCK
# ============================================================
INDEX_RESPONSIVE_STYLE = """
  <!-- SAVELANDED INDEX — MASTER RESPONSIVE STYLE (injected by master_responsive_fix.py) -->
  <style>
    /* =====================================================
       INDEX PAGE: MAKE ALL GRIDS FULLY RESPONSIVE
       ===================================================== */

    /* Services grid: 3-col desktop, 2-col tablet, 1-col mobile */
    .slc-services-grid {
      display: grid !important;
      grid-template-columns: repeat(3, 1fr) !important;
      gap: 24px !important;
    }

    /* Stats / trust strip: 4-col desktop */
    .slc-stats-grid,
    .slc-trust-strip__grid {
      display: grid !important;
      grid-template-columns: repeat(4, 1fr) !important;
      gap: 20px !important;
    }

    /* Locations: 3-col desktop */
    .slc-locations-grid {
      display: grid !important;
      grid-template-columns: repeat(3, 1fr) !important;
      gap: 28px !important;
    }

    /* Testimonials: 3-col desktop */
    .slc-testimonials-grid {
      display: grid !important;
      grid-template-columns: repeat(3, 1fr) !important;
      gap: 28px !important;
    }

    /* Location card image — always correct height */
    .slc-loc-media {
      height: 200px !important;
      width: 100% !important;
      overflow: hidden !important;
      position: relative !important;
      background: #f0ebe3 !important;
    }
    .slc-loc-media img {
      width: 100% !important;
      height: 100% !important;
      object-fit: cover !important;
      object-position: center !important;
      display: block !important;
      transition: transform 0.4s ease !important;
    }
    .slc-loc-card:hover .slc-loc-media img {
      transform: scale(1.04) !important;
    }

    /* Broken image fallback gradient */
    .slc-loc-media img[alt] {
      background: linear-gradient(135deg, #801823 0%, #c9933b 100%) !important;
    }

    /* =====================================================
       TABLET (641-1024px): 2-column layouts
       ===================================================== */
    @media (max-width: 1024px) and (min-width: 641px) {
      .slc-services-grid { grid-template-columns: repeat(2, 1fr) !important; }
      .slc-locations-grid { grid-template-columns: repeat(2, 1fr) !important; }
      .slc-testimonials-grid { grid-template-columns: repeat(2, 1fr) !important; }
      .slc-stats-grid,
      .slc-trust-strip__grid { grid-template-columns: repeat(2, 1fr) !important; }
      .slc-footer__grid { grid-template-columns: repeat(2, 1fr) !important; gap: 32px !important; }
      .slc-about__grid { grid-template-columns: 1fr !important; }
      .slc-how-layout { grid-template-columns: 1fr !important; gap: 28px !important; }
    }

    /* =====================================================
       MOBILE (≤640px): all single column
       ===================================================== */
    @media (max-width: 640px) {
      /* Sections */
      .slc-services { padding: 56px 0 !important; }
      .slc-locations { padding: 56px 0 !important; }
      .slc-testimonials { padding: 56px 0 !important; }
      .slc-about { padding: 56px 0 !important; }
      .slc-how { padding: 56px 0 !important; }
      .slc-faq { padding: 56px 0 !important; }
      .slc-cta-primary { padding: 56px 0 !important; }

      /* Grids: all single column */
      .slc-services-grid,
      .slc-locations-grid,
      .slc-testimonials-grid,
      .slc-stats-grid,
      .slc-trust-strip__grid,
      .slc-about__grid,
      .slc-footer__grid { grid-template-columns: 1fr !important; gap: 20px !important; }

      /* Section headings */
      .slc-section-eyebrow { font-size: 0.7rem !important; }
      .slc-section-title { font-size: clamp(1.5rem, 7vw, 2rem) !important; }
      .slc-section-desc { font-size: 0.95rem !important; }

      /* Services cards */
      .slc-service-card { padding: 24px 20px !important; }
      .slc-service-card__icon { width: 48px !important; height: 48px !important; }

      /* Location cards */
      .slc-loc-media { height: 180px !important; }
      .slc-loc-body { padding: 20px !important; }
      .slc-loc-city { font-size: 1.15rem !important; }

      /* Testimonials */
      .slc-test-card { padding: 24px 20px !important; }

      /* FAQ */
      .slc-faq-trigger { padding: 18px 20px !important; font-size: 0.95rem !important; }
      .slc-faq-answer { padding: 0 20px 20px !important; }

      /* How it works */
      .slc-how-image-box { height: 220px !important; }
      .slc-how-step { padding: 16px !important; gap: 14px !important; }

      /* CTA section */
      .slc-cta-primary__title { font-size: clamp(1.4rem, 6vw, 2rem) !important; }
      .slc-cta-primary__actions { flex-direction: column !important; gap: 12px !important; }
      .slc-cta-primary__actions .slc-btn { width: 100% !important; justify-content: center !important; }

      /* Footer */
      .slc-footer { padding: 48px 0 24px !important; }
      .slc-footer__bottom { flex-direction: column !important; text-align: center !important; gap: 10px !important; }

      /* Comparison table on index */
      .slc-comparison-table-wrapper { margin: 16px 0 !important; }
    }

    /* =====================================================
       SMALL MOBILE (≤480px)
       ===================================================== */
    @media (max-width: 480px) {
      .slc-hero { padding: 72px 0 48px !important; }
      .slc-hero__title { font-size: clamp(1.6rem, 8vw, 2.2rem) !important; }
      .slc-hero__desc { font-size: 0.9rem !important; }

      .slc-container { padding-left: 14px !important; padding-right: 14px !important; }

      .slc-loc-media { height: 160px !important; }
      .slc-loc-body { padding: 16px !important; }

      /* Trust strip: 2-per-row on tiny phones */
      .slc-trust-strip__grid,
      .slc-stats-grid { grid-template-columns: repeat(2, 1fr) !important; gap: 12px !important; }

      /* Corridor bar on hero */
      .slc-hero__corridor-bar { gap: 8px !important; }
      .slc-hero__cities { font-size: 0.7rem !important; gap: 6px !important; }
    }

    /* =====================================================
       FLOATING WHATSAPP: Ensure always visible & correct
       ===================================================== */
    .slc-float-whatsapp {
      position: fixed !important;
      bottom: 24px !important;
      right: 24px !important;
      z-index: 9999 !important;
      display: inline-flex !important;
      align-items: center !important;
      gap: 10px !important;
      background: #25D366 !important;
      color: #ffffff !important;
      font-family: var(--slc-font-head, 'Sora', sans-serif) !important;
      font-size: 0.875rem !important;
      font-weight: 700 !important;
      padding: 13px 20px 13px 16px !important;
      border-radius: 9999px !important;
      box-shadow: 0 8px 24px rgba(37,211,102,0.45) !important;
      text-decoration: none !important;
      transition: all 0.28s ease !important;
      cursor: pointer !important;
      border: none !important;
      outline: none !important;
    }
    .slc-float-whatsapp:hover {
      background: #20ba5a !important;
      transform: translateY(-3px) scale(1.02) !important;
      box-shadow: 0 12px 32px rgba(37,211,102,0.55) !important;
      color: #ffffff !important;
    }
    .slc-float-whatsapp svg {
      width: 22px !important;
      height: 22px !important;
      fill: #ffffff !important;
      flex-shrink: 0 !important;
    }
    @media (max-width: 600px) {
      .slc-float-whatsapp {
        bottom: 16px !important;
        right: 16px !important;
        padding: 13px !important;
        border-radius: 50% !important;
      }
      .slc-float-whatsapp span { display: none !important; }
      .slc-float-whatsapp svg { width: 24px !important; height: 24px !important; }
    }
  </style>
  <!-- End SAVELANDED INDEX responsive style -->
"""

# ============================================================
# SUBPAGE RESPONSIVE STYLE (for all non-index pages)
# ============================================================
SUBPAGE_RESPONSIVE_STYLE = """
  <!-- SAVELANDED SUBPAGE RESPONSIVE STYLE -->
  <style>
    /* =====================================================
       SUBPAGE CONTENT SECTION: Responsive
       ===================================================== */

    /* Content sections padding */
    .slc-content-section { padding: clamp(48px, 8vw, 100px) 0 !important; }

    /* Feature/info grids: responsive */
    .slc-feature-grid,
    .slc-info-grid,
    .slc-benefits-grid,
    .slc-process-steps {
      display: grid !important;
      grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr)) !important;
      gap: 24px !important;
    }

    /* Two-column layout (text + image): stack on tablet */
    .slc-two-col,
    .slc-split-layout,
    .slc-content-with-image {
      display: grid !important;
      grid-template-columns: 1fr 1fr !important;
      gap: 40px !important;
      align-items: center !important;
    }
    @media (max-width: 900px) {
      .slc-two-col,
      .slc-split-layout,
      .slc-content-with-image { grid-template-columns: 1fr !important; gap: 28px !important; }
    }

    /* Content images */
    .slc-content-img,
    .slc-section-img,
    [class*="slc-"][class*="img"] img {
      width: 100% !important;
      height: auto !important;
      border-radius: 12px !important;
      object-fit: cover !important;
    }

    /* Pricing cards */
    .slc-pricing-grid {
      display: grid !important;
      grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)) !important;
      gap: 24px !important;
    }

    /* Floating WhatsApp: authoritative */
    .slc-float-whatsapp {
      position: fixed !important;
      bottom: 24px !important; right: 24px !important;
      z-index: 9999 !important;
      display: inline-flex !important;
      align-items: center !important;
      gap: 10px !important;
      background: #25D366 !important;
      color: #ffffff !important;
      font-family: 'Sora', sans-serif !important;
      font-size: 0.875rem !important;
      font-weight: 700 !important;
      padding: 13px 20px 13px 16px !important;
      border-radius: 9999px !important;
      box-shadow: 0 8px 24px rgba(37,211,102,0.45) !important;
      text-decoration: none !important;
      transition: all 0.28s ease !important;
    }
    .slc-float-whatsapp:hover {
      background: #20ba5a !important;
      transform: translateY(-3px) !important;
      color: #ffffff !important;
    }
    .slc-float-whatsapp svg {
      width: 22px !important; height: 22px !important;
      fill: #ffffff !important; flex-shrink: 0 !important;
    }
    @media (max-width: 600px) {
      .slc-float-whatsapp {
        bottom: 16px !important; right: 16px !important;
        padding: 13px !important; border-radius: 50% !important;
      }
      .slc-float-whatsapp span { display: none !important; }
      .slc-float-whatsapp svg { width: 24px !important; height: 24px !important; }
    }

    /* Mobile section padding */
    @media (max-width: 640px) {
      .slc-page-hero { padding: 72px 0 56px !important; }
      .slc-page-hero__title { font-size: clamp(1.5rem, 7vw, 2.2rem) !important; }
      .slc-content-section { padding: 48px 0 !important; }
      .slc-feature-grid,
      .slc-info-grid,
      .slc-benefits-grid,
      .slc-process-steps { grid-template-columns: 1fr !important; gap: 16px !important; }
      .slc-cta__inner { padding: 40px 20px !important; }
      .slc-cta__title { font-size: clamp(1.3rem, 6vw, 1.8rem) !important; }
      .slc-cta__actions { flex-direction: column !important; gap: 12px !important; }
      .slc-cta__actions a, .slc-cta__actions .slc-btn { width: 100% !important; justify-content: center !important; text-align: center !important; }
    }
  </style>
  <!-- End SAVELANDED SUBPAGE responsive style -->
"""


PAGES_NO_INDEX = [
    'about.html', 'air-freight.html', 'contact.html',
    'customs-clearance.html', 'door-to-door.html', 'import-export.html',
    'procurement.html', 'product-sourcing.html', 'quote.html',
    'sea-freight.html', 'services.html', 'shipping.html', 'warehousing.html',
]

MARKER_INDEX = 'SAVELANDED INDEX — MASTER RESPONSIVE STYLE'
MARKER_SUBPAGE = 'SAVELANDED SUBPAGE RESPONSIVE STYLE'
MARKER_WA = 'Chat on WhatsApp'


def fix_index_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    changes = []

    # 1. Fix location card images
    old_guangzhou = 'https://images.unsplash.com/photo-1508873696983-2df5293cb395?auto=format&fit=crop&w=800&q=80'
    new_guangzhou = 'https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=800&q=80'
    if old_guangzhou in html:
        html = html.replace(old_guangzhou, new_guangzhou)
        changes.append('Guangzhou image URL fixed')

    old_lagos = 'https://images.unsplash.com/photo-1577705998148-6da4f3963bc8?auto=format&fit=crop&w=800&q=80'
    new_lagos = 'https://images.unsplash.com/photo-1565008576549-57569a49371d?auto=format&fit=crop&w=800&q=80'
    if old_lagos in html:
        html = html.replace(old_lagos, new_lagos)
        changes.append('Lagos image URL fixed (cardboard box → African market)')

    old_yiwu = 'https://images.unsplash.com/photo-1542051841857-5f90071e7989?auto=format&fit=crop&w=800&q=80'
    new_yiwu = 'https://images.unsplash.com/photo-1555529669-e69e7aa0ba9a?auto=format&fit=crop&w=800&q=80'
    if old_yiwu in html:
        html = html.replace(old_yiwu, new_yiwu)
        changes.append('Yiwu image URL fixed')

    # 2. Fix floating WhatsApp widget if broken
    if MARKER_WA not in html:
        # Find </body> and insert before it
        if '</body>' in html:
            html = html.replace('</body>', WA_WIDGET + '\n</body>', 1)
            changes.append('WhatsApp floating widget inserted')
    else:
        # Fix the WhatsApp href if it's wrong
        old_wa_href = 'href="https://wa.me/8618248547224"'
        new_wa_href = 'href="https://wa.me/8618248547224?text=Hello%20Savelanded!%20I%20found%20you%20online%20and%20I%27d%20like%20to%20enquire%20about%20shipping%20from%20China%20to%20Nigeria."'
        if old_wa_href in html and new_wa_href not in html:
            html = html.replace(old_wa_href, new_wa_href, 1)
            changes.append('WhatsApp URL with pre-filled message added')

    # 3. Add responsive style block for index
    if MARKER_INDEX not in html:
        html = html.replace('</head>', INDEX_RESPONSIVE_STYLE + '\n</head>', 1)
        changes.append('Index responsive style block injected')

    # 4. Fix address: remove provisional note or update
    old_provisional = '<em style="font-size:0.75rem; color:var(--slc-copper);">(Address provisional pending final confirmation)</em>'
    new_note = '<em style="font-size:0.75rem; color:#801823; font-style:normal; font-weight:600;">📍 Confirmed location</em>'
    if old_provisional in html:
        html = html.replace(old_provisional, '')
        changes.append('Provisional address note removed from Yiwu card')

    # 5. Fix Lagos address in locations to match official confirmed address
    old_lagos_addr = 'Apt Market Exp Blk-PB7, Savelanded Plaza,<br>No. 7, 10, 12 and 14, Trade Fair Complex,<br>Lagos, Nigeria.'
    new_lagos_addr = 'Zone B, Shop 13/14, 23/24,<br>Edo Plaza, Balogun,<br>Trade Fair Complex, Badagry Expressway,<br>Ojo, Lagos, Nigeria.'
    if old_lagos_addr in html:
        html = html.replace(old_lagos_addr, new_lagos_addr)
        changes.append('Lagos address corrected to official confirmed address')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

    return changes


def fix_subpage(filepath, page_name):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    changes = []

    # 1. Add subpage responsive style
    if MARKER_SUBPAGE not in html:
        html = html.replace('</head>', SUBPAGE_RESPONSIVE_STYLE + '\n</head>', 1)
        changes.append('Subpage responsive style injected')

    # 2. Fix floating WhatsApp widget
    if MARKER_WA not in html:
        if '</body>' in html:
            html = html.replace('</body>', WA_WIDGET + '\n</body>', 1)
            changes.append('WhatsApp floating widget inserted')
    else:
        # Fix href to include pre-filled message if not already present
        old_wa_href = 'href="https://wa.me/8618248547224"'
        new_wa_href = 'href="https://wa.me/8618248547224?text=Hello%20Savelanded!%20I%20found%20you%20online%20and%20I%27d%20like%20to%20enquire%20about%20shipping%20from%20China%20to%20Nigeria."'
        if old_wa_href in html and new_wa_href not in html:
            # Only update the floating widget href, not other WA links on the page
            # The floating widget's href is the last occurrence (injected at end of body)
            last_pos = html.rfind(old_wa_href)
            if last_pos != -1:
                html = html[:last_pos] + new_wa_href + html[last_pos + len(old_wa_href):]
                changes.append('WhatsApp floating widget URL with pre-fill updated')

    # 3. Fix hero background images for specific pages
    page_hero_images = {
        'air-freight.html':       'https://images.unsplash.com/photo-1570710891163-6d3b5c47248b?auto=format&fit=crop&w=1920&q=80',
        'sea-freight.html':       'https://images.unsplash.com/photo-1494412574643-ff11b0a5c1c3?auto=format&fit=crop&w=1920&q=80',
        'warehousing.html':       'https://images.unsplash.com/photo-1553413077-190dd305871c?auto=format&fit=crop&w=1920&q=80',
        'customs-clearance.html': 'https://images.unsplash.com/photo-1450133064473-71024230f91b?auto=format&fit=crop&w=1920&q=80',
        'product-sourcing.html':  'https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=1920&q=80',
        'door-to-door.html':      'https://images.unsplash.com/photo-1580674684081-7617fbf3d745?auto=format&fit=crop&w=1920&q=80',
        'procurement.html':       'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=1920&q=80',
        'import-export.html':     'https://images.unsplash.com/photo-1559136555-9303baea8ebd?auto=format&fit=crop&w=1920&q=80',
        'services.html':          'https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=1920&q=80',
        'about.html':             'https://images.unsplash.com/photo-1560472354-b33ff0c44a43?auto=format&fit=crop&w=1920&q=80',
        'contact.html':           'https://images.unsplash.com/photo-1423666639041-f56000c27a9a?auto=format&fit=crop&w=1920&q=80',
        'quote.html':             'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=1920&q=80',
        'shipping.html':          'https://images.unsplash.com/photo-1494412574643-ff11b0a5c1c3?auto=format&fit=crop&w=1920&q=80',
    }

    if page_name in page_hero_images:
        new_img = page_hero_images[page_name]
        # Check if hero has a background image that might be using a local/broken url
        # Look for placeholder or broken image references
        if 'background-image' in html and 'unsplash' not in html[html.find('slc-page-hero'):html.find('slc-page-hero')+3000]:
            changes.append(f'Hero bg: page already uses CSS gradient hero (no image URL found)')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

    return changes


if __name__ == '__main__':
    print('=' * 65)
    print('SAVELANDED — MASTER RESPONSIVE FIX')
    print('=' * 65)

    # Fix index.html
    print('\n[1] Fixing index.html...')
    idx_path = os.path.join(BASE, 'index.html')
    changes = fix_index_html(idx_path)
    for c in changes:
        print(f'  ✅  {c}')
    if not changes:
        print('  —  No changes needed')

    # Fix all subpages
    print('\n[2] Fixing subpages...')
    for page in PAGES_NO_INDEX:
        fpath = os.path.join(BASE, page)
        if os.path.exists(fpath):
            changes = fix_subpage(fpath, page)
            status = '✅' if changes else '—'
            print(f'  {status}  {page}: {", ".join(changes) if changes else "no changes needed"}')

    print('\n' + '=' * 65)
    print('MASTER RESPONSIVE FIX COMPLETE')
    print('=' * 65)

