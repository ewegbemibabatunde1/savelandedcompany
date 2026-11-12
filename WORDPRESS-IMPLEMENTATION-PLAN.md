# UPDATED WORDPRESS IMPLEMENTATION PLAN
## Savelanded Import and Export Company Limited
**Corporate Domain:** https://savelandedcompany.com/  
**Document Phase:** Stage 2 — Architecture, Multipage Hierarchy & Deployment Blueprint  
**Revision Date:** November 12, 2026  

---

### 1. Executive Architecture Summary
This updated implementation plan expands upon the approved homepage prototype (`index.html`) to support the full **multipage corporate architecture** of Savelanded Import and Export Company Limited. 

The website is engineered as a bespoke, lightweight WordPress theme (`savelanded-theme`) backed by a companion functionality plugin (`savelanded-core`). It adheres strictly to WordPress coding standards, eliminates dependencies on third-party page builders (such as Elementor or Divi), and guarantees long-term maintainability, SEO dominance, and high-performance Core Web Vitals.

---

### 2. Full Multipage Information Architecture & URL Slugs

The WordPress implementation will register and render the planned corporate hierarchy:

```
https://savelandedcompany.com/
├── /                              # front-page.php (Master Homepage)
├── /about/                        # page-about.php (About Savelanded, Mission, Executive Presence)
├── /services/                     # page-services.php (Services Hub)
│   ├── /air-freight-china-to-nigeria/            # single-slc_service.php
│   ├── /sea-freight-china-to-nigeria/            # single-slc_service.php
│   ├── /product-sourcing-china/                  # single-slc_service.php
│   ├── /purchasing-procurement/                  # single-slc_service.php
│   ├── /customs-clearance-documentation/         # single-slc_service.php
│   ├── /cargo-consolidation-china/               # single-slc_service.php
│   ├── /international-import-export/             # single-slc_service.php
│   └── /door-to-door-shipping-nigeria/           # single-slc_service.php
├── /shipping/                     # page-shipping.php (Air vs Sea Guide, Freight Economics)
├── /locations/                    # page-locations.php (Yiwu, Guangzhou, Lagos Trade Fair Hub)
├── /resources/ (or /blog/)        # home.php & archive.php (Import Guides, Trade Insights)
│   └── /sample-guide-slug/        # single.php (Editorial trade articles)
├── /contact/                      # page-contact.php (Office Maps, Direct Hotlines, Inquiries)
├── /request-a-quote/              # page-quote.php (Dedicated Quote Wizard)
└── /privacy-policy/               # page.php (NDPR & International Privacy Compliance)
```

---

### 3. Theme Directory Structure & Template Hierarchy

```
wp-content/themes/savelanded-theme/
├── style.css                      # Theme declaration header & scoped .slc- CSS
├── functions.php                  # Theme setup, asset enqueuing, customizer, menus
├── header.php                     # Announcement bar, brand identity & multipage navigation
├── footer.php                     # Multipage directory footer, legal links & quote modal
├── front-page.php                 # Homepage master template rendering template parts
├── index.php                      # Universal fallback template
├── page.php                       # Default Gutenberg page template
├── single.php                     # Editorial blog/guide article template
├── archive.php                    # Resource & article category archive
├── single-slc_service.php         # Dedicated individual service template
├── screenshot.png                 # Theme preview thumbnail (1200x900px)
├── template-parts/                # Modular, reusable components
│   ├── hero.php                   # Section 3: Flagship Hero component
│   ├── trust-bar.php              # Section 4: 5 Trust & Value propositions
│   ├── about.php                  # Section 5: Company mission & ground operations
│   ├── services-flagship.php      # Section 6a: Air & Sea Freight hero split
│   ├── services-grid.php          # Section 6b: Sourcing, Procurement & Ground services
│   ├── why-us.php                 # Section 7: 6 Core competitive advantages
│   ├── how-it-works.php           # Section 8: 5-Step visual cargo journey
│   ├── shipping-comparison.php    # Section 9: Air vs. Sea Freight matrix
│   ├── locations.php              # Section 10: Yiwu, Guangzhou & Lagos offices
│   ├── testimonials.php           # Section 11: Verified customer testimonials
│   ├── faq.php                    # Section 12: Accordion FAQ module
│   ├── cta.php                    # Section 13: High-impact pre-footer conversion block
│   └── modal-quote.php            # Global quotation & inquiry modal
└── assets/
    ├── css/
    │   └── main.css               # Production stylesheet
    ├── js/
    │   └── main.js                # Vanilla JavaScript (drawer, accordion, modal)
    └── images/
        ├── logo.jpg               # Savelanded official emblem
        └── logistics/             # Optimized WebP photography
```

---

### 4. Companion Functionality Plugin (`savelanded-core`)

To ensure business functionality remains fully independent of theme styling:
- **Custom Post Types:**
  - `slc_service`: Powers the 8 individual service pages with custom metadata (transit suitability, cargo parameters, origin receiving hubs).
  - `slc_testimonial`: Manages client quotes, client city, and permission tracking.
  - `slc_faq`: Manages searchable question-and-answer pairs.
- **Quote Processing & Email Dispatch:**
  - Registers the custom REST API endpoint: `POST /wp-json/savelanded/v1/quote`.
  - Validates nonces via `wp_verify_nonce()` and sanitizes all inputs.
  - Dispatches immediate transactional notifications to `svgadmsavelandedimpexpcomltd@gmail.com` via `wp_mail()`.
  - Persists quote records to a custom database table (`wp_slc_quotes`) with customer contact details and cargo specifications.

---

### 5. Asset Enqueuing & Core Web Vitals Strategy

```php
function savelanded_enqueue_assets() {
    // 1. Enqueue Google Fonts: Sora, DM Sans, Cormorant Garamond
    wp_enqueue_style(
        'savelanded-fonts',
        'https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@1,500;1,600&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=Sora:wght@400;500;600;700;800&display=swap',
        array(),
        null
    );

    // 2. Enqueue Theme Scoped Stylesheet
    wp_enqueue_style(
        'savelanded-main',
        get_stylesheet_uri(),
        array('savelanded-fonts'),
        wp_get_theme()->get('Version')
    );

    // 3. Enqueue Vanilla JavaScript (Deferred in Footer)
    wp_enqueue_script(
        'savelanded-script',
        get_template_directory_uri() . '/assets/js/main.js',
        array(),
        wp_get_theme()->get('Version'),
        true
    );

    // 4. Localize Nonces & Endpoint Variables
    wp_localize_script('savelanded-script', 'savelanded_data', array(
        'rest_url'   => esc_url_raw(rest_url('savelanded/v1/quote')),
        'rest_nonce' => wp_create_nonce('wp_rest')
    ));
}
add_action('wp_enqueue_scripts', 'savelanded_enqueue_assets');
```

---

### 6. Deployment & Rollback Protocol

1. **Staging Review:** Test theme and core plugin on a password-protected staging subdomain (e.g., `staging.savelandedcompany.com`).
2. **Database & File Backup:** Full cPanel / WP-CLI backup (`wp db export`) of the existing installation prior to activation.
3. **Menu & Permalinks Setup:** Register primary and footer navigation in `wp-admin > Appearance > Menus`, and verify rewrite rules under `Settings > Permalinks` (`/%postname%/`).
4. **SMTP Verification:** Confirm deliverability of outgoing quote inquiries using a dedicated SMTP service (e.g., SendGrid, Mailgun, or Google Workspace SMTP).
