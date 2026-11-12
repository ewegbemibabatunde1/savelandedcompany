# -*- coding: utf-8 -*-
"""
Expansion Content Module for Savelanded 14-Page Website
Contains comprehensive, compliant, authoritative HTML blocks with:
- Target keywords naturally distributed
- Authoritative external references (IATA, IMO, NCS, SON, etc.)
- Concrete calculations & comparison tables
- Step-by-step procedures
- Reviewer attribution badges
- Clear warnings against scams/misunderstandings
"""

AIR_FREIGHT_ADDITION = """
          <!-- Chargeable Weight Deep-Dive & Practical Numerical Examples -->
          <h2 id="chargeable-weight-examples">Chargeable Weight Calculation Examples: Actual vs. Volumetric Weight</h2>
          <p>
            One of the most frequent sources of confusion for Nigerian importers is how airlines calculate air cargo costs. Following <a href="https://www.iata.org/" target="_blank" rel="noopener noreferrer" class="slc-ext-link">IATA (International Air Transport Association)</a> rules, air freight charges are always billed based on whichever is greater: the <strong>Actual Gross Scale Weight</strong> or the <strong>Volumetric (Dimensional) Weight</strong>.
          </p>
          <div class="slc-definition-box">
            <div class="slc-definition-term">IATA Air Cargo Volumetric Formula</div>
            <p class="slc-definition-desc">
              <strong>Volumetric Weight (kg) = [Length (cm) &times; Width (cm) &times; Height (cm)] &divide; 6,000</strong><br>
              <em>Note: Some express courier services like DHL or FedEx use a 5,000 divisor, making commercial air cargo with a 6,000 divisor significantly more economical for bulky goods.</em>
            </p>
          </div>

          <div class="slc-comparison-table-wrapper">
            <table class="slc-comparison-table">
              <thead>
                <tr>
                  <th>Cargo Scenario</th>
                  <th>Carton Dimensions</th>
                  <th>Actual Weight</th>
                  <th>Volumetric Weight</th>
                  <th>Billed Weight &amp; Explanation</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Heavy Dense Goods</strong> (e.g., copper wire, hardware tools)</td>
                  <td>40cm &times; 30cm &times; 25cm (30,000 cm&sup3;)</td>
                  <td>22.0 kg</td>
                  <td>30,000 &divide; 6,000 = <strong>5.0 kg</strong></td>
                  <td><strong>22.0 kg</strong> (Actual scale weight applies because physical mass exceeds dimensional volume)</td>
                </tr>
                <tr>
                  <td><strong>Bulky Lightweight Goods</strong> (e.g., shoes in boxes, hats, plush toys)</td>
                  <td>70cm &times; 60cm &times; 50cm (210,000 cm&sup3;)</td>
                  <td>14.0 kg</td>
                  <td>210,000 &divide; 6,000 = <strong>35.0 kg</strong></td>
                  <td><strong>35.0 kg</strong> (Volumetric weight applies because cargo consumes significant aircraft hold space)</td>
                </tr>
                <tr>
                  <td><strong>Balanced Electronics Carton</strong> (e.g., smart watches, phone accessories)</td>
                  <td>50cm &times; 40cm &times; 30cm (60,000 cm&sup3;)</td>
                  <td>11.5 kg</td>
                  <td>60,000 &divide; 6,000 = <strong>10.0 kg</strong></td>
                  <td><strong>11.5 kg</strong> (Scale weight slightly exceeds volume; billed on exact 11.5 kg)</td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- Shipping Restrictions & Dangerous Goods Compliance -->
          <h2 id="air-shipping-restrictions">Air Freight Restrictions &amp; Dangerous Goods (DG) Guidelines</h2>
          <p>
            International aviation safety regulations strictly enforce what can and cannot board cargo aircraft. Understanding these restrictions saves Nigerian businesses weeks of delays and prevents cargo confiscation at airport customs.
          </p>
          <div class="slc-step-grid">
            <div class="slc-step-card">
              <span class="slc-tag slc-tag--official">Standard Air Clearance</span>
              <h3 class="slc-step-title">General Cargo (General Goods)</h3>
              <p class="slc-step-text">
                Apparel, unbranded footwear, machine spare parts, phone cases, solar lamps (without internal lithium batteries), and hardware accessories. Clears customs rapidly with standard commercial invoice and packing list.
              </p>
            </div>
            <div class="slc-step-card">
              <span class="slc-tag">Special DG Routing</span>
              <h3 class="slc-step-title">Battery &amp; Electronic Goods</h3>
              <p class="slc-step-text">
                Phones, laptops, power banks, and rechargeable tools require Material Safety Data Sheets (MSDS), UN38.3 test summaries, and dangerous goods declarations under <a href="https://www.icao.int/" target="_blank" rel="noopener noreferrer" class="slc-ext-link">ICAO (International Civil Aviation Organization)</a> rules. Flown via designated battery freighter lanes.
              </p>
            </div>
            <div class="slc-step-card">
              <span class="slc-tag slc-tag--warning">Strictly Prohibited Air Items</span>
              <h3 class="slc-step-title">Restricted Substances</h3>
              <p class="slc-step-text">
                Flammable liquids, perfumes, aerosols, uncertified powders, corrosive acids, perishable fresh foods without reefer air containers, and brand-infringing (counterfeit) designer items are strictly rejected by airline security.
              </p>
            </div>
          </div>

          <!-- Cargo Documentation & Air Freight Transit Breakdown -->
          <h2 id="air-documentation-routes">Required Documentation &amp; Route Logistics</h2>
          <p>
            Every air cargo consignment moving between China and Lagos requires rigorous cross-border documentation:
          </p>
          <ul class="slc-checklist">
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">&bull;</span>
              <div>
                <strong>Air Waybill (AWB):</strong> The fundamental contract of carriage issued by the carrier or forwarder detailing shipper, consignee, airport codes (CAN/SZX to LOS), weight, and piece count.
              </div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">&bull;</span>
              <div>
                <strong>Commercial Invoice (CI) &amp; Packing List (PL):</strong> Itemized list of merchandise, unit values, gross/net weights, and harmonized system (HS) codes.
              </div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">&bull;</span>
              <div>
                <strong>Lagos Airport Handling Sheds:</strong> Upon landing at Murtala Muhammed International Airport (LOS), cargo is received into official cargo handling sheds operated by NAHCO (Nigerian Aviation Handling Company) or SAHCO (Skyway Aviation Handling Company) before Nigeria Customs Service inspection.
              </div>
            </li>
          </ul>

          <!-- Cost Factors and Transit Explanation -->
          <h2 id="air-cost-factors">Air Freight Cost Drivers &amp; Transit Expectations</h2>
          <p>
            Air cargo rates fluctuate dynamically based on aviation fuel surcharges (baf), airline peak season demand (especially from September to December before Christmas and Chinese New Year), and cargo classification (General cargo vs. DG battery rates).
          </p>
          <p>
            <strong>Standard air transit:</strong> 5 to 8 working days from flight departure in Guangzhou. <strong>Priority express:</strong> 3 to 5 working days. Note that supplier production delays or Chinese domestic courier delays to our warehouse are outside the flight transit window.
          </p>

          <div class="slc-reviewer-badge">
            <div class="slc-reviewer-avatar">WO</div>
            <div>
              <strong>Technical Guidance by Wolex (CEO, Savelanded)</strong> &bull; China–Nigeria Air Cargo &amp; Sourcing Specialist<br>
              <span style="font-size:0.8rem; color:#718096;">Verified with IATA air cargo standards &bull; Direct flight allocations CAN &rarr; LOS</span>
            </div>
          </div>
"""

