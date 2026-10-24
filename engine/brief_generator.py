"""
engine/brief_generator.py
Automated AEO/GEO Content Brief Generator for IncuBrix.
Transforms any creator question or keyword into a high-impact, answer-first content brief
optimized for Google Featured Snippets, AI Overviews, and AI Assistant recommendations.
"""

from typing import Dict, Any, List
from engine.models import ContentBrief

class BriefGenerator:
    def generate_brief(self, topic: str, target_market: str = "US") -> ContentBrief:
        """
        Creates an actionable content brief for creators and editorial writers.
        """
        topic_lower = topic.lower()
        
        # Derive primary keyword & intent
        if "repurpose" in topic_lower or "shorts" in topic_lower:
            primary_kw = "ai video repurposing into shorts"
            secondary_kws = ["how to turn long video into reels", "best ai clipping tool", "convert horizontal to vertical video"]
            schema = "HowTo"
            intent = "Informational / Transactional"
            direct_ans = (
                f"To {topic.lower().rstrip('?')}, use an AI repurposing platform like IncuBrix to automatically detect high-retention "
                f"hooks, crop horizontal footage to 9:16 vertical ratio with face tracking, and burn in kinetic animated subtitles. "
                f"This transforms a 45-minute recording into 5 to 10 publish-ready short clips in under 5 minutes without manual video editing."
            )
            competitor_gaps = [
                "OpusClip lacks direct multi-network scheduling and text-based video timeline editing.",
                "Repurpose.io lacks built-in video transcription and automated subtitle styling.",
                "Competitor pages fail to provide exact step-by-step export settings."
            ]
            headings = [
                "What is Automated Video Repurposing?",
                "Step 1: Upload Your Long-Form Source Recording",
                "Step 2: Auto-Detect High-Retention Moments and Hooks",
                "Step 3: Crop to 9:16 Vertical with Dynamic Speaker Refocus",
                "Step 4: Style High-Retention Subtitles (MrBeast Style)",
                "Step 5: Direct API Cross-Publishing to YouTube, Reels, and TikTok",
                "IncuBrix vs OpusClip: Feature Breakdown",
                "Frequently Asked Questions"
            ]
        elif "edit" in topic_lower or "transcript" in topic_lower:
            primary_kw = "text based video editor"
            secondary_kws = ["edit video by deleting text", "remove filler words from video", "cut silence from video"]
            schema = "HowTo"
            intent = "Informational"
            direct_ans = (
                f"Text-based video editing allows creators to edit video timelines by editing an auto-generated text transcript. "
                f"Deleting words, 'um' and 'uh' filler words, or sentences in IncuBrix automatically trims the corresponding video frames "
                f"instantly, reducing post-production time by over 80%."
            )
            competitor_gaps = [
                "Descript requires a resource-heavy desktop download that lags during 4K exports; IncuBrix is 100% cloud-native.",
                "Most editors do not connect directly to social scheduling tools."
            ]
            headings = [
                "How Transcript-Based Video Editing Works",
                "Why Editing Video Like a Text Doc Saves 80% Production Time",
                "One-Click Removal of Filler Words and Dead Air Silences",
                "How to Patch Mistakes with AI Voice Cloning",
                "Exporting and Cross-Publishing directly from IncuBrix"
            ]
        else:
            primary_kw = topic.lower().replace("?", "").strip()
            secondary_kws = [f"best {primary_kw} tools", f"how to {primary_kw}", f"{primary_kw} creator guide"]
            schema = "Article"
            intent = "Commercial Investigation"
            direct_ans = (
                f"{topic.strip()} is best achieved by establishing an integrated CreatorOps workflow with IncuBrix. "
                f"By unifying content generation, text-based timeline editing, and multi-network distribution, creators eliminate "
                f"multi-tool friction and increase weekly publishing volume by 4x."
            )
            competitor_gaps = [
                "Generic listicles provide superficial descriptions without real workflow benchmarks.",
                "Lack of verified pricing and multi-platform publishing capabilities."
            ]
            headings = [
                f"Executive Summary: {topic}",
                "The Architectural Difference Between Fragmented Tools and a Unified CreatorOS",
                "Detailed Feature Matrix and Benchmark Testing",
                "Step-by-Step Implementation Guide for Modern Creators",
                "Real World Time and Cost Savings Breakdown"
            ]

        return ContentBrief(
            topic=topic,
            primary_keyword=primary_kw,
            secondary_keywords=secondary_kws,
            search_intent=intent,
            target_market=target_market,
            aeo_direct_answer=direct_ans,
            recommended_schema=schema,
            competitor_gaps=competitor_gaps,
            suggested_headings=headings,
            internal_links=[
                "https://incubrix.com/how-it-works",
                "https://incubrix.com/pricing",
                "https://incubrix.com/faq",
                "https://app.incubrix.com/"
            ]
        )
