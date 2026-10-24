"""
engine/config.py
Configuration parameters, weights, markets, and runtime options for the IncuBrix Visibility Engine.
"""

import os
from typing import Dict, List

# Target Markets
TARGET_MARKETS: List[str] = ["US", "UK", "IN"]

# Default Question File
DEFAULT_QUESTIONS_PATH = os.path.join(os.path.dirname(__file__), "..", "visibility", "visibility.csv")
RAW_ANSWERS_DIR = os.path.join(os.path.dirname(__file__), "..", "visibility", "raw_answers")
REPORTS_DIR = os.path.join(os.path.dirname(__file__), "..", "reports")

# Target Search & AI Engines
TRACKED_ENGINES: List[str] = [
    "Google SERP",
    "Google AI Overviews",
    "OpenAI ChatGPT (GPT-4o)",
    "Google Gemini 1.5 Pro",
    "Perplexity Sonar",
    "Anthropic Claude 3.5 Sonnet"
]

# Scoring Weights (Total: 100 points)
SCORING_WEIGHTS: Dict[str, float] = {
    "google_top_3": 40.0,
    "google_page_1": 20.0,
    "answer_box_share": 25.0,
    "ai_assistant_mention": 35.0  # Distributed across the 4 AI assistants (8.75 pts each)
}

# Runtime Cost Estimation (USD per 1,000 queries)
COST_ESTIMATES = {
    "serp_api_per_query": 0.003,       # ~$3.00 per 1,000 SERP checks
    "llm_query_avg_cost": 0.004,       # ~$4.00 per 1,000 LLM queries
    "total_cost_per_question": 0.019   # 1 SERP + 4 LLMs = ~$0.019 per question check
}

# Thresholds for Visibility Change Alerts
ALERT_THRESHOLDS = {
    "rank_improvement_delta": 3,       # Alert if rank improves by 3+ positions
    "ai_mention_change": True,         # Alert if AI mention status flips (No -> Yes or Yes -> No)
    "answer_box_won": True             # Alert if IncuBrix captures an answer box
}
