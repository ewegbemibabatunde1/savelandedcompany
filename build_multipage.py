import os
import re
import json

# Comprehensive Mobile-Responsive & Subpage CSS
SUBPAGE_AND_MOBILE_CSS = """
/* ==========================================================================
   MOBILE RESPONSIVENESS OVERHAUL & SUBPAGE STYLING (.slc-)
   ========================================================================== */

/* Universal Responsive Base */
html, body {
  overflow-x: hidden;
  max-width: 100vw;
  width: 100%;
}

*, *::before, *::after {
  box-sizing: border-box;
}

img {
  max-width: 100%;
  height: auto;
}

/* Header Sticky at Top 0 (No Announcement Bar) */
.slc-header {
  position: sticky;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  background: rgba(255, 255, 255, 0.98);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-bottom: 1px solid rgba(0, 0, 0, 0.08);
  transition: var(--slc-transition);
}

.slc-header__inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 80px;
}

/* Mobile Drawer & Overlay */
.slc-mobile-drawer {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  width: 85%;
  max-width: 340px;
  background: var(--slc-white);
  z-index: 2000;
  box-shadow: -10px 0 30px rgba(0,0,0,0.25);
  padding: 24px;
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
  transform: translateX(100%);
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.slc-mobile-drawer.is-open {
  transform: translateX(0);
}

.slc-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.65);
  z-index: 1999;
  display: none;
}

.slc-overlay.is-open,
.slc-overlay.is-visible {
  display: block;
}

/* Subpage Hero */
.slc-page-hero {
  position: relative;
  background-color: var(--slc-dark-bg);
  background-image: 
    radial-gradient(circle at 80% 20%, rgba(248, 210, 146, 0.08) 0%, transparent 45%),
    radial-gradient(circle at 20% 80%, rgba(184, 140, 117, 0.06) 0%, transparent 45%);
  padding: 80px 0 55px;
  border-bottom: 1px solid var(--slc-border-dark);
  color: var(--slc-white);
}

.slc-breadcrumbs {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
  font-size: 0.85rem;
  color: var(--slc-gray-500);
  margin-bottom: 18px;
}

.slc-breadcrumbs a {
  color: var(--slc-gold);
  transition: var(--slc-transition);
}

.slc-breadcrumbs a:hover {
  text-decoration: underline;
  color: var(--slc-white);
}

.slc-breadcrumbs__separator {
  color: var(--slc-gray-500);
  font-size: 0.75rem;
}

.slc-breadcrumbs__current {
  color: rgba(255, 255, 255, 0.85);
  font-weight: 500;
}

.slc-page-hero__pill {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background-color: rgba(248, 210, 146, 0.1);
  border: 1px solid rgba(248, 210, 146, 0.3);
  color: var(--slc-gold);
  padding: 6px 14px;
  border-radius: var(--slc-radius-pill);
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-bottom: 16px;
}

.slc-page-hero__pill::before {
  content: "";
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background-color: var(--slc-gold);
}

.slc-page-hero__title {
  font-family: var(--slc-font-head);
  font-size: clamp(1.85rem, 5.5vw, 3.2rem);
  font-weight: 800;
  line-height: 1.2;
  letter-spacing: -0.02em;
  margin-bottom: 18px;
  color: var(--slc-white);
  word-break: break-word;
}

.slc-page-hero__title em {
  font-family: var(--slc-font-accent);
  font-style: italic;
  font-weight: 500;
  color: var(--slc-gold);
}

.slc-page-hero__lead {
  font-size: clamp(1rem, 2vw, 1.15rem);
  line-height: 1.7;
  color: rgba(255, 255, 255, 0.84);
  max-width: 820px;
  margin-bottom: 28px;
}

.slc-page-hero__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  align-items: center;
}

/* Subpage Content & Grids */
.slc-content-section {
  padding: 70px 0;
}

.slc-content-section--ivory {
  background-color: var(--slc-ivory);
}

.slc-content-section--white {
  background-color: var(--slc-white);
}

.slc-content-section--dark {
  background-color: var(--slc-dark-bg);
  color: var(--slc-white);
}

.slc-layout-with-sidebar {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 48px;
  align-items: start;
}

.slc-sidebar-card {
  background-color: var(--slc-white);
  border: 1px solid rgba(0, 0, 0, 0.08);
  border-radius: var(--slc-radius-lg);
  padding: 26px;
  margin-bottom: 24px;
  box-shadow: var(--slc-shadow-sm);
}

.slc-sidebar-card--dark {
  background-color: var(--slc-dark-surface);
  border: 1px solid var(--slc-border-dark);
  color: var(--slc-white);
}

.slc-sidebar-heading {
  font-family: var(--slc-font-head);
  font-size: 1.15rem;
  font-weight: 700;
  margin-bottom: 18px;
  padding-bottom: 10px;
  border-bottom: 2px solid var(--slc-gold);
}

.slc-sidebar-nav {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.slc-sidebar-nav__link {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 14px;
  border-radius: var(--slc-radius-sm);
  background-color: var(--slc-gray-100);
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--slc-charcoal);
  transition: var(--slc-transition);
}

.slc-sidebar-nav__link:hover,
.slc-sidebar-nav__link.is-active {
  background-color: var(--slc-black);
  color: var(--slc-gold);
  transform: translateX(4px);
}

.slc-feature-grid-3 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
  margin: 32px 0;
}

.slc-feature-grid-2 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
  margin: 32px 0;
}

.slc-feature-box {
  background-color: var(--slc-white);
  border: 1px solid var(--slc-gray-200);
  border-radius: var(--slc-radius-md);
  padding: 26px;
  transition: var(--slc-transition);
}

.slc-feature-box:hover {
  border-color: var(--slc-gold);
  box-shadow: var(--slc-shadow-md);
  transform: translateY(-4px);
}

.slc-feature-box__icon {
  width: 48px;
  height: 48px;
  border-radius: var(--slc-radius-md);
  background-color: var(--slc-ivory);
  border: 1px solid rgba(248, 210, 146, 0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 16px;
  color: var(--slc-copper);
}

.slc-feature-box__icon svg {
  width: 24px;
  height: 24px;
  fill: currentColor;
}

.slc-feature-box__title {
  font-family: var(--slc-font-head);
  font-size: 1.2rem;
  font-weight: 700;
  margin-bottom: 10px;
  color: var(--slc-black);
}

.slc-feature-box__desc {
  font-size: 0.925rem;
  color: var(--slc-gray-700);
  line-height: 1.6;
}

.slc-checklist {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 14px;
  margin: 22px 0;
}

.slc-checklist__item {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  font-size: 0.95rem;
  line-height: 1.6;
}

.slc-checklist__icon {
  flex-shrink: 0;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background-color: var(--slc-gold);
  color: var(--slc-black);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: 800;
  margin-top: 2px;
}

.slc-prose {
  font-size: 1rem;
  line-height: 1.75;
  color: var(--slc-charcoal);
}

.slc-prose h2 {
  font-family: var(--slc-font-head);
  font-size: clamp(1.5rem, 3.2vw, 1.85rem);
  font-weight: 700;
  color: var(--slc-black);
  margin: 36px 0 14px;
}

.slc-prose h3 {
  font-family: var(--slc-font-head);
  font-size: clamp(1.2rem, 2.5vw, 1.4rem);
  font-weight: 700;
  color: var(--slc-black);
  margin: 28px 0 12px;
}

.slc-prose p {
  margin-bottom: 18px;
}

.slc-prose ul {
  margin-bottom: 22px;
  padding-left: 20px;
}

.slc-prose li {
  margin-bottom: 8px;
}

/* Forms & Tables */
.slc-form-card {
  background-color: var(--slc-white);
  border: 1px solid var(--slc-gray-200);
  border-radius: var(--slc-radius-xl);
  padding: 36px;
  box-shadow: var(--slc-shadow-md);
}

.slc-form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 18px;
}

.slc-form-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin-bottom: 16px;
}

.slc-form-group--full {
  grid-column: 1 / -1;
}

.slc-label {
  font-family: var(--slc-font-head);
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--slc-black);
}

.slc-input,
.slc-select,
.slc-textarea {
  width: 100%;
  padding: 12px 14px;
  border: 1px solid var(--slc-gray-300);
  border-radius: var(--slc-radius-sm);
  font-family: var(--slc-font-body);
  font-size: 0.9375rem;
  color: var(--slc-charcoal);
  background-color: var(--slc-white);
  transition: var(--slc-transition);
}

.slc-input:focus,
.slc-select:focus,
.slc-textarea:focus {
  outline: none;
  border-color: var(--slc-gold);
  box-shadow: 0 0 0 3px rgba(248, 210, 146, 0.35);
}

.slc-textarea {
  min-height: 110px;
  resize: vertical;
}

.slc-table-wrap {
  width: 100%;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  border-radius: var(--slc-radius-md);
  border: 1px solid var(--slc-gray-200);
  margin: 24px 0;
  box-shadow: var(--slc-shadow-sm);
}

.slc-spec-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
  text-align: left;
}

.slc-spec-table th {
  background-color: var(--slc-black);
  color: var(--slc-gold);
  font-family: var(--slc-font-head);
  font-weight: 700;
  padding: 14px 16px;
  letter-spacing: 0.05em;
  font-size: 0.8125rem;
  text-transform: uppercase;
  white-space: nowrap;
}

.slc-spec-table td {
  padding: 14px 16px;
  border-bottom: 1px solid var(--slc-gray-200);
  color: var(--slc-charcoal);
}

.slc-spec-table tr:last-child td {
  border-bottom: none;
}

.slc-spec-table tr:nth-child(even) td {
  background-color: var(--slc-ivory-alt);
}

.slc-calc-card {
  background-color: var(--slc-ivory);
  border: 1px solid rgba(248, 210, 146, 0.6);
  border-radius: var(--slc-radius-lg);
  padding: 28px;
  margin: 28px 0;
}

.slc-calc-result {
  background-color: var(--slc-black);
  color: var(--slc-white);
  border-radius: var(--slc-radius-md);
  padding: 20px;
  text-align: center;
  margin-top: 18px;
}

.slc-calc-val {
  font-family: var(--slc-font-head);
  font-size: 2rem;
  font-weight: 800;
  color: var(--slc-gold);
  line-height: 1.2;
}

.slc-callout {
  border-left: 4px solid var(--slc-gold);
  background-color: var(--slc-ivory-alt);
  padding: 18px 20px;
  border-radius: 0 var(--slc-radius-md) var(--slc-radius-md) 0;
  margin: 24px 0;
  font-size: 0.925rem;
  line-height: 1.6;
}

/* AI Engine & GEO Quick Summary Card */
.slc-ai-summary {
  background: linear-gradient(135deg, rgba(248, 210, 146, 0.12) 0%, rgba(255, 243, 232, 0.6) 100%);
  border: 1px solid rgba(248, 210, 146, 0.85);
  border-left: 5px solid var(--slc-gold);
  border-radius: var(--slc-radius-md);
  padding: 22px 24px;
  margin: 24px 0 28px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.03);
}
.slc-ai-summary__badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-family: var(--slc-font-head);
  font-size: 0.72rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--slc-copper);
  margin-bottom: 10px;
}
.slc-ai-summary__badge svg {
  width: 14px;
  height: 14px;
  fill: currentColor;
}
.slc-ai-summary__title {
  font-family: var(--slc-font-head);
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--slc-black);
  margin-bottom: 10px;
}
.slc-ai-summary__content {
  font-size: 0.95rem;
  line-height: 1.68;
  color: var(--slc-charcoal);
}
.slc-ai-summary__content p:last-child {
  margin-bottom: 0;
}
.slc-ai-facts {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 12px;
  margin-top: 14px;
  padding-top: 14px;
  border-top: 1px dashed rgba(184, 140, 117, 0.35);
}
.slc-ai-fact {
  font-size: 0.85rem;
  line-height: 1.5;
  color: var(--slc-charcoal);
}
.slc-ai-fact strong {
  color: var(--slc-black);
  display: block;
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--slc-copper);
}

/* On-Page Table of Contents (TOC) */
.slc-toc {
  background-color: var(--slc-ivory);
  border: 1px solid rgba(248, 210, 146, 0.7);
  border-radius: var(--slc-radius-md);
  padding: 20px 24px;
  margin: 24px 0 32px;
}
.slc-toc__title {
  font-family: var(--slc-font-head);
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--slc-black);
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.slc-toc__list {
  list-style: none;
  padding-left: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.slc-toc__link {
  font-size: 0.925rem;
  color: var(--slc-charcoal);
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: var(--slc-transition);
}
.slc-toc__link:hover {
  color: var(--slc-copper);
  padding-left: 4px;
}

/* Subpage FAQ Accordions */
.slc-faq-subpage {
  margin: 36px 0;
}
.slc-faq-item {
  border: 1px solid var(--slc-gray-200);
  border-radius: var(--slc-radius-md);
  margin-bottom: 12px;
  background-color: var(--slc-white);
  overflow: hidden;
  transition: var(--slc-transition);
}
.slc-faq-item:hover {
  border-color: rgba(248, 210, 146, 0.7);
}
.slc-faq-item details {
  width: 100%;
}
.slc-faq-item summary {
  font-family: var(--slc-font-head);
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--slc-black);
  padding: 18px 22px;
  cursor: pointer;
  list-style: none;
  display: flex;
  justify-content: space-between;
  align-items: center;
  user-select: none;
}
.slc-faq-item summary::-webkit-details-marker {
  display: none;
}
.slc-faq-item summary::after {
  content: "+";
  font-size: 1.4rem;
  font-weight: 400;
  color: var(--slc-copper);
  transition: transform 0.25s ease;
}
.slc-faq-item details[open] summary::after {
  transform: rotate(45deg);
}
.slc-faq-item details[open] summary {
  background-color: var(--slc-ivory-alt);
  border-bottom: 1px solid var(--slc-gray-200);
}
.slc-faq-item__answer {
  padding: 18px 22px;
  font-size: 0.95rem;
  line-height: 1.7;
  color: var(--slc-charcoal);
  background-color: var(--slc-white);
}

/* Authoritative External Citation Link */
.slc-ext-link {
  color: var(--slc-copper);
  font-weight: 600;
  text-decoration: underline;
  text-underline-offset: 3px;
  transition: var(--slc-transition);
}
.slc-ext-link:hover {
  color: var(--slc-black);
}

/* ==========================================================================
   BREAKPOINTS: TABLET & MOBILE (< 1024px, < 768px, < 480px)
   ========================================================================== */

@media (max-width: 1024px) {
  .slc-nav-wrap, .slc-header__cta {
    display: none !important;
  }
  .slc-menu-toggle {
    display: block !important;
  }
  .slc-services-grid {
    grid-template-columns: repeat(2, 1fr) !important;
  }
  .slc-trust-strip__grid {
    grid-template-columns: repeat(3, 1fr) !important;
  }
  .slc-how-layout {
    grid-template-columns: 1fr !important;
    gap: 32px !important;
  }
  .slc-how-image-box {
    height: 320px !important;
  }
  .slc-about__grid {
    grid-template-columns: 1fr !important;
    gap: 36px !important;
  }
  .slc-layout-with-sidebar {
    grid-template-columns: 1fr !important;
    gap: 36px !important;
  }
  .slc-footer__grid {
    grid-template-columns: 1fr 1fr !important;
    gap: 36px !important;
  }
}

@media (max-width: 768px) {
  .slc-container {
    padding-left: 16px !important;
    padding-right: 16px !important;
  }
  .slc-header__inner {
    height: 68px !important;
  }
  .slc-brand__logo {
    width: 42px !important;
    height: 42px !important;
  }
  .slc-brand__name {
    font-size: 1.05rem !important;
  }
  .slc-brand__sub {
    font-size: 0.6rem !important;
  }
  
  /* Hero on Mobile */
  .slc-hero {
    min-height: auto !important;
    padding: 60px 0 50px !important;
  }
  .slc-hero__title {
    font-size: clamp(1.75rem, 6.5vw, 2.6rem) !important;
    line-height: 1.2 !important;
    margin-bottom: 16px !important;
  }
  .slc-hero__desc {
    font-size: 0.95rem !important;
    line-height: 1.6 !important;
    margin-bottom: 28px !important;
  }
  .slc-hero__actions {
    flex-direction: column !important;
    align-items: stretch !important;
    gap: 12px !important;
    margin-bottom: 32px !important;
  }
  .slc-hero__actions .slc-btn {
    width: 100% !important;
    justify-content: center !important;
    padding: 14px 20px !important;
  }
  .slc-hero__corridor-bar {
    flex-direction: column !important;
    align-items: flex-start !important;
    gap: 10px !important;
    padding-top: 20px !important;
  }
  .slc-hero__cities {
    flex-wrap: wrap !important;
    font-size: 0.75rem !important;
    letter-spacing: 0.1em !important;
    gap: 8px !important;
  }

  /* Trust Strip on Mobile */
  .slc-trust-strip {
    padding: 24px 0 !important;
  }
  .slc-trust-strip__grid {
    grid-template-columns: 1fr !important;
    gap: 16px !important;
  }

  /* About Visual on Mobile */
  .slc-visual-frame {
    height: 260px !important;
  }
  .slc-float-pill {
    position: static !important;
    margin: 8px 0 0 0 !important;
    width: 100% !important;
    box-sizing: border-box !important;
    box-shadow: var(--slc-shadow-sm) !important;
  }

  /* Services Grid on Mobile */
  .slc-services-dark {
    padding: 60px 0 !important;
  }
  .slc-services-header {
    flex-direction: column !important;
    align-items: flex-start !important;
    gap: 16px !important;
    margin-bottom: 32px !important;
  }
  .slc-services-header .slc-btn {
    width: 100% !important;
    justify-content: center !important;
  }
  .slc-services-grid {
    grid-template-columns: 1fr !important;
    gap: 20px !important;
  }

  /* How It Works on Mobile */
  .slc-how-lux {
    padding: 60px 0 !important;
  }
  .slc-how-header {
    flex-direction: column !important;
    align-items: flex-start !important;
    gap: 16px !important;
    margin-bottom: 32px !important;
  }
  .slc-how-header .slc-btn {
    width: 100% !important;
    justify-content: center !important;
  }

  /* Shipping & Locations on Mobile */
  .slc-shipping, .slc-locations, .slc-testimonials, .slc-faq, .slc-cta {
    padding: 60px 0 !important;
  }
  .slc-shipping-grid, .slc-locations-grid, .slc-testimonials-grid {
    grid-template-columns: 1fr !important;
    gap: 20px !important;
  }
  .slc-compare-card, .slc-form-card, .slc-calc-card, .slc-feature-box, .slc-sidebar-card {
    padding: 22px 16px !important;
  }
  
  /* Subpage Hero on Mobile */
  .slc-page-hero {
    padding: 50px 0 36px !important;
  }
  .slc-page-hero__actions {
    flex-direction: column !important;
    align-items: stretch !important;
    width: 100% !important;
  }
  .slc-page-hero__actions .slc-btn {
    width: 100% !important;
    justify-content: center !important;
  }

  /* Forms & CTA */
  .slc-form-grid {
    grid-template-columns: 1fr !important;
  }
  .slc-cta__actions {
    flex-direction: column !important;
    align-items: stretch !important;
    width: 100% !important;
    gap: 12px !important;
  }
  .slc-cta__actions .slc-btn {
    width: 100% !important;
    justify-content: center !important;
  }
  
  /* Footer on Mobile */
  .slc-footer {
    padding: 50px 0 24px !important;
  }
  .slc-footer__grid {
    grid-template-columns: 1fr !important;
    gap: 32px !important;
  }
  .slc-footer__bottom {
    flex-direction: column !important;
    align-items: flex-start !important;
    gap: 12px !important;
  }
}
"""

