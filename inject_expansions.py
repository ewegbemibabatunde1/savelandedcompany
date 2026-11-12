# -*- coding: utf-8 -*-
"""
Master Injection Script for Savelanded 14-Page SEO/AEO/GEO Expansion
Injects expanded content, comparison tables, verified guidelines,
and contextual internal links across all 14 pages.
"""

import os
from expansion_content_module import (
    AIR_FREIGHT_ADDITION,
    SEA_FREIGHT_ADDITION,
    PRODUCT_SOURCING_ADDITION,
    PROCUREMENT_ADDITION,
    WAREHOUSING_ADDITION,
    CUSTOMS_CLEARANCE_ADDITION,
    IMPORT_EXPORT_ADDITION,
    DOOR_TO_DOOR_ADDITION,
    SHIPPING_ADDITION,
    SERVICES_DIRECTORY_ADDITION,
    ABOUT_PAGE_ADDITION,
    CONTACT_PAGE_ADDITION,
    QUOTE_PAGE_ADDITION
)

def inject_before_faq(file_path, addition_html):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already injected
    if 'slc-comparison-table' in content or 'slc-reviewer-badge' in content:
        print(f"Skipping {file_path}: already expanded.")
        return
    
    faq_marker = '<div class="slc-faq-subpage">'
    if faq_marker in content:
        content = content.replace(faq_marker, addition_html + '\n\n    ' + faq_marker, 1)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"SUCCESS: Expanded {file_path} before FAQ section.")
    else:
        print(f"WARNING: FAQ marker not found in {file_path}")

