with open('contact.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = '<a href="tel:+8618248547224" style="color:var(--slc-gold); font-weight:700; font-size:1.05rem;">+86 182 4854 7224</a>'
replacement = '<a href="https://wa.me/8618248547224" target="_blank" rel="noopener noreferrer" style="color:#25D366; font-weight:700; font-size:1.05rem;">+86 182 4854 7224 (WhatsApp / Direct Call)</a>'

chibueze_card = '''
              <div>
                <strong style="color:var(--slc-white);">Nigeria Operations (Chibueze):</strong><br>
                <a href="tel:+2348038037353" style="color:var(--slc-gold); font-weight:700; font-size:1.05rem;">+234 803 803 7353</a>
                <div style="font-size:0.8rem; color:rgba(255,255,255,0.7); margin-top:2px;">Lagos Trade Fair Complex Depot &amp; Local Deliveries</div>
              </div>'''

if target in text:
    text = text.replace(target, replacement, 1)
    # Now find Star's card and prepend Chibueze's card
    star_target = '<strong style="color:var(--slc-white);">Procurement Lead (Star):</strong>'
    text = text.replace(star_target, chibueze_card + '\n\n              <div>\n                <strong style="color:var(--slc-white);">Procurement Lead (Star):</strong>', 1)
    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("SUCCESS: Embedded WhatsApp and Chibueze in contact.html")
else:
    print("Target not found")