def update_css():
    css_path = "assets/css/savelanded.css"
    with open(css_path, "r", encoding="utf-8") as f:
        existing = f.read()

    existing = re.sub(r'/\* =+\s*SECTION 1: TOP ANNOUNCEMENT BAR.*?(?=/\* =+\s*SECTION 2: FLOATING)', '', existing, flags=re.DOTALL)
    existing = re.sub(r'\.slc-announcement[^{]*\{[^}]*\}', '', existing)

    if "MOBILE RESPONSIVENESS OVERHAUL" in existing:
        base_css = existing.split("/* ==========================================================================\n   MOBILE RESPONSIVENESS OVERHAUL")[0]
        new_css = base_css.strip() + "\n\n" + SUBPAGE_AND_MOBILE_CSS.strip()
    else:
        new_css = existing.strip() + "\n\n" + SUBPAGE_AND_MOBILE_CSS.strip()

    with open(css_path, "w", encoding="utf-8") as f:
        f.write(new_css)

    theme_css_path = "savelanded-theme/assets/css/style.css"
    if os.path.exists(theme_css_path):
        with open(theme_css_path, "w", encoding="utf-8") as f:
            f.write(new_css)

def get_header(active_page=""):
    home_active = ' is-active' if active_page == 'home' else ''
    about_active = ' is-active' if active_page == 'about' else ''
    services_active = ' is-active' if active_page in ['services', 'air-freight', 'sea-freight', 'product-sourcing', 'procurement', 'warehousing', 'customs-clearance', 'import-export', 'door-to-door'] else ''
    shipping_active = ' is-active' if active_page == 'shipping' else ''
    contact_active = ' is-active' if active_page == 'contact' else ''

    return f'''
  <!-- ==========================================================================
       PRIMARY MULTIPAGE HEADER & NAVIGATION (Sticky at top:0)
       ========================================================================== -->
  <header class="slc-header">
    <div class="slc-container slc-header__inner">
      
      <!-- Brand Logo -->
      <a href="index.html" class="slc-brand" aria-label="Savelanded Home">
        <div class="slc-brand__logo">
          <img src="logo.jpg" alt="Savelanded Import and Export Company Limited Logo" width="52" height="52" onerror="this.style.display='none'">
        </div>
        <div>
          <div class="slc-brand__name">SAVELANDED</div>
          <div class="slc-brand__sub">Import &amp; Export Co. Ltd</div>
        </div>
      </a>

      <!-- Desktop Multipage Navigation -->
      <nav class="slc-nav-wrap" aria-label="Primary Navigation">
        <ul class="slc-nav">
          <li class="slc-nav__item">
            <a href="index.html" class="slc-nav__link{home_active}">Home</a>
          </li>
          <li class="slc-nav__item">
            <a href="about.html" class="slc-nav__link{about_active}">About Us</a>
          </li>
          <li class="slc-nav__item">
            <a href="services.html" class="slc-nav__link{services_active}">
              <span>Services</span>
              <svg viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg>
            </a>
            <ul class="slc-dropdown">
              <li class="slc-dropdown__header">Freight &amp; Cargo</li>
              <li>
                <a href="air-freight.html" class="slc-dropdown__link">
                  <span class="slc-dropdown__title">Air Freight from China to Nigeria</span>
                  <svg class="slc-dropdown__arrow" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </a>
              </li>
              <li>
                <a href="sea-freight.html" class="slc-dropdown__link">
                  <span class="slc-dropdown__title">Sea Freight from China to Nigeria</span>
                  <svg class="slc-dropdown__arrow" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </a>
              </li>
              <li class="slc-dropdown__header">Sourcing &amp; Procurement</li>
              <li>
                <a href="product-sourcing.html" class="slc-dropdown__link">
                  <span class="slc-dropdown__title">Product Sourcing &amp; Verification</span>
                  <svg class="slc-dropdown__arrow" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </a>
              </li>
              <li>
                <a href="procurement.html" class="slc-dropdown__link">
                  <span class="slc-dropdown__title">Purchasing and Procurement</span>
                  <svg class="slc-dropdown__arrow" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </a>
              </li>
              <li class="slc-dropdown__header">Ground &amp; Trade Operations</li>
              <li>
                <a href="warehousing.html" class="slc-dropdown__link">
                  <span class="slc-dropdown__title">Warehousing &amp; Cargo Consolidation</span>
                  <svg class="slc-dropdown__arrow" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </a>
              </li>
              <li>
                <a href="customs-clearance.html" class="slc-dropdown__link">
                  <span class="slc-dropdown__title">Customs Clearance &amp; Documentation</span>
                  <svg class="slc-dropdown__arrow" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </a>
              </li>
              <li>
                <a href="import-export.html" class="slc-dropdown__link">
                  <span class="slc-dropdown__title">International Import &amp; Export</span>
                  <svg class="slc-dropdown__arrow" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </a>
              </li>
              <li>
                <a href="door-to-door.html" class="slc-dropdown__link">
                  <span class="slc-dropdown__title">Door-to-Door Delivery in Nigeria</span>
                  <svg class="slc-dropdown__arrow" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </a>
              </li>
            </ul>
          </li>
          <li class="slc-nav__item">
            <a href="shipping.html" class="slc-nav__link{shipping_active}">Shipping</a>
          </li>
          <li class="slc-nav__item">
            <a href="contact.html" class="slc-nav__link{contact_active}">Contact</a>
          </li>
        </ul>
      </nav>

      <!-- Primary Action CTA Button -->
      <div class="slc-header__cta">
        <a href="quote.html" class="slc-btn slc-btn-gold">
          <span>GET A QUOTE</span>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </a>
      </div>

      <!-- Mobile Hamburger Toggle -->
      <button type="button" class="slc-menu-toggle" id="slc-menu-toggle" aria-label="Open Navigation">
        <svg viewBox="0 0 24 24"><path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"/></svg>
      </button>

    </div>
  </header>

  <!-- Mobile Drawer & Overlay -->
  <div class="slc-overlay" id="slc-overlay"></div>
  <aside class="slc-mobile-drawer" id="slc-mobile-drawer" aria-label="Mobile Navigation Drawer">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:28px; padding-bottom:14px; border-bottom:1px solid var(--slc-gray-200);">
      <div style="display:flex; align-items:center; gap:10px;">
        <img src="logo.jpg" alt="Savelanded Import and Export Company Limited Logo" width="36" height="36" style="border-radius:4px;">
        <span style="font-family:var(--slc-font-head); font-weight:800; font-size:1.15rem; color:var(--slc-black);">SAVELANDED</span>
      </div>
      <button type="button" id="slc-menu-close" style="background:none; border:none; cursor:pointer; font-size:1.8rem; line-height:1; color:var(--slc-black); padding:4px 8px;" aria-label="Close Navigation">&times;</button>
    </div>
    <ul style="list-style:none; display:flex; flex-direction:column; gap:16px;">
      <li><a href="index.html" style="font-family:var(--slc-font-head); font-weight:700; font-size:1.05rem;">Home</a></li>
      <li><a href="about.html" style="font-family:var(--slc-font-head); font-weight:700; font-size:1.05rem;">About Us</a></li>
      <li>
        <a href="services.html" style="font-family:var(--slc-font-head); font-weight:700; font-size:1.05rem; display:block; margin-bottom:8px;">All Services</a>
        <ul style="list-style:none; padding-left:14px; display:flex; flex-direction:column; gap:10px; font-size:0.925rem; border-left:2px solid var(--slc-gold);">
          <li><a href="air-freight.html">Air Freight</a></li>
          <li><a href="sea-freight.html">Sea Freight</a></li>
          <li><a href="product-sourcing.html">Product Sourcing &amp; Verification</a></li>
          <li><a href="procurement.html">Purchasing &amp; Procurement</a></li>
          <li><a href="warehousing.html">Warehousing &amp; Consolidation</a></li>
          <li><a href="customs-clearance.html">Customs Clearance</a></li>
          <li><a href="import-export.html">Import &amp; Export</a></li>
          <li><a href="door-to-door.html">Door-to-Door Delivery</a></li>
        </ul>
      </li>
      <li><a href="shipping.html" style="font-family:var(--slc-font-head); font-weight:700; font-size:1.05rem;">Shipping Solutions</a></li>
      <li><a href="contact.html" style="font-family:var(--slc-font-head); font-weight:700; font-size:1.05rem;">Contact &amp; Locations</a></li>
    </ul>
    <div style="margin-top:32px; display:flex; flex-direction:column; gap:12px;">
      <a href="quote.html" class="slc-btn slc-btn-gold" style="width:100%; justify-content:center;">REQUEST A QUOTE</a>
      <a href="tel:+8618248547224" class="slc-btn slc-btn-outline" style="width:100%; justify-content:center;">CALL CEO WOLEX</a>
    </div>
  </aside>
'''

