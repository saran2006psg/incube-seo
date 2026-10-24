"""
engine/scoring.py
Visibility scoring algorithm, competitor share-of-voice calculations,
and metric aggregation for IncuBrix.
"""

from typing import List, Dict
from engine.models import EngineResult, VisibilityScore

def calculate_visibility_score(results: List[EngineResult]) -> VisibilityScore:
    """
    Computes mathematical visibility metrics across Google SERPs and 4 AI assistants.
    Ensures 100% reproducible and verifiable numbers.
    """
    total = len(results)
    if total == 0:
        return VisibilityScore(
            total_questions=0,
            incubrix_google_page1_count=0,
            incubrix_answer_box_count=0,
            chatgpt_mention_rate=0.0,
            gemini_mention_rate=0.0,
            perplexity_mention_rate=0.0,
            claude_mention_rate=0.0,
            aggregate_ai_mention_rate=0.0,
            overall_visibility_index=0.0,
            competitor_share_of_voice={}
        )

    page1_count = 0
    answer_box_count = 0
    chatgpt_count = 0
    gemini_count = 0
    perplexity_count = 0
    claude_count = 0
    competitor_mentions: Dict[str, int] = {}

    for r in results:
        # Check Google Page 1 (Rank 1-10)
        try:
            rank_num = int(r.google_rank)
            if rank_num <= 10:
                page1_count += 1
        except ValueError:
            pass  # ">100" or unranked

        # Check Answer Box capture
        if r.answer_box_domain.lower() in ["incubrix.com", "www.incubrix.com"]:
            answer_box_count += 1

        # Check AI mentions
        if r.chatgpt_mentions:
            chatgpt_count += 1
        if r.gemini_mentions:
            gemini_count += 1
        if r.perplexity_mentions:
            perplexity_count += 1
        if r.claude_mentions:
            claude_count += 1

        # Tally competitors
        for comp in r.top_competitors:
            comp_clean = comp.strip()
            if comp_clean:
                competitor_mentions[comp_clean] = competitor_mentions.get(comp_clean, 0) + 1

    chatgpt_rate = round((chatgpt_count / total) * 100, 2)
    gemini_rate = round((gemini_count / total) * 100, 2)
    perplexity_rate = round((perplexity_count / total) * 100, 2)
    claude_rate = round((claude_count / total) * 100, 2)
    
    total_ai_checks = total * 4
    total_ai_mentions = chatgpt_count + gemini_count + perplexity_count + claude_count
    aggregate_ai_rate = round((total_ai_mentions / total_ai_checks) * 100, 2)

    # Calculate Overall Visibility Index (0 - 100 scale)
    # Weights: Page 1 rank (30%), Answer box (30%), AI mentions (40%)
    serp_component = (page1_count / total) * 30.0
    ans_box_component = (answer_box_count / total) * 30.0
    ai_component = (aggregate_ai_rate / 100.0) * 40.0
    visibility_index = round(serp_component + ans_box_component + ai_component, 2)

    # Share of voice among top competitors
    sov = {}
    total_comp_mentions = sum(competitor_mentions.values()) or 1
    for comp, count in sorted(competitor_mentions.items(), key=lambda x: x[1], reverse=True)[:10]:
        sov[comp] = round((count / total_comp_mentions) * 100, 1)

    return VisibilityScore(
        total_questions=total,
        incubrix_google_page1_count=page1_count,
        incubrix_answer_box_count=answer_box_count,
        chatgpt_mention_rate=chatgpt_rate,
        gemini_mention_rate=gemini_rate,
        perplexity_mention_rate=perplexity_rate,
        claude_mention_rate=claude_rate,
        aggregate_ai_mention_rate=aggregate_ai_rate,
        overall_visibility_index=visibility_index,
        competitor_share_of_voice=sov
    )
