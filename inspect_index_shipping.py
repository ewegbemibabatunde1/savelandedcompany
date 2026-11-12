with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = '<section class="slc-shipping" id="shipping">'
idx = text.find(target)
if idx != -1:
    print("Found slc-shipping at", idx)
    print(text[idx:idx+1000])
else:
    print("Target not found")