SEA_FREIGHT_ADDITION = """
          <!-- FCL vs LCL Detailed Comparison -->
          <h2 id="fcl-vs-lcl-comparison">FCL vs. LCL: Choosing the Right Ocean Freight Mode</h2>
          <p>
            Sea freight is the lifeblood of high-volume China–Nigeria commerce. Understanding whether your shipment warrants a Full Container Load (FCL) or Less than Container Load (LCL / Groupage) directly determines your shipping cost per unit and your landing speed.
          </p>

          <div class="slc-comparison-table-wrapper">
            <table class="slc-comparison-table">
              <thead>
                <tr>
                  <th>Feature</th>
                  <th>FCL (Full Container Load)</th>
                  <th>LCL (Less than Container Load / Groupage)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Minimum Volume</strong></td>
                  <td>Standard 20ft container (approx. 28 CBM) or 40ft/40HQ (approx. 68 CBM)</td>
                  <td>1 CBM (Cubic Meter) or even fractions for small commercial parcels</td>
                </tr>
                <tr>
                  <td><strong>Billing Basis</strong></td>
                  <td>Flat rate per container plus terminal handling &amp; marine bunker fees</td>
                  <td>Per Cubic Meter (CBM) all-inclusive or ocean rate + clearing fee</td>
                </tr>
                <tr>
                  <td><strong>Container Exclusivity</strong></td>
                  <td>100% reserved for your enterprise. Sealed at factory or port in China.</td>
                  <td>Consolidated with vetted cargo from other reputable Nigerian importers.</td>
                </tr>
                <tr>
                  <td><strong>Customs Clearance</strong></td>
                  <td>Single consignee clearance via Form M &amp; PAAR or bespoke agent release.</td>
                  <td>Consolidated clearance managed entirely by Savelanded at Lagos bonded terminals.</td>
                </tr>
                <tr>
                  <td><strong>Best Suited For</strong></td>
                  <td>Heavy machinery, bulk industrial raw materials, building supplies, large stock.</td>
                  <td>SMEs, growing e-commerce sellers, spare parts importers, test merchandise batches.</td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- Container Dimensions & CBM Calculations -->
          <h2 id="container-dimensions-cbm">20ft vs. 40ft Containers &amp; Accurate CBM Calculations</h2>
          <p>
            Cubic Meters (CBM) measure cargo volume. In ocean shipping, rates are quoted per CBM. Knowing standard maritime equipment capacities allows you to negotiate factory carton packing sizes to maximize container payload.
          </p>
          <div class="slc-definition-box">
            <div class="slc-definition-term">Maritime CBM Calculation Formula</div>
            <p class="slc-definition-desc">
              <strong>CBM per carton = [Length (m) &times; Width (m) &times; Height (m)]</strong><br>
              <em>Example: A carton measuring 50cm &times; 40cm &times; 40cm = 0.50m &times; 0.40m &times; 0.40m = 0.08 CBM. If you have 50 cartons: 50 &times; 0.08 = 4.0 CBM total volume.</em>
            </p>
          </div>

          <div class="slc-step-grid">
            <div class="slc-step-card">
              <span class="slc-tag slc-tag--official">Standard Dry 20FT</span>
              <h3 class="slc-step-title">20-Foot General Purpose (20GP)</h3>
              <p class="slc-step-text">
                Internal Dimensions: 5.90m &times; 2.35m &times; 2.39m.<br>
                Usable Cargo Volume: <strong>28 to 30 CBM</strong>.<br>
                Maximum Payload: Approx. 21,500 kg to 25,000 kg.<br>
                Best for dense, heavy goods like tiles, metal fittings, fasteners, or paper reels.
              </p>
            </div>
            <div class="slc-step-card">
              <span class="slc-tag slc-tag--official">High Cube 40HQ</span>
              <h3 class="slc-step-title">40-Foot High Cube (40HQ)</h3>
              <p class="slc-step-text">
                Internal Dimensions: 12.03m &times; 2.35m &times; 2.69m.<br>
                Usable Cargo Volume: <strong>66 to 68 CBM</strong>.<br>
                Maximum Payload: Approx. 26,000 kg to 28,000 kg.<br>
                Best for volumetric, lighter cargo such as furniture, luggage, footwear, textiles, and plasticware.
              </p>
            </div>
          </div>

          <!-- Chinese Loading Ports to Nigerian Destination Ports -->
          <h2 id="sea-ports-routes">Chinese Loading Ports &amp; Nigerian Destination Terminals</h2>
          <p>
            Vessels sail from premier deepwater container hubs in China following international maritime conventions supervised by the <a href="https://www.imo.org/" target="_blank" rel="noopener noreferrer" class="slc-ext-link">International Maritime Organization (IMO)</a>:
          </p>
          <ul class="slc-checklist">
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">&bull;</span>
              <div>
                <strong>Ningbo-Zhoushan &amp; Shanghai Ports:</strong> Primary maritime gateways for cargo originating from Yiwu, Hangzhou, Wenzhou, and Jiangsu manufacturing clusters.
              </div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">&bull;</span>
              <div>
                <strong>Guangzhou (Nansha) &amp; Shenzhen (Yantian / Shekou):</strong> Main ports of departure for Guangdong industrial regions (Foshan, Dongguan, Zhongshan).
              </div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">&bull;</span>
              <div>
                <strong>Lagos Destination Ports:</strong> Containers call at <strong>Lagos Port Complex (Apapa)</strong>, <strong>Tin Can Island Port</strong>, and the modern deepwater <strong>Lekki Deep Sea Port</strong>, with bonded terminal transfers for swift clearing and congestion avoidance.
              </div>
            </li>
          </ul>

          <!-- Ocean Transit Times & Cost Factors -->
          <h2 id="sea-transit-cost-factors">Ocean Transit Times &amp; Key Cost Factors</h2>
          <p>
            <strong>Port-to-port ocean transit</strong> from China to Lagos typically ranges between <strong>35 to 45 days</strong> depending on whether the vessel sails directly through the Cape of Good Hope or transships at international ports such as Singapore or Pointe-Noire.
          </p>
          <p>
            Key cost components include ocean freight (O/F), bunker adjustment factors (BAF), currency adjustment factors (CAF), terminal handling charges (THC) at both load and discharge ports, Nigerian port tariffs, and demurrage avoidance strategies.
          </p>

          <div class="slc-reviewer-badge">
            <div class="slc-reviewer-avatar">WO</div>
            <div>
              <strong>Technical Guidance by Wolex (CEO, Savelanded)</strong> &bull; Maritime Logistics &amp; Container Freight Forwarder<br>
              <span style="font-size:0.8rem; color:#718096;">Verified with global container shipping lines &bull; Servicing Apapa, Tin Can Island, &amp; Lekki ports</span>
            </div>
          </div>
"""

