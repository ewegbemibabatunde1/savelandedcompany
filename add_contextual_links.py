# -*- coding: utf-8 -*-
"""
add_contextual_links.py
Enriches internal cross-links from key service pages to the master Shipping Guide (shipping.html)
"""

import re

def enrich_pages():
    pages_to_update = [
        ('air-freight.html', 
         'For comprehensive cargo comparisons, indicative rates, and our live dimensional calculator, consult our master <a href="shipping.html" style="color:var(--slc-wine); font-weight:700; text-decoration:underline;">China to Nigeria Shipping Guide & Rate Calculator</a>.'),
        ('sea-freight.html', 
         'Need to calculate cubic meters (CBM) or compare ocean groupage versus full container rates? Visit our master <a href="shipping.html" style="color:var(--slc-wine); font-weight:700; text-decoration:underline;">Shipping from China to Nigeria</a> guide.'),
        ('door-to-door.html', 
         'Explore detailed freight breakdowns, origin warehouse staging hubs, and delivery schedules in our master <a href="shipping.html" style="color:var(--slc-wine); font-weight:700; text-decoration:underline;">China to Nigeria Shipping Solutions</a> page.'),
        ('customs-clearance.html', 
         'Learn more about how our consolidated DDP freight lanes bypass destination clearing bottlenecks in our master <a href="shipping.html" style="color:var(--slc-wine); font-weight:700; text-decoration:underline;">China to Nigeria Shipping Guide</a>.'),
        ('services.html', 
         'Calculate freight volumes and view indicative air and sea freight tables in our complete <a href="shipping.html" style="color:var(--slc-wine); font-weight:700; text-decoration:underline;">Shipping from China to Nigeria Guide & Calculator</a>.')
    ]

    for filename, banner_html in pages_to_update:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        if 'master <a href="shipping.html"' not in content:
            # Inject just after the first AI summary box or first lead paragraph
            if '</section>' in content and 'slc-ai-summary' in content:
                pattern = r'(</section>\s*(?:<!--.*?-->\s*)*<nav class="slc-toc")'
                replacement = r'<div class="slc-callout" style="margin:20px 0; border-left:4px solid var(--slc-wine); background:#faf7f2;">' + banner_html + r'</div>\n\1'
                new_content = re.sub(pattern, replacement, content, count=1)
                if new_content != content:
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Added contextual link to {filename}")
                else:
                    print(f"Pattern not matched for {filename}")
            else:
                print(f"AI summary section not found in {filename}")
        else:
            print(f"Contextual link already present in {filename}")

if __name__ == '__main__':
    enrich_pages()
