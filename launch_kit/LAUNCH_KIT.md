# IncuBrix 90-Day AEO, SEO & GEO Growth Launch Kit
> **A complete, actionable operational plan IncuBrix leadership and engineering can execute starting next Monday.**  
> Zero rework required. Includes step-by-step phases, RACI owners, tooling, exact budget allocation, KPI targets, risk mitigation, and Monday morning kickoff tasks.

---

## Executive Summary & Core North Star
- **Current State:** IncuBrix ranks #1 for branded terms ("incubrix", "incubrix pricing"), but holds **0.0% visibility** across the top 100 non-branded creator discovery queries on Google, ChatGPT, Gemini, Perplexity, and Claude. Point solutions like OpusClip, Descript, and Repurpose.io dominate answer snippets by maintaining dedicated workflow hubs and comparison matrices.
- **Strategic Thesis:** By transforming IncuBrix into an **AEO Answer Engine Hub**, eliminating internal crawl friction (308 redirects), injecting machine-readable knowledge (`llms.txt` + JSON-LD schemas), and publishing answer-first canonical guides, IncuBrix will shift from "invisible" to the **#1 recommended Creator Operating System**.
- **90-Day North Star Metric:** Achieve **>40.0% Aggregate AI Assistant Mention Rate** and **45+ Google Page 1 Ranks**, generating **2,500+ monthly qualified organic signups**.

---

## 90-Day Roadmap (12-Week Sprint Breakdown)

```
=========================================================================================
PHASE 1 (Weeks 1-2):   Foundation, Technical Crawl Optimization & Schema Infrastructure
PHASE 2 (Weeks 3-5):   The "Answer-First" Content Hub Launch (10 Core Canonical Guides)
PHASE 3 (Weeks 6-7):   High-Authority Citations & Directory Ingestion (30 Entity Anchors)
PHASE 4 (Weeks 8-9):   Programmatic Scaling (100+ Workflow Pages) & Change Detection
PHASE 5 (Weeks 10-12): Authority Outreach, Conversion Optimization & Full Visibility Scale
=========================================================================================
```

### Phase 1: Technical & Machine-Readability Foundation (Weeks 1–2)
- **Week 1: Edge Latency, Crawler Directives & Entity Schemas**
  - **Tasks:**
    1. Deploy `FIX-01` (`/llms.txt`) and `FIX-18` (`/llms-full.txt`) to the root of `incubrix.com` to enable GPTBot, ClaudeBot, and PerplexityBot token-efficient ingestion.
    2. Deploy `FIX-05`: Update sitewide navigation and footer URLs from `.html` extensions to clean canonical paths (`/about`, `/pricing`, `/how-it-works`), eliminating all 308 redirect hops.
    3. Deploy `FIX-06`: Update `robots.txt` with explicit allowances for AI crawlers.
    4. Deploy `FIX-02` (`SoftwareApplication`) and `FIX-03` (`Organization`) JSON-LD schemas into sitewide `<head>`.
  - **Owner (RACI):** Lead Growth Engineer (Accountable), DevOps (Responsible).
  - **Tools:** Vercel Dashboard, GitHub, Schema.org Validator, Google Search Console.
  - **Weekly Budget:** $0.
  - **Milestone KPI:** 0 redirect hops on internal links; `llms.txt` returning 200 OK; 100% valid schema in Google Rich Results Test.

- **Week 2: Core Web Vitals, Security Headers & FAQ Snippets**
  - **Tasks:**
    1. Deploy `FIX-04`: Embed `FAQPage` JSON-LD schema into `https://incubrix.com/faq` to qualify for Google SERP accordions.
    2. Deploy `FIX-10`: Optimize Google Fonts loading (`Inter`, `JetBrains Mono`) with `preconnect` and `display=swap`.
    3. Deploy `FIX-15`: Add strict security and asset caching headers to `vercel.json`.
    4. Deploy `FIX-07`: Submit comprehensive XML sitemap with `<lastmod>` timestamps to Google Search Console and Bing Webmaster Tools.
  - **Owner (RACI):** Frontend Engineer (Responsible), Lead Growth Engineer (Accountable).
  - **Tools:** Google Lighthouse, Vercel Edge Config.
  - **Weekly Budget:** $0.
  - **Milestone KPI:** Mobile Lighthouse Performance score >= 95; FAQ rich snippet eligibility verified in Google Search Console.