PRODUCT_SOURCING_ADDITION = """
          <!-- China Manufacturing Hubs Breakdown -->
          <h2 id="china-manufacturing-hubs">Specialized Chinese Industrial Hubs &amp; Wholesale Markets</h2>
          <p>
            Source smarter by tapping directly into the specialized industrial cluster dedicated to your product category. In China, entire cities specialize in individual industries, offering unbeatable pricing and immense factory variety.
          </p>

          <div class="slc-comparison-table-wrapper">
            <table class="slc-comparison-table">
              <thead>
                <tr>
                  <th>Industrial City / Region</th>
                  <th>Famous Wholesale Markets</th>
                  <th>Primary Product Specialization</th>
                  <th>Why Nigerian Buyers Source Here</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Yiwu (Zhejiang)</strong></td>
                  <td>Yiwu International Trade City (Futian Market Districts 1–5), Huangyuan Clothing Market</td>
                  <td>Small commodities, jewelry, bags, stationery, hardware, kitchenware, cosmetics, toys</td>
                  <td>Low minimum order quantities (MOQs), ready stock availability, rapid consolidation capability.</td>
                </tr>
                <tr>
                  <td><strong>Guangzhou (Guangdong)</strong></td>
                  <td>Shisanhang &amp; Baima Clothing Markets, Zhanxi Watch Market, Nanfang Building Electronics</td>
                  <td>Fashion apparel, premium denim, fabrics, beauty equipment, hotel supplies, cosmetics</td>
                  <td>Trend-setting designs, proximity to Baiyun airport and Nansha seaport, vast trading ecosystem.</td>
                </tr>
                <tr>
                  <td><strong>Shenzhen (Guangdong)</strong></td>
                  <td>Huaqiangbei Electronics Market, Bao'an High-Tech Industrial Park</td>
                  <td>Consumer electronics, smartphone accessories, LED lighting, motherboards, surveillance</td>
                  <td>The hardware capital of the world with immediate access to cutting-edge component factories.</td>
                </tr>
                <tr>
                  <td><strong>Foshan (Guangdong)</strong></td>
                  <td>Lecong Furniture City, China Ceramics City, Nanhai Aluminum Wholesale Center</td>
                  <td>Home &amp; office furniture, porcelain tiles, architectural sanitaryware, doors &amp; windows</td>
                  <td>World leader in interior decoration and building materials essential for Nigerian construction.</td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- Supplier Discovery & On-Site Verification -->
          <h2 id="supplier-verification-methods">Supplier Discovery &amp; On-Site Due Diligence</h2>
          <p>
            Online marketplaces like 1688.com, Made-in-China, and Alibaba list millions of vendors, but up to 40% are trading middlemen or shell entities rather than direct manufacturers. Savelanded performs multi-point on-site verifications across China:
          </p>
          <div class="slc-step-grid">
            <div class="slc-step-card">
              <div class="slc-step-num">1</div>
              <h3 class="slc-step-title">Business License Audit</h3>
              <p class="slc-step-text">
                Verification of the supplier's Unified Social Credit Code (USCC) against the State Administration for Market Regulation (SAMR) database to confirm authorized business scope, registered capital, and operational status.
              </p>
            </div>
            <div class="slc-step-card">
              <div class="slc-step-num">2</div>
              <h3 class="slc-step-title">Factory Floor Inspection</h3>
              <p class="slc-step-text">
                Physical visit to the production workshop to confirm machinery presence, worker headcount, daily output capacity, and compliance with quality control standards.
              </p>
            </div>
            <div class="slc-step-card">
              <div class="slc-step-num">3</div>
              <h3 class="slc-step-title">Sample Testing &amp; Approval</h3>
              <p class="slc-step-text">
                Receiving pre-production samples at our Yiwu or Guangzhou office, examining material thickness, seam strength, technical specs, and couriering directly to you in Nigeria for sign-off.
              </p>
            </div>
          </div>

          <!-- Common Sourcing Traps to Avoid -->
          <h2 id="sourcing-mistakes-scams">Common China Sourcing Mistakes &amp; How to Prevent Them</h2>
          <p>
            Nigerian entrepreneurs frequently lose capital to avoidable purchasing blunders. Savelanded acts as your protective ground buffer:
          </p>
          <ul class="slc-checklist">
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">&times;</span>
              <div>
                <strong>Ordering Without Pre-Shipment Sample Approval:</strong> Never initiate full production based solely on catalog photos. Subtle changes in fabric weight (GSM) or plastic grade can ruin marketability.
              </div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">&times;</span>
              <div>
                <strong>Paying 100% Upfront:</strong> Standard international terms are 30% deposit to begin production, and 70% balance payable only AFTER post-production quality inspection passes.
              </div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">&times;</span>
              <div>
                <strong>Vague Purchase Specifications:</strong> "Good quality" has no legal standing in China. Specifications must document exact Pantone colors, dimensions, voltage (220V for Nigeria), plug types (UK standard Type G), and carton burst-strength.
              </div>
            </li>
          </ul>

          <div class="slc-reviewer-badge">
            <div class="slc-reviewer-avatar">ST</div>
            <div>
              <strong>Field Verification Lead: Star</strong> &bull; Savelanded Sourcing &amp; Procurement Desk (Yiwu)<br>
              <span style="font-size:0.8rem; color:#718096;">Fluent in Mandarin &amp; English &bull; 10+ years factory audits in Zhejiang &amp; Guangdong</span>
            </div>
          </div>
"""

