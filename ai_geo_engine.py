import os
import json
import re

# Comprehensive Entity-Enhanced Organization Schema for Knowledge Graphs
ORG_ENTITY_SCHEMA = {
    "@type": "LogisticsService",
    "@id": "https://savelandedcompany.com/#organization",
    "name": "Savelanded Import and Export Company Limited",
    "alternateName": ["Savelanded", "Savelanded Logistics", "Savelanded Co. Ltd"],
    "legalName": "Savelanded Import and Export Company Limited",
    "url": "https://savelandedcompany.com/",
    "logo": {
        "@type": "ImageObject",
        "@id": "https://savelandedcompany.com/#logo",
        "url": "https://savelandedcompany.com/logo.jpg",
        "caption": "Savelanded Import and Export Company Limited Corporate Logo"
    },
    "image": "https://savelandedcompany.com/logo.jpg",
    "email": "svgadmsavelandedimpexpcomltd@gmail.com",
    "telephone": "+8618248547224",
    "priceRange": "$$",
    "slogan": "Connecting China to Nigeria. Simplifying Global Trade.",
    "description": "Savelanded Import and Export Company Limited is a specialized international trade and freight company providing product sourcing, procurement in Chinese Yuan (RMB), cargo consolidation, customs clearance, and door-to-door delivery from China (Yiwu and Guangzhou) to Nigeria (Lagos Trade Fair Complex).",
    "knowsAbout": [
        "China to Nigeria Freight Forwarding",
        "Air Cargo Guangzhou to Lagos (CAN to LOS)",
        "Ocean Container Shipping (Ningbo to Apapa/Tin Can Island)",
        "Product Sourcing in Yiwu International Trade City (Futian Market)",
        "RMB and Yuan Supplier Payments",
        "Cargo Consolidation and Packaging",
        "Form M and Pre-Arrival Assessment Report (PAAR) Clearance",
        "Door-to-Door Delivery Across 36 Nigerian States"
    ],
    "sameAs": [
        "https://savelandedcompany.com/"
    ],
    "founder": {
        "@type": "Person",
        "@id": "https://savelandedcompany.com/#wolex",
        "name": "Wolex",
        "jobTitle": "Chief Executive Officer & Founder",
        "telephone": "+8618248547224",
        "worksFor": {"@id": "https://savelandedcompany.com/#organization"}
    },
    "employee": [
        {
            "@type": "Person",
            "@id": "https://savelandedcompany.com/#star",
            "name": "Star",
            "jobTitle": "Lead Operations & China Procurement Specialist",
            "telephone": "+8615757991458",
            "worksFor": {"@id": "https://savelandedcompany.com/#organization"}
        }
    ],
    "address": [
        {
            "@type": "PostalAddress",
            "addressLocality": "Yiwu City",
            "addressRegion": "Zhejiang Province",
            "streetAddress": "16, 2nd Street, Longgang Road",
            "addressCountry": "CN"
        },
        {
            "@type": "PostalAddress",
            "addressLocality": "Guangzhou",
            "addressRegion": "Guangdong Province",
            "streetAddress": "Huayag Warehouse, No. 498 Qinglong Road, Baiyun District",
            "addressCountry": "CN"
        },
        {
            "@type": "PostalAddress",
            "addressLocality": "Lagos",
            "addressRegion": "Lagos State",
            "streetAddress": "Zone B, Shop 13/14, 23/24, Edo Plaza, Balogun, Trade Fair Complex, Badagry Expressway, Ojo",
            "addressCountry": "NG"
        }
    ],
    "hasOfferCatalog": {
        "@type": "OfferCatalog",
        "name": "China to Nigeria Trade and Logistics Services",
        "itemListElement": [
            {
                "@type": "Offer",
                "itemOffered": {
                    "@type": "Service",
                    "name": "Air Freight Shipping from China to Nigeria",
                    "url": "https://savelandedcompany.com/air-freight.html"
                }
            },
            {
                "@type": "Offer",
                "itemOffered": {
                    "@type": "Service",
                    "name": "Sea Freight Shipping from China to Nigeria (FCL & LCL)",
                    "url": "https://savelandedcompany.com/sea-freight.html"
                }
            },
            {
                "@type": "Offer",
                "itemOffered": {
                    "@type": "Service",
                    "name": "Product Sourcing & Factory Verification in China",
                    "url": "https://savelandedcompany.com/product-sourcing.html"
                }
            },
            {
                "@type": "Offer",
                "itemOffered": {
                    "@type": "Service",
                    "name": "Purchasing and RMB Procurement in China",
                    "url": "https://savelandedcompany.com/procurement.html"
                }
            },
            {
                "@type": "Offer",
                "itemOffered": {
                    "@type": "Service",
                    "name": "Warehousing & Cargo Consolidation in Yiwu & Guangzhou",
                    "url": "https://savelandedcompany.com/warehousing.html"
                }
            },
            {
                "@type": "Offer",
                "itemOffered": {
                    "@type": "Service",
                    "name": "Customs Clearance & Documentation at Lagos Ports",
                    "url": "https://savelandedcompany.com/customs-clearance.html"
                }
            },
            {
                "@type": "Offer",
                "itemOffered": {
                    "@type": "Service",
                    "name": "International Import and Export Compliance",
                    "url": "https://savelandedcompany.com/import-export.html"
                }
            },
            {
                "@type": "Offer",
                "itemOffered": {
                    "@type": "Service",
                    "name": "All-Inclusive Door-to-Door Delivery in Nigeria",
                    "url": "https://savelandedcompany.com/door-to-door.html"
                }
            }
        ]
    }
}