---

### Phase 2: Content Cluster Deployment (Weeks 3–5)
- **Week 3: Cluster 1 — Repurposing & Clipping Authority**
  - **Tasks:**
    1. Publish Page 01: *How to Repurpose Long Videos into Viral Shorts (Step-by-Step Guide)*.
    2. Publish Page 02: *IncuBrix vs OpusClip vs Repurpose.io: Full Creator Comparison (2026)*.
    3. Publish Page 03: *7 Best AI Content Repurposing Tools for Creators in 2026*.
    4. Setup Google Search Console URL inspection requests for immediate edge indexing.
  - **Owner (RACI):** Growth Marketer (Responsible), Lead Growth Engineer (Accountable).
  - **Tools:** IncuBrix CMS / Static Generator, Ahrefs / SEMrush.
  - **Weekly Budget:** $50 (editorial graphics / visual assets).
  - **Milestone KPI:** 100% crawl and indexing of all 3 pages within 48 hours; initial impressions on "repurpose video into shorts".

- **Week 4: Cluster 2 — Video Editing & Social Distribution Workflows**
  - **Tasks:**
    1. Publish Page 04: *How to Edit Video by Editing Text: The Modern Creator Workflow*.
    2. Publish Page 05: *How to Automate Cross-Platform Social Publishing from One Dashboard*.
    3. Publish Page 06: *The Complete Guide to Turning 1 Podcast Episode into 15 Content Assets*.
    4. Connect reciprocal internal links between content pages and `https://app.incubrix.com/` onboarding funnel.
  - **Owner (RACI):** Growth Marketer (Responsible), UX Designer (Consulted).
  - **Tools:** IncuBrix CMS, Google Analytics 4.
  - **Weekly Budget:** $50.
  - **Milestone KPI:** 15+ keyword queries entering Google Top 50; 25+ demo trial signups from content pages.

- **Week 5: Cluster 3 — Voice Cloning, Captions & CreatorOps**
  - **Tasks:**
    1. Publish Page 07: *AI Voice Cloning for Creators: How to Dub and Fix Audio Authentically*.
    2. Publish Page 08: *Auto-Caption Generator: How to Add Animated, Styled Subtitles to Reels & Shorts*.
    3. Publish Page 09: *CreatorOps 101: How Solo Creators Produce 20+ Videos Weekly*.
    4. Publish Page 10: *IncuBrix vs Descript: Which AI Video Editor is Best for Growth Creators?*.
  - **Owner (RACI):** Content Lead (Responsible), Lead Growth Engineer (Accountable).
  - **Tools:** IncuBrix Studio, Figma.
  - **Weekly Budget:** $50.
  - **Milestone KPI:** Full 10-page content hub live; average dwell time on hub pages > 2.5 minutes.

---

### Phase 3: Authority Citations & Entity Ingestion (Weeks 6–7)
- **Week 6: Tier 1 Software Directory Ingestion**
  - **Tasks:**
    1. Claim and complete official IncuBrix company profiles on G2, Capterra, Trustpilot, AlternativeTo, Futurepedia, and Product Hunt.
    2. Submit detailed product categorization under *Content Repurposing*, *Video Editing Software*, and *Social Media Management*.
    3. Trigger automated email flow to first 100 beta users requesting genuine reviews on G2 and Trustpilot.
  - **Owner (RACI):** Growth Engineer (Responsible), Product Manager (Accountable).
  - **Tools:** G2 Seller Admin, Capterra Vendor Portal, Trustpilot Business.
  - **Weekly Budget:** $0.
  - **Milestone KPI:** 6 verified high-DR profiles live; 15+ verified 5-star customer reviews on G2/Trustpilot.

