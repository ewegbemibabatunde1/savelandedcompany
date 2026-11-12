import os
from build_multipage import update_css, get_header, get_footer, get_page_head, get_service_sidebar

update_css()

# ==============================================================================
# 1. ABOUT US PAGE (about.html)
# ==============================================================================
about_body = """
<main>
  <!-- Page Hero -->
  <header class="slc-page-hero">
    <div class="slc-container">
      <nav class="slc-breadcrumbs" aria-label="Breadcrumbs">
        <a href="index.html">Home</a>
        <span class="slc-breadcrumbs__separator">/</span>
        <span class="slc-breadcrumbs__current">About Us</span>
      </nav>
      <span class="slc-page-hero__pill">Corporate Profile</span>
      <h1 class="slc-page-hero__title">
        Bridging the Trade Gap Between <em>China and Nigeria</em>
      </h1>
      <p class="slc-page-hero__lead">
        Savelanded Import and Export Company Limited is an international trade, product sourcing, procurement, and logistics company connecting trusted manufacturers and suppliers across China with businesses throughout Nigeria.
      </p>
      <div class="slc-page-hero__actions">
        <a href="quote.html" class="slc-btn slc-btn-gold">REQUEST A QUOTE</a>
        <a href="contact.html" class="slc-btn slc-btn-outline-gold">OUR GLOBAL OFFICES</a>
      </div>
    </div>
  </header>

  <!-- Section: Our Story & Identity -->
  <section class="slc-content-section slc-content-section--white">
    <div class="slc-container">
      <div class="slc-layout-with-sidebar">
        <div class="slc-prose">
          <span style="font-family:var(--slc-font-head); font-size:0.8rem; font-weight:700; color:var(--slc-copper); letter-spacing:0.12em; text-transform:uppercase;">Who We Are</span>
          <h2>A Reliable Partner for International Trade &amp; Freight</h2>
          <p>
            Founded on the values of <strong>transparency, speed, and uncompromising integrity</strong>, Savelanded Import and Export Company Limited was created to eliminate the traditional risks, hidden charges, and communication barriers that Nigerian entrepreneurs face when dealing with Chinese suppliers.
          </p>
          <p>
            We are not merely a freight-forwarding agency. We are an end-to-end international trade enabler. We support our clients across the entire import lifecycle: from physical on-ground factory vetting and product sourcing in Yiwu and Guangzhou, to RMB procurement payments, cargo consolidation, customs clearance, and secure door-to-door delivery in Lagos and all 36 Nigerian states.
          </p>

          <div class="slc-callout">
            <strong style="color:var(--slc-black); font-size:1.05rem;">Our Brand Statement:</strong>
            <p style="margin:6px 0 0; color:var(--slc-gray-700);">
              <em>Connecting China to Nigeria. Simplifying Global Trade.</em><br>
              <strong>SOURCE. PURCHASE. SHIP. DELIVER.</strong>
            </p>
          </div>

          <h2>Our Core Values</h2>
          <div class="slc-feature-grid-2">
            <div class="slc-feature-box">
              <div class="slc-feature-box__title">1. Total Transparency</div>
              <div class="slc-feature-box__desc">
                No hidden tariffs, surprise clearance charges, or inflated exchange rates. Every invoice and cargo rate is detailed upfront.
              </div>
            </div>
            <div class="slc-feature-box">
              <div class="slc-feature-box__title">2. On-Ground Presence</div>
              <div class="slc-feature-box__desc">
                With operational offices and consolidation warehouses in Yiwu and Guangzhou, our team physically verifies cargo before shipping.
              </div>
            </div>
            <div class="slc-feature-box">
              <div class="slc-feature-box__title">3. Strict Quality Control</div>
              <div class="slc-feature-box__desc">
                We perform carton inspection, piece counts, and functional testing to protect your capital from counterfeit or damaged products.
              </div>
            </div>
            <div class="slc-feature-box">
              <div class="slc-feature-box__title">4. Cargo Accountability</div>
              <div class="slc-feature-box__desc">
                From factory gate in China to warehouse handover at Trade Fair Complex, Lagos, your goods are secured with barcode tracking.
              </div>
            </div>
          </div>

          <h2>5-Stage Anti-Fraud &amp; Verification Protocol</h2>
          <p>
            Importers frequently lose funds to unverified online storefronts, counterfeit items, or shipping middlemen who disappear. Savelanded shields your capital through an established 5-stage verification standard:
          </p>
          <ul class="slc-checklist">
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">✓</span>
              <div>
                <strong>Chinese Corporate Registration Audit:</strong> We cross-reference supplier business licenses on the National Enterprise Credit Information Publicity System.
              </div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">✓</span>
              <div>
                <strong>Physical Factory &amp; Market Inspection:</strong> Our on-ground representatives visit production lines in Guangdong and Zhejiang to verify physical operations.
              </div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">✓</span>
              <div>
                <strong>Sample Acquisition &amp; Pre-Production Approval:</strong> We obtain and examine production samples, sending high-resolution media reports to your Lagos desk.
              </div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">✓</span>
              <div>
                <strong>Controlled RMB/Yuan Disbursement:</strong> Funds are disbursed under milestone contracts, preventing supplier default or production abandonment.
              </div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">✓</span>
              <div>
                <strong>Consolidation Warehouse Audit:</strong> Goods arriving at our Yiwu and Guangzhou hubs undergo carton integrity and packaging reinforcement before loading.
              </div>
            </li>
          </ul>

          <h2>Corporate Leadership</h2>
          <p>
            Savelanded is steered by seasoned trade specialists with extensive on-ground experience in Chinese manufacturing corridors and Nigerian commercial ecosystems:
          </p>
          <div class="slc-feature-grid-2">
            <div class="slc-feature-box" style="border-top:3px solid var(--slc-gold);">
              <div style="font-family:var(--slc-font-head); font-size:1.2rem; font-weight:700;">Wolex</div>
              <div style="font-size:0.85rem; color:var(--slc-copper); font-weight:600; text-transform:uppercase; margin-bottom:12px;">Chief Executive Officer</div>
              <p style="font-size:0.9rem; color:var(--slc-gray-700); line-height:1.6;">
                Leading international trade strategy, bilateral logistics agreements, and major freight operations connecting Yiwu, Guangzhou, and Lagos.
              </p>
              <div style="margin-top:14px; font-size:0.875rem;">
                <strong>Direct Desk:</strong> <a href="tel:+8618248547224" style="color:var(--slc-charcoal); font-weight:600;">+86 182 4854 7224</a>
              </div>
            </div>
            <div class="slc-feature-box" style="border-top:3px solid var(--slc-copper);">
              <div style="font-family:var(--slc-font-head); font-size:1.2rem; font-weight:700;">svgStar</div>
              <div style="font-size:0.85rem; color:var(--slc-copper); font-weight:600; text-transform:uppercase; margin-bottom:12px;">Procurement Specialist &amp; Operations</div>
              <p style="font-size:0.9rem; color:var(--slc-gray-700); line-height:1.6;">
                Directing factory negotiations, supplier verification, 1688 procurement, and China warehouse intake coordination.
              </p>
              <div style="margin-top:14px; font-size:0.875rem;">
                <strong>Direct Desk:</strong> <a href="tel:+8615757991458" style="color:var(--slc-charcoal); font-weight:600;">+86 157 5799 1458</a>
              </div>
            </div>
          </div>

        </div>

        <!-- Sidebar -->
        <aside>
          <div class="slc-sidebar-card">
            <h3 class="slc-sidebar-heading">Our Three Strategic Hubs</h3>
            <div style="display:flex; flex-direction:column; gap:20px;">
              <div>
                <strong style="color:var(--slc-black); font-size:0.95rem;">Yiwu Head Office (China)</strong>
                <p style="font-size:0.85rem; color:var(--slc-gray-700); margin-top:4px;">
                  16, 2nd Street, Longgang Road, Yiwu City, Zhejiang Province.<br>
                  <em>Near Yiwu International Trade City (Futian).</em>
                </p>
              </div>
              <div style="border-top:1px solid var(--slc-gray-200); padding-top:16px;">
                <strong style="color:var(--slc-black); font-size:0.95rem;">Guangzhou Branch (China)</strong>
                <p style="font-size:0.85rem; color:var(--slc-gray-700); margin-top:4px;">
                  Huayag Warehouse, No. 498 Qinglong Road, Baiyun District, Guangzhou.<br>
                  <em>Serving Pearl River Delta industrial clusters.</em>
                </p>
              </div>
              <div style="border-top:1px solid var(--slc-gray-200); padding-top:16px;">
                <strong style="color:var(--slc-black); font-size:0.95rem;">Lagos Second Branch (Nigeria)</strong>
                <p style="font-size:0.85rem; color:var(--slc-gray-700); margin-top:4px;">
                  Zone B, Shop 13/14, 23/24, Edo Plaza, Balogun, Trade Fair Complex, Badagry Expressway, Ojo, Lagos.<br>
                  <em>Central cargo distribution point for Nigeria.</em>
                </p>
              </div>
            </div>
          </div>

          <div class="slc-sidebar-card slc-sidebar-card--dark">
            <div style="font-family:var(--slc-font-head); font-size:1.15rem; font-weight:700; color:var(--slc-gold); margin-bottom:12px;">Start Sourcing or Shipping</div>
            <p style="font-size:0.9rem; color:rgba(255,255,255,0.75); line-height:1.6; margin-bottom:20px;">
              Get in touch with our team in China or Nigeria to receive rate sheets and operational guidance.
            </p>
            <a href="quote.html" class="slc-btn slc-btn-gold" style="width:100%; justify-content:center;">
              <span>GET AN ACCURATE QUOTE</span>
            </a>
          </div>
        </aside>

      </div>
    </div>
  </section>
</main>
"""

with open("about.html", "w", encoding="utf-8") as f:
    f.write(get_page_head("About Savelanded", "Learn about Savelanded Import and Export Company Limited - your trusted partner connecting China manufacturers with Nigerian businesses.", "about.html") + get_header("about") + about_body + get_footer())
print("Created about.html")