PROCUREMENT_ADDITION = """
          <!-- 1688 & Taobao Purchasing Process -->
          <h2 id="1688-procurement-guide">Procuring Directly from 1688.com, Taobao &amp; Chinese Factories</h2>
          <p>
            <strong>1688.com</strong> is Alibaba Group's domestic Chinese wholesale platform where manufacturers sell directly to local trade businesses at true domestic prices—frequently <strong>20% to 40% cheaper</strong> than international export platforms. However, 1688 is exclusively in Chinese, requires domestic Chinese business bank cards or Alipay, and does not ship internationally.
          </p>
          <p>
            Savelanded bridges this gap as your registered Chinese purchasing agent, conducting seamless RMB payments, supplier communication, and domestic logistics tracking.
          </p>

          <div class="slc-step-grid">
            <div class="slc-step-card">
              <div class="slc-step-num">1</div>
              <h3 class="slc-step-title">Submit 1688 / Factory Links</h3>
              <p class="slc-step-text">
                Send us the product links, specifications, quantities, and model numbers. If you only have photos or samples, our Yiwu sourcing team locates the primary manufacturing source.
              </p>
            </div>
            <div class="slc-step-card">
              <div class="slc-step-num">2</div>
              <h3 class="slc-step-title">Supplier Price &amp; Stock Audit</h3>
              <p class="slc-step-text">
                We contact the supplier directly via AliWangWang or WeChat, confirm real-time inventory, negotiate wholesale tier discounts, and verify domestic Chinese delivery fees.
              </p>
            </div>
            <div class="slc-step-card">
              <div class="slc-step-num">3</div>
              <h3 class="slc-step-title">Transparent Pro-Forma Invoice</h3>
              <p class="slc-step-text">
                We generate an itemized invoice detailing the exact RMB purchase price, verified currency conversion, and nominal procurement service fee. You make payment securely.
              </p>
            </div>
            <div class="slc-step-card">
              <div class="slc-step-num">4</div>
              <h3 class="slc-step-title">RMB Payment &amp; Order Execution</h3>
              <p class="slc-step-text">
                Our Chinese corporate entity releases payment to the supplier through secure domestic escrow channels, ensuring vendor accountability before goods are dispatched.
              </p>
            </div>
          </div>

          <!-- Payment Verification & Currency Management -->
          <h2 id="procurement-payment-security">Safe Payment Protocols &amp; Avoiding Black-Market Currency Traps</h2>
          <p>
            Cross-border financial transactions present serious legal and financial risks if mishandled. Using unverified peer-to-peer (P2P) currency traders frequently leads to frozen Chinese bank accounts under strict anti-money laundering (AML) crackdowns by the People's Bank of China.
          </p>
          <div class="slc-callout">
            <strong>Why Savelanded Payment Processing Protects You:</strong><br>
            All RMB payments to suppliers originate from legally registered, verified corporate bank accounts in China. We provide full official receipt vouchers (Fapiao where applicable) and transaction transaction reference numbers, guaranteeing your supplier recognizes your payment immediately without disputes.
          </div>

          <div class="slc-reviewer-badge">
            <div class="slc-reviewer-avatar">ST</div>
            <div>
              <strong>Procurement Operations: Star</strong> &bull; Savelanded Purchasing Desk (Yiwu Head Office)<br>
              <span style="font-size:0.8rem; color:#718096;">Specialist in 1688 escrow, Taobao procurement, and RMB supplier settlements</span>
            </div>
          </div>
"""

WAREHOUSING_ADDITION = """
          <!-- Warehouse Operations & Multi-Supplier Consolidation -->
          <h2 id="consolidation-process">How Multi-Supplier Cargo Consolidation Works</h2>
          <p>
            Most successful Nigerian merchants do not buy all their merchandise from a single factory. You might purchase shoes in Wenzhou, bags in Yiwu, and phone chargers in Shenzhen. Paying separate shipping and clearing fees for each individual package is financially prohibitive.
          </p>
          <p>
            Our multi-supplier cargo consolidation unites all your purchases into a single unified consignment, cutting your landed shipping costs by up to <strong>35%</strong>.
          </p>

          <div class="slc-step-grid">
            <div class="slc-step-card">
              <div class="slc-step-num">1</div>
              <h3 class="slc-step-title">Intake &amp; Unique Shipping Mark</h3>
              <p class="slc-step-text">
                Suppliers deliver to our Guangzhou or Yiwu warehouse marked with your unique client code (e.g., <code>SLC-LAGOS-XXXX</code>). Every carton is scanned into our tracking registry.
              </p>
            </div>
            <div class="slc-step-card">
              <div class="slc-step-num">2</div>
              <h3 class="slc-step-title">Inspection, Weighing &amp; CBM Measurement</h3>
              <p class="slc-step-text">
                We inspect outer cartons for transit damage, record scale weight, measure precise dimensional length &times; width &times; height, and photograph goods for your verification.
              </p>
            </div>
            <div class="slc-step-card">
              <div class="slc-step-num">3</div>
              <h3 class="slc-step-title">Free Storage &amp; Repacking</h3>
              <p class="slc-step-text">
                Goods are safely stored in our secure, dry warehouse while awaiting other supplier deliveries. We provide complimentary storage up to 14 days to complete your collection.
              </p>
            </div>
            <div class="slc-step-card">
              <div class="slc-step-num">4</div>
              <h3 class="slc-step-title">Reinforced Packaging &amp; Dispatch</h3>
              <p class="slc-step-text">
                Cartons are grouped, consolidated, reinforced with high-density strapping, waterproof woven sacks, and corner protectors before loading into air pallets or sea containers.
              </p>
            </div>
          </div>

          <!-- Warehouse Specifications & Facilities -->
          <h2 id="warehouse-facilities">Guangzhou &amp; Yiwu Warehouse Facilities Matrix</h2>
          <div class="slc-comparison-table-wrapper">
            <table class="slc-comparison-table">
              <thead>
                <tr>
                  <th>Facility Feature</th>
                  <th>Guangzhou Logistics Hub (Baiyun)</th>
                  <th>Yiwu Consolidation Center (Longgang Rd)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Primary Function</strong></td>
                  <td>Air freight flight staging, South China container stuffing, Guangdong factory intake</td>
                  <td>Futian market purchasing intake, small commodities consolidation, Zhejiang cargo staging</td>
                </tr>
                <tr>
                  <td><strong>Security &amp; Surveillance</strong></td>
                  <td>24/7 CCTV monitoring, perimeter security, electronic access control</td>
                  <td>Continuous HD camera recording, fire suppression systems, insured storage zones</td>
                </tr>
                <tr>
                  <td><strong>Value-Added Services</strong></td>
                  <td>Wooden crating for fragile goods, pallet wrapping, bubble wrapping, repackaging</td>
                  <td>Product sorting, supplier sample merging, barcode labeling, carton bundling</td>
                </tr>
                <tr>
                  <td><strong>Free Storage Policy</strong></td>
                  <td>Up to 14 complimentary storage days during active cargo consolidation</td>
                  <td>Up to 14 complimentary storage days during active cargo consolidation</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div class="slc-reviewer-badge">
            <div class="slc-reviewer-avatar">WO</div>
            <div>
              <strong>Supervised by Wolex (CEO, Savelanded)</strong> &bull; China Warehouse Director<br>
              <span style="font-size:0.8rem; color:#718096;">Direct oversight over Guangzhou Huayag Warehouse &amp; Yiwu intake facilities</span>
            </div>
          </div>
"""

