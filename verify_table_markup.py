with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="air-sea-comparison-table"')
if idx != -1:
    print("Found table at", idx)
    print(text[idx:idx+1200])
else:
    print("Table not found")