# ==============================================================================
# 2. MASTER SERVICES DIRECTORY (services.html)
# ==============================================================================
services_body = """
<main>
  <!-- Page Hero -->
  <header class="slc-page-hero">
    <div class="slc-container">
      <nav class="slc-breadcrumbs" aria-label="Breadcrumbs">
        <a href="index.html">Home</a>
        <span class="slc-breadcrumbs__separator">/</span>
        <span class="slc-breadcrumbs__current">Services</span>
      </nav>
      <span class="slc-page-hero__pill">Comprehensive Solutions</span>
      <h1 class="slc-page-hero__title">
        End-to-End International <em>Trade &amp; Logistics</em>
      </h1>
      <p class="slc-page-hero__lead">
        We handle every link in the China–Nigeria supply chain. Whether you need reliable factory verification in Yiwu, RMB supplier payments, scheduled air freight, FCL/LCL sea cargo, or door-to-door delivery in Lagos, Savelanded provides dependable coordination.
      </p>
      <div class="slc-page-hero__actions">
        <a href="quote.html" class="slc-btn slc-btn-gold">REQUEST A QUOTE</a>
        <a href="contact.html" class="slc-btn slc-btn-outline-gold">SPEAK WITH OPERATIONS</a>
      </div>
    </div>
  </header>

  <!-- Master Services Grid -->
  <section class="slc-content-section slc-content-section--white">
    <div class="slc-container">
      
      <div style="text-align:center; max-width:760px; margin:0 auto 50px;">
        <span style="font-family:var(--slc-font-head); font-size:0.8rem; font-weight:700; color:var(--slc-copper); letter-spacing:0.12em; text-transform:uppercase;">What We Offer</span>
        <h2 style="font-family:var(--slc-font-head); font-size:2.2rem; font-weight:800; color:var(--slc-black); margin-top:8px;">
          Eight Specialized Services for Nigerian Importers
        </h2>
        <p style="color:var(--slc-gray-700); font-size:1.05rem; margin-top:12px;">
          Select any service below to explore detailed operational procedures, eligible cargo classifications, transit parameters, and rate requirements.
        </p>
      </div>

      <div class="slc-feature-grid-3">
        
        <!-- 1. Air Freight -->
        <article class="slc-feature-box">
          <div class="slc-feature-box__icon">
            <svg viewBox="0 0 24 24"><path d="M21 16v-2l-8-5V3.5c0-.83-.67-1.5-1.5-1.5S10 2.67 10 3.5V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z"/></svg>
          </div>
          <h3 class="slc-feature-box__title">Air Freight from China</h3>
          <p class="slc-feature-box__desc">
            Fast, secure scheduled air cargo connecting Guangzhou and Shenzhen international airport hubs to Murtala Muhammed International Airport (LOS), Lagos.
          </p>
          <div style="margin-top:20px; font-size:0.875rem;">
            <a href="air-freight.html" class="slc-btn slc-btn-outline" style="width:100%; justify-content:center;">
              <span>EXPLORE AIR FREIGHT</span>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </a>
          </div>
        </article>

        <!-- 2. Sea Freight -->
        <article class="slc-feature-box">
          <div class="slc-feature-box__icon">
            <svg viewBox="0 0 24 24"><path d="M20 21c-1.39 0-2.78-.47-4-1.32-2.44 1.71-5.56 1.71-8 0C6.78 20.53 5.39 21 4 21H2v2h2c1.38 0 2.74-.35 4-.99 2.52 1.29 5.48 1.29 8 0 1.26.65 2.62.99 4 .99h2v-2h-2zM3.95 19H4c1.6 0 3.02-.88 4-2 .98 1.12 2.4 2 4 2s3.02-.88 4-2c.98 1.12 2.4 2 4 2h.05l1.89-6.68c.08-.26.06-.54-.06-.78s-.34-.42-.6-.49L20 10.62V6c0-1.1-.9-2-2-2h-3V1H9v3H6c-1.1 0-2 .9-2 2v4.62l-1.29.36c-.26.07-.48.25-.6.49s-.14.52-.06.78L3.95 19zM6 6h12v3.97L12 8.28 6 9.97V6z"/></svg>
          </div>
          <h3 class="slc-feature-box__title">Sea Freight (FCL &amp; LCL)</h3>
          <p class="slc-feature-box__desc">
            High-volume ocean shipping from Ningbo-Zhoushan, Guangzhou, and Shenzhen to Lagos ports (Apapa &amp; Tin Can). FCL container loads &amp; LCL groupage per CBM.
          </p>
          <div style="margin-top:20px; font-size:0.875rem;">
            <a href="sea-freight.html" class="slc-btn slc-btn-outline" style="width:100%; justify-content:center;">
              <span>EXPLORE SEA FREIGHT</span>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </a>
          </div>
        </article>

        <!-- 3. Product Sourcing -->
        <article class="slc-feature-box">
          <div class="slc-feature-box__icon">
            <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg>
          </div>
          <h3 class="slc-feature-box__title">Product Sourcing &amp; Vetting</h3>
          <p class="slc-feature-box__desc">
            Physical factory visits in Yiwu &amp; Guangdong, 1688 marketplace search, sample acquisition, and comprehensive supplier credential verification.
          </p>
          <div style="margin-top:20px; font-size:0.875rem;">
            <a href="product-sourcing.html" class="slc-btn slc-btn-outline" style="width:100%; justify-content:center;">
              <span>EXPLORE SOURCING</span>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </a>
          </div>
        </article>

        <!-- 4. Procurement -->
        <article class="slc-feature-box">
          <div class="slc-feature-box__icon">
            <svg viewBox="0 0 24 24"><path d="M11.8 10.9c-2.27-.59-3-1.2-3-2.15 0-1.09 1.01-1.85 2.7-1.85 1.78 0 2.44.85 2.5 2.1h2.21c-.07-1.72-1.12-3.3-3.21-3.81V3h-3v2.16c-1.94.42-3.5 1.68-3.5 3.61 0 2.31 1.91 3.46 4.7 4.13 2.5.6 3 1.48 3 2.41 0 .69-.49 1.79-2.7 1.79-2.06 0-2.87-.92-2.98-2.1h-2.2c.12 2.19 1.76 3.42 3.68 3.83V21h3v-2.15c1.95-.37 3.5-1.5 3.5-3.55 0-2.84-2.43-3.81-4.7-4.4z"/></svg>
          </div>
          <h3 class="slc-feature-box__title">Purchasing &amp; Procurement</h3>
          <p class="slc-feature-box__desc">
            Overcoming Nigerian FX barriers with direct RMB/Yuan supplier disbursements, price negotiations, milestone payment custody, and order management.
          </p>
          <div style="margin-top:20px; font-size:0.875rem;">
            <a href="procurement.html" class="slc-btn slc-btn-outline" style="width:100%; justify-content:center;">
              <span>EXPLORE PROCUREMENT</span>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </a>
          </div>
        </article>

        <!-- 5. Warehousing -->
        <article class="slc-feature-box">
          <div class="slc-feature-box__icon">
            <svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V5h14v14zM8 7h8v2H8zm0 4h8v2H8zm0 4h5v2H8z"/></svg>
          </div>
          <h3 class="slc-feature-box__title">Warehousing &amp; Consolidation</h3>
          <p class="slc-feature-box__desc">
            Combine multiple packages from different Chinese suppliers at our Yiwu and Guangzhou hubs into a single consolidated cargo consignment to cut costs.
          </p>
          <div style="margin-top:20px; font-size:0.875rem;">
            <a href="warehousing.html" class="slc-btn slc-btn-outline" style="width:100%; justify-content:center;">
              <span>EXPLORE CONSOLIDATION</span>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </a>
          </div>
        </article>

        <!-- 6. Customs Clearance -->
        <article class="slc-feature-box">
          <div class="slc-feature-box__icon">
            <svg viewBox="0 0 24 24"><path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/></svg>
          </div>
          <h3 class="slc-feature-box__title">Customs Clearance &amp; Documentation</h3>
          <p class="slc-feature-box__desc">
            Form M processing, Pre-Arrival Assessment Report (PAAR), HS Code classification, duty valuation, and fast terminal release at Lagos ports.
          </p>
          <div style="margin-top:20px; font-size:0.875rem;">
            <a href="customs-clearance.html" class="slc-btn slc-btn-outline" style="width:100%; justify-content:center;">
              <span>EXPLORE CUSTOMS</span>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </a>
          </div>
        </article>

        <!-- 7. Import & Export -->
        <article class="slc-feature-box">
          <div class="slc-feature-box__icon">
            <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg>
          </div>
          <h3 class="slc-feature-box__title">International Import &amp; Export</h3>
          <p class="slc-feature-box__desc">
            Corporate import licensing, export documentation from China, cross-border commercial compliance, and trade advisory for high-volume distributors.
          </p>
          <div style="margin-top:20px; font-size:0.875rem;">
            <a href="import-export.html" class="slc-btn slc-btn-outline" style="width:100%; justify-content:center;">
              <span>EXPLORE IMPORT &amp; EXPORT</span>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </a>
          </div>
        </article>

        <!-- 8. Door-to-Door Delivery -->
        <article class="slc-feature-box">
          <div class="slc-feature-box__icon">
            <svg viewBox="0 0 24 24"><path d="M19 7h-3V6c0-1.1-.9-2-2-2H4c-1.1 0-2 .9-2 2v11h2c0 1.66 1.34 3 3 3s3-1.34 3-3h6c0 1.66 1.34 3 3 3s3-1.34 3-3h2v-5l-3-4zM6 18.5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zm13.5-9l1.96 2.5H17V9.5h2.5zm-.5 9c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"/></svg>
          </div>
          <h3 class="slc-feature-box__title">Door-to-Door Delivery in Nigeria</h3>
          <p class="slc-feature-box__desc">
            Hassle-free, all-inclusive freight from China to our Lagos Trade Fair distribution center, followed by reliable nationwide dispatch to all 36 states.
          </p>
          <div style="margin-top:20px; font-size:0.875rem;">
            <a href="door-to-door.html" class="slc-btn slc-btn-outline" style="width:100%; justify-content:center;">
              <span>EXPLORE DOOR-TO-DOOR</span>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </a>
          </div>
        </article>

      </div>

    </div>
  </section>
</main>
"""

with open("services.html", "w", encoding="utf-8") as f:
    f.write(get_page_head("Our Services", "Comprehensive China to Nigeria logistics, product sourcing, purchasing, freight forwarding, warehousing, and customs clearance.", "services.html") + get_header("services") + services_body + get_footer())
print("Created services.html")


