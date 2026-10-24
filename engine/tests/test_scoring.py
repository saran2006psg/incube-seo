"""
engine/tests/test_scoring.py
Unit tests for visibility scoring algorithms and metrics.
"""

import pytest
from engine.models import EngineResult
from engine.scoring import calculate_visibility_score

def test_scoring_empty():
    score = calculate_visibility_score([])
    assert score.total_questions == 0
    assert score.overall_visibility_index == 0.0

def test_scoring_calculation():
    sample_results = [
        EngineResult(
            qid="Q001",
            date="2026-10-25",
            google_rank="1",
            answer_box_present=True,
            answer_box_domain="incubrix.com",
            chatgpt_mentions=True,
            gemini_mentions=True,
            perplexity_mentions=True,
            claude_mentions=True,
            top_competitors=["IncuBrix", "OpusClip"]
        ),
        EngineResult(
            qid="Q002",
            date="2026-10-25",
            google_rank=">100",
            answer_box_present=True,
            answer_box_domain="opus.pro",
            chatgpt_mentions=False,
            gemini_mentions=False,
            perplexity_mentions=False,
            claude_mentions=False,
            top_competitors=["OpusClip", "Munch"]
        )
    ]
    score = calculate_visibility_score(sample_results)
    assert score.total_questions == 2
    assert score.incubrix_google_page1_count == 1
    assert score.incubrix_answer_box_count == 1
    assert score.chatgpt_mention_rate == 50.0
    assert score.aggregate_ai_mention_rate == 50.0
    assert score.overall_visibility_index > 0