CUSTOMS_CLEARANCE_ADDITION = """
          <!-- Official Regulatory Authority Integration -->
          <h2 id="nigeria-customs-regulatory">Official Nigerian Import Regulations: Form M, PAAR &amp; SONCAP</h2>
          <p>
            Clearing commercial cargo smoothly through Nigerian ports requires strict adherence to regulations established by the <a href="https://customs.gov.ng/" target="_blank" rel="noopener noreferrer" class="slc-ext-link">Nigeria Customs Service (NCS)</a>, the <a href="https://www.cbn.gov.ng/" target="_blank" rel="noopener noreferrer" class="slc-ext-link">Central Bank of Nigeria (CBN)</a>, and the <a href="https://son.gov.ng/" target="_blank" rel="noopener noreferrer" class="slc-ext-link">Standards Organisation of Nigeria (SON)</a>.
          </p>
          <p>
            Whether importing full containers (FCL) requiring individual statutory documentation or utilizing our consolidated groupage clearance, understanding these instruments protects your trade legality.
          </p>

          <div class="slc-comparison-table-wrapper">
            <table class="slc-comparison-table">
              <thead>
                <tr>
                  <th>Regulatory Document</th>
                  <th>Issuing / Regulating Body</th>
                  <th>Core Purpose in Import Clearance</th>
                  <th>Mandatory For</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Form M</strong></td>
                  <td>Central Bank of Nigeria (CBN) &amp; Authorized Dealer Banks via Nigeria Single Window Trade Portal</td>
                  <td>Statutory registration of intent to import goods into Nigeria. Mandatory for commercial foreign exchange allocation and PAAR generation.</td>
                  <td>Commercial FCL container sea shipments and high-value formal air cargo.</td>
                </tr>
                <tr>
                  <td><strong>PAAR (Pre-Arrival Assessment Report)</strong></td>
                  <td>Nigeria Customs Service (NCS) Ruling Center</td>
                  <td>Electronic assessment of tariff classification, customs value, and duty calculation before cargo discharges at Nigerian ports.</td>
                  <td>Required to calculate statutory import duty, VAT, and Port Development levies.</td>
                </tr>
                <tr>
                  <td><strong>SONCAP Certificate</strong></td>
                  <td>Standards Organisation of Nigeria (SON)</td>
                  <td>Conformity assessment verifying that imported industrial and consumer products meet Nigerian Industrial Standards (NIS).</td>
                  <td>Regulated manufactured products, electrical appliances, auto parts, building materials.</td>
                </tr>
                <tr>
                  <td><strong>NAFDAC Permit</strong></td>
                  <td>National Agency for Food and Drug Administration and Control</td>
                  <td>Import authorization for chemicals, food substances, cosmetics, medical devices, and packaged water.</td>
                  <td>Cosmetics, chemicals, pharmaceuticals, packaged consumables.</td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- HS Code Classification & Duty Calculation -->
          <h2 id="hs-code-duty-calculation">Harmonized System (HS) Codes &amp; Duty Calculation Structure</h2>
          <p>
            Every product entering Nigeria must be accurately classified under the ECOWAS Common External Tariff (CET) using 10-digit Harmonized System (HS) codes. Misclassifying an HS Code to evade duty is considered false declaration under the Nigeria Customs Service Act and carries severe penalties, seizure, and demurrage.
          </p>
          <div class="slc-definition-box">
            <div class="slc-definition-term">Standard Nigeria Customs Duty Structure (CET)</div>
            <p class="slc-definition-desc">
              <strong>Total Payable Duty = Import Duty (0%, 5%, 10%, or 20% of CIF value) + 7.5% VAT + 7% Port Surcharge + 0.5% Comprehensive Import Supervision Scheme (CISS) + 0.5% ECOWAS Trade Liberalization Scheme (ETLS).</strong><br>
              <em>Savelanded assists clients with pre-classification audits to ensure full compliance while legitimately optimizing duty liability.</em>
            </p>
          </div>

          <!-- Common Clearance Blunders to Avoid -->
          <h2 id="clearance-mistakes">Critical Customs Mistakes That Lead to Port Demurrage</h2>
          <ul class="slc-checklist">
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">&times;</span>
              <div>
                <strong>Discrepancies Between Invoice &amp; Physical Cargo:</strong> If the packing list states 500 cartons of hardware but the physical container holds 450 cartons of hardware and 50 cartons of unlisted electronics, the container is immediately red-flagged for 100% manual examination.
              </div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">&times;</span>
              <div>
                <strong>Delayed Form M and PAAR Processing:</strong> Initiating Form M after the ship has already departed China leads to cargo arriving at Lagos ports before PAAR is issued, racking up exorbitant terminal demurrage and shipping line detention charges.
              </div>
            </li>
            <li class="slc-checklist__item">
              <span class="slc-checklist__icon">&times;</span>
              <div>
                <strong>Importing Items on the Absolute Import Prohibition List:</strong> Nigeria maintains strict prohibitions on certain commodities to encourage local production (e.g., certain bagged mineral waters, second-hand clothing, select pharmaceutical categories). Check with Savelanded before committing capital.
              </div>
            </li>
          </ul>

          <div class="slc-reviewer-badge">
            <div class="slc-reviewer-avatar">WO</div>
            <div>
              <strong>Verified by Savelanded Regulatory Affairs Desk</strong> &bull; Licensed Clearing &amp; Forwarding Management<br>
              <span style="font-size:0.8rem; color:#718096;">Accredited operations at Apapa Port, Tin Can Island, &amp; Lagos Airport Cargo Terminals</span>
            </div>
          </div>
"""