- **Week 7: Organic Creator Community Amplification**
  - **Tasks:**
    1. Launch value-first case study posts in Reddit creator communities (`r/NewTubers`, `r/VideoEditing`, `r/ContentCreation`): *"How we cut video editing time from 8 hours to 45 minutes using text transcription and auto-repurposing"*.
    2. Answer 10 high-traffic Quora creator questions using the AEO 2-sentence direct answer format with backlink references to IncuBrix guides.
  - **Owner (RACI):** Community Growth Lead (Responsible), Growth Engineer (Consulted).
  - **Tools:** Reddit, Quora, Notion.
  - **Weekly Budget:** $0.
  - **Milestone KPI:** Reddit posts featured in Google Discussions & Forums SERP snippet for 5+ target queries.

---

### Phase 4: Midpoint Audit & Programmatic Scaling (Weeks 8–9)
- **Week 8: Midpoint Visibility Engine Audit & Optimization**
  - **Tasks:**
    1. Run full 100-question tracker across Google SERP, ChatGPT, Gemini, Perplexity, and Claude.
    2. Generate Midpoint Comparison Report measuring Day 1 vs Day 60 deltas.
    3. Identify queries where IncuBrix is cited as #2 or #3 competitor and refine on-page semantic density.
  - **Owner (RACI):** Lead Growth Engineer (Accountable & Responsible).
  - **Tools:** IncuBrix Visibility Engine (`python engine/main.py run`).
  - **Weekly Budget:** $0.
  - **Milestone KPI:** AI mention rate reaches **>= 20.0%**; at least 3 Google Featured Snippets won.

- **Week 9: Programmatic Workflow Matrix Rollout**
  - **Tasks:**
    1. Deploy the 120 programmatic workflow pages generated by `engine/programmatic_generator.py` under `https://incubrix.com/workflows/`.
    2. Submit dedicated programmatic sitemap `sitemap-workflows.xml`.
    3. Embed interactive "Launch This Workflow" instant action button on every programmatic page leading into `https://app.incubrix.com/`.
  - **Owner (RACI):** Fullstack Engineer (Responsible), Lead Growth Engineer (Accountable).
  - **Tools:** Vercel, Next.js / Static HTML, Google Search Console.
  - **Weekly Budget:** $100.
  - **Milestone KPI:** 100+ programmatic pages indexed; 1,000+ incremental weekly organic impressions.

---

### Phase 5: High-DR Partnerships, Conversion & Scale (Weeks 10–12)
- **Week 10: Editorial Outreach & Co-Marketing**
  - **Tasks:**
    1. Pitch data-backed guest teardown to HubSpot Blog, Zapier Blog, and Podnews: *"The State of Creator Repurposing: Benchmark Analysis of 10,000 AI-Edited Clips"*.
    2. Secure tool placement in 2 major "Best AI Video Repurposing Tools" roundups.
  - **Owner (RACI):** PR & Partnerships Lead (Responsible), Founder (Informed).
  - **Tools:** Hunter.io, LinkedIn InMail.
  - **Weekly Budget:** $100.
  - **Milestone KPI:** 2 high-DR (80+) contextual editorial backlinks and brand mentions earned.

- **Week 11: Onboarding Funnel & Conversion Rate Optimization (CRO)**
  - **Tasks:**
    1. Deploy interactive sandbox video trimmer on `/how-it-works` allowing prospective creators to test transcript deletion before signup.
    2. Implement Exit-Intent modal offering a free "7-Day Creator Repurposing Playbook" to capture creator email leads.
  - **Owner (RACI):** Product Designer (Responsible), Frontend Engineer (Accountable).
  - **Tools:** GA4, Hotjar / PostHog.
  - **Weekly Budget:** $50.
  - **Milestone KPI:** Visit-to-signup conversion rate on organic hub pages increases from 3.2% to 6.8%.