def get_footer():
    return '''
  <!-- ==========================================================================
       SECTION 12: HIGH-IMPACT FINAL CTA
       ========================================================================== -->
  <section class="slc-cta">
    <div class="slc-container slc-cta__inner">
      <span class="slc-cta__pill">Direct China–Nigeria Logistics Desk</span>
      <h2 class="slc-cta__title">
        Ready to Ship <em>Without Delays</em> or Stress?
      </h2>
      <p class="slc-cta__desc">
        Join hundreds of Nigerian importers, wholesalers, and entrepreneurs who trust Savelanded for reliable product sourcing, verified supplier purchasing, and safe door-to-door delivery.
      </p>
      <div class="slc-cta__actions">
        <a href="quote.html" class="slc-btn slc-btn-gold">
          <span>REQUEST AN ACCURATE QUOTE</span>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </a>
        <a href="contact.html" class="slc-btn slc-btn-outline-gold">
          <span>CONTACT OUR TEAM</span>
        </a>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       SECTION 13: COMPREHENSIVE MULTIPAGE FOOTER
       ========================================================================== -->
  <footer class="slc-footer">
    <div class="slc-container">
      
      <div class="slc-footer__grid">
        
        <div>
          <a href="index.html" class="slc-footer__logo-wrap">
            <div class="slc-footer__logo-img">
              <img src="logo.jpg" alt="Savelanded Import and Export Company Limited Official Logo" width="48" height="48" loading="lazy" onerror="this.style.display='none'">
            </div>
            <div>
              <div class="slc-footer__brand-title">SAVELANDED</div>
              <div style="font-size:0.6875rem; color:var(--slc-copper); letter-spacing:0.1em; text-transform:uppercase;">Import &amp; Export Co. Ltd</div>
            </div>
          </a>
          <p class="slc-footer__desc">
            Reliable China–Nigeria sourcing, procurement, and international logistics connecting trusted Chinese suppliers with businesses across Nigeria.
          </p>
          <div style="font-family:var(--slc-font-head); font-size:0.75rem; font-weight:700; color:var(--slc-gold); letter-spacing:0.12em; text-transform:uppercase;">
            Connecting China to Nigeria. Simplifying Global Trade.
          </div>
        </div>

        <div>
          <h3 class="slc-footer__heading">Quick Navigation</h3>
          <ul class="slc-footer__links">
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About Savelanded</a></li>
            <li><a href="services.html">Our Services</a></li>
            <li><a href="shipping.html">Shipping from China</a></li>
            <li><a href="contact.html">Office Locations</a></li>
            <li><a href="quote.html">Request a Quote</a></li>
          </ul>
        </div>

        <div>
          <h3 class="slc-footer__heading">Services Directory</h3>
          <ul class="slc-footer__links">
            <li><a href="air-freight.html">Air Freight from China</a></li>
            <li><a href="sea-freight.html">Sea Freight from China</a></li>
            <li><a href="product-sourcing.html">Product Sourcing &amp; Vetting</a></li>
            <li><a href="procurement.html">Purchasing &amp; Procurement</a></li>
            <li><a href="warehousing.html">Warehousing Consolidation</a></li>
            <li><a href="customs-clearance.html">Customs Clearance</a></li>
            <li><a href="import-export.html">Import &amp; Export</a></li>
            <li><a href="door-to-door.html">Door-to-Door Delivery</a></li>
          </ul>
        </div>

        <div>
          <h3 class="slc-footer__heading">Business Contacts</h3>
          <div class="slc-footer__office-block">
            <div class="slc-footer__office-city">Yiwu Head Office (China)</div>
            <div class="slc-footer__office-text">16, 2nd Street, Longgang Road, Yiwu City, Zhejiang Province.</div>
          </div>
          <div class="slc-footer__office-block">
            <div class="slc-footer__office-city">Guangzhou Warehouse Branch</div>
            <div class="slc-footer__office-text">Huayag Warehouse, No. 498 Qinglong Road, Baiyun District.</div>
          </div>
          <div class="slc-footer__office-block">
            <div class="slc-footer__office-city">Lagos Second Branch (Nigeria)</div>
            <div class="slc-footer__office-text">Zone B, Shop 13/14, 23/24, Edo Plaza, Balogun, Trade Fair Complex, Badagry Expressway, Ojo, Lagos.</div>
          </div>
          <div class="slc-footer__phones">
            <a href="tel:+8618248547224">CEO Wolex: +86 182 4854 7224</a>
            <a href="tel:+8615757991458">Procurement (Star): +86 157 5799 1458</a>
            <a href="mailto:admsavelandedimpexpcomltd@gmail.com">admsavelandedimpexpcomltd@gmail.com</a>
          </div>
        </div>

      </div>

      <div class="slc-footer__bottom">
        <div>
          &copy; 2026 Savelanded Import and Export Company Limited. All rights reserved.
        </div>
        <div style="display:flex; gap:20px; flex-wrap:wrap;">
          <a href="about.html">Corporate Profile</a>
          <a href="contact.html">Global Hubs</a>
          <a href="quote.html">Instant Rates</a>
        </div>
      </div>

    </div>
  </footer>

  <!-- Unified Mobile & Interactive JavaScript -->
  <script>
    (function() {
      'use strict';
      var toggle = document.getElementById('slc-menu-toggle');
      var drawer = document.getElementById('slc-mobile-drawer');
      var overlay = document.getElementById('slc-overlay');
      var closeBtn = document.getElementById('slc-menu-close');

      function openDrawer() {
        if (drawer && overlay) {
          drawer.classList.add('is-open');
          overlay.classList.add('is-open');
          overlay.classList.add('is-visible');
          document.body.style.overflow = 'hidden';
        }
      }

      function closeDrawer() {
        if (drawer && overlay) {
          drawer.classList.remove('is-open');
          overlay.classList.remove('is-open');
          overlay.classList.remove('is-visible');
          document.body.style.overflow = '';
        }
      }

      if (toggle) toggle.addEventListener('click', openDrawer);
      if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
      if (overlay) overlay.addEventListener('click', closeDrawer);

      document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') closeDrawer();
      });
    })();
  </script>
'''