IMPORT_EXPORT_ADDITION = """
          <!-- Complete Landed Cost Architecture -->
          <h2 id="landed-cost-architecture">Understanding Total Landed Cost: The Importer's Profitability Formula</h2>
          <p>
            A common failure among new Nigerian importers is calculating profit margins based solely on the supplier's ex-factory quotation. True business profitability depends on calculating your <strong>Total Landed Cost</strong> per unit.
          </p>

          <div class="slc-comparison-table-wrapper">
            <table class="slc-comparison-table">
              <thead>
                <tr>
                  <th>Cost Element</th>
                  <th>Description</th>
                  <th>How to Calculate &amp; Control</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>1. Ex-Factory Price (EXW)</strong></td>
                  <td>The unit manufacturing price charged by the Chinese factory.</td>
                  <td>Negotiate tiered volume discounts or purchase on 1688 via Savelanded to avoid middleman markups.</td>
                </tr>
                <tr>
                  <td><strong>2. China Domestic Logistics</strong></td>
                  <td>Courier or truck transportation from factory to our Guangzhou/Yiwu warehouse.</td>
                  <td>Consolidate orders from multiple vendors at one hub to eliminate redundant courier drops.</td>
                </tr>
                <tr>
                  <td><strong>3. International Freight (Air / Sea)</strong></td>
                  <td>Cross-border carriage from China airport or seaport to Lagos.</td>
                  <td>Select Sea Freight (LCL/FCL) for high volume and non-urgent inventory to minimize cost per kg/CBM.</td>
                </tr>
                <tr>
                  <td><strong>4. Terminal Handling &amp; Customs Duty</strong></td>
                  <td>Port levies, NCS import duty, PAAR/Form M statutory charges, and agency clearing.</td>
                  <td>Ensure accurate HS classification; choose Savelanded all-inclusive groupage to eliminate hidden port fees.</td>
                </tr>
                <tr>
                  <td><strong>5. Nigerian Last-Mile Dispatch</strong></td>
                  <td>Trucking from Lagos port or Trade Fair depot to your retail warehouse or retail shop.</td>
                  <td>Coordinate direct interstate haulage via Savelanded logistics network across all 36 states.</td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- Incoterms Simplified for Nigerian Traders -->
          <h2 id="incoterms-guide">Commercial Incoterms 2020: EXW, FOB &amp; CIF Explained</h2>
          <p>
            Published by the <a href="https://iccwbo.org/" target="_blank" rel="noopener noreferrer" class="slc-ext-link">International Chamber of Commerce (ICC)</a>, Incoterms define the exact point where risk and freight cost transfer from seller to buyer:
          </p>
          <div class="slc-step-grid">
            <div class="slc-step-card">
              <span class="slc-tag slc-tag--official">Best with Savelanded</span>
              <h3 class="slc-step-title">EXW (Ex-Works)</h3>
              <p class="slc-step-text">
                The seller makes goods available at their factory floor. Savelanded handles domestic collection in China, warehouse receiving, export customs, and onward transit. Offers maximum cost control.
              </p>
            </div>
            <div class="slc-step-card">
              <span class="slc-tag">Common for Sea FCL</span>
              <h3 class="slc-step-title">FOB (Free on Board)</h3>
              <p class="slc-step-text">
                The Chinese factory pays domestic transport and export port clearance, delivering goods loaded on the vessel at Ningbo or Guangzhou. Savelanded manages ocean freight and Lagos clearing.
              </p>
            </div>
            <div class="slc-step-card">
              <span class="slc-tag slc-tag--warning">Higher Hidden Costs</span>
              <h3 class="slc-step-title">CIF (Cost, Insurance &amp; Freight)</h3>
              <p class="slc-step-text">
                The seller arranges ocean freight to Lagos port. While convenient, foreign forwarders often impose exorbitant destination terminal handling fees upon arrival in Nigeria.
              </p>
            </div>
          </div>

          <div class="slc-reviewer-badge">
            <div class="slc-reviewer-avatar">WO</div>
            <div>
              <strong>Trade Advisory by Wolex (CEO, Savelanded)</strong> &bull; International Trade Specialist<br>
              <span style="font-size:0.8rem; color:#718096;">Advising commercial importers across Lagos, Kano, Onitsha, and Abuja</span>
            </div>
          </div>
"""

DOOR_TO_DOOR_ADDITION = """
          <!-- Door-to-Door Workflow & Nationwide Coverage -->
          <h2 id="door-to-door-nigeria-coverage">Nationwide Cargo Delivery Across All 36 Nigerian States</h2>
          <p>
            While our corporate reception and major distribution hub is situated at <strong>Savelanded Plaza, Trade Fair Complex, Lagos</strong>, our door-to-door logistics service covers every state in Nigeria. Once your cargo completes port clearing, you can either pick up freely at Trade Fair or have our transport division dispatch directly to your warehouse, store, or residence.
          </p>

          <div class="slc-comparison-table-wrapper">
            <table class="slc-comparison-table">
              <thead>
                <tr>
                  <th>Destination Zone</th>
                  <th>Key Delivery Cities</th>
                  <th>Typical Transit After Lagos Clearance</th>
                  <th>Handling &amp; Security Protocol</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Lagos Metropolis</strong></td>
                  <td>Ikeja, Alaba International, Trade Fair, Idumota, Lekki, Victoria Island, Yaba</td>
                  <td>Same-day or next-day direct delivery</td>
                  <td>Dedicated city delivery vans &amp; light trucks with verified driver manifest.</td>
                </tr>
                <tr>
                  <td><strong>South-West States</strong></td>
                  <td>Ibadan (Oyo), Abeokuta (Ogun), Akure (Ondo), Osogbo (Osun)</td>
                  <td>24 to 48 hours</td>
                  <td>Interstate bonded logistics vehicles with cargo-tracking updates.</td>
                </tr>
                <tr>
                  <td><strong>South-East Commercial Hubs</strong></td>
                  <td>Onitsha, Aba, Nnewi, Enugu, Owerri</td>
                  <td>2 to 3 working days</td>
                  <td>Heavy-duty haulage trucks serving major wholesale markets with armed security escorts for high-value container cargo.</td>
                </tr>
                <tr>
                  <td><strong>Northern Commercial Centers</strong></td>
                  <td>Abuja (FCT), Kano, Kaduna, Jos, Sokoto</td>
                  <td>3 to 5 working days</td>
                  <td>Direct highway transit to regional distribution depots in Kano and Abuja.</td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- All-Inclusive Pricing Structure & Service Exclusions -->
          <h2 id="door-to-door-pricing-exclusions">All-Inclusive Cargo Rates: What Is Included &amp; What Is Excluded</h2>
          <p>
            Our all-inclusive door-to-door pricing provides peace of mind by wrapping multiple fragmented logistics fees into one predictable rate per kilogram or CBM:
          </p>
          <div class="slc-step-grid">
            <div class="slc-step-card">
              <span class="slc-tag slc-tag--official">Included in Rate</span>
              <h3 class="slc-step-title">What Savelanded Covers</h3>
              <p class="slc-step-text">
                &bull; China warehouse receiving &amp; weight confirmation<br>
                &bull; International air or sea freight to Nigeria<br>
                &bull; Terminal handling charges (THC) at Lagos ports<br>
                &bull; Complete customs clearance &amp; documentation release<br>
                &bull; Secure staging at our Trade Fair Lagos distribution center
              </p>
            </div>
            <div class="slc-step-card">
              <span class="slc-tag slc-tag--warning">Applicable Surcharges</span>
              <h3 class="slc-step-title">Service Exclusions / Conditional Fees</h3>
              <p class="slc-step-text">
                &bull; Special dangerous goods (DG) lithium battery flight surcharges<br>
                &bull; Specialized wooden crating for delicate glass/ceramics in China<br>
                &bull; Interstate road haulage fees from Lagos to upcountry states<br>
                &bull; Demurrage caused by client delays in paying freight balances
              </p>
            </div>
          </div>

          <div class="slc-reviewer-badge">
            <div class="slc-reviewer-avatar">WO</div>
            <div>
              <strong>Supervised by Wolex (CEO, Savelanded)</strong> &bull; Door-to-Door Delivery Operations<br>
              <span style="font-size:0.8rem; color:#718096;">Headquartered at Trade Fair Complex, Lagos with nationwide haulage network</span>
            </div>
          </div>
"""