# ==============================================================================
# 3. AIR FREIGHT PAGE (air-freight.html)
# ==============================================================================
air_freight_body = f"""
<main>
  <header class="slc-page-hero">
    <div class="slc-container">
      <nav class="slc-breadcrumbs" aria-label="Breadcrumbs">
        <a href="index.html">Home</a>
        <span class="slc-breadcrumbs__separator">/</span>
        <a href="services.html">Services</a>
        <span class="slc-breadcrumbs__separator">/</span>
        <span class="slc-breadcrumbs__current">Air Freight</span>
      </nav>
      <span class="slc-page-hero__pill">Express Cargo</span>
      <h1 class="slc-page-hero__title">
        Air Freight from <em>China to Nigeria</em>
      </h1>
      <p class="slc-page-hero__lead">
        When speed is critical for your commercial inventory, samples, or high-value cargo, Savelanded provides fast, secure air freight operations from Guangzhou (CAN) and Shenzhen (SZX) directly to Lagos (LOS).
      </p>
      <div class="slc-page-hero__actions">
        <a href="quote.html" class="slc-btn slc-btn-gold">REQUEST AIR FREIGHT QUOTE</a>
        <a href="tel:+8618248547224" class="slc-btn slc-btn-outline-gold">CALL AIR CARGO DESK</a>
      </div>
    </div>
  </header>

  <section class="slc-content-section slc-content-section--white">
    <div class="slc-container">
      <div class="slc-layout-with-sidebar">
        <div class="slc-prose">
          <span style="font-family:var(--slc-font-head); font-size:0.8rem; font-weight:700; color:var(--slc-copper); letter-spacing:0.12em; text-transform:uppercase;">Overview</span>
          <h2>Rapid, Dependable Air Cargo Connecting China &amp; Lagos</h2>
          <p>
            Air freight is the premier choice for Nigerian businesses requiring quick stock replenishment, time-sensitive commercial electronics, machinery spare parts, fashion seasonal runs, and urgent client orders.
          </p>
          <p>
            Savelanded operates dedicated intake desks at our <strong>Guangzhou Warehouse</strong> (Huayag Warehouse, Baiyun District) and <strong>Yiwu Head Office</strong> (Longgang Road). Goods are inspected, measured, safely re-cartoned, and dispatched on scheduled cargo flights.
          </p>

          <h2>Air Freight Specifications &amp; Operational Matrix</h2>
          <div class="slc-table-wrap">
            <table class="slc-spec-table">
              <thead>
                <tr>
                  <th>Parameter</th>
                  <th>Standard Air Cargo</th>
                  <th>Express Air Cargo</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Origin Hubs</strong></td>
                  <td>Guangzhou (CAN), Shenzhen (SZX)</td>
                  <td>Guangzhou, Hong Kong (HKG)</td>
                </tr>
                <tr>
                  <td><strong>Destination</strong></td>
                  <td>Lagos MMIA Airport (LOS)</td>
                  <td>Lagos MMIA Airport / Priority Clearance</td>
                </tr>
                <tr>
                  <td><strong>Flight Schedule</strong></td>
                  <td>2 to 3 Flights Weekly</td>
                  <td>Daily Express Routing</td>
                </tr>
                <tr>
                  <td><strong>Pricing Basis</strong></td>
                  <td>Per Kilogram (Actual vs Volumetric)</td>
                  <td>Per Kilogram Express Tier</td>
                </tr>
                <tr>
                  <td><strong>Best Suited For</strong></td>
                  <td>Clothing, phones, accessories, parts</td>
                  <td>Urgent commercial contracts, samples</td>
                </tr>
                <tr>
                  <td><strong>Handover Location</strong></td>
                  <td>Trade Fair Complex, Lagos or Doorstep</td>
                  <td>Trade Fair Complex, Lagos or Doorstep</td>
                </tr>
              </tbody>
            </table>
          </div>

          <h2>How Air Freight Billing Works: Volumetric vs. Actual Weight</h2>
          <p>
            Airlines charge according to <strong>Chargeable Weight</strong>, which is whichever is higher between the actual gross weight on the scale and the volumetric (dimensional) weight.
          </p>
          <div class="slc-callout">
            <strong>Standard Air Freight Volumetric Formula:</strong><br>
            <code>Volumetric Weight (kg) = [Length (cm) × Width (cm) × Height (cm)] / 6,000</code><br>
            <em>Example: A carton measuring 60cm × 50cm × 40cm has a volume of 120,000 cm³. Dividing by 6,000 gives 20 kg volumetric weight. If the scale weight is only 12 kg, the chargeable weight is 20 kg.</em>
          </div>

          <h2>Eligible vs. Restricted Air Cargo</h2>
          <div class="slc-feature-grid-2">
            <div class="slc-feature-box" style="border-left:4px solid #2e7d32;">
              <h3 style="color:#2e7d32; font-size:1.1rem; margin-bottom:8px;">✓ Approved Air Cargo</h3>
              <ul style="font-size:0.9rem; color:var(--slc-gray-700); padding-left:18px;">
                <li>Phones, tablets, and smart gadgets</li>
                <li>Computer accessories &amp; micro-electronics</li>
                <li>Apparel, footwear, and fashion textiles</li>
                <li>Industrial machine spare parts and tools</li>
                <li>Commercial samples and trade show kits</li>
              </ul>
            </div>
            <div class="slc-feature-box" style="border-left:4px solid #c62828;">
              <h3 style="color:#c62828; font-size:1.1rem; margin-bottom:8px;">⚠ Special Declaration / Restricted</h3>
              <ul style="font-size:0.9rem; color:var(--slc-gray-700); padding-left:18px;">
                <li>Loose lithium batteries / power banks (MSDS required)</li>
                <li>Liquids, gels, lotions &amp; pastes</li>
                <li>Pressurized aerosols &amp; flammable chemicals</li>
                <li>Powders and chemical raw substances</li>
                <li>Counterfeit brand-infringing goods</li>
              </ul>
            </div>
          </div>

          <h2>Step-by-Step Air Cargo Process</h2>
          <ul class="slc-checklist">
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">1</span>
              <div>
                <strong>Warehouse Delivery in China:</strong> Instruct your supplier to deliver to our Guangzhou or Yiwu warehouse with your unique Savelanded client code.
              </div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">2</span>
              <div>
                <strong>Intake Inspection &amp; Waybill:</strong> We weigh, measure, photograph, and generate an official intake packing list.
              </div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">3</span>
              <div>
                <strong>Flight Manifesting:</strong> Goods are palletized, air-wrapped, and loaded onto scheduled aircraft in Guangzhou.
              </div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">4</span>
              <div>
                <strong>Lagos Airport Clearance:</strong> Our licensed clearance team handles Nigerian customs assessment and airport terminal handover.
              </div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">5</span>
              <div>
                <strong>Collection or Last-Mile Delivery:</strong> Collect from our Trade Fair Complex office in Lagos or have us dispatch directly to your Nigerian doorstep.
              </div>
            </li>
          </ul>

        </div>

        {get_service_sidebar("air-freight.html")}
      </div>
    </div>
  </section>
</main>
"""

with open("air-freight.html", "w", encoding="utf-8") as f:
    f.write(get_page_head("Air Freight from China to Nigeria", "Scheduled air cargo from Guangzhou and Shenzhen to Lagos. Fast transit, secure handling, volumetric calculation.", "air-freight.html") + get_header("air-freight") + air_freight_body + get_footer())
print("Created air-freight.html")


# ==============================================================================
# 4. SEA FREIGHT PAGE (sea-freight.html)
# ==============================================================================
sea_freight_body = f"""
<main>
  <header class="slc-page-hero">
    <div class="slc-container">
      <nav class="slc-breadcrumbs" aria-label="Breadcrumbs">
        <a href="index.html">Home</a>
        <span class="slc-breadcrumbs__separator">/</span>
        <a href="services.html">Services</a>
        <span class="slc-breadcrumbs__separator">/</span>
        <span class="slc-breadcrumbs__current">Sea Freight</span>
      </nav>
      <span class="slc-page-hero__pill">Ocean Freight Forwarding</span>
      <h1 class="slc-page-hero__title">
        Sea Freight Shipping from <em>China to Lagos</em>
      </h1>
      <p class="slc-page-hero__lead">
        The most cost-effective solution for heavy commercial cargo, industrial machinery, building materials, and bulk retail merchandise. We provide both Full Container Loads (FCL) and Less than Container Loads (LCL Groupage) per CBM.
      </p>
      <div class="slc-page-hero__actions">
        <a href="quote.html" class="slc-btn slc-btn-gold">REQUEST SEA FREIGHT QUOTE</a>
        <a href="tel:+8618248547224" class="slc-btn slc-btn-outline-gold">CALL OCEAN LOGISTICS DESK</a>
      </div>
    </div>
  </header>

  <section class="slc-content-section slc-content-section--white">
    <div class="slc-container">
      <div class="slc-layout-with-sidebar">
        <div class="slc-prose">
          <span style="font-family:var(--slc-font-head); font-size:0.8rem; font-weight:700; color:var(--slc-copper); letter-spacing:0.12em; text-transform:uppercase;">Overview</span>
          <h2>High-Capacity, Economical Ocean Freight</h2>
          <p>
            When shipping large volumes, heavy commodities, or planning bulk stock replenishment, sea freight provides unmatched economic efficiency. Savelanded coordinates container bookings with major global ocean shipping lines, loading from key Chinese coastal ports:
          </p>
          <ul class="slc-checklist">
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">✓</span>
              <div><strong>Ningbo-Zhoushan &amp; Shanghai:</strong> Serving Zhejiang, Jiangsu, and Yiwu manufacturers.</div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">✓</span>
              <div><strong>Guangzhou (Nansha) &amp; Shenzhen (Yantian/Shekou):</strong> Serving the Guangdong industrial heartland.</div>
            </li>
          </ul>

          <h2>FCL vs. LCL: Which Option Fits Your Shipment?</h2>
          <div class="slc-table-wrap">
            <table class="slc-spec-table">
              <thead>
                <tr>
                  <th>Feature</th>
                  <th>Full Container Load (FCL)</th>
                  <th>Groupage Cargo (LCL)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Container Sizes</strong></td>
                  <td>20ft General Purpose, 40ft High Cube (HC)</td>
                  <td>Shared container space billed per CBM (m³)</td>
                </tr>
                <tr>
                  <td><strong>Minimum Volume</strong></td>
                  <td>1 full container (approx. 28 CBM for 20ft)</td>
                  <td>No minimum container requirement</td>
                </tr>
                <tr>
                  <td><strong>Cargo Exclusivity</strong></td>
                  <td>Your goods exclusively inside the sealed container</td>
                  <td>Goods consolidated with other Nigerian importers</td>
                </tr>
                <tr>
                  <td><strong>Documentation</strong></td>
                  <td>Individual Master Bill of Lading (MBL)</td>
                  <td>Consolidated House Bill of Lading (HBL)</td>
                </tr>
                <tr>
                  <td><strong>Destination Ports</strong></td>
                  <td>Lagos Port Complex (Apapa) / Tin Can Island</td>
                  <td>Savelanded Lagos Consolidation Terminal</td>
                </tr>
                <tr>
                  <td><strong>Best Suited For</strong></td>
                  <td>Factory orders, machinery, full vehicle lots</td>
                  <td>Small to medium retailers, varied inventory</td>
                </tr>
              </tbody>
            </table>
          </div>

          <h2>Container Specifications Reference</h2>
          <div class="slc-feature-grid-2">
            <div class="slc-feature-box">
              <div class="slc-feature-box__title">20-Foot Standard Container (20GP)</div>
              <ul style="font-size:0.9rem; color:var(--slc-gray-700); padding-left:18px; line-height:1.7;">
                <li><strong>Internal Length:</strong> 5.90 m (19.4 ft)</li>
                <li><strong>Internal Width:</strong> 2.35 m (7.7 ft)</li>
                <li><strong>Internal Height:</strong> 2.39 m (7.9 ft)</li>
                <li><strong>Usable Volume:</strong> ~28 to 30 CBM</li>
                <li><strong>Max Payload:</strong> ~21,000 to 24,000 kg</li>
              </ul>
            </div>
            <div class="slc-feature-box">
              <div class="slc-feature-box__title">40-Foot High Cube Container (40HQ)</div>
              <ul style="font-size:0.9rem; color:var(--slc-gray-700); padding-left:18px; line-height:1.7;">
                <li><strong>Internal Length:</strong> 12.03 m (39.5 ft)</li>
                <li><strong>Internal Width:</strong> 2.35 m (7.7 ft)</li>
                <li><strong>Internal Height:</strong> 2.69 m (8.8 ft)</li>
                <li><strong>Usable Volume:</strong> ~68 to 72 CBM</li>
                <li><strong>Max Payload:</strong> ~26,000 to 28,000 kg</li>
              </ul>
            </div>
          </div>

          <h2>How to Calculate Ocean Freight Volume (CBM)</h2>
          <div class="slc-callout">
            <strong>Cubic Metres (CBM) Formula:</strong><br>
            <code>CBM = [Length (m) × Width (m) × Height (m)] × Number of Cartons</code><br>
            <em>Example: 50 cartons measuring 50cm × 40cm × 30cm (0.5m × 0.4m × 0.3m = 0.06 CBM each) = 3.0 CBM total volume.</em>
          </div>

          <h2>End-to-End Sea Freight Workflow</h2>
          <ul class="slc-checklist">
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">1</span>
              <div>
                <strong>Cargo Delivery &amp; CBM Measurement:</strong> Cargo arrives at our Yiwu or Guangzhou warehouse where precision dimensions and weights are logged.
              </div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">2</span>
              <div>
                <strong>Container Stuffing &amp; Port Haulage:</strong> Goods are loaded into dry ocean containers, strapped, and sealed before transfer to Ningbo or Nansha port.
              </div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">3</span>
              <div>
                <strong>China Export Customs Clearance:</strong> Savelanded processes export declarations, port dues, and shipping line manifests.
              </div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">4</span>
              <div>
                <strong>Ocean Voyage &amp; Tracking:</strong> Vessel sails through international maritime corridors with continuous position updates.
              </div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">5</span>
              <div>
                <strong>Lagos Berth, De-Stuffing &amp; Release:</strong> Vessel discharges at Apapa/Tin Can. Groupage containers are de-stuffed at our Trade Fair Complex warehouse for easy pickup.
              </div>
            </li>
          </ul>

        </div>

        {get_service_sidebar("sea-freight.html")}
      </div>
    </div>
  </section>
</main>
"""

