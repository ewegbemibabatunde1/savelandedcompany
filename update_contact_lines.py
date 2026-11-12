with open('contact.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = '''              <div>
                <strong style="color:var(--slc-white);">Procurement Lead (Star):</strong><br>
                <a href="tel:+8615757991458" style="color:var(--slc-gold); font-weight:700; font-size:1.05rem;">+86 157 5799 1458</a>
                <div style="font-size:0.8rem; color:rgba(255,255,255,0.7); margin-top:2px;">Yiwu &amp; Guangzhou Operations / 1688 Purchasing</div>
              </div>'''

replacement = '''              <div>
                <strong style="color:var(--slc-white);">CEO Wolex &amp; WhatsApp Hotline:</strong><br>
                <a href="https://wa.me/8618248547224" target="_blank" rel="noopener noreferrer" style="color:#25D366; font-weight:700; font-size:1.05rem;">+86 182 4854 7224 (WhatsApp / Call)</a>
                <div style="font-size:0.8rem; color:rgba(255,255,255,0.7); margin-top:2px;">Strategic Accounts, Air &amp; Ocean Logistics</div>
              </div>

              <div>
                <strong style="color:var(--slc-white);">Nigeria Operations (Chibueze):</strong><br>
                <a href="tel:+2348038037353" style="color:var(--slc-gold); font-weight:700; font-size:1.05rem;">+234 803 803 7353</a>
                <div style="font-size:0.8rem; color:rgba(255,255,255,0.7); margin-top:2px;">Lagos Trade Fair Complex Depot &amp; Nationwide Deliveries</div>
              </div>

              <div>
                <strong style="color:var(--slc-white);">Procurement Lead (Star):</strong><br>
                <a href="tel:+8615757991458" style="color:var(--slc-gold); font-weight:700; font-size:1.05rem;">+86 157 5799 1458</a>
                <div style="font-size:0.8rem; color:rgba(255,255,255,0.7); margin-top:2px;">Yiwu &amp; Guangzhou Operations / 1688 Purchasing</div>
              </div>'''

if target in text:
    text = text.replace(target, replacement, 1)
    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("SUCCESS: Added Chibueze and WhatsApp directly into contact.html executive lines card.")
else:
    print("Target block not found in contact.html")