SHIPPING_ADDITION = """
          <!-- Master Mode Decision Matrix -->
          <h2 id="master-shipping-matrix">Master Shipping Decision Matrix: Air vs. Sea Freight</h2>
          <p>
            Choosing the most cost-effective and dependable transport mode depends on your inventory volume, cargo weight, commercial urgency, and cash-flow cycle.
          </p>

          <div class="slc-comparison-table-wrapper">
            <table class="slc-comparison-table">
              <thead>
                <tr>
                  <th>Evaluation Metric</th>
                  <th>Express Air Cargo</th>
                  <th>Standard Air Cargo</th>
                  <th>Sea Freight LCL (Groupage)</th>
                  <th>Sea Freight FCL (Full Container)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Transit Time</strong></td>
                  <td>3 to 5 working days</td>
                  <td>5 to 8 working days</td>
                  <td>35 to 45 days</td>
                  <td>35 to 45 days</td>
                </tr>
                <tr>
                  <td><strong>Billing Metric</strong></td>
                  <td>Per Kg (Actual vs Dimensional)</td>
                  <td>Per Kg (Actual vs Dimensional)</td>
                  <td>Per Cubic Meter (CBM)</td>
                  <td>Flat rate per 20ft / 40ft box</td>
                </tr>
                <tr>
                  <td><strong>Cost Profile</strong></td>
                  <td>High cost / kg</td>
                  <td>Moderate cost / kg</td>
                  <td>Low cost / unit</td>
                  <td>Lowest cost per CBM/unit</td>
                </tr>
                <tr>
                  <td><strong>Ideal Cargo</strong></td>
                  <td>Urgent samples, high-end electronics, emergency spare parts</td>
                  <td>Apparel, phones, accessories, urgent retail restock</td>
                  <td>1 to 15 CBM of general merchandise, cosmetics, small machinery</td>
                  <td>Heavy industrial equipment, building materials, full commercial stock</td>
                </tr>
                <tr>
                  <td><strong>Risk of Port Congestion</strong></td>
                  <td>Very Low (Airport clearing)</td>
                  <td>Very Low (Airport clearing)</td>
                  <td>Moderate (Terminal clearing)</td>
                  <td>Subject to port berthing windows</td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- Practical Shipping Calculation Walkthrough -->
          <h2 id="practical-calculation-walkthrough">Practical Freight Cost Calculation Walkthrough</h2>
          <p>
            Let us walk through a practical scenario: A Lagos boutique owner orders <strong>10 cartons of fashion apparel</strong> from a supplier in Guangzhou.
          </p>
          <div class="slc-callout">
            <strong>Consignment Details:</strong><br>
            &bull; Number of Cartons: 10<br>
            &bull; Dimensions per carton: 60cm &times; 50cm &times; 40cm<br>
            &bull; Scale weight per carton: 15 kg (Total gross weight = 150 kg)<br><br>
            <strong>Calculation 1: Air Freight Option</strong><br>
            Total volume = 10 &times; (60 &times; 50 &times; 40) = 1,200,000 cm&sup3;.<br>
            Air Volumetric Weight = 1,200,000 &divide; 6,000 = <strong>200 kg</strong>.<br>
            Because the volumetric weight (200 kg) is higher than the scale weight (150 kg), airlines will bill on <strong>200 kg chargeable weight</strong>.<br><br>
            <strong>Calculation 2: Sea Freight LCL Option</strong><br>
            Total volume in CBM = 10 &times; (0.60m &times; 0.50m &times; 0.40m) = <strong>1.20 CBM</strong>.<br>
            Billed strictly on 1.2 CBM ocean freight.<br><br>
            <em>Conclusion: If the merchant needs goods in 1 week for a festive launch, Air Freight (200 kg) is selected. If planning inventory for the next quarter, Sea Freight (1.2 CBM) costs approximately 75% less.</em>
          </div>

          <div class="slc-reviewer-badge">
            <div class="slc-reviewer-avatar">WO</div>
            <div>
              <strong>Guidance by Savelanded Master Logistics Team</strong> &bull; China–Nigeria Trade Authority<br>
              <span style="font-size:0.8rem; color:#718096;">Providing verified logistics data &bull; Active offices in Yiwu, Guangzhou, and Lagos</span>
            </div>
          </div>
"""

SERVICES_DIRECTORY_ADDITION = """
          <!-- How Customers Choose Between Services -->
          <h2 id="service-selection-guide" style="font-family:var(--slc-font-head); font-size:1.8rem; font-weight:800; color:var(--slc-black); margin-top:40px; margin-bottom:16px;">
            How to Choose the Right Service for Your Business
          </h2>
          <p style="color:var(--slc-gray-700); font-size:1.05rem; line-height:1.7; margin-bottom:24px;">
            Every enterprise has unique commercial priorities. Use this quick decision guide to match your operational stage with Savelanded's tailored solutions:
          </p>

          <div class="slc-comparison-table-wrapper">
            <table class="slc-comparison-table">
              <thead>
                <tr>
                  <th>Your Business Situation</th>
                  <th>Recommended Service</th>
                  <th>Key Benefits</th>
                  <th>Next Step</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Looking for verified factories or new products in China</strong></td>
                  <td><a href="product-sourcing.html"><strong>Product Sourcing &amp; Vetting</strong></a></td>
                  <td>On-site factory audits in Yiwu and Guangzhou, sample verification, counterfeit prevention</td>
                  <td><a href="product-sourcing.html">Explore Sourcing</a></td>
                </tr>
                <tr>
                  <td><strong>Found goods on 1688 or Taobao but cannot pay RMB</strong></td>
                  <td><a href="procurement.html"><strong>Purchasing &amp; Procurement</strong></a></td>
                  <td>Safe RMB supplier settlements, official invoice checks, verified escrow payments</td>
                  <td><a href="procurement.html">Explore Procurement</a></td>
                </tr>
                <tr>
                  <td><strong>Buying from 3+ suppliers and want to avoid high shipping costs</strong></td>
                  <td><a href="warehousing.html"><strong>Warehousing &amp; Consolidation</strong></a></td>
                  <td>Free 14-day storage, carton measurement, repacking into one unified shipment</td>
                  <td><a href="warehousing.html">Explore Warehousing</a></td>
                </tr>
                <tr>
                  <td><strong>Need goods urgently in Lagos within 5 to 8 days</strong></td>
                  <td><a href="air-freight.html"><strong>Air Freight from China</strong></a></td>
                  <td>Scheduled flights CAN/SZX to LOS, airport clearing, express delivery options</td>
                  <td><a href="air-freight.html">Explore Air Freight</a></td>
                </tr>
                <tr>
                  <td><strong>Shipping large volume, heavy stock, or full containers (CBM)</strong></td>
                  <td><a href="sea-freight.html"><strong>Sea Freight (FCL / LCL)</strong></a></td>
                  <td>Lowest cost per unit, 20ft/40ft containers, Ningbo to Apapa and Tin Can ports</td>
                  <td><a href="sea-freight.html">Explore Sea Freight</a></td>
                </tr>
                <tr>
                  <td><strong>Want complete end-to-end delivery without customs hassle</strong></td>
                  <td><a href="door-to-door.html"><strong>Door-to-Door Delivery</strong></a></td>
                  <td>All-inclusive freight, terminal clearance, nationwide delivery across Nigeria</td>
                  <td><a href="door-to-door.html">Explore Door-to-Door</a></td>
                </tr>
              </tbody>
            </table>
          </div>
"""

