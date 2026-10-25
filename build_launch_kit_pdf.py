"""
build_launch_kit_pdf.py
Generates a stunning, executive-grade PDF document for the IncuBrix 90-Day Growth Launch Kit.
Features:
- IncuBrix modern brand styling (Deep Navy, Electric Blue, Cyan, Slate text, Clean card layouts)
- Numbered running header and footer ("Page X of Y")
- Complete 12-week roadmap (Phase 1 to Phase 5) with RACI, tools, budgets, milestones
- Target KPI Progression Table & Tool Stack Budget Table
- Risk Assessment Matrix & Monday Morning Kickoff Action Checklist
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

# Palette
PRIMARY = colors.HexColor("#0E1A3A")      # IncuBrix Deep Navy
SECONDARY = colors.HexColor("#2B6BFF")    # IncuBrix Electric Blue
ACCENT = colors.HexColor("#0D9488")       # Deep Cyan Accent
ACCENT_LIGHT = colors.HexColor("#E6FFFA")
DARK_TEXT = colors.HexColor("#0F172A")
BODY_TEXT = colors.HexColor("#334155")
MUTED_TEXT = colors.HexColor("#64748B")
LIGHT_BG = colors.HexColor("#F8FAFC")
CARD_BG = colors.HexColor("#F1F5F9")
BORDER_COLOR = colors.HexColor("#CBD5E1")
BORDER_LIGHT = colors.HexColor("#E2E8F0")

class LaunchKitCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.setFont("Helvetica-Bold", 8)
            self.setFillColor(MUTED_TEXT)
            
            # Running Header
            if self._pageNumber > 1:
                self.drawString(54, 752, "INCUBRIX PRIVATE LIMITED  |  90-DAY AEO, SEO & GEO LAUNCH KIT")
                self.setStrokeColor(BORDER_LIGHT)
                self.setLineWidth(0.6)
                self.line(54, 744, 558, 744)

            # Running Footer
            self.setFont("Helvetica", 8)
            self.drawString(54, 38, "CONFIDENTIAL  |  Operational Growth Engine  |  Zero Rework Execution Plan")
            self.drawRightString(558, 38, f"Page {self._pageNumber} of {num_pages}")
            self.setStrokeColor(BORDER_LIGHT)
            self.setLineWidth(0.6)
            self.line(54, 48, 558, 48)
            super().showPage()
        super().save()

def create_kit_styles():
    base = getSampleStyleSheet()
    return {
        "Badge": ParagraphStyle(
            "Badge",
            fontName="Helvetica-Bold",
            fontSize=8,
            leading=10,
            textColor=SECONDARY,
            spaceAfter=6
        ),
        "Title": ParagraphStyle(
            "Title",
            parent=base["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=22,
            leading=26,
            textColor=PRIMARY,
            spaceAfter=6
        ),
        "Subtitle": ParagraphStyle(
            "Subtitle",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=10.5,
            leading=15,
            textColor=MUTED_TEXT,
            spaceAfter=14
        ),
        "SectionHeader": ParagraphStyle(
            "SectionHeader",
            parent=base["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=13,
            leading=17,
            textColor=PRIMARY,
            spaceBefore=14,
            spaceAfter=8,
            keepWithNext=True
        ),
        "PhaseBadge": ParagraphStyle(
            "PhaseBadge",
            fontName="Helvetica-Bold",
            fontSize=9.5,
            leading=13,
            textColor=SECONDARY,
            spaceBefore=10,
            spaceAfter=4,
            keepWithNext=True
        ),
        "Body": ParagraphStyle(
            "Body",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8.5,
            leading=12.5,
            textColor=BODY_TEXT,
            spaceAfter=5
        ),
        "Bullet": ParagraphStyle(
            "Bullet",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8.5,
            leading=12,
            textColor=BODY_TEXT,
            leftIndent=12,
            spaceAfter=3
        ),
        "TableHeader": ParagraphStyle(
            "TableHeader",
            fontName="Helvetica-Bold",
            fontSize=8,
            leading=11,
            textColor=colors.white,
            alignment=1
        ),
        "TableCell": ParagraphStyle(
            "TableCell",
            fontName="Helvetica",
            fontSize=7.5,
            leading=10.5,
            textColor=DARK_TEXT
        ),
        "TableCellBold": ParagraphStyle(
            "TableCellBold",
            fontName="Helvetica-Bold",
            fontSize=7.5,
            leading=10.5,
            textColor=DARK_TEXT
        ),
        "TableCellCenter": ParagraphStyle(
            "TableCellCenter",
            fontName="Helvetica",
            fontSize=7.5,
            leading=10.5,
            textColor=DARK_TEXT,
            alignment=1
        )
    }

def generate_launch_kit_pdf():
    pdf_path = "launch_kit/IncuBrix_90_Day_Launch_Kit.pdf"
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )
    
    styles = create_kit_styles()
    story = []

    # ================= COVER BANNER =================
    story.append(Paragraph("INCUBRIX CREATOR OPERATIONS & GROWTH ENGINE", styles["Badge"]))
    story.append(Paragraph("90-Day AEO, SEO & GEO Growth Launch Kit", styles["Title"]))
    story.append(Paragraph(
        "A complete, actionable operational plan IncuBrix leadership and engineering can execute starting next Monday. "
        "Includes step-by-step roadmap, RACI ownership, lean budget allocation, KPI targets, risk mitigation, and Monday morning checklist.",
        styles["Subtitle"]
    ))
    story.append(HRFlowable(width="100%", thickness=2, color=SECONDARY, spaceAfter=12))

    # ================= NORTH STAR CARD =================
    north_star_data = [
        [
            Paragraph("<b>North Star Targets (Day 90):</b>", styles["TableCellBold"]),
            Paragraph("<b>>40.0% Aggregate AI Mention Rate</b>", styles["TableCellCenter"]),
            Paragraph("<b>45+ Google Page 1 Ranks</b>", styles["TableCellCenter"]),
            Paragraph("<b>20+ Featured Snippets</b>", styles["TableCellCenter"]),
            Paragraph("<b>2,500+ Monthly Signups</b>", styles["TableCellCenter"])
        ]
    ]
    t_ns = Table(north_star_data, colWidths=[130, 95, 95, 85, 99])
    t_ns.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('BOX', (0,0), (-1,-1), 1, SECONDARY),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_LIGHT),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_ns)
    story.append(Spacer(1, 10))

    # ================= 12-WEEK ROADMAP PHASES =================
    story.append(Paragraph("The 90-Day Strategic Roadmap (12-Week Implementation)", styles["SectionHeader"]))

    # PHASE 1
    story.append(Paragraph("PHASE 1 (WEEKS 1–2): TECHNICAL FOUNDATION, AI DIRECTIVES & SCHEMA INFRASTRUCTURE", styles["PhaseBadge"]))
    p1_tasks = [
        "<b>Week 1 — Edge Latency & Entity Schemas:</b> Deploy <code>FIX-01</code> (/llms.txt) and <code>FIX-18</code> (/llms-full.txt) to root; deploy <code>FIX-05</code> updating all navbar/footer links from .html to clean canonical paths (/about, /pricing), eliminating 308 redirect hops; update robots.txt with explicit GPTBot & ClaudeBot directives (<code>FIX-06</code>); inject SoftwareApplication and Organization JSON-LD schemas (<code>FIX-02, 03</code>).",
        "<b>Week 2 — Core Web Vitals & FAQ Snippets:</b> Deploy FAQPage schema to /faq (<code>FIX-04</code>); optimize font display swap & preconnect (<code>FIX-10</code>); configure security & asset cache headers in vercel.json (<code>FIX-15</code>); submit comprehensive XML sitemaps.",
        "<b>RACI:</b> Lead Growth Engineer (Accountable), DevOps / Frontend (Responsible) | <b>Budget:</b> $0 | <b>Milestone:</b> 0 redirect hops, llms.txt 200 OK, Lighthouse 95+."
    ]
    for pt in p1_tasks:
        story.append(Paragraph(f"• {pt}", styles["Bullet"]))
    story.append(Spacer(1, 6))

    # PHASE 2
    story.append(Paragraph("PHASE 2 (WEEKS 3–5): 'ANSWER-FIRST' CONTENT HUB DEPLOYMENT (10 CANONICAL PAGES)", styles["PhaseBadge"]))
    p2_tasks = [
        "<b>Week 3 — Cluster 1 (Repurposing Authority):</b> Publish Page 01 (How to Repurpose Long Videos into Shorts), Page 02 (IncuBrix vs OpusClip vs Repurpose.io), and Page 03 (7 Best AI Content Repurposing Tools 2026). Submit to GSC for priority indexing.",
        "<b>Week 4 — Cluster 2 (Video Editing & Distribution):</b> Publish Page 04 (How to Edit Video by Editing Text), Page 05 (Automate Cross-Platform Social Publishing), and Page 06 (Podcast Episode to 15 Assets). Connect deep links to app onboarding.",
        "<b>Week 5 — Cluster 3 (Voice & CreatorOps):</b> Publish Page 07 (Voice Cloning Guide), Page 08 (Auto-Caption Generator), Page 09 (CreatorOps 101), and Page 10 (IncuBrix vs Descript). Complete 10-page content mesh.",
        "<b>RACI:</b> Growth Marketer (Responsible), Content Lead (Responsible), Lead Growth Engineer (Accountable) | <b>Budget:</b> $150 ($50/wk) | <b>Milestone:</b> 100% crawl, 15+ top 50 ranks."
    ]
    for pt in p2_tasks:
        story.append(Paragraph(f"• {pt}", styles["Bullet"]))
    story.append(Spacer(1, 6))

    # PHASE 3
    story.append(Paragraph("PHASE 3 (WEEKS 6–7): HIGH-AUTHORITY CITATIONS & DIRECTORY INGESTION (30 TARGETS)", styles["PhaseBadge"]))
    p3_tasks = [
        "<b>Week 6 — Tier 1 Directory Footprints:</b> Claim and verify official IncuBrix vendor profiles on G2, Capterra, Product Hunt, Trustpilot, AlternativeTo, and Futurepedia. Trigger automated review requests to first 100 beta creators.",
        "<b>Week 7 — Organic Creator Community Amplification:</b> Launch value-first workflow breakdowns on Reddit (r/NewTubers, r/VideoEditing, r/ContentCreation) sharing real before/after metrics without spam. Answer 10 high-traffic Quora creator questions.",
        "<b>RACI:</b> Community Growth Lead (Responsible), Product Manager (Accountable) | <b>Budget:</b> $0 | <b>Milestone:</b> 6 verified high-DR profiles, Reddit discussions in SERPs."
    ]
    for pt in p3_tasks:
        story.append(Paragraph(f"• {pt}", styles["Bullet"]))
    story.append(Spacer(1, 6))

    # PHASE 4
    story.append(Paragraph("PHASE 4 (WEEKS 8–9): MIDPOINT ENGINE AUDIT & 120-PAGE PROGRAMMATIC SCALE", styles["PhaseBadge"]))
    p4_tasks = [
        "<b>Week 8 — Midpoint Audit & Semantic Tuning:</b> Rerun full 104-question tracker across Google SERP and 4 AI assistants; generate Day 1 vs Day 60 comparison; tune semantic density on near-win queries.",
        "<b>Week 9 — Programmatic Workflow Matrix Rollout:</b> Deploy the 120 programmatic pages generated by <code>engine/programmatic_generator.py</code> under <code>https://incubrix.com/workflows/</code>; submit programmatic sitemap.",
        "<b>RACI:</b> Lead Growth Engineer (Accountable & Responsible), Fullstack Engineer (Responsible) | <b>Budget:</b> $100 | <b>Milestone:</b> AI mention rate >= 20.0%, 100+ pages indexed."
    ]
    for pt in p4_tasks:
        story.append(Paragraph(f"• {pt}", styles["Bullet"]))
    story.append(Spacer(1, 6))

    # PHASE 5
    story.append(Paragraph("PHASE 5 (WEEKS 10–12): HIGH-DR PARTNERSHIPS, CONVERSION & SCALE", styles["PhaseBadge"]))
    p5_tasks = [
        "<b>Week 10 — High-DR Editorial Pitches:</b> Pitch original creator benchmark data teardown to HubSpot Blog, Zapier Blog, and Podnews; secure inclusion in 2 major software roundups.",
        "<b>Week 11 — Onboarding Funnel CRO:</b> Implement interactive sandbox video trimmer on /how-it-works; deploy exit-intent lead magnet with 7-Day Repurposing Playbook.",
        "<b>Week 12 — Automated Weekly Cron Activation & Executive Review:</b> Set up weekly automated tracking cron job running every Monday at 06:00 UTC with Slack alert webhooks; final executive presentation.",
        "<b>RACI:</b> Lead Growth Engineer (Accountable), PR Lead (Responsible), Product Designer (Consulted) | <b>Budget:</b> $50 | <b>Milestone:</b> >40% AI mentions, 45+ Page 1s, 2,500+ signups."
    ]
    for pt in p5_tasks:
        story.append(Paragraph(f"• {pt}", styles["Bullet"]))
    story.append(Spacer(1, 10))

    # ================= BUDGET & TOOL STACK TABLE =================
    story.append(Paragraph("Detailed Tool Stack & Budget Allocation ($255 Total)", styles["SectionHeader"]))
    budget_rows = [
        [Paragraph("<b>Tool / Platform</b>", styles["TableHeader"]), Paragraph("<b>Core Purpose</b>", styles["TableHeader"]), Paragraph("<b>Monthly Cost</b>", styles["TableHeader"]), Paragraph("<b>90-Day Total</b>", styles["TableHeader"]), Paragraph("<b>Ownership / Notes</b>", styles["TableHeader"])],
        [Paragraph("Vercel Pro", styles["TableCellBold"]), Paragraph("Edge hosting, routing rules, edge caching", styles["TableCell"]), Paragraph("$20 / mo", styles["TableCellCenter"]), Paragraph("$60", styles["TableCellCenter"]), Paragraph("Existing production tier", styles["TableCell"])],
        [Paragraph("Google Search Console", styles["TableCellBold"]), Paragraph("Indexation, sitemaps, performance metrics", styles["TableCell"]), Paragraph("$0 (Free)", styles["TableCellCenter"]), Paragraph("$0", styles["TableCellCenter"]), Paragraph("Official search console", styles["TableCell"])],
        [Paragraph("IncuBrix Visibility Engine", styles["TableCellBold"]), Paragraph("Automated tracking, scoring, briefs, alerts", styles["TableCell"]), Paragraph("$0 (In-house)", styles["TableCellCenter"]), Paragraph("$0", styles["TableCellCenter"]), Paragraph("Built custom in Python", styles["TableCell"])],
        [Paragraph("OpenAI / Claude APIs", styles["TableCellBold"]), Paragraph("Weekly automated AI assistant evaluations", styles["TableCell"]), Paragraph("$15 / mo", styles["TableCellCenter"]), Paragraph("$45", styles["TableCellCenter"]), Paragraph("~$0.019 per 100 checks", styles["TableCell"])],
        [Paragraph("G2 / Capterra Verification", styles["TableCellBold"]), Paragraph("Official vendor profile claims and reviews", styles["TableCell"]), Paragraph("$0 (Free)", styles["TableCellCenter"]), Paragraph("$0", styles["TableCellCenter"]), Paragraph("Claimed organic vendor pages", styles["TableCell"])],
        [Paragraph("Visual Assets & Media", styles["TableCellBold"]), Paragraph("Figma comparison matrices, feature SVGs", styles["TableCell"]), Paragraph("$50 / mo", styles["TableCellCenter"]), Paragraph("$150", styles["TableCellCenter"]), Paragraph("Design team sprints", styles["TableCell"])],
        [Paragraph("<b>Total Investment</b>", styles["TableCellBold"]), Paragraph("<b>Complete 90-Day Execution</b>", styles["TableCellBold"]), Paragraph("<b>$85 / mo</b>", styles["TableCellCenter"]), Paragraph("<b>$255 Total</b>", styles["TableCellCenter"]), Paragraph("<b>High capital efficiency</b>", styles["TableCellBold"])]
    ]
    t_budget = Table(budget_rows, colWidths=[105, 175, 75, 75, 74])
    t_budget.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_LIGHT),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-2), [colors.white, LIGHT_BG]),
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor("#E2E8F0")),
    ]))
    story.append(t_budget)
    story.append(Spacer(1, 10))

    # ================= TARGET KPI PROGRESSION TABLE =================
    story.append(Paragraph("Target KPI Progression Table", styles["SectionHeader"]))
    kpi_rows = [
        [Paragraph("<b>Metric</b>", styles["TableHeader"]), Paragraph("<b>Baseline (Day 1)</b>", styles["TableHeader"]), Paragraph("<b>Day 30 Target</b>", styles["TableHeader"]), Paragraph("<b>Day 60 Target</b>", styles["TableHeader"]), Paragraph("<b>Day 90 North Star</b>", styles["TableHeader"])],
        [Paragraph("IncuBrix Google Page 1 Ranks", styles["TableCellBold"]), Paragraph("0 (Non-Brand)", styles["TableCellCenter"]), Paragraph("8 Keywords", styles["TableCellCenter"]), Paragraph("22 Keywords", styles["TableCellCenter"]), Paragraph("<b>45+ Keywords</b>", styles["TableCellCenter"])],
        [Paragraph("Google Featured Snippets (AEO)", styles["TableCellBold"]), Paragraph("0", styles["TableCellCenter"]), Paragraph("2 Snippets", styles["TableCellCenter"]), Paragraph("8 Snippets", styles["TableCellCenter"]), Paragraph("<b>20+ Snippets</b>", styles["TableCellCenter"])],
        [Paragraph("ChatGPT (GPT-4o) Mention Rate", styles["TableCellBold"]), Paragraph("0.0%", styles["TableCellCenter"]), Paragraph("12.0%", styles["TableCellCenter"]), Paragraph("25.0%", styles["TableCellCenter"]), Paragraph("<b>> 40.0%</b>", styles["TableCellCenter"])],
        [Paragraph("Perplexity Sonar Mention Rate", styles["TableCellBold"]), Paragraph("0.0%", styles["TableCellCenter"]), Paragraph("15.0%", styles["TableCellCenter"]), Paragraph("30.0%", styles["TableCellCenter"]), Paragraph("<b>> 50.0%</b>", styles["TableCellCenter"])],
        [Paragraph("Google Gemini Mention Rate", styles["TableCellBold"]), Paragraph("0.0%", styles["TableCellCenter"]), Paragraph("10.0%", styles["TableCellCenter"]), Paragraph("20.0%", styles["TableCellCenter"]), Paragraph("<b>> 35.0%</b>", styles["TableCellCenter"])],
        [Paragraph("Claude 3.5 Sonnet Mention Rate", styles["TableCellBold"]), Paragraph("0.0%", styles["TableCellCenter"]), Paragraph("10.0%", styles["TableCellCenter"]), Paragraph("20.0%", styles["TableCellCenter"]), Paragraph("<b>> 35.0%</b>", styles["TableCellCenter"])],
        [Paragraph("Aggregate AI Mention Rate", styles["TableCellBold"]), Paragraph("<b>0.0%</b>", styles["TableCellCenter"]), Paragraph("<b>11.8%</b>", styles["TableCellCenter"]), Paragraph("<b>23.8%</b>", styles["TableCellCenter"]), Paragraph("<b>> 40.0%</b>", styles["TableCellCenter"])],
        [Paragraph("Monthly Qualified Signups", styles["TableCellBold"]), Paragraph("~40 users", styles["TableCellCenter"]), Paragraph("350 users", styles["TableCellCenter"]), Paragraph("1,100 users", styles["TableCellCenter"]), Paragraph("<b>2,500+ Users</b>", styles["TableCellCenter"])]
    ]
    t_kpi = Table(kpi_rows, colWidths=[150, 85, 85, 85, 99])
    t_kpi.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_LIGHT),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG])
    ]))
    story.append(t_kpi)
    story.append(Spacer(1, 10))

    # ================= RISK ASSESSMENT MATRIX =================
    story.append(Paragraph("Risk Assessment & Mitigation Matrix", styles["SectionHeader"]))
    risk_rows = [
        [Paragraph("<b>Risk Factor</b>", styles["TableHeader"]), Paragraph("<b>Prob / Impact</b>", styles["TableHeader"]), Paragraph("<b>Proactive Mitigation Strategy</b>", styles["TableHeader"])],
        [Paragraph("<b>LLM Output Stochasticity</b>", styles["TableCellBold"]), Paragraph("High / Med", styles["TableCellCenter"]), Paragraph("Measure on 2 distinct days; use temperature=0 or deterministic scraping; track multiple models (ChatGPT, Gemini, Perplexity, Claude) to smooth variance.", styles["TableCell"])],
        [Paragraph("<b>Google Helpful Content Updates</b>", styles["TableCellBold"]), Paragraph("Med / High", styles["TableCellCenter"]), Paragraph("100% original content, authentic product screenshots, verified step-by-step guides, answers in first 2 sentences. Strictly zero keyword stuffing or low-quality AI rehash.", styles["TableCell"])],
        [Paragraph("<b>Competitor Retaliation</b>", styles["TableCellBold"]), Paragraph("High / Low", styles["TableCellCenter"]), Paragraph("Compete on IncuBrix's unique value proposition: the ONLY tool combining text video editing + 1-to-10 repurposing + direct publishing. Point solutions cannot easily duplicate this.", styles["TableCell"])],
        [Paragraph("<b>Subdomain Authority Leaks</b>", styles["TableCellBold"]), Paragraph("Med / Med", styles["TableCellCenter"]), Paragraph("Implement cross-subdomain canonical headers and reciprocal linking from app.incubrix.com dashboard directly back to marketing workflow hubs.", styles["TableCell"])]
    ]
    t_risk = Table(risk_rows, colWidths=[130, 80, 294])
    t_risk.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_LIGHT),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG])
    ]))
    story.append(t_risk)
    story.append(Spacer(1, 10))

    # ================= MONDAY MORNING KICKOFF CHECKLIST =================
    story.append(Paragraph("Immediate Next Monday Morning Sprint Checklist (Day 1)", styles["SectionHeader"]))
    checklist_data = [
        [Paragraph("<b>Time</b>", styles["TableHeader"]), Paragraph("<b>Action Item & Specific Deliverable</b>", styles["TableHeader"]), Paragraph("<b>PR / Verification Target</b>", styles["TableHeader"])],
        [Paragraph("09:00 AM", styles["TableCellCenter"]), Paragraph("<b>Standup & Ownership Assignment:</b> Review workbook with Growth Engineer; assign PRs.", styles["TableCell"]), Paragraph("PR 1 (Redirects), PR 2 (llms.txt), PR 3 (Schema)", styles["TableCell"])],
        [Paragraph("10:30 AM", styles["TableCellCenter"]), Paragraph("<b>Fix 308 Redirects:</b> Update sitewide nav/footer links from .html to canonical root paths (/about, /pricing).", styles["TableCell"]), Paragraph("PR 1 merged; curl -I /about.html returns 0 redirect hops", styles["TableCell"])],
        [Paragraph("11:15 AM", styles["TableCellCenter"]), Paragraph("<b>Deploy AI Manifests:</b> Copy FIX-01 (/llms.txt) and FIX-18 (/llms-full.txt) to root; update robots.txt (FIX-06).", styles["TableCell"]), Paragraph("curl -I https://incubrix.com/llms.txt returns 200 OK", styles["TableCell"])],
        [Paragraph("01:00 PM", styles["TableCellCenter"]), Paragraph("<b>Schema Injection:</b> Paste SoftwareApplication and Organization JSON-LD schemas into index.html <head>.", styles["TableCell"]), Paragraph("Google Rich Results Test confirms valid schema", styles["TableCell"])],
        [Paragraph("02:30 PM", styles["TableCellCenter"]), Paragraph("<b>Edge Verification:</b> Run curl edge headers and Lighthouse audit.", styles["TableCell"]), Paragraph("Lighthouse Mobile Performance >= 95, 0 errors", styles["TableCell"])],
        [Paragraph("04:00 PM", styles["TableCellCenter"]), Paragraph("<b>First Content Page Staging:</b> Stage Page 01 ('How to repurpose long video into shorts') under /hub/.", styles["TableCell"]), Paragraph("Submit URL to Google Search Console for immediate crawl", styles["TableCell"])],
        [Paragraph("05:30 PM", styles["TableCellCenter"]), Paragraph("<b>Automated Tracker Setup:</b> Verify local Python tracker and configure weekly scheduled task.", styles["TableCell"]), Paragraph("python engine/main.py run --quick executes cleanly", styles["TableCell"])]
    ]
    t_chk = Table(checklist_data, colWidths=[65, 275, 164])
    t_chk.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_LIGHT),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG])
    ]))
    story.append(t_chk)

    doc.build(story, canvasmaker=LaunchKitCanvas)
    print(f"Generated cool executive PDF: {pdf_path}")

if __name__ == "__main__":
    generate_launch_kit_pdf()
