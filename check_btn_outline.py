import glob

html_files = glob.glob('*.html')
for f in html_files:
    if 'backup' in f: continue
    with open(f, 'r', encoding='utf-8') as fh:
        text = fh.read()
    cnt = text.count('slc-btn-outline"') + text.count('slc-btn-outline ')
    if cnt > 0:
        print(f, cnt, "occurrences of slc-btn-outline")

