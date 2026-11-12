# -*- coding: utf-8 -*-
"""
audit_all_pages.py
Runs a technical SEO and integrity audit on all 14 HTML pages, sitemap.xml, and robots.txt.
"""

import os
import glob
import re

EXPECTED_PAGES = [
    'index.html',
    'about.html',
    'services.html',
    'air-freight.html',
    'sea-freight.html',
    'product-sourcing.html',
    'procurement.html',
    'warehousing.html',
    'customs-clearance.html',
    'import-export.html',
    'door-to-door.html',
    'shipping.html',
    'quote.html',
    'contact.html'
]

def run_audit():
    print("====================================================")
    print("      SAVELANDED 14-PAGE TECHNICAL SEO AUDIT        ")
    print("====================================================")

    all_passed = True

    for p in EXPECTED_PAGES:
        if not os.path.exists(p):
            print(f"[FAIL] Missing page: {p}")
            all_passed = False
            continue

        with open(p, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check H1
        h1_matches = re.findall(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
        h1_count = len(h1_matches)

        # Check Title
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        title = title_match.group(1).strip() if title_match else "MISSING"

        # Check Description
        desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE | re.DOTALL)
        desc = desc_match.group(1).strip() if desc_match else "MISSING"

        # Check Canonical
        canon_match = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', content, re.IGNORECASE)
        canon = canon_match.group(1).strip() if canon_match else "MISSING"

        # Check GTM
        gtm_count = content.count('GTM-WSW25L7G')

        # Check old email
        old_email = content.count('svgadmsavelandedimpexpcomltd@gmail.com')

        # Check old domain in href/canonical (exclude mailto)
        old_domains = re.findall(r'href=["\']https://savelandedcompany\.com[^"\']*["\']', content)

        # Check closing tags
        has_body_close = '</body>' in content
        has_html_close = '</html>' in content

        # Check WhatsApp float
        has_wa = 'slc-float-whatsapp' in content

        errors = []
        if h1_count != 1:
            errors.append(f"H1 count is {h1_count} (expected 1)")
        if title == "MISSING" or len(title) < 10:
            errors.append("Title tag missing or too short")
        if desc == "MISSING" or len(desc) < 20:
            errors.append("Meta description missing or too short")
        if not canon.startswith("https://savelandedcompany.vercel.app"):
            errors.append(f"Invalid canonical URL: {canon}")
        if canon.endswith(".html"):
            errors.append(f"Canonical contains .html extension: {canon}")
        if gtm_count != 2:
            errors.append(f"GTM count is {gtm_count} (expected 2)")
        if old_email > 0:
            errors.append(f"Found {old_email} instances of old email")
        if len(old_domains) > 0:
            errors.append(f"Found old domain links: {old_domains}")
        if not has_body_close:
            errors.append("Missing </body> tag")
        if not has_html_close:
            errors.append("Missing </html> tag")
        if not has_wa:
            errors.append("Missing slc-float-whatsapp widget")

        if errors:
            print(f"[FAIL] {p}:")
            for e in errors:
                print(f"       - {e}")
            all_passed = False
        else:
            print(f"[PASS] {p.ljust(22)} | H1: 1 | GTM: 2 | Canon: Clean | WA: Yes | Title: {title[:40]}...")

    print("\n---------------- CHECKING SITEMAP & ROBOTS ----------------")
    # Audit sitemap.xml
    if os.path.exists('sitemap.xml'):
        with open('sitemap.xml', 'r', encoding='utf-8') as f:
            sm = f.read()
        sm_urls = re.findall(r'<loc>(.*?)</loc>', sm)
        print(f"sitemap.xml entries found: {len(sm_urls)}")
        sm_errors = []
        if len(sm_urls) != 14:
            sm_errors.append(f"Expected 14 URLs, found {len(sm_urls)}")
        for u in sm_urls:
            if not u.startswith("https://savelandedcompany.vercel.app/"):
                sm_errors.append(f"Non-Vercel URL: {u}")
            if u.endswith(".html"):
                sm_errors.append(f"URL contains .html: {u}")
        if sm_errors:
            print("[FAIL] sitemap.xml issues:")
            for e in sm_errors:
                print(f"       - {e}")
            all_passed = False
        else:
            print("[PASS] sitemap.xml: 14 clean HTTPS URLs matching Vercel domain")
    else:
        print("[FAIL] Missing sitemap.xml")
        all_passed = False

    # Audit robots.txt
    if os.path.exists('robots.txt'):
        with open('robots.txt', 'r', encoding='utf-8') as f:
            rob = f.read()
        if 'Sitemap: https://savelandedcompany.vercel.app/sitemap.xml' in rob:
            print("[PASS] robots.txt declares sitemap correctly")
        else:
            print("[FAIL] robots.txt missing correct sitemap declaration")
            all_passed = False
    else:
        print("[FAIL] Missing robots.txt")
        all_passed = False

    print("====================================================")
    if all_passed:
        print(">>> ALL 14 PAGES & SEO ASSETS PASSED THE AUDIT! <<<")
    else:
        print(">>> SOME CHECKS FAILED. SEE DETAILS ABOVE. <<<")
    print("====================================================")

if __name__ == '__main__':
    run_audit()