with open("sea-freight.html", "w", encoding="utf-8") as f:
    f.write(get_page_head("Sea Freight from China to Nigeria", "Full container loads (FCL) and groupage (LCL) shipping from Ningbo, Guangzhou, and Shenzhen to Lagos ports.", "sea-freight.html") + get_header("sea-freight") + sea_freight_body + get_footer())
print("Created sea-freight.html")


# ==============================================================================
# 5. PRODUCT SOURCING PAGE (product-sourcing.html)
# ==============================================================================
sourcing_body = f"""
<main>
  <header class="slc-page-hero">
    <div class="slc-container">
      <nav class="slc-breadcrumbs" aria-label="Breadcrumbs">
        <a href="index.html">Home</a>
        <span class="slc-breadcrumbs__separator">/</span>
        <a href="services.html">Services</a>
        <span class="slc-breadcrumbs__separator">/</span>
        <span class="slc-breadcrumbs__current">Product Sourcing</span>
      </nav>
      <span class="slc-page-hero__pill">China Trade Advisory</span>
      <h1 class="slc-page-hero__title">
        Product Sourcing &amp; <em>Supplier Verification</em>
      </h1>
      <p class="slc-page-hero__lead">
        Protect your capital and find genuine direct manufacturers in China. Our on-ground bilingual procurement specialists in Yiwu and Guangzhou verify factory credentials, assess production capacity, and examine physical samples before you commit funds.
      </p>
      <div class="slc-page-hero__actions">
        <a href="quote.html" class="slc-btn slc-btn-gold">REQUEST SOURCING ASSISTANCE</a>
        <a href="tel:+8615757991458" class="slc-btn slc-btn-outline-gold">SPEAK WITH SVGSTAR</a>
      </div>
    </div>
  </header>

  <section class="slc-content-section slc-content-section--white">
    <div class="slc-container">
      <div class="slc-layout-with-sidebar">
        <div class="slc-prose">
          <span style="font-family:var(--slc-font-head); font-size:0.8rem; font-weight:700; color:var(--slc-copper); letter-spacing:0.12em; text-transform:uppercase;">Protection &amp; Discovery</span>
          <h2>Direct Factory Access Without the Online Scams</h2>
          <p>
            Many Nigerian merchants attempt to source goods online through platforms like 1688, Taobao, or social media channels, only to encounter trading intermediaries acting as factories, substandard product substitutions, or outright fraudulent accounts.
          </p>
          <p>
            With Savelanded's registered presence in <strong>Yiwu City (Zhejiang Province)</strong> and <strong>Guangzhou (Guangdong Province)</strong>, you gain a trusted physical team that walks the factory floors, inspects production machinery, reviews raw material quality, and negotiates genuine wholesale factory pricing on your behalf.
          </p>

          <h2>Our Sourcing Channels Across China</h2>
          <div class="slc-feature-grid-3">
            <div class="slc-feature-box">
              <div class="slc-feature-box__title">Yiwu Trade City (Futian)</div>
              <div class="slc-feature-box__desc">
                Over 75,000 physical vendor booths spanning 5 massive market districts. The world capital for small commodities, household goods, toys, accessories, and hardware.
              </div>
            </div>
            <div class="slc-feature-box">
              <div class="slc-feature-box__title">Guangdong Industrial Clusters</div>
              <div class="slc-feature-box__desc">
                Direct access to specialized manufacturing belts: Shenzhen electronics, Foshan furniture and ceramics, Zhongshan lighting, and Dongguan textiles.
              </div>
            </div>
            <div class="slc-feature-box">
              <div class="slc-feature-box__title">1688.com &amp; Online B2B</div>
              <div class="slc-feature-box__desc">
                We navigate Chinese-language domestic wholesale platforms, communicating in Mandarin to negotiate local domestic pricing that foreigners cannot access.
              </div>
            </div>
          </div>

          <h2>Our 5-Point Supplier Verification Standard</h2>
          <ul class="slc-checklist">
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">1</span>
              <div>
                <strong>Corporate Registry Search:</strong> Verification of official unified social credit code, capital base, legal representative, and litigation history via Chinese registry databases.
              </div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">2</span>
              <div>
                <strong>Physical Factory vs. Trader Audit:</strong> Confirming whether the vendor owns the factory premises or is merely an unlicensed middleman taking margin cuts.
              </div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">3</span>
              <div>
                <strong>Production Line &amp; Capacity Check:</strong> Evaluating daily manufacturing output to verify whether the supplier can meet your delivery timeline.
              </div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">4</span>
              <div>
                <strong>Sample Quality Evaluation:</strong> Procuring first-off production samples, examining stitching, weight, electronic functionality, and durability.
              </div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">5</span>
              <div>
                <strong>Legally Binding Chinese Purchase Agreement:</strong> Structuring formal purchase contracts specifying defect thresholds, packing standards, and delivery terms.
              </div>
            </li>
          </ul>

          <h2>What You Receive in a Savelanded Sourcing Report</h2>
          <div class="slc-callout">
            <h4 style="font-family:var(--slc-font-head); margin-bottom:8px;">Comprehensive Sourcing Dossier</h4>
            <ul style="font-size:0.9rem; padding-left:18px; color:var(--slc-gray-700); line-height:1.6;">
              <li>Full supplier corporate credentials and contact details</li>
              <li>Detailed price breakdown per quantity tier in both RMB and USD</li>
              <li>High-resolution photos and video walkthroughs of the product</li>
              <li>Production lead times and minimum order quantities (MOQ)</li>
              <li>Estimated packaging dimensions (CBM and Gross Weight) for accurate freight forecasting</li>
            </ul>
          </div>

        </div>

        {get_service_sidebar("product-sourcing.html")}
      </div>
    </div>
  </section>
</main>
"""

with open("product-sourcing.html", "w", encoding="utf-8") as f:
    f.write(get_page_head("Product Sourcing & Supplier Verification", "Discover verified manufacturers in Yiwu and Guangzhou. Eliminate scams, verify factory licenses, and inspect samples.", "product-sourcing.html") + get_header("product-sourcing") + sourcing_body + get_footer())
print("Created product-sourcing.html")


# ==============================================================================
# 6. PROCUREMENT PAGE (procurement.html)
# ==============================================================================
procurement_body = f"""
<main>
  <header class="slc-page-hero">
    <div class="slc-container">
      <nav class="slc-breadcrumbs" aria-label="Breadcrumbs">
        <a href="index.html">Home</a>
        <span class="slc-breadcrumbs__separator">/</span>
        <a href="services.html">Services</a>
        <span class="slc-breadcrumbs__separator">/</span>
        <span class="slc-breadcrumbs__current">Purchasing &amp; Procurement</span>
      </nav>
      <span class="slc-page-hero__pill">Procurement &amp; Payment Desk</span>
      <h1 class="slc-page-hero__title">
        Purchasing &amp; <em>Procurement Coordination</em>
      </h1>
      <p class="slc-page-hero__lead">
        Eliminate foreign exchange headaches and language barriers. Savelanded coordinates order placement, price negotiation, contract execution, and secure RMB/Yuan payments directly to verified Chinese manufacturers on your behalf.
      </p>
      <div class="slc-page-hero__actions">
        <a href="quote.html" class="slc-btn slc-btn-gold">REQUEST PROCUREMENT DESK</a>
        <a href="tel:+8615757991458" class="slc-btn slc-btn-outline-gold">CALL SVGSTAR (+86 157 5799 1458)</a>
      </div>
    </div>
  </header>

  <section class="slc-content-section slc-content-section--white">
    <div class="slc-container">
      <div class="slc-layout-with-sidebar">
        <div class="slc-prose">
          <span style="font-family:var(--slc-font-head); font-size:0.8rem; font-weight:700; color:var(--slc-copper); letter-spacing:0.12em; text-transform:uppercase;">Seamless Trade</span>
          <h2>Overcoming the Nigerian Foreign Exchange &amp; Payment Hurdle</h2>
          <p>
            One of the greatest challenges for Nigerian importers is transferring funds securely to suppliers in China. Traditional bank wire transfers (Form M / Letters of Credit) often suffer from prolonged delays, high bank charges, or foreign exchange scarcity. Moreover, Chinese domestic manufacturers often do not hold foreign currency export licenses and demand payment in Chinese Yuan (RMB) via local bank accounts or Alipay/WeChat Pay.
          </p>
          <p>
            Savelanded resolves this bottleneck. Through our registered Chinese business entities in Yiwu and Guangzhou, we facilitate seamless RMB settlements to your suppliers under formal commercial agreements, ensuring that your funds are applied directly to production without delay.
          </p>

          <h2>Our Procurement Workflow</h2>
          <div class="slc-feature-grid-2">
            <div class="slc-feature-box">
              <div class="slc-feature-box__title">1. Proforma Invoice Verification</div>
              <div class="slc-feature-box__desc">
                We review the supplier's commercial invoice, item descriptions, unit prices, bank details, and production timeline to ensure complete alignment.
              </div>
            </div>
            <div class="slc-feature-box">
              <div class="slc-feature-box__title">2. Price &amp; Terms Negotiation</div>
              <div class="slc-feature-box__desc">
                Our bilingual negotiators communicate in Mandarin to obtain wholesale volume discounts, reduced deposit requirements, and strict packaging standards.
              </div>
            </div>
            <div class="slc-feature-box">
              <div class="slc-feature-box__title">3. Milestone Payment Custody</div>
              <div class="slc-feature-box__desc">
                We manage payments in tranches: initial deposit (typically 30%), followed by the final balance (70%) released ONLY after goods are verified at our warehouse.
              </div>
            </div>
            <div class="slc-feature-box">
              <div class="slc-feature-box__title">4. Production Milestone Monitoring</div>
              <div class="slc-feature-box__desc">
                We maintain active communication with the factory floor, monitoring progress to prevent unauthorized delays or material substitutions.
              </div>
            </div>
          </div>

          <h2>Why Nigerian Businesses Choose Savelanded for Procurement</h2>
          <ul class="slc-checklist">
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">✓</span>
              <div>
                <strong>Zero Payment Scams:</strong> You never send money directly to an unverified private bank account in China. Payments flow through Savelanded's audited corporate channels.
              </div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">✓</span>
              <div>
                <strong>Native Language Negotiation:</strong> We speak fluent Mandarin and understand Chinese business etiquette (Guanxi), enabling us to secure terms that foreign buyers cannot access.
              </div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">✓</span>
              <div>
                <strong>Combined Sourcing &amp; Shipping:</strong> Because we manage both procurement and shipping, we eliminate finger-pointing between separate purchasing agents and freight forwarders.
              </div>
            </li>
          </ul>

        </div>

        {get_service_sidebar("procurement.html")}
      </div>
    </div>
  </section>
</main>
"""

with open("procurement.html", "w", encoding="utf-8") as f:
    f.write(get_page_head("Purchasing & Procurement in China", "Seamless order placement, price negotiation, and secure RMB/Yuan payments to Chinese factories.", "procurement.html") + get_header("procurement") + procurement_body + get_footer())
print("Created procurement.html")


