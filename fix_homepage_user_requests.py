#!/usr/bin/env python3
"""
fix_homepage_user_requests.py
==============================
Applies the three specific homepage user requests:
1. Trust Value Strip: all 5 items on the SAME LINE on desktop, responsive on mobile & tablet:
   - China–Nigeria Network
   - Transparent Sourcing
   - Quality Assurance
   - Professional Logistics
   - Dedicated Support
2. Services: Exactly 4 in a row on desktop (2 rows of 4 for 8 total services), 2 in a row on tablet, 1 in a row on mobile.
3. Step-by-Step Workflow Image: Substantially increase image size (width proportion 1.25fr, height min 640px on desktop, 480px on tablet, 360px on mobile).
"""

import os
import re

BASE_DIR = r"c:\Users\Dell\OneDrive\Desktop\SLC Website"
INDEX_PATH = os.path.join(BASE_DIR, "index.html")
CSS_PATH = os.path.join(BASE_DIR, "assets", "css", "savelanded.css")

# ============================================================
# 1. Update index.html
# ============================================================
def update_index_html():
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Replacement for SAVELANDED INDEX — MASTER RESPONSIVE STYLE block
    marker_start = "<!-- SAVELANDED INDEX"
    marker_end = "<!-- End SAVELANDED INDEX responsive style -->"

    start_idx = content.find(marker_start)
    end_idx = content.find(marker_end)

    if start_idx != -1 and end_idx != -1:
        end_idx += len(marker_end)
    else:
        print("Warning: Index responsive style marker not found. Will append before </head>")

    NEW_INDEX_STYLE = """<!-- SAVELANDED INDEX — MASTER RESPONSIVE STYLE (Updated for 5-in-row Trust Strip, 4-in-row Services, Large Workflow Image) -->
  <style>
    /* =====================================================
       1. TRUST & VALUE STRIP — ALL 5 ITEMS ON THE SAME LINE (DESKTOP)
       ===================================================== */
    .slc-trust-strip {
      background: #141414 !important;
      color: #ffffff !important;
      padding: 26px 0 !important;
      border-bottom: 1px solid rgba(201, 147, 59, 0.28) !important;
      border-top: 1px solid rgba(255, 255, 255, 0.08) !important;
    }
    .slc-trust-strip__grid {
      display: grid !important;
      grid-template-columns: repeat(5, 1fr) !important; /* All 5 items on the exact same line */
      gap: 16px !important;
      align-items: flex-start !important;
    }
    .slc-trust-item {
      display: flex !important;
      align-items: flex-start !important;
      gap: 12px !important;
      min-width: 0 !important;
    }
    .slc-trust-icon {
      width: 38px !important;
      height: 38px !important;
      border-radius: 8px !important;
      background: rgba(201, 147, 59, 0.15) !important;
      border: 1px solid rgba(201, 147, 59, 0.35) !important;
      color: #c9933b !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      flex-shrink: 0 !important;
    }
    .slc-trust-icon svg {
      width: 19px !important;
      height: 19px !important;
      fill: currentColor !important;
    }
    .slc-trust-title {
      font-family: var(--slc-font-head, 'Sora', sans-serif) !important;
      font-size: 0.875rem !important;
      font-weight: 700 !important;
      color: #ffffff !important;
      margin-bottom: 4px !important;
      line-height: 1.25 !important;
    }
    .slc-trust-desc {
      font-size: 0.75rem !important;
      line-height: 1.45 !important;
      color: rgba(255, 255, 255, 0.72) !important;
    }

    /* Tablet: All 5 on the same line with smooth swipe/scroll */
    @media (max-width: 1024px) and (min-width: 768px) {
      .slc-trust-strip {
        padding: 22px 0 !important;
      }
      .slc-trust-strip__grid {
        display: flex !important;
        flex-wrap: nowrap !important;
        overflow-x: auto !important;
        -webkit-overflow-scrolling: touch !important;
        gap: 16px !important;
        padding-bottom: 8px !important;
        scrollbar-width: thin !important;
      }
      .slc-trust-item {
        flex: 0 0 220px !important;
        background: rgba(255, 255, 255, 0.03) !important;
        padding: 10px 12px !important;
        border-radius: 8px !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
      }
    }

    /* Mobile: Beautiful responsive stacked cards */
    @media (max-width: 767px) {
      .slc-trust-strip {
        padding: 24px 0 !important;
      }
      .slc-trust-strip__grid {
        display: flex !important;
        flex-direction: column !important;
        gap: 12px !important;
      }
      .slc-trust-item {
        display: flex !important;
        align-items: flex-start !important;
        gap: 14px !important;
        padding: 12px 14px !important;
        background: rgba(255, 255, 255, 0.04) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 10px !important;
      }
      .slc-trust-icon {
        width: 38px !important;
        height: 38px !important;
      }
      .slc-trust-title {
        font-size: 0.92rem !important;
        color: #ffffff !important;
      }
      .slc-trust-desc {
        font-size: 0.8rem !important;
        color: rgba(255, 255, 255, 0.75) !important;
      }
    }


    /* =====================================================
       2. SERVICES GRID — EXACTLY 4 IN A ROW ON DESKTOP
       ===================================================== */
    .slc-services-grid {
      display: grid !important;
      grid-template-columns: repeat(4, 1fr) !important; /* 4 in a row */
      gap: 22px !important;
    }
    .slc-service-card-lux {
      display: flex !important;
      flex-direction: column !important;
      height: 100% !important;
    }
    .slc-service-card-lux__image-box {
      height: 165px !important; /* Ideal height for 4-column cards */
      width: 100% !important;
    }
    .slc-service-card-lux__body {
      padding: 20px 18px !important;
      display: flex !important;
      flex-direction: column !important;
      flex-grow: 1 !important;
    }
    .slc-service-card-lux__title {
      font-size: 1.05rem !important;
      line-height: 1.3 !important;
      margin-bottom: 8px !important;
    }
    .slc-service-card-lux__desc {
      font-size: 0.835rem !important;
      line-height: 1.55 !important;
      margin-bottom: 14px !important;
    }
    .slc-service-card-lux__features {
      margin-top: auto !important;
      padding-top: 10px !important;
    }

    /* Tablet: 2 in a row (4 balanced rows of 2) */
    @media (max-width: 1024px) and (min-width: 641px) {
      .slc-services-grid {
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 20px !important;
      }
      .slc-service-card-lux__image-box {
        height: 180px !important;
      }
    }

    /* Mobile: 1 in a row (full width cards) */
    @media (max-width: 640px) {
      .slc-services-grid {
        grid-template-columns: 1fr !important;
        gap: 18px !important;
      }
      .slc-service-card-lux__image-box {
        height: 180px !important;
      }
    }


    /* =====================================================
       3. STEP-BY-STEP WORKFLOW — SUBSTANTIALLY INCREASED IMAGE
       ===================================================== */
    .slc-how-lux {
      padding: 100px 0 !important;
    }
    .slc-how-layout {
      display: grid !important;
      grid-template-columns: 1.25fr 1fr !important; /* Image gets 55.5% of row, steps get 44.5% */
      gap: 48px !important;
      align-items: stretch !important; /* Full vertical stretch to match steps */
    }
    .slc-how-image-box {
      width: 100% !important;
      height: 100% !important;
      min-height: 640px !important; /* High-impact large workflow image */
      border-radius: 20px !important;
      overflow: hidden !important;
      box-shadow: 0 20px 48px rgba(0, 0, 0, 0.16) !important;
      border: 2px solid rgba(128, 24, 35, 0.12) !important;
      position: relative !important;
      background: #f0ebe3 !important;
    }
    .slc-how-image-box img {
      width: 100% !important;
      height: 100% !important;
      object-fit: cover !important;
      object-position: center !important;
      display: block !important;
      transition: transform 0.5s ease !important;
    }
    .slc-how-image-box:hover img {
      transform: scale(1.03) !important;
    }

    /* Tablet: Increased image height */
    @media (max-width: 1024px) and (min-width: 641px) {
      .slc-how-layout {
        grid-template-columns: 1fr !important;
        gap: 36px !important;
      }
      .slc-how-image-box {
        height: 480px !important;
        min-height: 480px !important;
      }
    }

    /* Mobile: Increased image height */
    @media (max-width: 640px) {
      .slc-how-layout {
        grid-template-columns: 1fr !important;
        gap: 24px !important;
      }
      .slc-how-image-box {
        height: 360px !important;
        min-height: 360px !important;
      }
    }


    /* =====================================================
       LOCATIONS & OTHER SECTIONS RESPONSIVENESS
       ===================================================== */
    .slc-locations-grid {
      display: grid !important;
      grid-template-columns: repeat(3, 1fr) !important;
      gap: 28px !important;
    }
    .slc-testimonials-grid {
      display: grid !important;
      grid-template-columns: repeat(3, 1fr) !important;
      gap: 28px !important;
    }
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
      display: block !important;
    }

    @media (max-width: 1024px) and (min-width: 641px) {
      .slc-locations-grid { grid-template-columns: repeat(2, 1fr) !important; }
      .slc-testimonials-grid { grid-template-columns: repeat(2, 1fr) !important; }
      .slc-about__grid { grid-template-columns: 1fr !important; gap: 32px !important; }
    }

    @media (max-width: 640px) {
      .slc-locations-grid,
      .slc-testimonials-grid,
      .slc-about__grid {
        grid-template-columns: 1fr !important;
        gap: 20px !important;
      }
      .slc-loc-media { height: 180px !important; }
    }

    /* Floating WhatsApp widget */
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
    }
    .slc-float-whatsapp:hover {
      background: #20ba5a !important;
      transform: translateY(-3px) scale(1.02) !important;
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
  <!-- End SAVELANDED INDEX responsive style -->"""

    if start_idx != -1 and end_idx != -1:
        content = content[:start_idx] + NEW_INDEX_STYLE + content[end_idx:]
    else:
        content = content.replace("</head>", NEW_INDEX_STYLE + "\n</head>")

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print("index.html updated successfully!")


