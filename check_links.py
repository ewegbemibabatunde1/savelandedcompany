with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
tags = re.findall(r'<link[^>]+>', text)
for t in tags:
    if 'stylesheet' in t or '.css' in t:
        print(t)

