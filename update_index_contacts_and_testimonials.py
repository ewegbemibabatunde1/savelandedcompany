#!/usr/bin/env python3
"""
update_index_contacts_and_testimonials.py
=========================================
1. Remove contact lines from the 3 location cards in index.html:
   - Contact: Star • +86 157 5799 1458
   - Contact: Wolex CEO • +86 182 4854 7224
   - Email: admsavelandedimpexpcomltd@gmail.com info@savelandedcompany.com
2. Add 3 more SEO-rich testimonials in index.html to make 6 total, 3 in a row on desktop.
"""

import os
import re

INDEX_PATH = r"c:\Users\Dell\OneDrive\Desktop\SLC Website\index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# ----------------------------------------------------------------------
# 1. Remove contact lines from the 3 location cards
# ----------------------------------------------------------------------
# Star
content = re.sub(
    r'<div style="font-size:0\.875rem;\s*font-weight:600;">\s*Contact:\s*Star\s*&bull;\s*<a href="tel:\+8615757991458">\+86 157 5799 1458</a>\s*</div>',
    '',
    content
)

# Wolex CEO
content = re.sub(
    r'<div style="font-size:0\.875rem;\s*font-weight:600;">\s*Contact:\s*Wolex CEO\s*&bull;\s*<a href="tel:\+8618248547224">\+86 182 4854 7224</a>\s*</div>',
    '',
    content
)

# Email line in Lagos card
content = re.sub(
    r'<div style="font-size:0\.875rem;\s*font-weight:600;">\s*Email:\s*<a href="mailto:admsavelandedimpexpcomltd@gmail\.com">admsavelandedimpexpcomltd@gmail\.com</a>\s*<a href="mailto:info@savelandedcompany\.com">info@savelandedcompany\.com</a>\s*</div>',
    '',
    content
)

# Also catch any variations with linebreaks or different whitespace
content = re.sub(
    r'<div style="font-size:0\.875rem;\s*font-weight:600;">\s*Email:[\s\S]*?info@savelandedcompany\.com</a>\s*</div>',
    '',
    content
)
content = re.sub(
    r'<div style="font-size:0\.875rem;\s*font-weight:600;">\s*Contact:[\s\S]*?\+86 157 5799 1458</a>\s*</div>',
    '',
    content
)
content = re.sub(
    r'<div style="font-size:0\.875rem;\s*font-weight:600;">\s*Contact:[\s\S]*?\+86 182 4854 7224</a>\s*</div>',
    '',
    content
)

# ----------------------------------------------------------------------
# 2. Update testimonials to 6 items (3 in a row)
# ----------------------------------------------------------------------
OLD_TESTIMONIALS_PATTERN = re.compile(
    r'<div class="slc-testimonials-grid">[\s\S]*?</div>\s*</div>\s*</section>',
    re.MULTILINE
)

SIX_TESTIMONIALS_HTML = """<div class="slc-testimonials-grid">
          
          <!-- Testimonial 1 -->
          <article class="slc-test-card">
            <p class="slc-test-quote">
              "Their service is reliable and transparent. My electronics and phone accessories from Shenzhen arrived at Lagos Trade Fair on time and exactly as promised. The volumetric weight calculation was fair with zero hidden clearing charges."
            </p>
            <div class="slc-test-author">
              <div class="slc-test-avatar">CO</div>
              <div>
                <div class="slc-test-name">Chinedu Okafor</div>
                <div class="slc-test-loc">Trade Fair Complex, Lagos</div>
              </div>
            </div>
          </article>

          <!-- Testimonial 2 -->
          <article class="slc-test-card">
            <p class="slc-test-quote">
              "Professional, responsive, and trustworthy. They handled our boutique fashion order from Guangzhou smoothly &mdash; from factory verification and export packaging to swift air cargo arrival in Abuja within 6 days."
            </p>
            <div class="slc-test-author">
              <div class="slc-test-avatar">AB</div>
              <div>
                <div class="slc-test-name">Aisha Bello</div>
                <div class="slc-test-loc">Wuse II, Abuja FCT</div>
              </div>
            </div>
          </article>

          <!-- Testimonial 3 -->
          <article class="slc-test-card">
            <p class="slc-test-quote">
              "I have used several freight forwarders, but Savelanded stands out for honesty and speed. Sourcing machinery spare parts from Yiwu and receiving door delivery in Ibadan without customs headaches made them my permanent partner."
            </p>
            <div class="slc-test-author">
              <div class="slc-test-avatar">SA</div>
              <div>
                <div class="slc-test-name">Samuel Adeyemi</div>
                <div class="slc-test-loc">Dugbe Commercial Hub, Ibadan</div>
              </div>
            </div>
          </article>

          <!-- Testimonial 4 -->
          <article class="slc-test-card">
            <p class="slc-test-quote">
              "Shipping 40ft container loads and LCL groupage of building hardware from Foshan directly to Onitsha was handled flawlessly. Their customs clearance team in Lagos cleared our cargo with zero demurrage fees."
            </p>
            <div class="slc-test-author">
              <div class="slc-test-avatar">EN</div>
              <div>
                <div class="slc-test-name">Emeka Nwosu</div>
                <div class="slc-test-loc">Main Market, Onitsha</div>
              </div>
            </div>
          </article>

          <!-- Testimonial 5 -->
          <article class="slc-test-card">
            <p class="slc-test-quote">
              "We import wholesale textile fabrics and beauty goods from Yiwu commodity markets to Kano via air cargo. Savelanded's warehouse consolidation, package security, and direct RMB payment service saved our business immense stress."
            </p>
            <div class="slc-test-author">
              <div class="slc-test-avatar">MI</div>
              <div>
                <div class="slc-test-name">Maryam Ibrahim</div>
                <div class="slc-test-loc">Kanti Kwari Market, Kano</div>
              </div>
            </div>
          </article>

          <!-- Testimonial 6 -->
          <article class="slc-test-card">
            <p class="slc-test-quote">
              "Finding a dependable shipping agent in Guangzhou that inspects footwear soles and raw materials before container loading was a game changer for our factory in Aba. True door-to-door delivery and first-class communication."
            </p>
            <div class="slc-test-author">
              <div class="slc-test-avatar">KE</div>
              <div>
                <div class="slc-test-name">Chief Kenneth Eze</div>
                <div class="slc-test-loc">Ariaria International Market, Aba</div>
              </div>
            </div>
          </article>

        </div>
      </div>
    </section>"""

content = OLD_TESTIMONIALS_PATTERN.sub(SIX_TESTIMONIALS_HTML, content)

# Ensure equal height in testimonial cards
content = content.replace(
    ".slc-test-card {",
    ".slc-test-card {\n      display: flex;\n      flex-direction: column;\n      justify-content: space-between;\n      height: 100%;"
)

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("index.html updated successfully with removed contact lines and 6 testimonials (3 in a row)!")