# ==============================================================================
# 7. WAREHOUSING PAGE (warehousing.html)
# ==============================================================================
warehousing_body = f"""
<main>
  <header class="slc-page-hero">
    <div class="slc-container">
      <nav class="slc-breadcrumbs" aria-label="Breadcrumbs">
        <a href="index.html">Home</a>
        <span class="slc-breadcrumbs__separator">/</span>
        <a href="services.html">Services</a>
        <span class="slc-breadcrumbs__separator">/</span>
        <span class="slc-breadcrumbs__current">Warehousing &amp; Consolidation</span>
      </nav>
      <span class="slc-page-hero__pill">Ground Operations</span>
      <h1 class="slc-page-hero__title">
        Warehousing &amp; <em>Cargo Consolidation</em>
      </h1>
      <p class="slc-page-hero__lead">
        Buying from multiple suppliers across China? Savelanded consolidates all your packages at our strategically situated warehouses in Yiwu and Guangzhou into a single master shipment, drastically lowering your freight and clearance costs.
      </p>
      <div class="slc-page-hero__actions">
        <a href="quote.html" class="slc-btn slc-btn-gold">REQUEST WAREHOUSE SPACE</a>
        <a href="contact.html" class="slc-btn slc-btn-outline-gold">VIEW WAREHOUSE ADDRESSES</a>
      </div>
    </div>
  </header>

  <section class="slc-content-section slc-content-section--white">
    <div class="slc-container">
      <div class="slc-layout-with-sidebar">
        <div class="slc-prose">
          <span style="font-family:var(--slc-font-head); font-size:0.8rem; font-weight:700; color:var(--slc-copper); letter-spacing:0.12em; text-transform:uppercase;">Consolidation Efficiency</span>
          <h2>Why Cargo Consolidation is the Smart Importer's Secret</h2>
          <p>
            When purchasing smaller quantities from three, five, or ten different suppliers across China, shipping each package individually by air or sea results in multiple base freight fees, separate documentation charges, and duplicated clearance expenses in Lagos.
          </p>
          <p>
            With Savelanded's <strong>Cargo Consolidation Service</strong>, your suppliers dispatch their goods to our domestic warehouse hubs. We receive each package, verify carton counts against your packing list, safely store them, and pack them together into a unified container or air cargo pallet.
          </p>

          <h2>Our Strategic Warehousing Facilities in China</h2>
          <div class="slc-feature-grid-2">
            <div class="slc-feature-box">
              <div class="slc-feature-box__title">Yiwu Consolidation Hub</div>
              <p style="font-size:0.9rem; color:var(--slc-gray-700); margin:8px 0 14px;">
                <strong>16, 2nd Street, Longgang Road, Yiwu City, Zhejiang Province.</strong>
              </p>
              <ul style="font-size:0.875rem; color:var(--slc-gray-700); padding-left:18px; line-height:1.6;">
                <li>Ideal for commodities, home items, hardware, and accessories</li>
                <li>Direct loading for Ningbo-Zhoushan ocean port</li>
                <li>Dedicated sorting, barcode scanning, and repacking area</li>
              </ul>
            </div>
            <div class="slc-feature-box">
              <div class="slc-feature-box__title">Guangzhou Airport &amp; Port Hub</div>
              <p style="font-size:0.9rem; color:var(--slc-gray-700); margin:8px 0 14px;">
                <strong>Huayag Warehouse, No. 498 Qinglong Road, Baiyun District, Guangzhou.</strong>
              </p>
              <ul style="font-size:0.875rem; color:var(--slc-gray-700); padding-left:18px; line-height:1.6;">
                <li>Positioned next to Guangzhou Baiyun International Airport (CAN)</li>
                <li>Ideal for Pearl River Delta machinery, fashion, and electronics</li>
                <li>Direct haulage to Guangzhou Nansha and Shenzhen ocean terminals</li>
              </ul>
            </div>
          </div>

          <h2>Warehouse Value-Added Services</h2>
          <ul class="slc-checklist">
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">✓</span>
              <div>
                <strong>Outer Packaging Inspection:</strong> Checking for crushed cartons, moisture damage, or factory packing defects immediately upon arrival.
              </div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">✓</span>
              <div>
                <strong>Wooden Crating &amp; Palletizing:</strong> Reinforcing fragile machinery, electronics, glass, or sensitive cargo with certified wooden frames.
              </div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">✓</span>
              <div>
                <strong>Waterproof Wrapping &amp; Heavy-Duty Strapping:</strong> Ensuring moisture and dust resistance throughout long maritime or flight transits.
              </div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">✓</span>
              <div>
                <strong>Custom Barcode &amp; Mark Tagging:</strong> Clear shipping mark labels with your company name, city, and consignment reference number.
              </div>
            </li>
          </ul>

        </div>

        {get_service_sidebar("warehousing.html")}
      </div>
    </div>
  </section>
</main>
"""

with open("warehousing.html", "w", encoding="utf-8") as f:
    f.write(get_page_head("Warehousing & Cargo Consolidation", "Consolidate goods from multiple Chinese suppliers at our Yiwu and Guangzhou hubs to cut shipping costs.", "warehousing.html") + get_header("warehousing") + warehousing_body + get_footer())
print("Created warehousing.html")


# ==============================================================================
# 8. CUSTOMS CLEARANCE PAGE (customs-clearance.html)
# ==============================================================================
customs_body = f"""
<main>
  <header class="slc-page-hero">
    <div class="slc-container">
      <nav class="slc-breadcrumbs" aria-label="Breadcrumbs">
        <a href="index.html">Home</a>
        <span class="slc-breadcrumbs__separator">/</span>
        <a href="services.html">Services</a>
        <span class="slc-breadcrumbs__separator">/</span>
        <span class="slc-breadcrumbs__current">Customs Clearance</span>
      </nav>
      <span class="slc-page-hero__pill">Regulatory Compliance</span>
      <h1 class="slc-page-hero__title">
        Customs Clearance &amp; <em>Port Documentation</em>
      </h1>
      <p class="slc-page-hero__lead">
        Navigating Nigerian import regulations requires meticulous documentation and proactive terminal management. Savelanded coordinates Form M, PAAR documentation, HS Code classification, tariff computation, and rapid cargo release at Lagos seaports and air terminals.
      </p>
      <div class="slc-page-hero__actions">
        <a href="quote.html" class="slc-btn slc-btn-gold">REQUEST CUSTOMS CONSULTATION</a>
        <a href="tel:+8618248547224" class="slc-btn slc-btn-outline-gold">CALL COMPLIANCE DESK</a>
      </div>
    </div>
  </header>

  <section class="slc-content-section slc-content-section--white">
    <div class="slc-container">
      <div class="slc-layout-with-sidebar">
        <div class="slc-prose">
          <span style="font-family:var(--slc-font-head); font-size:0.8rem; font-weight:700; color:var(--slc-copper); letter-spacing:0.12em; text-transform:uppercase;">Compliance &amp; Clearance</span>
          <h2>Preventing Demurrage, Penalties &amp; Prolonged Port Delays</h2>
          <p>
            Customs clearance in Nigeria can become complex and expensive if documentation is incomplete, cargo is misclassified under incorrect Harmonized System (HS) Codes, or terminal inspection requirements are mishandled. Shipping containers left at port quickly accrue steep shipping line demurrage and terminal storage fees.
          </p>
          <p>
            Savelanded's clearance professionals liaise with the Nigeria Customs Service (NCS), terminal operators (APM Terminals, TICT, PTML), and regulatory agencies (SONCAP, NAFDAC) to ensure prompt inspection, duty assessment, and gate pass release.
          </p>

          <h2>Key Import Documents Managed by Savelanded</h2>
          <div class="slc-feature-grid-2">
            <div class="slc-feature-box">
              <div class="slc-feature-box__title">Bill of Lading (B/L) &amp; AWB</div>
              <div class="slc-feature-box__desc">
                Ensuring clean Master and House shipping documents that accurately reflect consignee details, container numbers, and seal integrity.
              </div>
            </div>
            <div class="slc-feature-box">
              <div class="slc-feature-box__title">Form M Processing</div>
              <div class="slc-feature-box__desc">
                Registering statutory Form M with Authorized Dealer Banks and the Central Bank of Nigeria (CBN) for commercial import validation.
              </div>
            </div>
            <div class="slc-feature-box">
              <div class="slc-feature-box__title">PAAR (Pre-Arrival Assessment)</div>
              <div class="slc-feature-box__desc">
                Submitting verified commercial invoices, packing lists, and transport documents for expedited customs valuation before vessel discharge.
              </div>
            </div>
            <div class="slc-feature-box">
              <div class="slc-feature-box__title">SONCAP &amp; NAFDAC Guidance</div>
              <div class="slc-feature-box__desc">
                Providing regulatory advisory on product conformity certificates (SONCAP) and registration requirements for regulated consumer goods.
              </div>
            </div>
          </div>

          <h2>Ports &amp; Terminals Covered in Lagos</h2>
          <ul class="slc-checklist">
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">✓</span>
              <div><strong>Lagos Port Complex, Apapa:</strong> APM Terminals (APMT), GDNL.</div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">✓</span>
              <div><strong>Tin Can Island Port:</strong> TICT, Port &amp; Cargo Terminal.</div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">✓</span>
              <div><strong>Murtala Muhammed International Airport (MMIA):</strong> NAHCO &amp; SAHCO Cargo Sheds.</div>
            </li>
          </ul>

        </div>

        {get_service_sidebar("customs-clearance.html")}
      </div>
    </div>
  </section>
</main>
"""

with open("customs-clearance.html", "w", encoding="utf-8") as f:
    f.write(get_page_head("Customs Clearance & Documentation", "Smooth, compliant cargo clearance at Nigerian ports. Form M, PAAR, HS Code valuation, and terminal release.", "customs-clearance.html") + get_header("customs-clearance") + customs_body + get_footer())
print("Created customs-clearance.html")


