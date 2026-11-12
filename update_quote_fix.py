from expansion_content_module import QUOTE_PAGE_ADDITION

with open('quote.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = '<form id="quote-form-el"'
if target in content:
    content = content.replace(target, QUOTE_PAGE_ADDITION + '\n          ' + target, 1)
    with open('quote.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS: Expanded quote.html with Preparation Guidance.")
else:
    print("Target not found in quote.html")