# ============================================================
# 2. Update assets/css/savelanded.css
# ============================================================
def update_savelanded_css():
    with open(CSS_PATH, "r", encoding="utf-8") as f:
        css = f.read()

    # Ensure .slc-trust-strip__grid in base CSS is 5 columns
    css = re.sub(
        r"\.slc-trust-strip__grid\s*\{[^}]*grid-template-columns:\s*repeat\(\s*[34]\s*,\s*1fr\s*\)",
        ".slc-trust-strip__grid {\n      display: grid;\n      grid-template-columns: repeat(5, 1fr)",
        css
    )

    # Ensure .slc-services-grid in base CSS is 4 columns
    css = re.sub(
        r"\.slc-services-grid\s*\{[^}]*grid-template-columns:\s*repeat\(\s*3\s*,\s*1fr\s*\)",
        ".slc-services-grid {\n      display: grid;\n      grid-template-columns: repeat(4, 1fr)",
        css
    )

    # Append authoritative override at the end of savelanded.css
    CSS_ADDITIONS = """
/* ==========================================================================
   SAVELANDED HOMEPAGE REFINEMENTS (Trust Strip 5-in-row, Services 4-in-row, Large Workflow Image)
   ========================================================================== */
.slc-trust-strip__grid {
  display: grid !important;
  grid-template-columns: repeat(5, 1fr) !important;
  gap: 16px !important;
  align-items: flex-start !important;
}

@media (max-width: 1024px) and (min-width: 768px) {
  .slc-trust-strip__grid {
    display: flex !important;
    flex-wrap: nowrap !important;
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
    gap: 16px !important;
    padding-bottom: 8px !important;
  }
  .slc-trust-item {
    flex: 0 0 220px !important;
  }
}

@media (max-width: 767px) {
  .slc-trust-strip__grid {
    display: flex !important;
    flex-direction: column !important;
    gap: 12px !important;
  }
}

.slc-services-grid {
  display: grid !important;
  grid-template-columns: repeat(4, 1fr) !important;
  gap: 22px !important;
}

@media (max-width: 1024px) and (min-width: 641px) {
  .slc-services-grid {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 20px !important;
  }
}

@media (max-width: 640px) {
  .slc-services-grid {
    grid-template-columns: 1fr !important;
    gap: 18px !important;
  }
}

.slc-how-layout {
  display: grid !important;
  grid-template-columns: 1.25fr 1fr !important;
  gap: 48px !important;
  align-items: stretch !important;
}

.slc-how-image-box {
  width: 100% !important;
  height: 100% !important;
  min-height: 640px !important;
  border-radius: 20px !important;
  overflow: hidden !important;
}

@media (max-width: 1024px) and (min-width: 641px) {
  .slc-how-layout {
    grid-template-columns: 1fr !important;
    gap: 36px !important;
  }
  .slc-how-image-box {
    height: 480px !important;
    min-height: 480px !important;
  }
}

@media (max-width: 640px) {
  .slc-how-layout {
    grid-template-columns: 1fr !important;
    gap: 24px !important;
  }
  .slc-how-image-box {
    height: 360px !important;
    min-height: 360px !important;
  }
}
"""

    if "HOMEPAGE REFINEMENTS (Trust Strip 5-in-row" not in css:
        css += "\n" + CSS_ADDITIONS

    with open(CSS_PATH, "w", encoding="utf-8") as f:
        f.write(css)
    print("assets/css/savelanded.css updated successfully!")

if __name__ == "__main__":
    print("Updating index.html and savelanded.css...")
    update_index_html()
    update_savelanded_css()
    print("Complete!")

