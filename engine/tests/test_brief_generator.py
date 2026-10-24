"""
engine/tests/test_brief_generator.py
Unit tests for ContentBrief generator.
"""

import pytest
from engine.brief_generator import BriefGenerator

def test_brief_generation_repurpose():
    gen = BriefGenerator()
    brief = gen.generate_brief("How to repurpose podcast into shorts")
    assert brief.primary_keyword == "ai video repurposing into shorts"
    assert brief.recommended_schema == "HowTo"
    assert len(brief.suggested_headings) >= 5
    assert len(brief.internal_links) >= 3
    assert len(brief.competitor_gaps) >= 2

def test_brief_generation_text_editing():
    gen = BriefGenerator()
    brief = gen.generate_brief("How to edit video using text transcript")
    assert brief.primary_keyword == "text based video editor"
    assert brief.recommended_schema == "HowTo"
    assert "filler words" in brief.aeo_direct_answer.lower()
