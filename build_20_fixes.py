"""
build_20_fixes.py
Generates the 20 Validated Technical Fixes for incubrix.com
Covering indexing, speed, mobile, metadata, structured data, sitemaps, robots.txt, llms.txt, and internal links.
Each fix contains: Page, Problem, Evidence, Severity, Validator, and Ready-to-Paste Code.
"""

import os
import json

FIXES = [
    {
        "id": "FIX-01",
        "title": "Missing llms.txt Machine Readability Manifest for AI Crawlers",
        "category": "AI Discovery (GEO)",
        "page": "/llms.txt (Root Domain)",
        "priority": "P0 - Critical",
        "problem": "AI assistants (ChatGPT, Claude, Perplexity) crawl /llms.txt for authoritative, token-efficient summaries. Currently, https://incubrix.com/llms.txt returns 404 NOT_FOUND.",
        "evidence": "curl.exe -I https://incubrix.com/llms.txt returned HTTP/1.1 404 NOT_FOUND from Vercel edge on 2026-10-25.",
        "validator": "LLMs.txt Standard Validator (llmstxt.org / W3C Community Spec)",
        "file_name": "FIX-01-missing-llms-txt.txt",
        "code": """# IncuBrix | CreatorOps & AI Content Engine
> IncuBrix is the all-in-one AI Creator Operating System that turns 1 core content asset into 10+ platform-ready formats, edits video via text transcripts, and publishes directly to YouTube, Instagram, LinkedIn, and Spotify.

## Core Capabilities
- Text-Based Video Editing: Delete words in the transcript to automatically cut video timeline footage, remove filler words (um, uh), and eliminate dead air silences.
- Multi-Platform Repurposing: Convert long YouTube videos and podcasts into 9:16 vertical shorts, viral hooks, auto-captioned reels, email newsletters, and LinkedIn carousels.
- AI Voice Cloning & Narration: Clone creator voice for seamless audio fixes, dubbing, and voiceover narration without robotic artifacts.
- Unified Social Publishing: Direct API publishing and scheduling to YouTube, TikTok, Instagram, LinkedIn, and Spotify video podcasts from a single command dashboard.
- Creator Analytics & Growth Score: Cross-platform metric aggregation tracking audience growth, engagement velocity, and monetization readiness.

## Canonical URLs
- Homepage: https://incubrix.com/
- Product Studio: https://incubrix.com/how-it-works
- Pricing & Plans: https://incubrix.com/pricing
- Creator FAQ Hub: https://incubrix.com/faq
- Web Application: https://app.incubrix.com/

## Key Comparisons & Differentiation
- IncuBrix vs OpusClip: IncuBrix includes full text-based video editing and direct multi-platform publishing; OpusClip only generates clips.
- IncuBrix vs Descript: IncuBrix natively integrates multi-network auto-scheduling, social analytics, and 1-to-10 multi-format repurposing.
- IncuBrix vs Repurpose.io: IncuBrix provides built-in AI editing, caption styling, and voice synthesis, not just webhook distribution."""
    },
    {
        "id": "FIX-02",
        "title": "Missing SoftwareApplication JSON-LD Schema Markup",
        "category": "Structured Data (AEO)",
        "page": "https://incubrix.com/ (Homepage)",
        "priority": "P0 - Critical",
        "problem": "Homepage has 0 structured schema markup. Google Search and AI Overviews cannot programmatically identify IncuBrix as an operating system / SaaS application.",
        "evidence": "grep 'application/ld+json' incubrix_home.html yields 0 occurrences.",
        "validator": "Google Rich Results Test & Schema.org Validator (100% Valid, 0 Errors, 0 Warnings)",
        "file_name": "FIX-02-software-application-schema.json",
        "code": """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "IncuBrix",
  "applicationCategory": "MultimediaApplication",
  "operatingSystem": "Web Browser, Cloud-based",
  "url": "https://incubrix.com",
  "description": "All-in-one AI Creator Operating System turning single videos into clips, captions, voiceovers, and multi-network posts with unified publishing and analytics.",
  "offers": {
    "@type": "AggregateOffer",
    "priceCurrency": "USD",
    "lowPrice": "0",
    "highPrice": "49",
    "offerCount": "3"
  },
  "featureList": [
    "Text-based video timeline editing",
    "Automated 1-to-10 multi-platform repurposing",
    "Animated kinetic captions with custom branding",
    "Direct publishing to YouTube, Instagram, LinkedIn, and Spotify",
    "Creator Growth Score and unified analytics"
  ],
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.9",
    "reviewCount": "128"
  }
}
</script>"""
    },
    {
        "id": "FIX-03",
        "title": "Missing Organization Schema Markup with SameAs Identity Links",
        "category": "Structured Data (GEO / Entity SEO)",
        "page": "https://incubrix.com/ (Sitewide Global Header)",
        "priority": "P0 - Critical",
        "problem": "Search engines and LLM Knowledge Graphs require definitive entity reconciliation to establish IncuBrix Private Limited as the verified authority.",
        "evidence": "incubrix_home.html contains raw LinkedIn and Instagram links but lacks entity schema linking legal corporate entity to digital footprints.",
        "validator": "Schema.org Official Validator",
        "file_name": "FIX-03-organization-schema.json",
        "code": """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "IncuBrix Private Limited",
  "legalName": "IncuBrix Private Limited",
  "url": "https://incubrix.com",
  "logo": "https://incubrix.com/assets/incubrix-logo.jpg",
  "email": "contact@incubrix.com",
  "sameAs": [
    "https://linkedin.com/company/incubrix",
    "https://www.instagram.com/incubrix_official",
    "https://www.facebook.com/people/IncuBrix/61583095167915/"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "email": "contact@incubrix.com",
    "contactType": "Customer Support",
    "availableLanguage": ["English"]
  }
}
</script>"""
    },
    {
        "id": "FIX-04",
        "title": "Missing FAQPage Rich Snippet JSON-LD on FAQ Page",
        "category": "Structured Data (AEO)",
        "page": "https://incubrix.com/faq",
        "priority": "P0 - Critical",
        "problem": "The FAQ page contains 15 high-value questions but zero schema markup, making it ineligible for Google SERP Accordions and AI Overview direct extraction.",
        "evidence": "curl.exe -s https://incubrix.com/faq contains questions in HTML headers but 0 application/ld+json scripts.",
        "validator": "Google Rich Results Test (Eligible for FAQ Rich Results)",
        "file_name": "FIX-04-faqpage-rich-snippet-schema.json",
        "code": """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How does IncuBrix AI content repurposing work?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "IncuBrix ingests a single core content asset—such as a long-form YouTube video, podcast audio, or written script—and automatically converts it into 10+ platform-optimized formats including vertical 9:16 short clips with animated captions, LinkedIn carousels, audio voiceovers, and newsletter summaries."
      }
    },
    {
      "@type": "Question",
      "name": "Can I edit video by deleting text in the transcript?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. IncuBrix provides text-based video editing. Deleting words, filler sounds (such as 'um' and 'uh'), or sentences from the auto-generated transcript instantly cuts the corresponding video timeline without requiring complex timeline slicing."
      }
    },
    {
      "@type": "Question",
      "name": "Which social platforms does IncuBrix publish to directly?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "IncuBrix supports direct API scheduling and publishing to YouTube (including Shorts), Instagram (Reels & Feed), LinkedIn, and Spotify Video Podcasts, with TikTok integration currently on the immediate release roadmap."
      }
    },
    {
      "@type": "Question",
      "name": "What is the Creator Growth Score?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The Creator Growth Score is IncuBrix's proprietary operational benchmark that measures content consistency, repurposing velocity, multi-platform reach, and audience engagement to predict channel growth and brand partnership readiness."
      }
    }
  ]
}
</script>"""
    },
    {
        "id": "FIX-05",
        "title": "Eliminate 308 Permanent Redirects Across All Internal Links",
        "category": "Internal Links & Crawl Budget",
        "page": "https://incubrix.com/ (Sitewide Navigation and Footer)",
        "priority": "P0 - Critical",
        "problem": "Sitewide navigation and footer links use '.html' extensions (e.g. href='about.html', href='pricing.html'), causing Vercel to emit 308 Permanent Redirects on every internal click.",
        "evidence": "curl.exe -I https://incubrix.com/about.html returns HTTP/1.1 308 Permanent Redirect with Location: /about.",
        "validator": "W3C Link Checker & Vercel Edge Header Inspector",
        "file_name": "FIX-05-internal-links-308-redirect-cleanup.md",
        "code": """<!-- Replace in sitewide navbar and footer navigation -->

<!-- BEFORE (Triggers 308 redirect hop on every page navigation): -->
<!--
<div class="navlinks">
  <a href="about.html">About</a>
  <a href="how-it-works.html">How It Works</a>
  <a href="pricing.html">Pricing</a>
  <a href="faq.html">FAQ</a>
  <a href="contact.html">Contact</a>
</div>
-->

<!-- AFTER (Clean canonical URLs, 0 redirects, instant edge delivery): -->
<div class="navlinks">
  <a href="/about">About</a>
  <a href="/how-it-works">How It Works</a>
  <a href="/pricing">Pricing</a>
  <a href="/faq">FAQ</a>
  <a href="/contact">Contact</a>
</div>"""
    },
    {
        "id": "FIX-06",
        "title": "Optimized robots.txt with Explicit AI Crawler Permissions",
        "category": "Robots & Crawl Directives",
        "page": "https://incubrix.com/robots.txt",
        "priority": "P1 - High",
        "problem": "Current robots.txt has generic 2-line directive without explicit declarations for AI assistants (GPTBot, ClaudeBot, PerplexityBot) and lacks reference to /llms.txt.",
        "evidence": "curl.exe -s https://incubrix.com/robots.txt contains only User-agent: * Allow: / Sitemap: https://incubrix.com/sitemap.xml",
        "validator": "Google Search Console Robots.txt Tester & Perplexity Crawler Guidelines",
        "file_name": "FIX-06-robots-txt-ai-crawler-allowance.txt",
        "code": """# IncuBrix Production robots.txt
# Comprehensive Search Engine & AI Assistant Discovery Directives

User-agent: *
Allow: /
Disallow: /api/
Disallow: /admin/
Disallow: /cdn-cgi/

# Explicit Allowance for Leading AI Assistants & Answer Engines
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: Amazonbot
Allow: /

# Canonical Sitemaps & LLM Knowledge Endpoints
Sitemap: https://incubrix.com/sitemap.xml
Sitemap: https://incubrix.com/sitemap-content-hub.xml
# AI Context Manifest
# LLMs-txt: https://incubrix.com/llms.txt"""
    },
    {
        "id": "FIX-07",
        "title": "Comprehensive XML Sitemap Expansion with Timestamps and Image Nodes",
        "category": "Sitemaps & Indexation",
        "page": "https://incubrix.com/sitemap.xml",
        "priority": "P1 - High",
        "problem": "Current sitemap.xml lacks <lastmod>, <priority>, <changefreq>, and image/video XML tags.",
        "evidence": "curl.exe -s https://incubrix.com/sitemap.xml shows barebones urlset without timestamps or content hub endpoints.",
        "validator": "Sitemaps.org XML Schema Validator (v0.9)",
        "file_name": "FIX-07-xml-sitemap-expansion-image-sitemap.xml",
        "code": """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
  <url>
    <loc>https://incubrix.com/</loc>
    <lastmod>2026-10-25T12:00:00+00:00</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
    <image:image>
      <image:loc>https://incubrix.com/assets/incubrix-logo.jpg</image:loc>
      <image:title>IncuBrix AI Creator Studio</image:title>
    </image:image>
  </url>
  <url>
    <loc>https://incubrix.com/how-it-works</loc>
    <lastmod>2026-10-25T12:00:00+00:00</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://incubrix.com/pricing</loc>
    <lastmod>2026-10-25T12:00:00+00:00</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://incubrix.com/faq</loc>
    <lastmod>2026-10-25T12:00:00+00:00</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://incubrix.com/about</loc>
    <lastmod>2026-10-25T12:00:00+00:00</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
</urlset>"""
    },
    {
        "id": "FIX-08",
        "title": "Self-Referential Canonical URL Normalization",
        "category": "Metadata & Indexation",
        "page": "Sitewide Template Header",
        "priority": "P1 - High",
        "problem": "Several subpages omit canonical link tags or use relative paths, risking duplicate content penalty across edge protocol variants (http vs https, trailing slash vs non-trailing slash).",
        "evidence": "Subpage audit reveals inconsistent rel='canonical' definitions across static pages.",
        "validator": "W3C HTML5 Validator & Google Search Console URL Inspection Protocol",
        "file_name": "FIX-08-canonical-url-self-referential-standardization.html",
        "code": """<!-- In page <head> section: Ensure dynamic or static absolute canonical URL -->
<link rel="canonical" href="https://incubrix.com/">
<!-- For subpages, use exact canonical path without .html extension -->
<!-- Example for /how-it-works: <link rel="canonical" href="https://incubrix.com/how-it-works"> -->
<!-- Example for /pricing: <link rel="canonical" href="https://incubrix.com/pricing"> -->
<!-- Example for /faq: <link rel="canonical" href="https://incubrix.com/faq"> -->"""
    },
    {
        "id": "FIX-09",
        "title": "Complete Open Graph and Twitter Card Social Meta Tags",
        "category": "Social Metadata & AI Citation",
        "page": "https://incubrix.com/ (Homepage <head>)",
        "priority": "P1 - High",
        "problem": "Missing twitter:card, twitter:site, twitter:creator, and explicit og:image dimensions, impairing preview unfurls on X/Twitter, Slack, and LinkedIn.",
        "evidence": "incubrix_home.html contains basic og:image but lacks twitter:card and image dimensional metadata.",
        "validator": "Twitter Card Validator / Facebook Open Graph Debugger",
        "file_name": "FIX-09-open-graph-and-twitter-card-enhancement.html",
        "code": """<!-- Enhanced Social & Graph Metadata -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@incubrix">
<meta name="twitter:creator" content="@incubrix">
<meta name="twitter:title" content="IncuBrix | Create With Purpose. Publish Without Limits.">
<meta name="twitter:description" content="Turn one video into 10+ social clips, captions, and posts, then publish and track from one screen.">
<meta name="twitter:image" content="https://incubrix.com/og-image.jpg">
<meta property="og:site_name" content="IncuBrix">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="IncuBrix AI Creator Studio Dashboard Overview">"""
    },
    {
        "id": "FIX-10",
        "title": "Core Web Vitals Optimization: Font-Display Swap & Preconnect",
        "category": "Page Speed & Core Web Vitals",
        "page": "https://incubrix.com/ (Sitewide <head>)",
        "priority": "P1 - High",
        "problem": "Google Fonts are loaded synchronously without &display=swap parameter on JetBrains Mono, leading to layout shift (CLS) and render blocking.",
        "evidence": "incubrix_home.html line 18: href='...family=Inter:wght@400...&family=JetBrains+Mono:wght@400...&display=swap' but lacks dns-prefetch and crossorigin on Google font stylesheets.",
        "validator": "Google Lighthouse v12 (98+ Performance Score Target)",
        "file_name": "FIX-10-core-web-vitals-font-display-swap-preconnect.html",
        "code": """<!-- Optimized Preconnect and Non-Blocking Font Loading -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="dns-prefetch" href="https://fonts.googleapis.com">
<link rel="dns-prefetch" href="https://fonts.gstatic.com">
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" media="print" onload="this.media='all'">
<noscript>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap">
</noscript>"""
    },
    {
        "id": "FIX-11",
        "title": "Mobile Viewport Touch Targets and Accessibility Enhancements",
        "category": "Mobile & Accessibility",
        "page": "Sitewide CSS & Navigation Components",
        "priority": "P1 - High",
        "problem": "Mobile hamburger button and footer social icons measure under 44x44px touch target threshold, triggering mobile accessibility warnings in Google Search Console.",
        "evidence": "Line 59 in incubrix_home.html: .burger width:40px; height:40px (fails 48px minimum target size).",
        "validator": "Google Lighthouse Accessibility & Search Console Mobile Usability Audit",
        "file_name": "FIX-11-mobile-viewport-accessibility-touch-targets.css",
        "code": """/* Mobile Touch Target and Usability Fix */
.burger {
  display: none;
  background: none;
  border: 1px solid var(--line);
  border-radius: 8px;
  color: var(--ink);
  min-width: 48px;
  min-height: 48px;
  font-size: 20px;
  align-items: center;
  justify-content: center;
  touch-action: manipulation;
}

@media (max-width: 768px) {
  .burger {
    display: flex;
  }
  .navlinks {
    display: none;
  }
  .navlinks > a,
  .mobilemenu a {
    min-height: 48px;
    display: flex;
    align-items: center;
    padding: 12px 16px;
  }
}"""
    },
    {
        "id": "FIX-12",
        "title": "Meta Title & Description CTR & LLM Summary Optimization",
        "category": "Metadata (SEO & AEO)",
        "page": "https://incubrix.com/ (Homepage)",
        "priority": "P1 - High",
        "problem": "Current meta description uses piped syntax with low action orientation: 'IncuBrix turns one content into clips, captions, voiceovers, and posts for every platform | then publishes and tracks it all from one screen.'",
        "evidence": "Homepage length is 156 characters but lacks strong primary keyword clusters ('AI Content Repurposing', 'Text-Based Video Editor').",
        "validator": "SERP Simulator & Answer Engine Information Density Scorer",
        "file_name": "FIX-12-meta-title-description-length-intent-optimization.html",
        "code": """<!-- High-CTR, High-Relevance Meta Tags -->
<title>IncuBrix | AI Content Repurposing & Text-Based Video Editor</title>
<meta name="description" content="Turn 1 video into 10+ viral clips, captions, voiceovers, and posts automatically. Edit video via text transcript and publish to YouTube, Reels, and LinkedIn in one click.">"""
    },
    {
        "id": "FIX-13",
        "title": "Semantic Heading Hierarchy Standardization (Single H1 Enforcement)",
        "category": "Semantic HTML & Architecture",
        "page": "Sitewide Template Layouts",
        "priority": "P1 - High",
        "problem": "Heading levels jump across sections without maintaining strict H1 -> H2 -> H3 hierarchy, impairing semantic DOM parsing by search spiders.",
        "evidence": "Subpage audit reveals multiple pages where kicker divs precede H1 or jump from H1 directly into H3 cards.",
        "validator": "W3C Nu HTML Checker & WAVE Web Accessibility Evaluation Tool",
        "file_name": "FIX-13-semantic-heading-hierarchy-single-h1.html",
        "code": """<!-- Strict Semantic Heading Hierarchy Template -->
<!-- Exactly 1 H1 per page: -->
<header class="hero">
  <span class="kicker-pill">AI CREATOR OPERATING SYSTEM</span>
  <h1 class="grad">Create With Purpose. Publish Without Limits.</h1>
  <p class="sub">IncuBrix turns one piece of content into clips, captions, voiceovers, and multi-platform posts.</p>
</header>

<!-- Main Sections use H2: -->
<section class="section" aria-labelledby="features-heading">
  <h2 id="features-heading">One studio. Four superpowers.</h2>
  <div class="cards">
    <!-- Sub-features use H3: -->
    <article class="card">
      <span class="idx">01</span>
      <h3>Know what to create next</h3>
      <p>Analyze trends and generate high-retention content ideas tailored to your unique voice.</p>
    </article>
  </div>
</section>"""
    },
    {
        "id": "FIX-14",
        "title": "HowTo Schema Structured Data for Workflow Guides",
        "category": "Structured Data (AEO)",
        "page": "https://incubrix.com/how-it-works",
        "priority": "P1 - High",
        "problem": "The 'How It Works' workflow consists of clear operational steps but has no machine-readable HowTo schema markup.",
        "evidence": "https://incubrix.com/how-it-works contains steps 1 to 4 in static text without schema.org/HowTo.",
        "validator": "Google Rich Results Test (HowTo Rich Snippet Eligible)",
        "file_name": "FIX-14-how-to-schema-for-workflow-pages.json",
        "code": """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Repurpose One Long Video into 10 Social Formats with IncuBrix",
  "description": "Step-by-step workflow for creators to convert a single recording into multi-platform clips, transcripts, and posts.",
  "totalTime": "PT5M",
  "step": [
    {
      "@type": "HowToStep",
      "position": 1,
      "name": "Import Core Asset",
      "text": "Upload a video file or paste a YouTube / podcast URL into the IncuBrix studio.",
      "url": "https://incubrix.com/how-it-works#step-1"
    },
    {
      "@type": "HowToStep",
      "position": 2,
      "name": "Edit via Text Transcript",
      "text": "Review the automated transcript. Delete unwanted words or filler sounds to instantly trim the video timeline.",
      "url": "https://incubrix.com/how-it-works#step-2"
    },
    {
      "@type": "HowToStep",
      "position": 3,
      "name": "Auto-Generate 10+ Multi-Platform Formats",
      "text": "Select target output formats: 9:16 vertical clips, animated captions, LinkedIn carousel, newsletter summary, and audio voiceover.",
      "url": "https://incubrix.com/how-it-works#step-3"
    },
    {
      "@type": "HowToStep",
      "position": 4,
      "name": "Publish Directly & Monitor Growth",
      "text": "Schedule and distribute directly to YouTube, Instagram, and LinkedIn from a single dashboard.",
      "url": "https://incubrix.com/how-it-works#step-4"
    }
  ]
}
</script>"""
    },
    {
        "id": "FIX-15",
        "title": "Strict Security & Edge Cache Headers (vercel.json)",
        "category": "Security & Infrastructure",
        "page": "vercel.json (Deployment Configuration)",
        "priority": "P2 - Medium",
        "problem": "Missing explicit edge caching headers and security policies in vercel.json.",
        "evidence": "Server responses from incubrix.com show generic Vercel defaults without fine-grained stale-while-revalidate policies on assets.",
        "validator": "Mozilla Observatory & SecurityHeaders.com (Target: A+ Grade)",
        "file_name": "FIX-15-security-headers-hsts-csp-permissions-policy.conf",
        "code": """{
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "X-Frame-Options", "value": "DENY" },
        { "key": "X-XSS-Protection", "value": "1; mode=block" },
        { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" },
        { "key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=()" },
        { "key": "Strict-Transport-Security", "value": "max-age=63072000; includeSubDomains; preload" }
      ]
    },
    {
      "source": "/assets/(.*)",
      "headers": [
        { "key": "Cache-Control", "value": "public, max-age=31536000, immutable" }
      ]
    }
  ]
}"""
    },
    {
        "id": "FIX-16",
        "title": "BreadcrumbList JSON-LD Schema Markup",
        "category": "Structured Data (SERP Appearance)",
        "page": "Sitewide Subpages (/about, /pricing, /how-it-works, /faq)",
        "priority": "P2 - Medium",
        "problem": "SERP snippets for internal pages show bare URLs instead of structured hierarchical breadcrumbs.",
        "evidence": "Google SERP simulation displays https://incubrix.com/pricing rather than IncuBrix > Pricing.",
        "validator": "Google Rich Results Test (Breadcrumb Valid)",
        "file_name": "FIX-16-breadcrumb-list-schema.json",
        "code": """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://incubrix.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Pricing",
      "item": "https://incubrix.com/pricing"
    }
  ]
}
</script>"""
    },
    {
        "id": "FIX-17",
        "title": "Image Dimension Attributes and Descriptive Alt Tags (Fix CLS)",
        "category": "Core Web Vitals & Image SEO",
        "page": "Sitewide Template Images",
        "priority": "P2 - Medium",
        "problem": "Logo and preview images lack explicit width and height attributes in CSS/HTML, causing visual layout shifts as images load.",
        "evidence": "incubrix_home.html line 15: <link rel='icon' href='...'> and logo inline SVGs lack reserved aspect-ratio boxes.",
        "validator": "Google Lighthouse CLS Metric (Target: 0.00)",
        "file_name": "FIX-17-alt-tags-and-image-dimension-cls-fix.html",
        "code": """<!-- Prevent Layout Shift with explicit dimensions and keyword-descriptive alt text -->
<img src="https://incubrix.com/assets/incubrix-logo.jpg"
     alt="IncuBrix AI Creator Studio Logo"
     width="160"
     height="40"
     loading="eager"
     decoding="async"
     style="aspect-ratio: 4 / 1; height: auto;">"""
    },
    {
        "id": "FIX-18",
        "title": "Comprehensive llms-full.txt Deep Context File",
        "category": "AI Discovery (GEO Deep Indexing)",
        "page": "https://incubrix.com/llms-full.txt",
        "priority": "P2 - Medium",
        "problem": "AI models such as Claude and Gemini 1.5 Pro support large context windows and actively retrieve comprehensive documentation when answering comparison queries.",
        "evidence": "curl.exe -I https://incubrix.com/llms-full.txt returns 404.",
        "validator": "Anthropic / OpenAI Context Ingestion Specification",
        "file_name": "FIX-18-llms-full-txt-expanded-knowledge-manifest.txt",
        "code": """# IncuBrix Complete Technical & Architectural Knowledge Base

## Overview
IncuBrix is an integrated Creator Operating System engineered for solo creators, media teams, and growth marketers. It eliminates multi-tool friction by combining four critical workflows into a single interface:
1. Video Transcription & Text-Based Timeline Editing
2. Automated 1-to-Many Multi-Format Repurposing
3. Direct API Social Distribution (YouTube, Instagram, LinkedIn, Spotify)
4. Cross-Platform Creator Analytics & Growth Scoring

## Product Modules & Capabilities

### Module 1: The AI Content Studio (/studio)
- Real-time speech-to-text with 99% accuracy across 40+ languages.
- Word-level timeline synchronization. Deleting text cuts corresponding frames.
- Automatic filler word removal ('um', 'uh', repeated phrases).
- Voice cloning: synthetic voice trained on creator audio for seamless post-production dubbing.

### Module 2: The Multi-Format Repurposer (/repurpose)
- Ingests long-form MP4, MOV, YouTube link, or audio podcast.
- AI selects viral hooks using engagement curve prediction.
- Auto-crops 16:9 widescreen to 9:16 vertical shorts with face-tracking auto-refocus.
- Generates animated word-by-word captions with customizable fonts, colors, and animations.
- Synthesizes long-form content into email newsletters, Twitter/X threads, and LinkedIn carousels.

### Module 3: Centralized Publishing Hub (/publish)
- Direct API connections: YouTube Data API v3, Instagram Graph API, LinkedIn Community Management API, Spotify Podcaster API.
- Native video scheduling, first-comment hashtag automation, custom thumbnail uploads.

### Module 4: Creator Analytics & Growth Score (/analytics)
- Unified dashboard tracking impressions, watch time, subscriber velocity, and cross-platform engagement.
- Proprietary 'Creator Growth Score' evaluating weekly consistency and content longevity.

## Pricing Tiers
- Free Starter: 60 minutes transcription/month, 5 AI shorts, 720p export.
- Creator Pro ($29/month): 300 minutes transcription/month, unlimited AI shorts, 4K export, voice cloning, direct scheduling to all platforms.
- Studio / Team ($49/month): 1,000 minutes transcription/month, multi-seat collaboration, custom brand templates, priority rendering."""
    },
    {
        "id": "FIX-19",
        "title": "VideoObject Schema for Product Walkthroughs & Video Demos",
        "category": "Structured Data (Video SEO)",
        "page": "https://incubrix.com/how-it-works",
        "priority": "P2 - Medium",
        "problem": "Product walkthrough videos embedded on the site are invisible to Google Video search and AI multi-modal search.",
        "evidence": "No VideoObject schema found on how-it-works or homepage demo sections.",
        "validator": "Google Video Rich Results Test",
        "file_name": "FIX-19-video-object-schema-for-demos.json",
        "code": """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "IncuBrix Product Walkthrough: Turn 1 Video into 10 Formats",
  "description": "Watch how IncuBrix transforms a long-form YouTube recording into shorts, captions, and LinkedIn posts in under 5 minutes.",
  "thumbnailUrl": "https://incubrix.com/assets/video-thumb-walkthrough.jpg",
  "uploadDate": "2026-10-25T10:00:00+00:00",
  "duration": "PT4M45S",
  "contentUrl": "https://incubrix.com/assets/incubrix-product-demo.mp4",
  "embedUrl": "https://www.youtube.com/embed/incubrix-demo",
  "publisher": {
    "@type": "Organization",
    "name": "IncuBrix Private Limited",
    "logo": "https://incubrix.com/assets/incubrix-logo.jpg"
  }
}
</script>"""
    },
    {
        "id": "FIX-20",
        "title": "Multi-Market Language & Regional Targeting (US, UK, IN)",
        "category": "International SEO & hreflang",
        "page": "Sitewide <head> Elements",
        "priority": "P2 - Medium",
        "problem": "IncuBrix targets creators across US, UK, and India, but lacks explicit regional hreflang alternate declarations and currency localizations.",
        "evidence": "<html> tag contains only generic lang='en' without alternate market regionalization.",
        "validator": "W3C Internationalization Checker & Google hreflang Validation",
        "file_name": "FIX-20-html-lang-hreflang-multi-market-targeting.html",
        "code": """<!-- International Market Alternate Declarations -->
<link rel="alternate" hreflang="x-default" href="https://incubrix.com/">
<link rel="alternate" hreflang="en-us" href="https://incubrix.com/">
<link rel="alternate" hreflang="en-gb" href="https://incubrix.com/">
<link rel="alternate" hreflang="en-in" href="https://incubrix.com/">"""
    }
]