def get_page_head(title, description, canonical_slug="", keywords="", schema_data=None):
    keywords_meta = f'<meta name="keywords" content="{keywords}">' if keywords else '<meta name="keywords" content="China to Nigeria shipping, freight forwarding China Nigeria, product sourcing China, air freight Lagos, sea freight Nigeria, cargo consolidation Yiwu Guangzhou">'
    
    schema_script = ""
    if schema_data:
        schema_script = f'''
  <!-- Structured Data (Schema.org JSON-LD) -->
  <script type="application/ld+json">
{json.dumps(schema_data, indent=2, ensure_ascii=False)}
  </script>'''

    clean_slug = canonical_slug[:-5] if canonical_slug.endswith('.html') else canonical_slug
    canonical_url = f"https://savelandedcompany.vercel.app/{clean_slug}" if clean_slug else "https://savelandedcompany.vercel.app/"

    return f'''<!DOCTYPE html>
<html lang="en" class="slc-html">
<head>
  <!-- Google Tag Manager -->
  <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
  new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
  j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
  'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
  })(window,document,'script','dataLayer','GTM-WSW25L7G');</script>
  <!-- End Google Tag Manager -->
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  
  <title>{title} | Savelanded Import &amp; Export Co. Ltd</title>
  <meta name="description" content="{description}">
  {keywords_meta}
  <meta name="author" content="Savelanded Import and Export Company Limited">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <link rel="canonical" href="{canonical_url}">
  
  <!-- International SEO: Hreflang Tagging -->
  <link rel="alternate" hreflang="en-ng" href="{canonical_url}">
  <link rel="alternate" hreflang="en" href="{canonical_url}">
  <link rel="alternate" hreflang="x-default" href="{canonical_url}">
  
  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Savelanded Import and Export Company Limited">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:title" content="{title} | Savelanded">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="https://savelandedcompany.vercel.app/logo.jpg">
  <meta property="og:locale" content="en_NG">
  <meta property="og:locale:alternate" content="en_US">

  <!-- Twitter Card Meta -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title} | Savelanded">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="https://savelandedcompany.vercel.app/logo.jpg">

  <link rel="icon" type="image/jpeg" href="logo.jpg">
  <link rel="apple-touch-icon" href="logo.jpg">

  <!-- Google Fonts: Sora, DM Sans, Cormorant Garamond -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@1,500;1,600&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=Sora:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <!-- Main Stylesheet -->
  <link rel="stylesheet" href="assets/css/savelanded.css">
{schema_script}
</head>
<body class="slc-body">
  <!-- Google Tag Manager (noscript) -->
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-WSW25L7G"
  height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
  <!-- End Google Tag Manager (noscript) -->
'''

