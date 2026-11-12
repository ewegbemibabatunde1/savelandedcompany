from apply_business_updates import FLOAT_WHATSAPP_HTML

html_files = [
    'index.html', 'about.html', 'services.html', 'contact.html', 'quote.html',
    'import-export.html', 'shipping.html', 'air-freight.html', 'sea-freight.html',
    'customs-clearance.html', 'door-to-door.html', 'warehousing.html',
    'procurement.html', 'product-sourcing.html'
]

for f in html_files:
    with open(f, 'r', encoding='utf-8') as fh:
        text = fh.read()
    if 'slc-float-whatsapp' not in text:
        text = text.replace('</body>', FLOAT_WHATSAPP_HTML + '\n</body>', 1)
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(text)
        print(f"Added floating WhatsApp button to {f}")
    else:
        print(f"Floating WhatsApp already in {f}")

