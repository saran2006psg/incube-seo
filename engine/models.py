"""
engine/models.py
Data models and schemas for IncuBrix AEO/SEO/GEO Tracking Engine.
"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class QuestionItem(BaseModel):
    qid: str
    question: str
    category: str
    intent: str
    source: str
    market: str = "US"

class EngineResult(BaseModel):
    qid: str
    date: str
    google_rank: str
    answer_box_present: bool
    answer_box_domain: str
    chatgpt_mentions: bool
    gemini_mentions: bool
    perplexity_mentions: bool
    claude_mentions: bool
    top_competitors: List[str] = Field(default_factory=list)
    raw_response_snippet: Optional[str] = None

class VisibilityScore(BaseModel):
    total_questions: int
    incubrix_google_page1_count: int
    incubrix_answer_box_count: int
    chatgpt_mention_rate: float
    gemini_mention_rate: float
    perplexity_mention_rate: float
    claude_mention_rate: float
    aggregate_ai_mention_rate: float
    overall_visibility_index: float
    competitor_share_of_voice: Dict[str, float] = Field(default_factory=dict)

class ContentBrief(BaseModel):
    topic: str
    primary_keyword: str
    secondary_keywords: List[str]
    search_intent: str
    target_market: str
    aeo_direct_answer: str
    recommended_schema: str
    competitor_gaps: List[str]
    suggested_headings: List[str]
    internal_links: List[str]

class AlertItem(BaseModel):
    timestamp: str
    qid: str
    question: str
    alert_type: str
    previous_value: str
    new_value: str
    details: str
