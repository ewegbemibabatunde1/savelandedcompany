# -*- coding: utf-8 -*-
with open('shipping.html', 'r', encoding='utf-8') as f:
    text = f.read()

gtm_count = text.count('GTM-WSW25L7G')
old_email_count = text.count('svgadmsavelandedimpexpcomltd@gmail.com')
old_domain_count = text.count('https://savelandedcompany.com')
h1_count = text.count('<h1')
has_body_close = '</body>' in text
has_html_close = '</html>' in text
has_canonical = 'rel="canonical" href="https://savelandedcompany.vercel.app/shipping"' in text
has_whatsapp = 'slc-float-whatsapp' in text
has_calc = 'runCalculation' in text

print('--- VERIFICATION AUDIT FOR shipping.html ---')
print('GTM count (target 2):', gtm_count)
print('Old email count (target 0):', old_email_count)
print('Old domain URL count (target 0):', old_domain_count)
print('H1 count (target 1):', h1_count)
print('Has </body> (target True):', has_body_close)
print('Has </html> (target True):', has_html_close)
print('Has correct canonical (target True):', has_canonical)
print('Has floating WhatsApp (target True):', has_whatsapp)
print('Has dynamic calculation engine (target True):', has_calc)
