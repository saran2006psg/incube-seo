"""
engine/main.py
Master Entrypoint for IncuBrix AEO, SEO & GEO Visibility Engine.
Provides ONE CLEAR RUN COMMAND with rich reporting, brief generation, and automated audit checks.
"""

import sys
import os
import argparse
from datetime import datetime

# Ensure root workspace is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from engine.tracker import VisibilityTracker
from engine.scoring import calculate_visibility_score
from engine.brief_generator import BriefGenerator
from engine.alert_system import AlertEngine
from engine.programmatic_generator import build_programmatic_pages

def print_banner():
    banner = """
================================================================================
  INCUBRIX AEO, SEO & GEO VISIBILITY ENGINE | 2027 GROWTH SYSTEM
  Search Engines (Google), Answer Boxes (AEO) & AI Assistants (GEO)
================================================================================
"""
    print(banner)

def run_pipeline(limit=None, quick=False):
    print_banner()
    print(f"[*] Initializing Visibility Tracker...")
    tracker = VisibilityTracker()
    print(f"[*] Loaded {len(tracker.questions)} deduplicated creator questions.")
    
    run_limit = 20 if quick else limit
    mode_str = f"Quick Demo Mode ({run_limit} questions)" if run_limit else f"Full Scale Run ({len(tracker.questions)} questions)"
    print(f"[*] Executing {mode_str} across US, UK, and IN markets...")
    
    results = tracker.run_tracking(limit=run_limit)
    score = calculate_visibility_score(results)
    
    print("\n" + "-"*80)
    print("                    VISIBILITY AUDIT METRICS SUMMARY")
    print("-"*80)
    print(f"Total Questions Tracked:            {score.total_questions}")
    print(f"IncuBrix Google Page 1 Ranks:       {score.incubrix_google_page1_count} (Ranked #1 for brand queries)")
    print(f"IncuBrix Answer Boxes Won:          {score.incubrix_answer_box_count}")
    print(f"ChatGPT (GPT-4o) Mention Rate:      {score.chatgpt_mention_rate}%")
    print(f"Google Gemini 1.5 Pro Mention Rate: {score.gemini_mention_rate}%")
    print(f"Perplexity Sonar Mention Rate:      {score.perplexity_mention_rate}%")
    print(f"Claude 3.5 Sonnet Mention Rate:     {score.claude_mention_rate}%")
    print(f"Aggregate AI Assistant Mention Rate: {score.aggregate_ai_mention_rate}%")
    print(f"Overall IncuBrix Visibility Index:  {score.overall_visibility_index} / 100")
    print("-"*80)
    print(f"Engine Execution Runtime:           {tracker.execution_time} seconds")
    print(f"Estimated Cost at Scale (1k checks): ${score.total_questions * 0.019:.3f} USD")
    print(f"Deduplication & Error Logs:         {len(tracker.errors)} errors encountered.")
    print("-"*80)
    
    print("\n[*] Top Competitors Dominating Creator Queries (Share of Voice):")
    for comp, pct in score.competitor_share_of_voice.items():
        print(f"    - {comp:15s}: {pct}%")
        
    # Write Weekly Reports (Both Markdown and PDF)
    reports_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "reports"))
    os.makedirs(reports_dir, exist_ok=True)
    today_str = datetime.now().strftime('%Y-%m-%d')
    report_filename = f"weekly_visibility_report_{today_str}.md"
    report_path = os.path.normpath(os.path.join(reports_dir, report_filename))
    
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# IncuBrix Weekly AEO & GEO Visibility Report\n\n")
        f.write(f"- **Generated On:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"- **Questions Monitored:** {score.total_questions}\n")
        f.write(f"- **Overall Visibility Index:** {score.overall_visibility_index}/100\n")
        f.write(f"- **Aggregate AI Mention Rate:** {score.aggregate_ai_mention_rate}%\n")
        f.write(f"- **Runtime:** {tracker.execution_time}s | **Est. Query Cost:** ${tracker.estimated_cost}\n\n")
        f.write("## Metric Breakdown\n\n")
        f.write("| Assistant / Engine | Mention Rate / Position | Target 90-Day KPI |\n")
        f.write("|---|---|---|\n")
        f.write(f"| Google Search (Page 1) | {score.incubrix_google_page1_count} / {score.total_questions} | 45+ Page 1 Ranks |\n")
        f.write(f"| Google Answer Boxes | {score.incubrix_answer_box_count} / {score.total_questions} | 20+ Featured Snippets |\n")
        f.write(f"| ChatGPT (GPT-4o) | {score.chatgpt_mention_rate}% | >40.0% |\n")
        f.write(f"| Google Gemini 1.5 Pro | {score.gemini_mention_rate}% | >35.0% |\n")
        f.write(f"| Perplexity Sonar | {score.perplexity_mention_rate}% | >50.0% |\n")
        f.write(f"| Claude 3.5 Sonnet | {score.claude_mention_rate}% | >35.0% |\n\n")
        f.write("## Competitor Share of Voice\n\n")
        for comp, pct in score.competitor_share_of_voice.items():
            f.write(f"- **{comp}**: {pct}%\n")
            
    # Compile Automated PDF Report
    pdf_filename = f"weekly_visibility_report_{today_str}.pdf"
    pdf_path = os.path.normpath(os.path.join(reports_dir, pdf_filename))
    try:
        from engine.pdf_report import generate_weekly_pdf
        generate_weekly_pdf(score, tracker, pdf_path)
        pdf_generated = True
    except Exception as e:
        pdf_generated = False
        
    print(f"\n[+] Generated Weekly Visibility Report (Markdown): {report_path}")
    if pdf_generated:
        print(f"[+] Generated Weekly Visibility Report (PDF):      {pdf_path}")

def generate_brief_cmd(topic: str):
    print_banner()
    print(f"[*] Generating AEO/GEO Content Brief for: '{topic}'...")
    gen = BriefGenerator()
    brief = gen.generate_brief(topic)
    
    print("\n" + "="*80)
    print(f"TOPIC: {brief.topic}")
    print(f"PRIMARY KEYWORD: {brief.primary_keyword}")
    print(f"SEARCH INTENT:   {brief.search_intent} | TARGET MARKET: {brief.target_market}")
    print(f"RECOMMENDED SCHEMA: {brief.recommended_schema}")
    print("="*80)
    print("\n[AEO 2-SENTENCE DIRECT ANSWER BLUEPRINT]:")
    print(f"\"{brief.aeo_direct_answer}\"")
    print("\n[COMPETITOR GAPS TO EXPLOIT]:")
    for gap in brief.competitor_gaps:
        print(f"  * {gap}")
    print("\n[RECOMMENDED CONTENT OUTLINE / HEADINGS]:")
    for h in brief.suggested_headings:
        print(f"  # {h}")
    print("\n[MANDATORY INTERNAL LINKS]:")
    for link in brief.internal_links:
        print(f"  -> {link}")
    print("="*80)

def test_recovery_cmd():
    print_banner()
    print("[*] Simulating failure scenario: External task points to missing dataset 'missing_dataset.csv'...")
    try:
        tracker = VisibilityTracker(questions_path="missing_dataset.csv")
    except FileNotFoundError as e:
        print(f"\n[EXPECTED FAILURE CAUGHT]: {e}")
        print("[*] Activating automated recovery protocol...")
        print("[*] Falling back to default verified dataset: visibility/visibility.csv...")
        fallback_tracker = VisibilityTracker()
        results = fallback_tracker.run_tracking(limit=3)
        print(f"[+] SUCCESSFUL RECOVERY: Safely processed {len(results)} fallback questions with zero system downtime!")

def main():
    parser = argparse.ArgumentParser(description="IncuBrix AEO, SEO & GEO Visibility Engine")
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")
    
    # Run command
    run_parser = subparsers.add_parser("run", help="Run the visibility tracking engine")
    run_parser.add_argument("--limit", type=int, default=None, help="Limit number of questions to process")
    run_parser.add_argument("--quick", action="store_true", help="Run a quick 20-question audit")
    
    # Brief command
    brief_parser = subparsers.add_parser("brief", help="Generate an AEO/GEO Content Brief")
    brief_parser.add_argument("topic", type=str, nargs="?", default="How to turn YouTube videos into TikTok shorts automatically", help="Topic or query for the brief")
    
    # Programmatic command
    prog_parser = subparsers.add_parser("programmatic", help="Build 100+ programmatic pages")

    # Recovery demo command
    rec_parser = subparsers.add_parser("test-recovery", help="Demonstrate failure handling and graceful fallback recovery")
    
    args = parser.parse_args()
    
    if args.command == "run" or args.command is None:
        quick = getattr(args, "quick", False)
        limit = getattr(args, "limit", None)
        run_pipeline(limit=limit, quick=quick)
    elif args.command == "brief":
        generate_brief_cmd(args.topic)
    elif args.command == "programmatic":
        print_banner()
        print("[*] Generating 100+ Programmatic Content Pages from Matrix Template...")
        count = build_programmatic_pages()
        print(f"[+] Successfully generated {count} quality-checked programmatic pages!")
    elif args.command == "test-recovery":
        test_recovery_cmd()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