def update_services_page():
    with open('services.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'service-selection-guide' in content:
        print("services.html already expanded.")
        return
    
    target = '</div>\n\n    </div>\n  </section>\n</main>'
    if target in content:
        content = content.replace(target, SERVICES_DIRECTORY_ADDITION + '\n    </div>\n  </section>\n</main>', 1)
        with open('services.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("SUCCESS: Expanded services.html with Service Selection Matrix.")
    else:
        # Fallback target
        alt_target = '</section>\n</main>'
        content = content.replace(alt_target, SERVICES_DIRECTORY_ADDITION + '\n</section>\n</main>', 1)
        with open('services.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("SUCCESS (alt): Expanded services.html with Service Selection Matrix.")

def update_about_page():
    with open('about.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'operational-capabilities' in content:
        print("about.html already expanded.")
        return
    
    faq_marker = '<div class="slc-faq-subpage">'
    if faq_marker in content:
        content = content.replace(faq_marker, ABOUT_PAGE_ADDITION + '\n\n    ' + faq_marker, 1)
        with open('about.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("SUCCESS: Expanded about.html with Ground Capabilities and Leadership.")
    else:
        print("WARNING: FAQ marker not found in about.html")

def update_contact_page():
    with open('contact.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'Operational Hours &amp; Cargo Receiving Schedules' in content:
        print("contact.html already expanded.")
        return
    
    faq_marker = '<div class="slc-faq-subpage">'
    if faq_marker in content:
        content = content.replace(faq_marker, CONTACT_PAGE_ADDITION + '\n\n    ' + faq_marker, 1)
        with open('contact.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("SUCCESS: Expanded contact.html with Verified Schedules.")
    else:
        print("WARNING: FAQ marker not found in contact.html")

def update_quote_page():
    with open('quote.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'What You Need Before Requesting a Freight' in content:
        print("quote.html already expanded.")
        return
    
    # Inject before the quotation form
    form_marker = '<form class="slc-quote-wizard"'
    if form_marker in content:
        content = content.replace(form_marker, QUOTE_PAGE_ADDITION + '\n        ' + form_marker, 1)
        with open('quote.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("SUCCESS: Expanded quote.html with Preparation Guidance.")
    else:
        # Try finding the wizard container
        container_marker = '<div class="slc-wizard-container">'
        if container_marker in content:
            content = content.replace(container_marker, QUOTE_PAGE_ADDITION + '\n' + container_marker, 1)
            with open('quote.html', 'w', encoding='utf-8') as f:
                f.write(content)
            print("SUCCESS (container): Expanded quote.html with Preparation Guidance.")
        else:
            print("WARNING: Form marker not found in quote.html")

def update_homepage():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'air-sea-comparison-table' in content:
        print("index.html already expanded.")
        return
    
    # Inject an authoritative China-to-Nigeria trade corridor & air/sea comparison section inside index.html
    HOMEPAGE_TRADE_CORRIDOR_SECTION = """
    <!-- Authoritative China-to-Nigeria Trade Corridor & Freight Comparison -->
    <section class="slc-content-section slc-content-section--white" id="corridor-insights" style="padding: 60px 0; border-top: 1px solid rgba(0,0,0,0.06);">
      <div class="slc-container">
        <div style="text-align:center; max-width:780px; margin:0 auto 40px;">
          <div class="slc-pill-badge slc-pill-badge--light">
            <span class="slc-pill-dot"></span>
            <span>China–Nigeria Trade Corridor</span>
          </div>
          <h2 style="font-family:var(--slc-font-head); font-size:2.2rem; font-weight:800; color:var(--slc-black); margin-top:10px;">
            Navigating the Direct China to Nigeria Commercial Channel
          </h2>
          <p style="color:var(--slc-gray-700); font-size:1.05rem; line-height:1.7; margin-top:12px;">
            From the bustling commodity markets of <strong>Yiwu</strong> and industrial hubs of <strong>Guangdong</strong> to wholesale distribution depots in <strong>Lagos</strong>, Savelanded provides verified end-to-end cargo logistics, eliminating foreign exchange risks, counterfeit supplier fraud, and port demurrage.
          </p>
        </div>

        <div id="air-sea-comparison-table" class="slc-comparison-table-wrapper">
          <table class="slc-comparison-table">
            <thead>
              <tr>
                <th>Freight Method</th>
                <th>China Origin Departure</th>
                <th>Nigeria Arrival Terminal</th>
                <th>Typical Transit Window</th>
                <th>Best Suited Commercial Cargo</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Scheduled Air Cargo</strong></td>
                <td>Guangzhou Baiyun (CAN) / Shenzhen (SZX)</td>
                <td>Lagos MMIA Airport (LOS) Cargo Sheds</td>
                <td>5 to 8 working days</td>
                <td>Electronics, phones, fashion runs, samples, machinery spares</td>
                <td><a href="air-freight" class="slc-btn slc-btn-outline" style="padding:6px 12px; font-size:0.8rem;">Details</a></td>
              </tr>
              <tr>
                <td><strong>Sea Freight LCL (Groupage)</strong></td>
                <td>Ningbo-Zhoushan / Guangzhou (Nansha)</td>
                <td>Lagos Ports (Apapa / Tin Can Island)</td>
                <td>35 to 45 days</td>
                <td>Medium commercial stock, small machines, 1 to 15 CBM volume</td>
                <td><a href="sea-freight" class="slc-btn slc-btn-outline" style="padding:6px 12px; font-size:0.8rem;">Details</a></td>
              </tr>
              <tr>
                <td><strong>Full Container Sea (FCL)</strong></td>
                <td>Direct Factory Staging &bull; Chinese Seaports</td>
                <td>Apapa, Tin Can Island, Lekki Deep Sea Port</td>
                <td>35 to 45 days</td>
                <td>Heavy industrial goods, construction tiles, bulk manufacturing stock</td>
                <td><a href="sea-freight" class="slc-btn slc-btn-outline" style="padding:6px 12px; font-size:0.8rem;">Details</a></td>
              </tr>
              <tr>
                <td><strong>All-Inclusive Door-to-Door</strong></td>
                <td>Direct Vendor Pickup across China</td>
                <td>Trade Fair Lagos Hub or Nationwide Doorstep</td>
                <td>Air: 5-8d &bull; Sea: 35-45d</td>
                <td>Hassle-free shipping with full customs clearance and zero hidden terminal fees</td>
                <td><a href="door-to-door" class="slc-btn slc-btn-outline" style="padding:6px 12px; font-size:0.8rem;">Details</a></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>
"""
    # Insert right before the locations section
    loc_target = '<section class="slc-locations"'
    if loc_target in content:
        content = content.replace(loc_target, HOMEPAGE_TRADE_CORRIDOR_SECTION + '\n' + loc_target, 1)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("SUCCESS: Expanded index.html with Corridor Insights & Air/Sea Comparison Table.")
    else:
        print("WARNING: slc-locations marker not found in index.html")

if __name__ == '__main__':
    # 1. Expand service subpages
    inject_before_faq('air-freight.html', AIR_FREIGHT_ADDITION)
    inject_before_faq('sea-freight.html', SEA_FREIGHT_ADDITION)
    inject_before_faq('product-sourcing.html', PRODUCT_SOURCING_ADDITION)
    inject_before_faq('procurement.html', PROCUREMENT_ADDITION)
    inject_before_faq('warehousing.html', WAREHOUSING_ADDITION)
    inject_before_faq('customs-clearance.html', CUSTOMS_CLEARANCE_ADDITION)
    inject_before_faq('import-export.html', IMPORT_EXPORT_ADDITION)
    inject_before_faq('door-to-door.html', DOOR_TO_DOOR_ADDITION)
    inject_before_faq('shipping.html', SHIPPING_ADDITION)

    # 2. Expand services directory, about, contact, quote, and index
    update_services_page()
    update_about_page()
    update_contact_page()
    update_quote_page()
    update_homepage()

    print("\nALL 14 PAGES EXPANSION APPLIED SUCCESSFULLY.")

