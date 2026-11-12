import os

ADDITIONAL_SEO_CSS = """
/* ==========================================================================
   ADVANCED SEO, AEO, GEO & COMPARISON STYLING
   ========================================================================== */

/* Responsive Comparison Table */
.slc-comparison-table-wrapper {
  width: 100%;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  margin: 28px 0;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.06);
  border: 1px solid rgba(0,0,0,0.08);
  background: #ffffff;
}

.slc-comparison-table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
  font-size: 0.95rem;
  line-height: 1.5;
}

.slc-comparison-table thead th {
  background: var(--slc-burgundy, #6a1a24);
  color: #ffffff;
  padding: 16px 20px;
  font-family: var(--slc-font-head, 'Sora', sans-serif);
  font-weight: 600;
  letter-spacing: 0.02em;
  white-space: nowrap;
}

.slc-comparison-table tbody td {
  padding: 16px 20px;
  border-bottom: 1px solid rgba(0,0,0,0.06);
  color: var(--slc-gray-800, #2d3748);
  vertical-align: top;
}

.slc-comparison-table tbody tr:nth-child(even) {
  background-color: #faf8f5;
}

.slc-comparison-table tbody tr:hover {
  background-color: #f5f0eb;
}

.slc-comparison-table td strong {
  color: var(--slc-burgundy, #6a1a24);
}

/* Feature & Step Grids */
.slc-step-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 20px;
  margin: 28px 0;
}

.slc-step-card {
  background: #ffffff;
  border: 1px solid rgba(0,0,0,0.08);
  border-radius: 12px;
  padding: 24px;
  position: relative;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.slc-step-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.08);
}

.slc-step-num {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  background: var(--slc-gold, #c5a059);
  color: #ffffff;
  font-weight: 700;
  border-radius: 50%;
  font-size: 1rem;
  margin-bottom: 14px;
}

.slc-step-title {
  font-family: var(--slc-font-head, 'Sora', sans-serif);
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--slc-burgundy, #6a1a24);
  margin-bottom: 10px;
}

.slc-step-text {
  font-size: 0.92rem;
  color: var(--slc-gray-700, #4a5568);
  line-height: 1.6;
}

/* Regulatory & Authority Badges */
.slc-tag {
  display: inline-block;
  padding: 4px 10px;
  font-size: 0.78rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  border-radius: 20px;
  background: #f0e6d6;
  color: #8c6225;
  margin-right: 6px;
  margin-bottom: 6px;
}

.slc-tag--official {
  background: #e6f4ea;
  color: #137333;
}

.slc-tag--warning {
  background: #fce8e6;
  color: #c5221f;
}

/* Definition Cards for AEO & Terminology */
.slc-definition-box {
  background: #fdfbf7;
  border-left: 4px solid var(--slc-gold, #c5a059);
  padding: 20px 24px;
  margin: 24px 0;
  border-radius: 0 8px 8px 0;
}

.slc-definition-term {
  font-weight: 700;
  font-size: 1.05rem;
  color: var(--slc-burgundy, #6a1a24);
  margin-bottom: 6px;
}

.slc-definition-desc {
  font-size: 0.95rem;
  color: var(--slc-gray-700, #4a5568);
  line-height: 1.6;
  margin: 0;
}

/* Author / Reviewer Attribution */
.slc-reviewer-badge {
  display: flex;
  align-items: center;
  gap: 14px;
  background: #f7fafc;
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  padding: 14px 18px;
  margin: 28px 0 20px;
  font-size: 0.88rem;
  color: #4a5568;
}

.slc-reviewer-avatar {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: var(--slc-burgundy, #6a1a24);
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 1.1rem;
  flex-shrink: 0;
}

@media (max-width: 768px) {
  .slc-comparison-table thead th,
  .slc-comparison-table tbody td {
    padding: 12px 14px;
    font-size: 0.88rem;
  }
}
"""

with open('assets/css/savelanded.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

if 'ADVANCED SEO, AEO, GEO & COMPARISON STYLING' not in css_content:
    with open('assets/css/savelanded.css', 'a', encoding='utf-8') as f:
        f.write('\n' + ADDITIONAL_SEO_CSS)
    print("Appended ADDITIONAL_SEO_CSS to assets/css/savelanded.css")
else:
    print("ADDITIONAL_SEO_CSS already present in assets/css/savelanded.css")