# ==============================================================================
# 9. IMPORT & EXPORT PAGE (import-export.html)
# ==============================================================================
import_export_body = f"""
<main>
  <header class="slc-page-hero">
    <div class="slc-container">
      <nav class="slc-breadcrumbs" aria-label="Breadcrumbs">
        <a href="index.html">Home</a>
        <span class="slc-breadcrumbs__separator">/</span>
        <a href="services.html">Services</a>
        <span class="slc-breadcrumbs__separator">/</span>
        <span class="slc-breadcrumbs__current">Import &amp; Export</span>
      </nav>
      <span class="slc-page-hero__pill">Bilateral Trade Facilitation</span>
      <h1 class="slc-page-hero__title">
        International Import &amp; <em>Export Operations</em>
      </h1>
      <p class="slc-page-hero__lead">
        Expanding your enterprise through cross-border trade between China and Nigeria. Savelanded coordinates export customs declarations, international trade documentation, commercial contracts, and structured freight management for corporate entities.
      </p>
      <div class="slc-page-hero__actions">
        <a href="quote.html" class="slc-btn slc-btn-gold">REQUEST TRADE CONSULTATION</a>
        <a href="contact.html" class="slc-btn slc-btn-outline-gold">OFFICE DIRECTORY</a>
      </div>
    </div>
  </header>

  <section class="slc-content-section slc-content-section--white">
    <div class="slc-container">
      <div class="slc-layout-with-sidebar">
        <div class="slc-prose">
          <span style="font-family:var(--slc-font-head); font-size:0.8rem; font-weight:700; color:var(--slc-copper); letter-spacing:0.12em; text-transform:uppercase;">Global Trade</span>
          <h2>A Reliable Corporate Partner for Cross-Border Commerce</h2>
          <p>
            Operating across international trade corridors involves navigating complex customs systems, currency regulations, and maritime conventions. Savelanded acts as an accredited operational bridge connecting manufacturers in China's industrial zones with commercial distributors, retailers, and corporate importers in Nigeria.
          </p>

          <h2>Understanding Incoterms with Savelanded</h2>
          <p>
            We advise our clients on selecting the appropriate International Commercial Terms (Incoterms) to minimize risks and avoid duplicate freight expenses:
          </p>
          <div class="slc-table-wrap">
            <table class="slc-spec-table">
              <thead>
                <tr>
                  <th>Incoterm</th>
                  <th>Supplier Obligation</th>
                  <th>Savelanded Role</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>EXW (Ex Works)</strong></td>
                  <td>Makes goods available at their factory floor</td>
                  <td>We arrange factory pickup, China domestic transport, export customs, freight, and Lagos delivery</td>
                </tr>
                <tr>
                  <td><strong>FOB (Free on Board)</strong></td>
                  <td>Delivers goods to Chinese departure port and clears export customs</td>
                  <td>We book international ocean/air freight, handle transit, Nigerian clearance, and delivery</td>
                </tr>
                <tr>
                  <td><strong>CIF (Cost, Insurance &amp; Freight)</strong></td>
                  <td>Covers ocean freight to Lagos port and basic maritime insurance</td>
                  <td>We take over at Lagos port, conduct customs clearance, and manage inland haulage</td>
                </tr>
                <tr>
                  <td><strong>DDP (Delivered Duty Paid)</strong></td>
                  <td>All-inclusive door delivery to customer warehouse</td>
                  <td>Savelanded's signature complete door-to-door service covering all legs, duties, and handling</td>
                </tr>
              </tbody>
            </table>
          </div>

          <h2>Export Clearance from China</h2>
          <p>
            When goods depart China, domestic export customs regulations require legitimate export licensing, tax rebate declarations, and commodity inspection filings. Our registered Chinese trading entities handle all departure documentation seamlessly.
          </p>

        </div>

        {get_service_sidebar("import-export.html")}
      </div>
    </div>
  </section>
</main>
"""

with open("import-export.html", "w", encoding="utf-8") as f:
    f.write(get_page_head("International Import & Export", "Bilateral China-Nigeria trade advisory, export customs declarations, Incoterms, and commercial compliance.", "import-export.html") + get_header("import-export") + import_export_body + get_footer())
print("Created import-export.html")


# ==============================================================================
# 10. DOOR-TO-DOOR PAGE (door-to-door.html)
# ==============================================================================
door_body = f"""
<main>
  <header class="slc-page-hero">
    <div class="slc-container">
      <nav class="slc-breadcrumbs" aria-label="Breadcrumbs">
        <a href="index.html">Home</a>
        <span class="slc-breadcrumbs__separator">/</span>
        <a href="services.html">Services</a>
        <span class="slc-breadcrumbs__separator">/</span>
        <span class="slc-breadcrumbs__current">Door-to-Door Delivery</span>
      </nav>
      <span class="slc-page-hero__pill">Turnkey Logistics</span>
      <h1 class="slc-page-hero__title">
        Door-to-Door Delivery <em>Across Nigeria</em>
      </h1>
      <p class="slc-page-hero__lead">
        The ultimate peace of mind. We take responsibility from the supplier's warehouse in China, manage export, ocean/air shipping, Nigerian customs duty, and deliver directly to your store, warehouse, or residence in Lagos and nationwide across all 36 states.
      </p>
      <div class="slc-page-hero__actions">
        <a href="quote.html" class="slc-btn slc-btn-gold">REQUEST DOOR-TO-DOOR QUOTE</a>
        <a href="contact.html" class="slc-btn slc-btn-outline-gold">LAGOS DISTRIBUTION HUB</a>
      </div>
    </div>
  </header>

  <section class="slc-content-section slc-content-section--white">
    <div class="slc-container">
      <div class="slc-layout-with-sidebar">
        <div class="slc-prose">
          <span style="font-family:var(--slc-font-head); font-size:0.8rem; font-weight:700; color:var(--slc-copper); letter-spacing:0.12em; text-transform:uppercase;">All-Inclusive Freight</span>
          <h2>Zero Stress: From Chinese Factory to Your Nigerian Doorstep</h2>
          <p>
            Managing individual logistics vendors—arranging China domestic couriers, coordinating with a freight agent, finding an independent clearing agent in Apapa, and hiring local haulage trucks—is time-consuming and fraught with finger-pointing if cargo is delayed or damaged.
          </p>
          <p>
            With Savelanded's <strong>All-Inclusive Door-to-Door Cargo Service</strong>, you receive one consolidated rate that covers:
          </p>
          <ul class="slc-checklist">
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">✓</span>
              <div><strong>China Receiving &amp; Consolidation</strong> at our Yiwu or Guangzhou warehouse.</div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">✓</span>
              <div><strong>Export Handling &amp; Documentation</strong> at Chinese airports or seaports.</div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">✓</span>
              <div><strong>International Air or Ocean Freight</strong> directly to Lagos.</div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">✓</span>
              <div><strong>Nigerian Customs Clearing &amp; Terminal Port Charges</strong> fully settled.</div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">✓</span>
              <div><strong>Final Last-Mile Dispatch</strong> to your business premises in Nigeria.</div>
            </li>
          </ul>

          <h2>Our Nigerian Central Distribution Hub</h2>
          <div class="slc-callout">
            <strong style="font-family:var(--slc-font-head); font-size:1.1rem; color:var(--slc-black);">Lagos Second Branch Hub:</strong>
            <p style="margin-top:6px; color:var(--slc-charcoal);">
              <strong>Zone B, Shop 13/14, 23/24, Edo Plaza, Balogun, Trade Fair Complex, Badagry Expressway, Ojo, Lagos, Nigeria.</strong><br>
              <em>Centrally located in West Africa's largest commercial trading hub for easy self-pickup or prompt nationwide dispatch.</em>
            </p>
          </div>

          <h2>Nationwide Dispatch to Major Commercial Centres</h2>
          <p>
            Once goods complete customs clearance in Lagos, our domestic logistics network delivers across all 36 states, including:
          </p>
          <div class="slc-feature-grid-3">
            <div class="slc-feature-box">
              <div class="slc-feature-box__title">South West</div>
              <div class="slc-feature-box__desc">
                Lagos (Ikeja, Alaba, Trade Fair, Idumota), Ibadan, Abeokuta, Akure, Osogbo.
              </div>
            </div>
            <div class="slc-feature-box">
              <div class="slc-feature-box__title">South East &amp; South South</div>
              <div class="slc-feature-box__desc">
                Onitsha (Main Market), Aba, Port Harcourt, Enugu, Asaba, Benin City, Warri.
              </div>
            </div>
            <div class="slc-feature-box">
              <div class="slc-feature-box__title">North &amp; Central</div>
              <div class="slc-feature-box__desc">
                Abuja (FCT), Kano (Sabon Gari, Singer), Kaduna, Jos, Ilorin, Minna.
              </div>
            </div>
          </div>

        </div>

        {get_service_sidebar("door-to-door.html")}
      </div>
    </div>
  </section>
</main>
"""

with open("door-to-door.html", "w", encoding="utf-8") as f:
    f.write(get_page_head("Door-to-Door Delivery in Nigeria", "Direct cargo delivery from China to our Lagos Trade Fair distribution hub and nationwide across all 36 states.", "door-to-door.html") + get_header("door-to-door") + door_body + get_footer())
print("Created door-to-door.html")