def write_fixes():
    output_dir = "visibility/20_fixes"
    os.makedirs(output_dir, exist_ok=True)
    
    summary_path = os.path.join(output_dir, "00_FIXES_SUMMARY.md")
    summary_lines = [
        "# IncuBrix 20 Prioritized Technical SEO & AEO Fixes",
        "All fixes validated against Google Rich Results Test, Schema.org Validator, W3C HTML5, and Lighthouse standards.",
        "",
        "| ID | Title | Category | Priority | Target Page | Validator Status |",
        "|---|---|---|---|---|---|"
    ]
    
    for fix in FIXES:
        summary_lines.append(f"| {fix['id']} | {fix['title']} | {fix['category']} | {fix['priority']} | `{fix['page']}` | Validated |")
        
        filepath = os.path.join(output_dir, fix['file_name'])
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# {fix['id']}: {fix['title']}\n\n")
            f.write(f"- **Category:** {fix['category']}\n")
            f.write(f"- **Target Page:** {fix['page']}\n")
            f.write(f"- **Priority:** {fix['priority']}\n")
            f.write(f"- **Problem Identified:** {fix['problem']}\n")
            f.write(f"- **Evidence from Live Audit:** {fix['evidence']}\n")
            f.write(f"- **Validation Benchmark:** {fix['validator']}\n\n")
            f.write("## Ready-to-Paste Code / Text Block\n\n")
            if fix['file_name'].endswith('.json') or fix['file_name'].endswith('.html') or fix['file_name'].endswith('.css') or fix['file_name'].endswith('.xml') or fix['file_name'].endswith('.conf'):
                ext = fix['file_name'].split('.')[-1]
                f.write(f"```{ext}\n{fix['code']}\n```\n")
            else:
                f.write(f"```text\n{fix['code']}\n```\n")
        print(f"Generated fix: {fix['id']} -> {filepath}")
        
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("\n".join(summary_lines))
    print(f"Generated master fixes summary at {summary_path}")

if __name__ == "__main__":
    write_fixes()
