from apply_business_updates import FLOAT_WHATSAPP_HTML

html_files = [
    'about.html', 'services.html', 'contact.html', 'quote.html',
    'import-export.html', 'shipping.html', 'air-freight.html', 'sea-freight.html',
    'customs-clearance.html', 'door-to-door.html', 'warehousing.html',
    'procurement.html', 'product-sourcing.html'
]

closing_tags = f"""
{FLOAT_WHATSAPP_HTML}
</body>
</html>
"""

for f in html_files:
    with open(f, 'r', encoding='utf-8') as fh:
        text = fh.read()
    if 'slc-float-whatsapp' not in text:
        text = text.rstrip() + '\n' + closing_tags
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(text)
        print(f"Appended closing tags and Floating WhatsApp to {f}")
    else:
        print(f"{f} already has Floating WhatsApp")

