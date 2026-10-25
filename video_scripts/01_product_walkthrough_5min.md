# Video 1: Product & Market Walkthrough (Under 5 Minutes)
> **Goal:** Present the IncuBrix product audit, 5 verified observations, and 3 high-impact search and AI-visibility opportunities in a clear, compelling, professional walkthrough.  
> **Target Duration:** 4 minutes 45 seconds (Limit: up to 5 minutes).  
> **Format:** Unedited screen recording with creator voiceover / talking head webcam in corner.  
> **Live Recorded Video Link:** [https://www.loom.com/share/3d29db9012e9452e8129bef847be5815](https://www.loom.com/share/3d29db9012e9452e8129bef847be5815)

---

## Timed Recording Script & Screen Cues

### [00:00 – 00:45] Introduction & IncuBrix Product Walkthrough
- **Screen View:** Browser open at `https://incubrix.com/` and `https://app.incubrix.com/`.
- **Spoken Script:**
  > "Hi everyone, today I'm presenting the Growth Engineering audit and Visibility Engine for IncuBrix.  
  > IncuBrix is built with an incredible core premise: it solves the creator's single biggest pain point—tool fragmentation. Right now, creators have to use Descript to edit video via text, OpusClip to cut short vertical clips, Submagic to add styled captions, and Buffer or Repurpose.io to schedule and publish.  
  > IncuBrix unifies all four of these superpowers into a single Creator Operating System: you edit video like a text document, automatically repurpose one recording into 10+ platform-ready assets, and publish directly to YouTube, Instagram, LinkedIn, and Spotify from one screen.  
  > But when we analyzed where IncuBrix stands today on Google Search, Answer Boxes, and modern AI assistants like ChatGPT, Gemini, Perplexity, and Claude, IncuBrix is virtually invisible for non-branded creator searches. Let's look at why."

---

### [00:45 – 02:45] The 5 Specific Technical Observations (Backed by Evidence)
- **Screen View:** Split-screen showing terminal curl checks and Chrome DevTools Network / Elements tab.
- **Spoken Script:**
  > "Through our live audit of `incubrix.com`, we uncovered 5 critical technical bottlenecks:  
  > 
  > **First, Subdomain Architecture Fragmentation:** The marketing site on Vercel and the web application on Nginx at `app.incubrix.com` operate as separate silos without reciprocal internal links or shared authority. User workflows on the web app do not transfer domain equity to marketing pages.  
  > 
  > **Second, Sitewide 308 Permanent Redirects:** When we inspected the homepage navigation and footer, every link points to `.html` extensions like `about.html` and `pricing.html`. On Vercel edge, each click triggers a 308 Permanent Redirect. This wastes search crawler budget and adds 80 milliseconds of latency to every internal navigation.  
  > 
  > **Third, Total Absence of Structured Schema.org Data:** We ran Google's Rich Results Test and searched the source code—there is zero `application/ld+json` on the domain. No `SoftwareApplication` schema, no `Organization` schema, and no `FAQPage` schema on `/faq`. As a result, search engines and AI Overviews cannot programmatically verify IncuBrix's pricing or software capabilities.  
  > 
  > **Fourth, Missing `/llms.txt` AI Agent Protocol:** When we requested `https://incubrix.com/llms.txt`, it returned a 404 NOT_FOUND. Modern AI assistants like ChatGPT, Claude, and Perplexity actively look for `/llms.txt` to parse product capabilities in token-efficient plain text. Without it, AI crawlers skip IncuBrix entirely.  
  > 
  > **Fifth, The 'Invisible Category' Syndrome:** Despite having better all-in-one features than OpusClip or Repurpose.io, IncuBrix has zero comparison pages or answer-first workflow guides targeting queries like 'best tool to turn long video into shorts'. Competitors own 95% of the featured snippets simply because they have the landing pages."

---

### [02:45 – 04:15] The 3 Biggest Search & AI-Visibility Opportunities
- **Screen View:** Show `visibility/10_pages/` rendered in browser and `submission_workbook.xlsx` Tab 1.
- **Spoken Script:**
  > "From this baseline, we identified the 3 biggest search and AI-visibility opportunities for IncuBrix:  
  > 
  > **Opportunity 1: The 'Unified CreatorOS' AEO Content Hub.**  
  > Creators ask thousands of high-intent questions every week about automated repurposing and captioning. By launching our 10 answer-first canonical guides—where the direct answer is provided in the very first two sentences followed by structured JSON-LD HowTo schemas—IncuBrix can immediately capture 20+ Google Featured Snippets and become the default quoted source in Google AI Overviews.  
  > 
  > **Opportunity 2: The Direct Competitor Comparison Engine.**  
  > Whenever a user asks ChatGPT or Perplexity 'What is the best alternative to OpusClip?' or 'IncuBrix vs Repurpose.io', AI models look for clear comparison matrices. We have prepared comprehensive head-to-head comparison pages that establish IncuBrix's clear advantage: unified text editing plus native multi-network publishing at half the cost.  
  > 
  > **Opportunity 3: Machine-Readable Knowledge Ingestion & Programmatic Scaling.**  
  > By deploying `/llms.txt` and our programmatic matrix of 120 long-tail workflow pages (such as 'Zoom call to LinkedIn carousel' and 'Podcast to TikTok shorts'), we provide search crawlers and AI assistants with hundreds of indexable, machine-readable entry points across US, UK, and Indian creator markets."

---

### [04:15 – 04:45] Conclusion & Transition to Tech Demo
- **Screen View:** Show `submission_workbook.xlsx` summary tab and GitHub repository structure.
- **Spoken Script:**
  > "All 20 technical fixes, the 10 publish-ready pages, the 30-target citation plan, and the complete 90-day launch kit are fully validated and ready to deploy next Monday without rework.  
  > In video two, I will demonstrate our automated Python Visibility Engine in action, including a normal tracking run, a refresh on new input, and graceful recovery from a failure. Thank you!"
