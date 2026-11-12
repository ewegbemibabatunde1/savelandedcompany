# -*- coding: utf-8 -*-
"""
Script to inject data-label attributes into all <table> elements
so that mobile card view displays clear labels (e.g., 'Typical Transit Window', 'Nigeria Arrival Terminal').
"""

import glob
import re

def enrich_tables_in_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    if '<table class="slc-comparison-table"' not in html and '<table class="slc-spec-table"' not in html:
        return 0

    modified = False

    # Regex to find each table
    table_pattern = re.compile(r'(<table[^>]*class="[^"]*(?:slc-comparison-table|slc-spec-table)[^"]*"[^>]*>)(.*?)(</table>)', re.DOTALL)

    def process_table(match):
        nonlocal modified
        start_tag = match.group(1)
        inner = match.group(2)
        end_tag = match.group(3)

        # Find thead th labels
        thead_match = re.search(r'<thead>(.*?)</thead>', inner, re.DOTALL)
        if not thead_match:
            return match.group(0)

        th_matches = re.findall(r'<th[^>]*>(.*?)</th>', thead_match.group(1), re.DOTALL)
        headers = [re.sub(r'<[^>]+>', '', h).strip() for h in th_matches]
        if not headers:
            return match.group(0)

        # Process tbody tr
        tbody_match = re.search(r'<tbody>(.*?)</tbody>', inner, re.DOTALL)
        if not tbody_match:
            return match.group(0)

        tbody_content = tbody_match.group(1)

        def process_row(row_match):
            row_html = row_match.group(1)
            td_matches = list(re.finditer(r'<td([^>]*)>(.*?)</td>', row_html, re.DOTALL))
            new_row_html = row_html
            for i, td in enumerate(td_matches):
                if i < len(headers):
                    label = headers[i]
                    attrs = td.group(1)
                    if 'data-label=' not in attrs:
                        new_td = f'<td{attrs} data-label="{label}">{td.group(2)}</td>'
                        new_row_html = new_row_html.replace(td.group(0), new_td, 1)
            return f'<tr>{new_row_html}</tr>'

        new_tbody_content = re.sub(r'<tr>(.*?)</tr>', process_row, tbody_content, flags=re.DOTALL)
        modified = True
        return f'{start_tag}{inner.replace(tbody_content, new_tbody_content)}{end_tag}'

    new_html = table_pattern.sub(process_table, html)
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Enriched tables with data-labels in {file_path}")
        return 1
    return 0

if __name__ == '__main__':
    count = 0
    for f in glob.glob('*.html'):
        if 'backup' in f: continue
        count += enrich_tables_in_html(f)
    print(f"\nCompleted: Enriched {count} HTML files with mobile data-labels.")