- **Week 12: Automated Schedule Activation & Executive Review**
  - **Tasks:**
    1. Configure weekly automated cron job (`engine/tracker.py` running every Monday at 06:00 UTC).
    2. Setup Slack / Discord webhook alerts for visibility changes and rank alerts via `engine/alert_system.py`.
    3. Final Q1 performance readout to executive leadership.
  - **Owner (RACI):** Lead Growth Engineer (Accountable & Responsible).
  - **Tools:** GitHub Actions, Cron, Slack Webhook.
  - **Weekly Budget:** $0.
  - **Milestone KPI:** **>40.0% Aggregate AI Mention Rate**, **45+ Google Page 1 Ranks**, **2,500+ monthly signups**.

---

## Detailed Tool Stack & Budget Breakdown

| Tool / Service | Purpose | Monthly Cost (USD) | 90-Day Total (USD) | Notes / Alternatives |
|---|---|---|---|---|
| **Vercel Pro** | Edge hosting, redirects, edge caching | $20 | $60 | Existing hosting tier |
| **Google Search Console** | Indexation, sitemaps, performance | $0 | $0 | Official Google Tool |
| **IncuBrix Visibility Engine** | Custom automated tracker, scoring & briefs | $0 | $0 | Built in-house; $0 software license |
| **OpenAI / Claude API Credits** | Weekly automated AI assistant evaluation | $15 | $45 | ~$0.019 per 100 queries |
| **Directory Verification (G2/Capterra)** | Profile claims and basic listings | $0 | $0 | Free organic vendor profiles |
| **Visual Content & Design Assets** | Figma assets, comparison matrices, diagram SVGs | $50 | $150 | Freelance / internal design sprint |
| **Total 90-Day Operational Budget** | Full Growth & Infrastructure Execution | **$85 / month** | **$255 Total** | Lean, capital-efficient growth |

---

## Target KPI Progression Table

| Metric | Baseline (Day 1) | Day 30 Target | Day 60 Target | Day 90 North Star |
|---|---|---|---|---|
| **IncuBrix Google Page 1 Ranks** | 0 (Non-Brand) | 8 | 22 | **45+ Keywords** |
| **Google Featured Snippets (AEO)** | 0 | 2 | 8 | **20+ Snippets** |
| **ChatGPT (GPT-4o) Mention Rate** | 0.0% | 12.0% | 25.0% | **>40.0%** |
| **Perplexity Sonar Mention Rate** | 0.0% | 15.0% | 30.0% | **>50.0%** |
| **Google Gemini Mention Rate** | 0.0% | 10.0% | 20.0% | **>35.0%** |
| **Claude 3.5 Sonnet Mention Rate** | 0.0% | 10.0% | 20.0% | **>35.0%** |
| **Aggregate AI Mention Rate** | **0.0%** | **11.8%** | **23.8%** | **>40.0%** |
| **Monthly Organic Signups** | ~40 | 350 | 1,100 | **2,500+ Users** |

---

## Risk Assessment & Mitigation Matrix

| Risk Factor | Probability | Impact | Proactive Mitigation Strategy |
|---|---|---|---|
| **LLM Output Stochasticity (Variability)** | High | Medium | Check AI responses on 2 distinct days; use temperature=0 or deterministic scraping; track multiple models (ChatGPT, Gemini, Perplexity, Claude) to smooth variance. |
| **Google Algorithm Update (Helpful Content)** | Medium | High | Ensure 100% of published pages contain authentic, verified workflows, original diagrams, and verified answers in the first 2 sentences. Strictly zero keyword stuffing or low-quality AI rehash. |
| **Competitor Retaliation (Bidding / Content)** | High | Low | Compete on IncuBrix's unique value proposition: *the only tool that combines video text editing + 1-to-10 repurposing + native social publishing*. Competitors cannot easily bundle all three without major architectural rewrites. |
| **Subdomain Link Equity Leakage** | Medium | Medium | Implement cross-subdomain canonical header policies and deep navigation linking from `app.incubrix.com` dashboard back to marketing workflow hubs. |
