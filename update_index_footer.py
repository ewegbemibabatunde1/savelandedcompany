with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = '''            <div>Wolex: <a href="tel:+8618248547224" style="color:var(--slc-gold);">+86 182 4854 7224</a></div>
            <div>Star: <a href="tel:+8615757991458" style="color:var(--slc-gold);">+86 157 5799 1458</a></div>
            <div>Email: <a href="mailto:admsavelandedimpexpcomltd@gmail.com" style="color:var(--slc-gold);">admsavelandedimpexpcomltd@gmail.com</a></div>'''

replacement = '''            <div>Nigeria Desk: <a href="tel:+2348038037353" style="color:var(--slc-gold);">Chibueze: +234 803 803 7353</a></div>
            <div>WhatsApp / Call: <a href="https://wa.me/8618248547224" target="_blank" rel="noopener noreferrer" style="color:#25D366; font-weight:700;">Wolex: +86 182 4854 7224</a></div>
            <div>Procurement (Yiwu): <a href="tel:+8615757991458" style="color:var(--slc-gold);">Star: +86 157 5799 1458</a></div>
            <div>Primary Email: <a href="mailto:admsavelandedimpexpcomltd@gmail.com" style="color:var(--slc-gold);">admsavelandedimpexpcomltd@gmail.com</a></div>
            <div>Corporate Email: <a href="mailto:info@savelandedcompany.com" style="color:var(--slc-gold);">info@savelandedcompany.com</a></div>'''

if target in text:
    text = text.replace(target, replacement, 1)

# Also add social links to index.html footer
from apply_business_updates import SOCIAL_MEDIA_FOOTER_HTML
if 'https://web.facebook.com' not in text:
    find_block = 'Connecting China to Nigeria. Simplifying Global Trade.\n          </div>'
    if find_block in text:
        text = text.replace(find_block, find_block + '\n' + SOCIAL_MEDIA_FOOTER_HTML, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("SUCCESS: Updated index.html footer contacts and social links.")
