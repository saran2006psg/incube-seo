# FIX-05: Eliminate 308 Permanent Redirects Across All Internal Links

- **Category:** Internal Links & Crawl Budget
- **Target Page:** https://incubrix.com/ (Sitewide Navigation and Footer)
- **Priority:** P0 - Critical
- **Problem Identified:** Sitewide navigation and footer links use '.html' extensions (e.g. href='about.html', href='pricing.html'), causing Vercel to emit 308 Permanent Redirects on every internal click.
- **Evidence from Live Audit:** curl.exe -I https://incubrix.com/about.html returns HTTP/1.1 308 Permanent Redirect with Location: /about.
- **Validation Benchmark:** W3C Link Checker & Vercel Edge Header Inspector

## Ready-to-Paste Code / Text Block

```text
<!-- Replace in sitewide navbar and footer navigation -->

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
</div>
```
