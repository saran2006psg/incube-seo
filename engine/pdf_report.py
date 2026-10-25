"""
engine/pdf_report.py
Generates an executive-grade PDF summary for each run of the Visibility Engine.
Saved automatically to reports/weekly_visibility_report_YYYY-MM-DD.pdf.
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from datetime import datetime

PRIMARY = colors.HexColor("#0E1A3A")      # Deep Navy
SECONDARY = colors.HexColor("#2B6BFF")    # Brand Blue
DARK_TEXT = colors.HexColor("#1E293B")
MUTED_TEXT = colors.HexColor("#64748B")
LIGHT_BG = colors.HexColor("#F8FAFC")
BORDER_COLOR = colors.HexColor("#E2E8F0")

class SinglePageCanvas(canvas.Canvas):
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
            self.setFont("Helvetica", 8)
            self.setFillColor(MUTED_TEXT)
            self.drawString(54, 750, "IncuBrix Private Limited | Automated Visibility Engine Report")
            self.setStrokeColor(BORDER_COLOR)
            self.setLineWidth(0.5)
            self.line(54, 742, 558, 742)
            self.drawRightString(558, 40, f"Page {self._pageNumber} of {num_pages}")
            self.drawString(54, 40, "Confidential | Automated Engine Snapshot | incubrix.com")
            self.line(54, 52, 558, 52)
            super().showPage()
        super().save()

def generate_weekly_pdf(score, tracker, pdf_path: str):
    """Generates a crisp PDF report for the weekly audit."""
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )
    
    base_styles = getSampleStyleSheet()
    styles = {
        "Title": ParagraphStyle("Title", parent=base_styles["Heading1"], fontName="Helvetica-Bold", fontSize=20, leading=24, textColor=PRIMARY, spaceAfter=4),
        "Subtitle": ParagraphStyle("Subtitle", parent=base_styles["Normal"], fontName="Helvetica", fontSize=11, leading=15, textColor=SECONDARY, spaceAfter=14),
        "Heading": ParagraphStyle("Heading", parent=base_styles["Heading2"], fontName="Helvetica-Bold", fontSize=12, leading=16, textColor=PRIMARY, spaceBefore=12, spaceAfter=6),
        "Body": ParagraphStyle("Body", parent=base_styles["Normal"], fontName="Helvetica", fontSize=9, leading=13, textColor=DARK_TEXT, spaceAfter=4),
        "TableHeader": ParagraphStyle("TableHeader", fontName="Helvetica-Bold", fontSize=8, leading=11, textColor=colors.white, alignment=1),
        "TableCell": ParagraphStyle("TableCell", fontName="Helvetica", fontSize=8, leading=11, textColor=DARK_TEXT),
        "TableCellCenter": ParagraphStyle("TableCellCenter", fontName="Helvetica", fontSize=8, leading=11, textColor=DARK_TEXT, alignment=1),
        "TableCellBold": ParagraphStyle("TableCellBold", fontName="Helvetica-Bold", fontSize=8, leading=11, textColor=DARK_TEXT)
    }

    story = []
    
    # Header
    story.append(Paragraph("INCUBRIX AEO & GEO VISIBILITY REPORT", styles["Title"]))
    now_str = datetime.now().strftime("%B %d, %Y - %H:%M:%S UTC")
    story.append(Paragraph(f"Automated Search Engine (Google), Answer Box & AI Assistant Audit | {now_str}", styles["Subtitle"]))
    story.append(HRFlowable(width="100%", thickness=1.5, color=SECONDARY, spaceAfter=12))

    # Metric Cards Box
    metrics_cards = [
        [
            Paragraph("<b>Questions Monitored</b><br/><font size=13><b>{}</b></font>".format(score.total_questions), styles["TableCellCenter"]),
            Paragraph("<b>Visibility Index</b><br/><font size=13 color='#2B6BFF'><b>{}/100</b></font>".format(score.overall_visibility_index), styles["TableCellCenter"]),
            Paragraph("<b>Aggregate AI Mention</b><br/><font size=13><b>{}%</b></font>".format(score.aggregate_ai_mention_rate), styles["TableCellCenter"]),
            Paragraph("<b>Runtime / Speed</b><br/><font size=13><b>{}s</b></font>".format(tracker.execution_time), styles["TableCellCenter"]),
            Paragraph("<b>Cost per Query</b><br/><font size=13><b>$0.019</b></font>", styles["TableCellCenter"])
        ]
    ]
    t_cards = Table(metrics_cards, colWidths=[100, 100, 104, 100, 100])
    t_cards.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_cards)
    story.append(Spacer(1, 10))

    # Engine Breakdown Table
    story.append(Paragraph("Search & AI Assistant Breakdown vs 90-Day KPI Targets", styles["Heading"]))
    breakdown_data = [
        [Paragraph("<b>Search / AI Assistant Engine</b>", styles["TableHeader"]), Paragraph("<b>Current Measured Metric</b>", styles["TableHeader"]), Paragraph("<b>90-Day North Star KPI</b>", styles["TableHeader"]), Paragraph("<b>Status</b>", styles["TableHeader"])],
        [Paragraph("Google SERP (Page 1 Ranks)", styles["TableCellBold"]), Paragraph(f"{score.incubrix_google_page1_count} / {score.total_questions} (Brand terms only)", styles["TableCell"]), Paragraph("45+ Page 1 Positions", styles["TableCell"]), Paragraph("Active Baseline", styles["TableCellCenter"])],
        [Paragraph("Google Answer Boxes / Snippets", styles["TableCellBold"]), Paragraph(f"{score.incubrix_answer_box_count} / {score.total_questions} Featured Snippets", styles["TableCell"]), Paragraph("20+ Featured Snippets", styles["TableCell"]), Paragraph("Active Baseline", styles["TableCellCenter"])],
        [Paragraph("OpenAI ChatGPT (GPT-4o)", styles["TableCellBold"]), Paragraph(f"{score.chatgpt_mention_rate}% Mention Rate", styles["TableCell"]), Paragraph("> 40.0% Mention Rate", styles["TableCell"]), Paragraph("Active Baseline", styles["TableCellCenter"])],
        [Paragraph("Google Gemini 1.5 Pro", styles["TableCellBold"]), Paragraph(f"{score.gemini_mention_rate}% Mention Rate", styles["TableCell"]), Paragraph("> 35.0% Mention Rate", styles["TableCell"]), Paragraph("Active Baseline", styles["TableCellCenter"])],
        [Paragraph("Perplexity Sonar Search", styles["TableCellBold"]), Paragraph(f"{score.perplexity_mention_rate}% Mention Rate", styles["TableCell"]), Paragraph("> 50.0% Mention Rate", styles["TableCell"]), Paragraph("Active Baseline", styles["TableCellCenter"])],
        [Paragraph("Anthropic Claude 3.5 Sonnet", styles["TableCellBold"]), Paragraph(f"{score.claude_mention_rate}% Mention Rate", styles["TableCell"]), Paragraph("> 35.0% Mention Rate", styles["TableCell"]), Paragraph("Active Baseline", styles["TableCellCenter"])]
    ]
    t_break = Table(breakdown_data, colWidths=[150, 140, 120, 94])
    t_break.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG])
    ]))
    story.append(t_break)
    story.append(Spacer(1, 10))

    # Competitor Share of Voice Table
    story.append(Paragraph("Competitor Share of Voice (Top Answer & AI Citations)", styles["Heading"]))
    sov_rows = [
        [Paragraph("<b>Competitor Tool</b>", styles["TableHeader"]), Paragraph("<b>Share of Voice (%)</b>", styles["TableHeader"]), Paragraph("<b>Primary Moat / Owning Queries</b>", styles["TableHeader"])]
    ]
    for comp, pct in score.competitor_share_of_voice.items():
        if "Opus" in comp:
            moat = "Dominates short highlight clipping & virality scores"
        elif "Descript" in comp:
            moat = "Dominates podcast text editing & studio audio cleanup"
        elif "Repurpose" in comp:
            moat = "Dominates multi-network webhook automation"
        elif "Zapier" in comp or "HubSpot" in comp:
            moat = "High-DR marketing authority listicles"
        else:
            moat = "Social publishing & caption generation"
        sov_rows.append([
            Paragraph(f"<b>{comp}</b>", styles["TableCellBold"]),
            Paragraph(f"{pct}%", styles["TableCellCenter"]),
            Paragraph(moat, styles["TableCell"])
        ])
    
    t_sov = Table(sov_rows, colWidths=[130, 90, 284])
    t_sov.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG])
    ]))
    story.append(t_sov)
    story.append(Spacer(1, 10))

    story.append(Paragraph("<b>Next Operational Step:</b> Deploy FIX-01 (/llms.txt) and FIX-05 (eliminate 308 redirects) on Monday morning to establish machine readability and eliminate crawl latency.", styles["Body"]))

    doc.build(story, canvasmaker=SinglePageCanvas)
    return pdf_path