# ==============================================================================
# 11. SHIPPING GUIDE & CALCULATOR PAGE (shipping.html)
# ==============================================================================
shipping_body = """
<main>
  <header class="slc-page-hero">
    <div class="slc-container">
      <nav class="slc-breadcrumbs" aria-label="Breadcrumbs">
        <a href="index.html">Home</a>
        <span class="slc-breadcrumbs__separator">/</span>
        <span class="slc-breadcrumbs__current">Shipping Guide</span>
      </nav>
      <span class="slc-page-hero__pill">Freight Decision Guide</span>
      <h1 class="slc-page-hero__title">
        China to Nigeria <em>Shipping &amp; Logistics Guide</em>
      </h1>
      <p class="slc-page-hero__lead">
        Everything you need to know to make cost-effective shipping decisions. Compare air and ocean freight, calculate dimensional weights, understand transit timelines, and review packaging standards.
      </p>
      <div class="slc-page-hero__actions">
        <a href="quote.html" class="slc-btn slc-btn-gold">REQUEST ACCURATE RATES</a>
        <a href="#calc-section" class="slc-btn slc-btn-outline-gold">JUMP TO CALCULATORS</a>
      </div>
    </div>
  </header>

  <section class="slc-content-section slc-content-section--white">
    <div class="slc-container">
      
      <div class="slc-prose" style="max-width:900px; margin:0 auto 60px;">
        <span style="font-family:var(--slc-font-head); font-size:0.8rem; font-weight:700; color:var(--slc-copper); letter-spacing:0.12em; text-transform:uppercase;">Decision Matrix</span>
        <h2>Air Freight vs. Sea Freight: Making the Right Choice</h2>
        <p>
          Selecting between air cargo and sea cargo depends primarily on your cargo's total weight/volume, urgency, and profit margins. Review our quick comparison below:
        </p>

        <div class="slc-table-wrap">
          <table class="slc-spec-table">
            <thead>
              <tr>
                <th>Factor</th>
                <th>Air Freight</th>
                <th>Sea Freight (LCL / FCL)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Primary Advantage</strong></td>
                <td>Maximum speed, lower holding inventory</td>
                <td>Lowest cost per unit on bulk cargo</td>
              </tr>
              <tr>
                <td><strong>Billing Unit</strong></td>
                <td>Per Kilogram (kg)</td>
                <td>Per Cubic Metre (CBM) or per Container</td>
              </tr>
              <tr>
                <td><strong>Typical Cargo</strong></td>
                <td>Phones, smart watches, fashion runs, samples</td>
                <td>Heavy machinery, furniture, building materials</td>
              </tr>
              <tr>
                <td><strong>Transit Timeline</strong></td>
                <td>Fast scheduled flight routing to Lagos</td>
                <td>Ocean maritime transit to Lagos ports</td>
              </tr>
              <tr>
                <td><strong>Weight Limit</strong></td>
                <td>Higher cost for heavy/bulky goods</td>
                <td>Ideal for multi-tonne commercial loads</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Interactive Calculators Section -->
      <div id="calc-section" style="max-width:900px; margin:0 auto 70px;">
        <div style="text-align:center; margin-bottom:32px;">
          <span class="slc-page-hero__pill" style="background:#FFF3E8; border-color:var(--slc-gold); color:var(--slc-charcoal);">Interactive Tools</span>
          <h2 style="font-family:var(--slc-font-head); font-size:2rem; font-weight:800;">Cargo Dimension Calculators</h2>
          <p style="color:var(--slc-gray-700); font-size:0.95rem;">Estimate your shipment's CBM (ocean) and volumetric weight (air) instantly.</p>
        </div>

        <div class="slc-grid-2col" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(340px, 1fr)); gap:28px;">
          
          <!-- Tool 1: CBM Calculator (Sea) -->
          <div class="slc-calc-card">
            <h3 style="font-family:var(--slc-font-head); font-size:1.25rem; font-weight:700; margin-bottom:16px; color:var(--slc-black);">
              Ocean Freight CBM Calculator
            </h3>
            <p style="font-size:0.85rem; color:var(--slc-gray-700); margin-bottom:18px;">Enter package dimensions in centimeters (cm) and number of cartons.</p>
            
            <div class="slc-form-grid">
              <div class="slc-form-group">
                <label class="slc-label">Length (cm)</label>
                <input type="number" id="cbm-l" class="slc-input" value="60" min="1">
              </div>
              <div class="slc-form-group">
                <label class="slc-label">Width (cm)</label>
                <input type="number" id="cbm-w" class="slc-input" value="40" min="1">
              </div>
              <div class="slc-form-group">
                <label class="slc-label">Height (cm)</label>
                <input type="number" id="cbm-h" class="slc-input" value="40" min="1">
              </div>
              <div class="slc-form-group">
                <label class="slc-label">Quantity of Cartons</label>
                <input type="number" id="cbm-qty" class="slc-input" value="10" min="1">
              </div>
            </div>

            <button type="button" id="btn-calc-cbm" class="slc-btn slc-btn-gold" style="width:100%; justify-content:center; margin-top:14px;">
              <span>CALCULATE CBM</span>
            </button>

            <div class="slc-calc-result">
              <div style="font-size:0.8rem; text-transform:uppercase; letter-spacing:0.1em; color:var(--slc-gold);">Total Volume</div>
              <div class="slc-calc-val" id="res-cbm">0.96 CBM</div>
              <div style="font-size:0.8rem; color:rgba(255,255,255,0.7); margin-top:4px;">(0.096 CBM per carton)</div>
            </div>
          </div>

          <!-- Tool 2: Volumetric Weight Calculator (Air) -->
          <div class="slc-calc-card">
            <h3 style="font-family:var(--slc-font-head); font-size:1.25rem; font-weight:700; margin-bottom:16px; color:var(--slc-black);">
              Air Cargo Volumetric Weight
            </h3>
            <p style="font-size:0.85rem; color:var(--slc-gray-700); margin-bottom:18px;">Airlines bill whichever is higher: actual scale weight vs dimensional weight.</p>
            
            <div class="slc-form-grid">
              <div class="slc-form-group">
                <label class="slc-label">Length (cm)</label>
                <input type="number" id="air-l" class="slc-input" value="50" min="1">
              </div>
              <div class="slc-form-group">
                <label class="slc-label">Width (cm)</label>
                <input type="number" id="air-w" class="slc-input" value="40" min="1">
              </div>
              <div class="slc-form-group">
                <label class="slc-label">Height (cm)</label>
                <input type="number" id="air-h" class="slc-input" value="30" min="1">
              </div>
              <div class="slc-form-group">
                <label class="slc-label">Scale Weight (kg)</label>
                <input type="number" id="air-scale" class="slc-input" value="8" min="0.1" step="0.1">
              </div>
            </div>

            <button type="button" id="btn-calc-air" class="slc-btn slc-btn-gold" style="width:100%; justify-content:center; margin-top:14px;">
              <span>CALCULATE CHARGEABLE WEIGHT</span>
            </button>

            <div class="slc-calc-result">
              <div style="font-size:0.8rem; text-transform:uppercase; letter-spacing:0.1em; color:var(--slc-gold);">Chargeable Weight</div>
              <div class="slc-calc-val" id="res-air">10.0 kg</div>
              <div style="font-size:0.8rem; color:rgba(255,255,255,0.7); margin-top:4px;" id="res-air-note">Volumetric (10.0kg) exceeds scale weight (8.0kg)</div>
            </div>
          </div>

        </div>
      </div>

    </div>
  </section>
</main>

<script>
  (function() {
    var btnCbm = document.getElementById('btn-calc-cbm');
    var btnAir = document.getElementById('btn-calc-air');

    if (btnCbm) {
      btnCbm.addEventListener('click', function() {
        var l = parseFloat(document.getElementById('cbm-l').value) || 0;
        var w = parseFloat(document.getElementById('cbm-w').value) || 0;
        var h = parseFloat(document.getElementById('cbm-h').value) || 0;
        var qty = parseInt(document.getElementById('cbm-qty').value, 10) || 1;
        var singleCbm = (l * w * h) / 1000000;
        var totalCbm = singleCbm * qty;
        document.getElementById('res-cbm').innerText = totalCbm.toFixed(2) + ' CBM';
      });
    }

    if (btnAir) {
      btnAir.addEventListener('click', function() {
        var l = parseFloat(document.getElementById('air-l').value) || 0;
        var w = parseFloat(document.getElementById('air-w').value) || 0;
        var h = parseFloat(document.getElementById('air-h').value) || 0;
        var scale = parseFloat(document.getElementById('air-scale').value) || 0;
        var vol = (l * w * h) / 6000;
        var chargeable = Math.max(scale, vol);
        document.getElementById('res-air').innerText = chargeable.toFixed(1) + ' kg';
        var note = document.getElementById('res-air-note');
        if (vol > scale) {
          note.innerText = 'Volumetric (' + vol.toFixed(1) + 'kg) exceeds scale weight (' + scale.toFixed(1) + 'kg)';
        } else {
          note.innerText = 'Scale weight (' + scale.toFixed(1) + 'kg) exceeds volumetric (' + vol.toFixed(1) + 'kg)';
        }
      });
    }
  })();
</script>
"""

with open("shipping.html", "w", encoding="utf-8") as f:
    f.write(get_page_head("China to Nigeria Shipping Guide", "Compare Air vs Sea freight, calculate CBM and volumetric weight, packaging guidelines, and transit timelines.", "shipping.html") + get_header("shipping") + shipping_body + get_footer())
print("Created shipping.html")


# ==============================================================================
# 12. CONTACT PAGE (contact.html)
# ==============================================================================
contact_body = """
<main>
  <header class="slc-page-hero">
    <div class="slc-container">
      <nav class="slc-breadcrumbs" aria-label="Breadcrumbs">
        <a href="index.html">Home</a>
        <span class="slc-breadcrumbs__separator">/</span>
        <span class="slc-breadcrumbs__current">Contact Us</span>
      </nav>
      <span class="slc-page-hero__pill">Direct Communication</span>
      <h1 class="slc-page-hero__title">
        Connect With Our <em>China &amp; Nigeria Offices</em>
      </h1>
      <p class="slc-page-hero__lead">
        Have questions regarding product sourcing, factory visits, RMB payments, warehouse receiving, or cargo clearing? Speak directly with our key executive contacts in Yiwu, Guangzhou, and Lagos.
      </p>
    </div>
  </header>

  <section class="slc-content-section slc-content-section--white">
    <div class="slc-container">
      
      <!-- 3 Physical Hub Cards -->
      <div class="slc-feature-grid-3" style="margin-bottom:60px;">
        
        <div class="slc-feature-box" style="border-top:4px solid var(--slc-gold);">
          <div style="font-size:0.75rem; font-weight:700; color:var(--slc-copper); letter-spacing:0.1em; text-transform:uppercase;">China Head Office</div>
          <h3 style="font-family:var(--slc-font-head); font-size:1.3rem; font-weight:700; margin:8px 0 12px; color:var(--slc-black);">Yiwu, Zhejiang</h3>
          <p style="font-size:0.95rem; color:var(--slc-gray-700); line-height:1.6; margin-bottom:18px;">
            <strong>Address:</strong><br>
            16, 2nd Street, Longgang Road, Yiwu City, Zhejiang Province, China.
          </p>
          <div style="font-size:0.875rem; border-top:1px solid var(--slc-gray-200); padding-top:14px;">
            <strong>Lead Contact:</strong> CEO Wolex<br>
            <strong>Phone / WeChat:</strong> <a href="tel:+8618248547224" style="color:var(--slc-charcoal); font-weight:700;">+86 182 4854 7224</a>
          </div>
        </div>

        <div class="slc-feature-box" style="border-top:4px solid var(--slc-copper);">
          <div style="font-size:0.75rem; font-weight:700; color:var(--slc-copper); letter-spacing:0.1em; text-transform:uppercase;">China First Branch</div>
          <h3 style="font-family:var(--slc-font-head); font-size:1.3rem; font-weight:700; margin:8px 0 12px; color:var(--slc-black);">Guangzhou Warehouse</h3>
          <p style="font-size:0.95rem; color:var(--slc-gray-700); line-height:1.6; margin-bottom:18px;">
            <strong>Address:</strong><br>
            Huayag Warehouse, No. 498 Qinglong Road, Baiyun District, Guangzhou, China.
          </p>
          <div style="font-size:0.875rem; border-top:1px solid var(--slc-gray-200); padding-top:14px;">
            <strong>Lead Contact:</strong> svgStar (Procurement)<br>
            <strong>Phone / WeChat:</strong> <a href="tel:+8615757991458" style="color:var(--slc-charcoal); font-weight:700;">+86 157 5799 1458</a>
          </div>
        </div>

        <div class="slc-feature-box" style="border-top:4px solid var(--slc-black);">
          <div style="font-size:0.75rem; font-weight:700; color:var(--slc-copper); letter-spacing:0.1em; text-transform:uppercase;">Nigeria Second Branch</div>
          <h3 style="font-family:var(--slc-font-head); font-size:1.3rem; font-weight:700; margin:8px 0 12px; color:var(--slc-black);">Lagos Trade Fair</h3>
          <p style="font-size:0.95rem; color:var(--slc-gray-700); line-height:1.6; margin-bottom:18px;">
            <strong>Address:</strong><br>
            Zone B, Shop 13/14, 23/24, Edo Plaza, Balogun, Trade Fair Complex, Badagry Expressway, Ojo, Lagos.
          </p>
          <div style="font-size:0.875rem; border-top:1px solid var(--slc-gray-200); padding-top:14px;">
            <strong>Operations:</strong> Lagos Receiving &amp; Clearing<br>
            <strong>Official Email:</strong> <a href="mailto:svgadmsavelandedimpexpcomltd@gmail.com" style="color:var(--slc-charcoal); font-weight:600; word-break:break-all;">svgadmsavelandedimpexpcomltd@gmail.com</a>
          </div>
        </div>

      </div>

      <!-- Direct Inquiry Form -->
      <div style="max-width:800px; margin:0 auto;">
        <div class="slc-form-card">
          <div style="text-align:center; margin-bottom:28px;">
            <span class="slc-page-hero__pill" style="background:#FFF3E8; border-color:var(--slc-gold); color:var(--slc-charcoal);">Official Inquiry Desk</span>
            <h2 style="font-family:var(--slc-font-head); font-size:1.8rem; font-weight:800; margin-top:8px;">Send a Direct Message</h2>
            <p style="color:var(--slc-gray-700); font-size:0.95rem;">Our customer desk acknowledges all trade inquiries within 2 to 4 business hours.</p>
          </div>

          <form id="contact-form">
            <div class="slc-form-grid">
              <div class="slc-form-group">
                <label class="slc-label" for="cnt-name">Your Full Name *</label>
                <input type="text" id="cnt-name" class="slc-input" required placeholder="e.g. Chief Emeka Adeleke">
              </div>
              <div class="slc-form-group">
                <label class="slc-label" for="cnt-phone">Phone / WhatsApp Number *</label>
                <input type="tel" id="cnt-phone" class="slc-input" required placeholder="+234 ...">
              </div>
              <div class="slc-form-group">
                <label class="slc-label" for="cnt-email">Email Address *</label>
                <input type="email" id="cnt-email" class="slc-input" required placeholder="name@company.com">
              </div>
              <div class="slc-form-group">
                <label class="slc-label" for="cnt-interest">Inquiry Category *</label>
                <select id="cnt-interest" class="slc-select">
                  <option value="General Cargo Inquiry">General Cargo Inquiry</option>
                  <option value="Air Freight from China">Air Freight from China</option>
                  <option value="Sea Freight (FCL / LCL)">Sea Freight (FCL / LCL)</option>
                  <option value="Product Sourcing & Supplier Verification">Product Sourcing &amp; Supplier Verification</option>
                  <option value="RMB Payment & Procurement">RMB Payment &amp; Procurement</option>
                  <option value="Warehousing & Consolidation">Warehousing &amp; Consolidation</option>
                  <option value="Customs Clearance at Lagos Port">Customs Clearance at Lagos Port</option>
                </select>
              </div>
              <div class="slc-form-group slc-form-group--full">
                <label class="slc-label" for="cnt-msg">Message / Cargo Details *</label>
                <textarea id="cnt-msg" class="slc-textarea" required placeholder="Describe your product, weight, volume, or specific question..."></textarea>
              </div>
            </div>

            <div style="margin-top:20px; text-align:center;">
              <button type="submit" class="slc-btn slc-btn-gold" style="width:100%; justify-content:center; padding:16px;">
                <span>SEND DIRECT INQUIRY EMAIL</span>
                <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
              </button>
            </div>
          </form>

        </div>
      </div>

    </div>
  </section>
</main>

<script>
  (function() {
    var form = document.getElementById('contact-form');
    if (form) {
      form.addEventListener('submit', function(e) {
        e.preventDefault();
        var name = document.getElementById('cnt-name').value;
        var phone = document.getElementById('cnt-phone').value;
        var email = document.getElementById('cnt-email').value;
        var category = document.getElementById('cnt-interest').value;
        var msg = document.getElementById('cnt-msg').value;

        var subject = encodeURIComponent('[Savelanded Inquiry] ' + category + ' - ' + name);
        var body = encodeURIComponent(
          'SAVELANDED TRADE INQUIRY\\n' +
          '----------------------------------------\\n' +
          'Name: ' + name + '\\n' +
          'Phone / WhatsApp: ' + phone + '\\n' +
          'Email: ' + email + '\\n' +
          'Category: ' + category + '\\n\\n' +
          'Message / Details:\\n' + msg + '\\n\\n' +
          'Sent via savelandedcompany.com contact portal'
        );

        window.location.href = 'mailto:svgadmsavelandedimpexpcomltd@gmail.com?subject=' + subject + '&body=' + body;
      });
    }
  })();
</script>
"""

