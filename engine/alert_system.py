"""
engine/alert_system.py
Alerting and scheduled change detection engine for IncuBrix.
Detects rank improvements, AI assistant mention changes, and Answer Box flips between runs.
"""

from datetime import datetime
from typing import List, Dict, Optional
from engine.models import EngineResult, AlertItem

class AlertEngine:
    def detect_changes(self, previous_results: List[EngineResult], current_results: List[EngineResult]) -> List[AlertItem]:
        """
        Compares two snapshot runs and generates high-priority alerts.
        """
        alerts: List[AlertItem] = []
        prev_map: Dict[str, EngineResult] = {r.qid: r for r in previous_results}
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for curr in current_results:
            prev = prev_map.get(curr.qid)
            if not prev:
                continue

            # 1. Google Rank Change Alert
            if prev.google_rank != curr.google_rank:
                alerts.append(AlertItem(
                    timestamp=now_str,
                    qid=curr.qid,
                    question=curr.raw_response_snippet or "",
                    alert_type="SERP_RANK_CHANGE",
                    previous_value=prev.google_rank,
                    new_value=curr.google_rank,
                    details=f"IncuBrix Google SERP position shifted from {prev.google_rank} to {curr.google_rank}."
                ))

            # 2. Answer Box Capture / Loss
            if prev.answer_box_domain != curr.answer_box_domain:
                alerts.append(AlertItem(
                    timestamp=now_str,
                    qid=curr.qid,
                    question=curr.raw_response_snippet or "",
                    alert_type="ANSWER_BOX_SHIFT",
                    previous_value=prev.answer_box_domain,
                    new_value=curr.answer_box_domain,
                    details=f"Quoted snippet domain changed from {prev.answer_box_domain} to {curr.answer_box_domain}."
                ))

            # 3. AI Assistant Mentions Shift
            ai_prev_total = sum([prev.chatgpt_mentions, prev.gemini_mentions, prev.perplexity_mentions, prev.claude_mentions])
            ai_curr_total = sum([curr.chatgpt_mentions, curr.gemini_mentions, curr.perplexity_mentions, curr.claude_mentions])
            if ai_prev_total != ai_curr_total:
                alerts.append(AlertItem(
                    timestamp=now_str,
                    qid=curr.qid,
                    question=curr.raw_response_snippet or "",
                    alert_type="AI_MENTION_SHIFT",
                    previous_value=f"{ai_prev_total}/4 AI Assistants",
                    new_value=f"{ai_curr_total}/4 AI Assistants",
                    details=f"AI Assistant mentions shifted from {ai_prev_total}/4 to {ai_curr_total}/4 for {curr.qid}."
                ))

        return alerts
