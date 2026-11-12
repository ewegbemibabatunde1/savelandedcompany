with open('build_multipage.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = 'canonical_url = f"https://savelandedcompany.vercel.app/{canonical_slug}" if canonical_slug else "https://savelandedcompany.vercel.app/"'
replacement = '''clean_slug = canonical_slug[:-5] if canonical_slug.endswith('.html') else canonical_slug
    canonical_url = f"https://savelandedcompany.vercel.app/{clean_slug}" if clean_slug else "https://savelandedcompany.vercel.app/"'''

if target in text:
    text = text.replace(target, replacement)
    with open('build_multipage.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("SUCCESS: Updated canonical URL clean slug in build_multipage.py")
else:
    print("Target not found in build_multipage.py")