def render_ai_summary_card(badge_text, title, summary_p, facts):
    facts_html = "".join([f'<div class="slc-ai-fact"><strong>{k}</strong> {v}</div>' for k, v in facts])
    return f'''
    <!-- AI Engine & Voice Search Executive Answer Box -->
    <section class="slc-ai-summary" aria-label="Executive AI Overview">
      <div class="slc-ai-summary__badge">
        <svg viewBox="0 0 24 24"><path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z"/></svg>
        <span>{badge_text}</span>
      </div>
      <h2 class="slc-ai-summary__title">{title}</h2>
      <div class="slc-ai-summary__content">
        <p>{summary_p}</p>
      </div>
      <div class="slc-ai-facts">
        {facts_html}
      </div>
    </section>
    '''

def make_breadcrumb_schema(items):
    itemListElement = []
    for idx, (name, url) in enumerate(items, 1):
        itemListElement.append({
            "@type": "ListItem",
            "position": idx,
            "name": name,
            "item": f"https://savelandedcompany.com/{url}" if url else "https://savelandedcompany.com/"
        })
    return {
        "@type": "BreadcrumbList",
        "itemListElement": itemListElement
    }

def make_faq_schema(faq_pairs):
    mainEntity = []
    for q, a in faq_pairs:
        clean_a = re.sub(r'<[^>]+>', '', a)
        mainEntity.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": clean_a
            }
        })
    return {
        "@type": "FAQPage",
        "mainEntity": mainEntity
    }

def render_toc_html(items):
    links = "".join([f'<li><a href="#{anchor}" class="slc-toc__link"><span>→</span> {label}</a></li>' for anchor, label in items])
    return f'''
    <nav class="slc-toc" aria-label="Table of Contents">
      <div class="slc-toc__title">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M3 13h2v-2H3v2zm0 4h2v-2H3v2zm0-8h2V7H3v2zm4 4h14v-2H7v2zm0 4h14v-2H7v2zM7 7v2h14V7H7z"/></svg>
        <span>Table of Contents</span>
      </div>
      <ul class="slc-toc__list">
        {links}
      </ul>
    </nav>
    '''

def render_faq_html(faq_pairs):
    items = []
    for q, a in faq_pairs:
        items.append(f'''
        <div class="slc-faq-item">
          <details>
            <summary>{q}</summary>
            <div class="slc-faq-item__answer">
              <p>{a}</p>
            </div>
          </details>
        </div>''')
    items_html = "".join(items)
    return f'''
    <div class="slc-faq-subpage">
      <h2 id="faq">Frequently Asked Questions</h2>
      <p style="color:var(--slc-gray-700); margin-bottom:20px;">Clear, honest answers to the most common questions about our operations and services.</p>
      {items_html}
    </div>
    '''

print("Created AI / GEO utility module.")
