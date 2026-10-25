# Monday Morning Sprint Execution Checklist
> **Day 1 Action Plan for IncuBrix Engineering & Growth Team**  
> Immediate copy-paste tasks to execute the first sprint.

---

## 09:00 AM – Standup & Ownership Assignment
- [ ] Review `submission_workbook.xlsx` with Growth Engineer and Lead Developer.
- [ ] Assign PR ownership for technical fixes:
  - PR 1: Edge routing and navigation cleanup (FIX-05)
  - PR 2: Machine discovery endpoints (FIX-01, FIX-06, FIX-18)
  - PR 3: Schema.org structured data injection (FIX-02, FIX-03, FIX-04)

---

## 10:30 AM – Commit & Deploy Technical Fixes (Phase 1)
- [ ] **Fix 308 Redirects:** Update sitewide navigation in `index.html` and template headers:
  - Replace `href="about.html"` -> `href="/about"`
  - Replace `href="pricing.html"` -> `href="/pricing"`
  - Replace `href="how-it-works.html"` -> `href="/how-it-works"`
  - Replace `href="faq.html"` -> `href="/faq"`
- [ ] **Deploy `/llms.txt`:** Copy `visibility/20_fixes/FIX-01-missing-llms-txt.txt` to `public/llms.txt`.
- [ ] **Deploy `/llms-full.txt`:** Copy `visibility/20_fixes/FIX-18-llms-full-txt-expanded-knowledge-manifest.txt` to `public/llms-full.txt`.
- [ ] **Update `robots.txt`:** Replace current 2-line file with `visibility/20_fixes/FIX-06-robots-txt-ai-crawler-allowance.txt`.
- [ ] **Inject JSON-LD Schemas:** Paste `SoftwareApplication` and `Organization` schemas into `<head>` of `index.html`.

---

## 02:00 PM – Verification & Edge Testing
- [ ] Run edge header check:
  ```bash
  curl.exe -I https://incubrix.com/about.html
  curl.exe -I https://incubrix.com/llms.txt
  ```
  *Target: `llms.txt` returns HTTP 200 OK; internal links resolve instantly.*
- [ ] Run Google Rich Results Test on `https://incubrix.com/`:
  *Target: SoftwareApplication and Organization detected with 0 errors and 0 warnings.*

---

## 04:00 PM – First Content Page Staging
- [ ] Stage `visibility/10_pages/01-how-to-repurpose-long-video-into-shorts.html` under `https://incubrix.com/hub/how-to-repurpose-long-video-into-shorts`.
- [ ] Stage `visibility/10_pages/02-incubrix-vs-opusclip-vs-repurpose-io.html` under `https://incubrix.com/hub/incubrix-vs-opusclip-vs-repurpose-io`.
- [ ] Submit URLs to Google Search Console for priority indexing.

---

## 05:30 PM – Automated Tracker Setup
- [ ] Verify local Python tracker:
  ```bash
  python engine/main.py run --quick
  ```
- [ ] Configure weekly scheduled task or GitHub Actions cron workflow.