def get_service_sidebar(active_slug):
    services = [
        ("air-freight.html", "Air Freight from China"),
        ("sea-freight.html", "Sea Freight (FCL/LCL)"),
        ("product-sourcing.html", "Product Sourcing & Vetting"),
        ("procurement.html", "Purchasing & Procurement"),
        ("warehousing.html", "Warehousing & Consolidation"),
        ("customs-clearance.html", "Customs Clearance & Documentation"),
        ("import-export.html", "International Import & Export"),
        ("door-to-door.html", "Door-to-Door Delivery"),
    ]
    links_html = ""
    for url, label in services:
        is_active = ' is-active' if url == active_slug else ''
        links_html += f'<li><a href="{url}" class="slc-sidebar-nav__link{is_active}"><span>{label}</span><svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a></li>\n'

    return f'''
    <aside>
      <div class="slc-sidebar-card">
        <h3 class="slc-sidebar-heading">All Services</h3>
        <ul class="slc-sidebar-nav">
          {links_html}
        </ul>
      </div>

      <div class="slc-sidebar-card slc-sidebar-card--dark">
        <div style="font-family:var(--slc-font-head); font-size:1.15rem; font-weight:700; color:var(--slc-gold); margin-bottom:12px;">Need Instant Cargo Support?</div>
        <p style="font-size:0.9rem; color:rgba(255,255,255,0.75); line-height:1.6; margin-bottom:20px;">
          Speak directly with our China–Nigeria logistics managers for cargo rates, warehouse receiving, and procurement assistance.
        </p>
        <div style="display:flex; flex-direction:column; gap:12px;">
          <a href="tel:+8618248547224" class="slc-btn slc-btn-gold" style="width:100%; justify-content:center;">
            <span>CALL CEO WOLEX</span>
          </a>
          <a href="quote.html" class="slc-btn slc-btn-outline-gold" style="width:100%; justify-content:center;">
            <span>GET A QUOTE</span>
          </a>
        </div>
      </div>
    </aside>
    '''

print("Updated build_multipage.py with full SEO and Schema.org generator.")