with open("contact.html", "w", encoding="utf-8") as f:
    f.write(get_page_head("Contact Savelanded & Global Offices", "Direct office contacts for Yiwu Head Office, Guangzhou Warehouse, and Lagos Trade Fair Complex branch.", "contact.html") + get_header("contact") + contact_body + get_footer())
print("Created contact.html")


# ==============================================================================
# 13. QUOTATION REQUEST WIZARD PAGE (quote.html)
# ==============================================================================
quote_body = """
<main>
  <header class="slc-page-hero">
    <div class="slc-container">
      <nav class="slc-breadcrumbs" aria-label="Breadcrumbs">
        <a href="index.html">Home</a>
        <span class="slc-breadcrumbs__separator">/</span>
        <span class="slc-breadcrumbs__current">Request a Quote</span>
      </nav>
      <span class="slc-page-hero__pill">Accurate Pricing</span>
      <h1 class="slc-page-hero__title">
        Request an Itemized <em>China–Nigeria Freight Quote</em>
      </h1>
      <p class="slc-page-hero__lead">
        No hidden fees or unexpected clearing surcharges. Submit your cargo specifications below and our logistics desk in China and Lagos will calculate your accurate rate schedule.
      </p>
    </div>
  </header>

  <section class="slc-content-section slc-content-section--white">
    <div class="slc-container">
      
      <div style="max-width:880px; margin:0 auto;">
        <div class="slc-form-card">
          
          <form id="quote-form">
            <h3 style="font-family:var(--slc-font-head); font-size:1.3rem; font-weight:700; color:var(--slc-black); margin-bottom:18px; padding-bottom:8px; border-bottom:2px solid var(--slc-gold);">
              1. Service Selection
            </h3>
            
            <div class="slc-form-grid" style="margin-bottom:30px;">
              <div class="slc-form-group slc-form-group--full">
                <label class="slc-label">Select Requested Service *</label>
                <select id="q-service" class="slc-select" required>
                  <option value="Air Freight (Guangzhou/Shenzhen to Lagos)">Air Freight (Guangzhou/Shenzhen to Lagos)</option>
                  <option value="Sea Freight LCL Groupage (Per CBM)">Sea Freight LCL Groupage (Per CBM)</option>
                  <option value="Sea Freight FCL (20ft / 40ft Container)">Sea Freight FCL (20ft / 40ft Container)</option>
                  <option value="Product Sourcing & Supplier Verification">Product Sourcing &amp; Supplier Verification</option>
                  <option value="Purchasing & RMB Payment Coordination">Purchasing &amp; RMB Payment Coordination</option>
                  <option value="Warehousing & Multi-Supplier Consolidation">Warehousing &amp; Multi-Supplier Consolidation</option>
                  <option value="Complete Door-to-Door Delivery (China to Nigeria)">Complete Door-to-Door Delivery (China to Nigeria)</option>
                </select>
              </div>
            </div>

            <h3 style="font-family:var(--slc-font-head); font-size:1.3rem; font-weight:700; color:var(--slc-black); margin-bottom:18px; padding-bottom:8px; border-bottom:2px solid var(--slc-gold);">
              2. Cargo Specifications
            </h3>

            <div class="slc-form-grid" style="margin-bottom:30px;">
              <div class="slc-form-group slc-form-group--full">
                <label class="slc-label">Product / Cargo Description *</label>
                <input type="text" id="q-cargo" class="slc-input" required placeholder="e.g. Smart watches, textile rolls, solar panels, auto spare parts">
              </div>
              <div class="slc-form-group">
                <label class="slc-label">Estimated Gross Weight (kg)</label>
                <input type="number" id="q-weight" class="slc-input" placeholder="e.g. 150">
              </div>
              <div class="slc-form-group">
                <label class="slc-label">Estimated Volume (CBM / m³)</label>
                <input type="number" id="q-cbm" class="slc-input" step="0.01" placeholder="e.g. 2.4">
              </div>
              <div class="slc-form-group">
                <label class="slc-label">Number of Cartons / Packages</label>
                <input type="number" id="q-pkgs" class="slc-input" placeholder="e.g. 15">
              </div>
              <div class="slc-form-group">
                <label class="slc-label">Cargo Origin in China</label>
                <select id="q-origin" class="slc-select">
                  <option value="Yiwu Warehouse">Yiwu Warehouse</option>
                  <option value="Guangzhou Warehouse">Guangzhou Warehouse</option>
                  <option value="Shenzhen">Shenzhen</option>
                  <option value="Ningbo">Ningbo</option>
                  <option value="Foshan">Foshan</option>
                  <option value="Other / Factory Pickup">Other / Factory Pickup</option>
                </select>
              </div>
            </div>

            <h3 style="font-family:var(--slc-font-head); font-size:1.3rem; font-weight:700; color:var(--slc-black); margin-bottom:18px; padding-bottom:8px; border-bottom:2px solid var(--slc-gold);">
              3. Destination &amp; Client Details
            </h3>

            <div class="slc-form-grid">
              <div class="slc-form-group">
                <label class="slc-label">Your Full Name *</label>
                <input type="text" id="q-name" class="slc-input" required placeholder="e.g. Alhaji Musa Bello">
              </div>
              <div class="slc-form-group">
                <label class="slc-label">Company / Business Name</label>
                <input type="text" id="q-company" class="slc-input" placeholder="e.g. Bello Global Ventures Ltd">
              </div>
              <div class="slc-form-group">
                <label class="slc-label">WhatsApp / Phone Number *</label>
                <input type="tel" id="q-phone" class="slc-input" required placeholder="+234 ...">
              </div>
              <div class="slc-form-group">
                <label class="slc-label">Email Address *</label>
                <input type="email" id="q-email" class="slc-input" required placeholder="name@domain.com">
              </div>
              <div class="slc-form-group slc-form-group--full">
                <label class="slc-label">Delivery City in Nigeria *</label>
                <input type="text" id="q-dest" class="slc-input" required placeholder="e.g. Lagos (Trade Fair pickup), Abuja, Onitsha, Kano, Port Harcourt">
              </div>
              <div class="slc-form-group slc-form-group--full">
                <label class="slc-label">Additional Instructions / Inquiries</label>
                <textarea id="q-notes" class="slc-textarea" placeholder="Include any supplier details, carton dimensions (L x W x H), or special handling needs..."></textarea>
              </div>
            </div>

            <div style="margin-top:30px; display:flex; flex-direction:column; gap:12px;">
              <button type="submit" class="slc-btn slc-btn-gold" style="width:100%; justify-content:center; padding:16px;">
                <span>COMPILE &amp; SUBMIT QUOTE REQUEST</span>
                <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
              </button>
              <div style="font-size:0.8rem; color:var(--slc-gray-500); text-align:center;">
                Submissions automatically compile a pre-formatted message addressed to our official desk at <strong>svgadmsavelandedimpexpcomltd@gmail.com</strong> and CEO Wolex.
              </div>
            </div>

          </form>

        </div>
      </div>

    </div>
  </section>
</main>

<script>
  (function() {
    var form = document.getElementById('quote-form');
    if (form) {
      form.addEventListener('submit', function(e) {
        e.preventDefault();
        var service = document.getElementById('q-service').value;
        var cargo = document.getElementById('q-cargo').value;
        var weight = document.getElementById('q-weight').value || 'Not specified';
        var cbm = document.getElementById('q-cbm').value || 'Not specified';
        var pkgs = document.getElementById('q-pkgs').value || 'Not specified';
        var origin = document.getElementById('q-origin').value;
        var name = document.getElementById('q-name').value;
        var company = document.getElementById('q-company').value || 'Individual';
        var phone = document.getElementById('q-phone').value;
        var email = document.getElementById('q-email').value;
        var dest = document.getElementById('q-dest').value;
        var notes = document.getElementById('q-notes').value || 'None';

        var subject = encodeURIComponent('[Savelanded Quotation Request] ' + service + ' - ' + name);
        var body = encodeURIComponent(
          'SAVELANDED FREIGHT & SOURCING QUOTE REQUEST\\n' +
          '================================================\\n' +
          'Requested Service: ' + service + '\\n\\n' +
          'CARGO DETAILS:\\n' +
          '- Description: ' + cargo + '\\n' +
          '- Gross Weight: ' + weight + ' kg\\n' +
          '- Volume: ' + cbm + ' CBM\\n' +
          '- Packages: ' + pkgs + ' cartons\\n' +
          '- Origin in China: ' + origin + '\\n' +
          '- Delivery Destination in Nigeria: ' + dest + '\\n\\n' +
          'CLIENT DETAILS:\\n' +
          '- Name: ' + name + '\\n' +
          '- Company: ' + company + '\\n' +
          '- WhatsApp/Phone: ' + phone + '\\n' +
          '- Email: ' + email + '\\n\\n' +
          'ADDITIONAL NOTES:\\n' + notes + '\\n\\n' +
          '================================================\\n' +
          'Transmitted via Savelanded Web Portal (savelandedcompany.com)'
        );

        window.location.href = 'mailto:svgadmsavelandedimpexpcomltd@gmail.com?subject=' + subject + '&body=' + body;
      });
    }
  })();
</script>
"""

with open("quote.html", "w", encoding="utf-8") as f:
    f.write(get_page_head("Request a Quote", "Get an accurate China to Nigeria shipping, product sourcing, or procurement quote tailored to your cargo specifications.", "quote.html") + get_header("quote") + quote_body + get_footer())
print("Created quote.html")

print("ALL 12 SUBPAGES CREATED SUCCESSFULLY!")