ABOUT_PAGE_ADDITION = """
          <!-- Operational Ground Capabilities -->
          <h2 id="operational-capabilities">Our Ground Infrastructure &amp; Operational Capabilities</h2>
          <p>
            Unlike digital middlemen who merely broker freight orders online, Savelanded operates physical facilities with bilingual staff in both China and Nigeria. This boots-on-the-ground presence ensures your cargo is inspected, protected, and accounted for at every transfer point.
          </p>

          <div class="slc-step-grid">
            <div class="slc-step-card">
              <span class="slc-tag slc-tag--official">China Head Office</span>
              <h3 class="slc-step-title">Yiwu Trading &amp; Procurement Hub</h3>
              <p class="slc-step-text">
                Located at 16, 2nd Street, Longgang Road, Yiwu City, Zhejiang Province. Immediate access to the world-renowned Yiwu International Trade City (Futian Market). Specializes in supplier vetting, market procurement, and sample inspection.
              </p>
            </div>
            <div class="slc-step-card">
              <span class="slc-tag slc-tag--official">China Logistics Hub</span>
              <h3 class="slc-step-title">Guangzhou Consolidation Warehouse</h3>
              <p class="slc-step-text">
                Located at Room 103, Warehouse 4, Huayag Warehouse, No. 498 Qinglong Road, Shijing Street, Baiyun District, Guangzhou. Dedicated to cargo intake, CBM measurement, repacking, and direct airport/port dispatch.
              </p>
            </div>
            <div class="slc-step-card">
              <span class="slc-tag slc-tag--official">Nigeria Distribution Hub</span>
              <h3 class="slc-step-title">Lagos Trade Fair Center</h3>
              <p class="slc-step-text">
                Located at Apt Market Exp Blk-PB7, Savelanded Plaza, No. 7, 10, 12 and 14, Trade Fair Complex, Lagos. Central corporate depot where clients inspect, verify, and collect their cleared goods or arrange nationwide dispatch.
              </p>
            </div>
          </div>

          <!-- Genuine Company Leadership -->
          <h2 id="leadership-team">Executive Leadership Dedicated to Commercial Integrity</h2>
          <p>
            Savelanded was founded on the principle that international trade between China and Nigeria must be transparent, predictable, and devoid of hidden surcharges or cargo abandonment risks.
          </p>
          <div class="slc-comparison-table-wrapper">
            <table class="slc-comparison-table">
              <thead>
                <tr>
                  <th>Executive Leader</th>
                  <th>Corporate Role</th>
                  <th>Primary Operational Jurisdiction</th>
                  <th>Direct Contact</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Wolex</strong></td>
                  <td>Chief Executive Officer &amp; Founder</td>
                  <td>Strategic trade corridors, air/sea carrier allocations, corporate logistics oversight</td>
                  <td><a href="tel:+8618248547224">+86 182 4854 7224</a></td>
                </tr>
                <tr>
                  <td><strong>Star</strong></td>
                  <td>Head of China Operations &amp; Sourcing</td>
                  <td>Yiwu &amp; Guangzhou warehouse management, factory verification, 1688 procurement</td>
                  <td><a href="tel:+8615757991458">+86 157 5799 1458</a></td>
                </tr>
              </tbody>
            </table>
          </div>
"""

CONTACT_PAGE_ADDITION = """
          <!-- Customer Support & Operational Hours -->
          <div style="margin-top:40px; padding:28px; background:#f7fafc; border-radius:12px; border:1px solid #e2e8f0;">
            <h2 style="font-family:var(--slc-font-head); font-size:1.4rem; font-weight:700; color:var(--slc-burgundy); margin-bottom:12px;">
              Operational Hours &amp; Cargo Receiving Schedules
            </h2>
            <div class="slc-step-grid" style="margin:16px 0 0;">
              <div>
                <strong>China Facilities (Yiwu &amp; Guangzhou)</strong><br>
                <span style="font-size:0.9rem; color:#4a5568;">
                  Monday &ndash; Saturday: 9:00 AM &ndash; 6:00 PM (CST / UTC+8)<br>
                  Sunday: Receiving only via advance booking for factory couriers<br>
                  Hotline / WhatsApp: <a href="tel:+8618248547224">+86 182 4854 7224</a>
                </span>
              </div>
              <div>
                <strong>Nigeria Hub (Trade Fair Complex, Lagos)</strong><br>
                <span style="font-size:0.9rem; color:#4a5568;">
                  Monday &ndash; Friday: 8:30 AM &ndash; 5:30 PM (WAT / UTC+1)<br>
                  Saturday: 9:00 AM &ndash; 2:00 PM (Cargo collections)<br>
                  Sunday: Closed (Security team on duty)
                </span>
              </div>
            </div>
            <div style="margin-top:20px; font-size:0.9rem; color:#718096; border-top:1px solid #e2e8f0; padding-top:12px;">
              Need an instant formal estimate before visiting our offices? <a href="quote.html" style="color:var(--slc-gold); font-weight:700;">Submit an online quotation request &rarr;</a>
            </div>
          </div>
"""

QUOTE_PAGE_ADDITION = """
          <!-- What Customers Need Before Requesting a Quote -->
          <div style="margin-bottom:32px; padding:24px; background:#fdfbf7; border-left:4px solid var(--slc-gold); border-radius:0 8px 8px 0;">
            <h2 style="font-family:var(--slc-font-head); font-size:1.25rem; font-weight:700; color:var(--slc-burgundy); margin-bottom:10px;">
              What You Need Before Requesting a Freight or Sourcing Quote
            </h2>
            <p style="font-size:0.92rem; color:#4a5568; line-height:1.6; margin-bottom:14px;">
              To ensure our operations team can provide you with a fast, 100% accurate quotation with zero guesswork, please have the following shipment information ready:
            </p>
            <div class="slc-step-grid" style="margin:0;">
              <div style="font-size:0.88rem; color:#2d3748;">
                &bull; <strong>Product Nature:</strong> Exact description (e.g. shoes, phone chargers, machine parts)<br>
                &bull; <strong>Supplier Location:</strong> City where goods are produced (e.g. Yiwu, Guangzhou, Shenzhen)<br>
                &bull; <strong>Packaging Specs:</strong> Number of cartons, dimensions per carton (L &times; W &times; H cm)
              </div>
              <div style="font-size:0.88rem; color:#2d3748;">
                &bull; <strong>Gross Weight:</strong> Total weight in kg across all cartons<br>
                &bull; <strong>Battery / Liquid Status:</strong> Disclose whether goods contain lithium batteries or liquids<br>
                &bull; <strong>Destination City:</strong> Lagos Trade Fair pickup or nationwide delivery address
              </div>
            </div>
          </div>
"""

print("Defined all expansion content modules.")

