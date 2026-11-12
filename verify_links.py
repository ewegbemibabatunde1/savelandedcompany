import glob
import re
import os

html_files = [f for f in glob.glob('*.html') if not f.endswith('.backup.html')]
print(f'Checking {len(html_files)} HTML files...')

all_internal_links = set()
broken_links = []

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    links = re.findall(r'href=[\'"]([^\'"]+)[\'"]', content)
    for link in links:
        if link.startswith(('http://', 'https://', 'tel:', 'mailto:', '#', 'javascript:')):
            continue
        clean_link = link.split('?')[0].split('#')[0]
        if not clean_link:
            continue
        all_internal_links.add(clean_link)
        if not os.path.exists(clean_link):
            broken_links.append((file, link))

print(f'Discovered {len(all_internal_links)} distinct internal links: {sorted(list(all_internal_links))}')
if broken_links:
    print('WARNING: Broken links found:')
    for f, l in broken_links:
        print(f'  In {f}: {l}')
else:
    print('SUCCESS: All internal links resolve to existing files on disk!')

