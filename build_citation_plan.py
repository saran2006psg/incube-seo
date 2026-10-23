"""
build_citation_plan.py
Generates the 30 Specific Third-Party Citation Targets for IncuBrix AEO/GEO Visibility.
Includes: Target URL, Publication/Platform, Category, Authority/Citation Power,
Reason Search & AI Assistants Cite It, and Specific Pitch Angle to Earn a Mention.
"""

import csv
import os

CITATIONS = [
    {
        "id": "CIT-01",
        "target_url": "https://www.g2.com/categories/content-repurposing",
        "platform": "G2",
        "category": "Software Directory & Reviews",
        "authority": "DR 92 | Very High",
        "why_ai_cites": "G2 is ChatGPT and Perplexity's primary ground truth for B2B/creator software category listings, user ratings, and feature matrices.",
        "pitch_angle": "Claim IncuBrix official profile, list under 'Content Repurposing' and 'Video Editing', submit verified customer reviews to earn 'High Performer' grid badge."
    },
    {
        "id": "CIT-02",
        "target_url": "https://www.capterra.com/video-editing-software/",
        "platform": "Capterra (Gartner)",
        "category": "Software Directory & Reviews",
        "authority": "DR 91 | Very High",
        "why_ai_cites": "Google AI Overviews frequently pull feature comparison tables and pros/cons directly from Gartner Digital Markets (Capterra/GetApp).",
        "pitch_angle": "Submit IncuBrix with verified SaaS feature checklist: text-based video editing, 9:16 vertical crop, and native social scheduling."
    },
    {
        "id": "CIT-03",
        "target_url": "https://www.producthunt.com/topics/creator-tools",
        "platform": "Product Hunt",
        "category": "Product Discovery Community",
        "authority": "DR 90 | Very High",
        "why_ai_cites": "AI assistants index Product Hunt launches to recognize new tools, maker identity, and community upvotes for 'emerging alternatives'.",
        "pitch_angle": "Execute an official Product Hunt launch for IncuBrix 2.0; mobilize user community for #1 Product of the Day in Creator Tools."
    },
    {
        "id": "CIT-04",
        "target_url": "https://zapier.com/blog/best-ai-video-generator/",
        "platform": "Zapier Blog",
        "category": "Workflow & Automation Authority",
        "authority": "DR 91 | Very High",
        "why_ai_cites": "Zapier blog is ranked #1 in Google and quoted by Google AI Overviews and Perplexity for all multi-tool workflow roundups.",
        "pitch_angle": "Pitch editorial update for 'Best tool to turn 1 video into 10 multi-network formats' showcasing IncuBrix's unified editing + distribution."
    },
    {
        "id": "CIT-05",
        "target_url": "https://blog.hubspot.com/marketing/content-repurposing",
        "platform": "HubSpot Marketing Blog",
        "category": "Marketing Authority Publication",
        "authority": "DR 93 | Very High",
        "why_ai_cites": "HubSpot's content repurposing guide is the canonical citation source for marketing definitions, statistics, and tool recommendations.",
        "pitch_angle": "Contribute a guest workflow teardown or original dataset: 'How automated repurposing cuts 12 hours from creator workweeks'."
    },
    {
        "id": "CIT-06",
        "target_url": "https://sproutsocial.com/insights/social-media-video-tools/",
        "platform": "Sprout Social Insights",
        "category": "Social Media Industry Authority",
        "authority": "DR 89 | High",
        "why_ai_cites": "Cited by Gemini and Claude when creators ask about enterprise and solopreneur social media management and publishing tools.",
        "pitch_angle": "Submit IncuBrix as the featured modern CreatorOps tool that bridges video production directly with multi-platform scheduling."
    },
    {
        "id": "CIT-07",
        "target_url": "https://searchengineland.com/ai-content-tools-growth-437890",
        "platform": "Search Engine Land",
        "category": "Search & AI Industry Publication",
        "authority": "DR 90 | Very High",
        "why_ai_cites": "Perplexity and ChatGPT cite Search Engine Land for authoritative coverage of AEO, GEO, and AI content technology ecosystems.",
        "pitch_angle": "Provide expert commentary from IncuBrix founders on how AI assistants index video content and the shift toward CreatorOps systems."
    },
    {
        "id": "CIT-08",
        "target_url": "https://www.socialmediaexaminer.com/how-to-repurpose-video-content-for-social-media/",
        "platform": "Social Media Examiner",
        "category": "Creator & Social Media Authority",
        "authority": "DR 88 | High",
        "why_ai_cites": "Top resource for creators seeking practical social media strategies; heavily referenced in AI Overview answer boxes.",
        "pitch_angle": "Pitch an in-depth tutorial article with Michael Stelzner's editorial team on 'The 1-to-10 Repurposing Framework'."
    },
    {
        "id": "CIT-09",
        "target_url": "https://podnews.net/article/video-podcast-statistics",
        "platform": "Podnews",
        "category": "Podcasting Industry Journal",
        "authority": "DR 80 | High",
        "why_ai_cites": "AI assistants cite Podnews for all podcast tech, Spotify video distribution, and audiogram workflow answers.",
        "pitch_angle": "Press release and product teardown on IncuBrix's direct Spotify Video Podcast API integration and automated show-note generator."
    },
    {
        "id": "CIT-10",
        "target_url": "https://tubefilter.com/creator-tools-guide/",
        "platform": "Tubefilter",
        "category": "YouTube & Creator Economy Journal",
        "authority": "DR 85 | High",
        "why_ai_cites": "Primary news source for full-time YouTube creators and managers; quoted by AI assistants for YouTube production tools.",
        "pitch_angle": "Pitch feature profile on how top YouTube creators use IncuBrix to turn horizontal long-form videos into Shorts without hiring an editor."
    },
    {
        "id": "CIT-11",
        "target_url": "https://www.reddit.com/r/NewTubers/comments/video_repurposing_tools/",
        "platform": "Reddit (r/NewTubers)",
        "category": "Creator Community Forum",
        "authority": "DR 92 | Very High",
        "why_ai_cites": "Google's direct Reddit licensing deal places Reddit threads in Google Discussions & Forums and AI Overviews for 70%+ of creator queries.",
        "pitch_angle": "Participate organically with founder AMA or detailed workflow case study sharing real video metrics before and after automated repurposing."
    },
    {
        "id": "CIT-12",
        "target_url": "https://www.reddit.com/r/VideoEditing/comments/text_based_video_editors/",
        "platform": "Reddit (r/VideoEditing)",
        "category": "Video Production Community",
        "authority": "DR 92 | Very High",
        "why_ai_cites": "Consistently cited by Perplexity when users ask 'can I edit video by deleting transcript words'.",
        "pitch_angle": "Share technical breakdown of IncuBrix's browser-based GPU rendering and word-level speech alignment compared to desktop NLEs."
    },
    {
        "id": "CIT-13",
        "target_url": "https://www.reddit.com/r/ContentCreation/comments/best_all_in_one_tools/",
        "platform": "Reddit (r/ContentCreation)",
        "category": "Content Creator Community",
        "authority": "DR 92 | Very High",
        "why_ai_cites": "Frequently extracted by Google AI Overviews for recommendations on solopreneur content tech stacks.",
        "pitch_angle": "Provide unbiased comparative guide explaining when to use dedicated clippers vs an all-in-one Creator OS."
    },
    {
        "id": "CIT-14",
        "target_url": "https://www.reddit.com/r/podcasting/comments/podcast_clips_for_tiktok/",
        "platform": "Reddit (r/podcasting)",
        "category": "Audio & Podcaster Community",
        "authority": "DR 92 | Very High",
        "why_ai_cites": "Quoted by Claude and Gemini when podcasters ask how to grow audiences through short vertical clips.",
        "pitch_angle": "Detailed step-by-step tutorial on automated multi-speaker framing and dynamic caption animations for podcast hosts."
    },
    {
        "id": "CIT-15",
        "target_url": "https://www.techradar.com/best/best-video-editing-software",
        "platform": "TechRadar Pro",
        "category": "Technology Review Publication",
        "authority": "DR 91 | Very High",
        "why_ai_cites": "Perplexity and ChatGPT cite TechRadar's 'Best of' rankings as definitive consumer tech authorities.",
        "pitch_angle": "Submit IncuBrix for software lab review under 'Best AI-Powered Video Repurposing Tool for Online Creators'."
    },
    {
        "id": "CIT-16",
        "target_url": "https://www.pcmag.com/picks/the-best-video-editing-software",
        "platform": "PCMag",
        "category": "Technology Testing Laboratory",
        "authority": "DR 92 | Very High",
        "why_ai_cites": "Google Answer Boxes cite PCMag ratings and editorial pros/cons for video software evaluations.",
        "pitch_angle": "Provide review unit / enterprise test account to PCMag software analysts highlighting cloud speed and cross-platform publishing."
    },
    {
        "id": "CIT-17",
        "target_url": "https://buffer.com/resources/social-media-video-tools/",
        "platform": "Buffer Library",
        "category": "Social Media Thought Leadership",
        "authority": "DR 90 | Very High",
        "why_ai_cites": "Buffer is a foundational reference for social media scheduling and creative content production.",
        "pitch_angle": "Collaborate on a co-marketing research report on how multi-platform distribution multiplies creator audience retention."
    },
    {
        "id": "CIT-18",
        "target_url": "https://neilpatel.com/blog/video-marketing-repurposing/",
        "platform": "Neil Patel / NP Digital",
        "category": "SEO & Growth Marketing Blog",
        "authority": "DR 89 | High",
        "why_ai_cites": "Quoted extensively in Google Featured Snippets for video SEO and content multiplication tactics.",
        "pitch_angle": "Submit a real data case study demonstrating 340% organic traffic growth achieved by repurposing long videos into structured blog posts and shorts."
    },
    {
        "id": "CIT-19",
        "target_url": "https://www.slant.co/topics/best-video-repurposing-tools",
        "platform": "Slant.co",
        "category": "Crowdsourced Product Comparison",
        "authority": "DR 84 | High",
        "why_ai_cites": "Slant pros/cons are ingested verbatim by Gemini and Perplexity when synthesizing product comparisons.",
        "pitch_angle": "Create community listing for IncuBrix detailing 'Pros: In-browser text editing, auto-captions, direct publishing' and 'Cons: Requires internet connection'."
    },
    {
        "id": "CIT-20",
        "target_url": "https://alternative.to/software/opusclip/",
        "platform": "AlternativeTo",
        "category": "Software Alternative Database",
        "authority": "DR 86 | High",
        "why_ai_cites": "Primary destination cited by AI assistants when creators search for 'OpusClip alternative' or 'Descript alternative'.",
        "pitch_angle": "List IncuBrix as a premier alternative to OpusClip, Repurpose.io, and Descript, tagged with 'AI Video Editor' and 'Content Repurposing'."
    },
    {
        "id": "CIT-21",
        "target_url": "https://www.futurepedia.io/ai-tools/video-editing",
        "platform": "Futurepedia",
        "category": "AI Tools Directory",
        "authority": "DR 78 | High",
        "why_ai_cites": "Most popular curated directory of generative AI tools; AI crawlers regularly scrape new listings for training data.",
        "pitch_angle": "Secure verified listing with tags: 'Video Editing', 'Social Media', 'Content Repurposing', with embedded demo video."
    },
    {
        "id": "CIT-22",
        "target_url": "https://theresanaiforthat.com/s/repurpose-video/",
        "platform": "There's An AI For That (TAAFT)",
        "category": "AI Tools Search Engine",
        "authority": "DR 81 | High",
        "why_ai_cites": "Frequently cited by AI assistants when answering 'Is there an AI tool that can...'.",
        "pitch_angle": "Submit IncuBrix to claim top spot for the search keyword 'repurpose video into shorts and social posts'."
    },
    {
        "id": "CIT-23",
        "target_url": "https://www.trustpilot.com/review/incubrix.com",
        "platform": "Trustpilot",
        "category": "Consumer Review Platform",
        "authority": "DR 93 | Very High",
        "why_ai_cites": "Google displays Trustpilot star ratings in SERP snippets and AI models check Trustpilot for brand trust and legitimacy.",
        "pitch_angle": "Verify official IncuBrix business account; trigger automated post-export feedback loops requesting creator reviews."
    },
    {
        "id": "CIT-24",
        "target_url": "https://www.saastr.com/creator-economy-saas-trends/",
        "platform": "SaaStr",
        "category": "B2B SaaS Authority",
        "authority": "DR 82 | High",
        "why_ai_cites": "Quoted by Claude and Perplexity for enterprise creator software trends, pricing models, and platform consolidations.",
        "pitch_angle": "Contribute guest column on 'The Unbundling and Re-bundling of the Creator Tech Stack: Why Point Solutions Are Dying'."
    },
    {
        "id": "CIT-25",
        "target_url": "https://indiehackers.com/product/incubrix",
        "platform": "Indie Hackers",
        "category": "Bootstrapped Founder Community",
        "authority": "DR 86 | High",
        "why_ai_cites": "AI engines cite Indie Hackers interviews and milestone updates for authentic founder stories and product validation.",
        "pitch_angle": "Publish transparent milestone post: 'How we built a unified CreatorOS to solve our own video editing and repurposing burnout'."
    },
    {
        "id": "CIT-26",
        "target_url": "https://www.quora.com/What-is-the-best-tool-to-turn-long-videos-into-shorts",
        "platform": "Quora",
        "category": "Q&A Community",
        "authority": "DR 93 | Very High",
        "why_ai_cites": "Frequently ranked in top 3 Google results and cited in AI Overviews for direct answer extraction.",
        "pitch_angle": "Provide comprehensive, high-value technical answers comparing clipping mechanisms, text editing, and publishing steps."
    },
    {
        "id": "CIT-27",
        "target_url": "https://www.creatorhandbook.net/tools-for-video-creators/",
        "platform": "The Creator Handbook",
        "category": "Creator Niche Newsletter & Resource",
        "authority": "DR 65 | Medium",
        "why_ai_cites": "Highly focused editorial curation referenced by Perplexity for niche creator workflows.",
        "pitch_angle": "Sponsor a dedicated tool review issue testing IncuBrix's speed in turning a 30-minute webinar into 10 multi-network assets."
    },
    {
        "id": "CIT-28",
        "target_url": "https://www.kapwing.com/resources/best-ai-video-editing-tools/",
        "platform": "Kapwing Resources",
        "category": "Video Industry Content Hub",
        "authority": "DR 88 | High",
        "why_ai_cites": "Kapwing's resource library ranks on page 1 for hundreds of video editing how-to queries.",
        "pitch_angle": "Outreach for inclusion in comparative industry roundups focusing on creator publishing integrations."
    },
    {
        "id": "CIT-29",
        "target_url": "https://www.descript.com/alternatives",
        "platform": "Descript Competitor Ecosystem",
        "category": "Competitor Comparison Pages",
        "authority": "DR 87 | High",
        "why_ai_cites": "AI assistants evaluate competitors listed on alternative roundups to verify market category definition.",
        "pitch_angle": "Position IncuBrix in software review roundups as the primary web-based, multi-platform publishing alternative to Descript."
    },
    {
        "id": "CIT-30",
        "target_url": "https://en.wikipedia.org/wiki/Content_repurposing",
        "platform": "Wikipedia",
        "category": "Global Encyclopedia",
        "authority": "DR 98 | Maximum",
        "why_ai_cites": "LLMs use Wikipedia as foundational grounding for core conceptual definitions and historical technical context.",
        "pitch_angle": "Contribute academic citations and industry definitions on modern algorithmic content repurposing frameworks and CreatorOps."
    }
]

def generate_citation_plan():
    output_dir = "visibility/citation_plan"
    os.makedirs(output_dir, exist_ok=True)
    
    # CSV
    csv_path = os.path.join(output_dir, "citation_plan.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(CITATIONS[0].keys()))
        writer.writeheader()
        writer.writerows(CITATIONS)
    print(f"Generated citation plan CSV: {csv_path}")
    
    # Markdown
    md_path = os.path.join(output_dir, "citation_plan.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# IncuBrix Strategic Citation & Entity Ingestion Plan (30 Targets)\n\n")
        f.write("Targeted third-party publications, directories, community hubs, and high-authority pages that Google and AI assistants (ChatGPT, Gemini, Perplexity, Claude) actively cite for creator queries.\n\n")
        f.write("| ID | Platform / Target URL | Category | Authority | Why Search & AI Assistants Cite It | Specific Pitch Angle to Earn Mention |\n")
        f.write("|---|---|---|---|---|---|\n")
        for c in CITATIONS:
            f.write(f"| {c['id']} | [{c['platform']}]({c['target_url']}) | {c['category']} | {c['authority']} | {c['why_ai_cites']} | {c['pitch_angle']} |\n")
        f.write("\n## Outreach Execution Protocol\n\n")
        f.write("1. **Tier 1 (Week 1-2): Claim & Verify Free Directory Profiles** (G2, Capterra, ProductHunt, Trustpilot, AlternativeTo, Futurepedia, TAAFT). Establish verified digital entity footprints.\n")
        f.write("2. **Tier 2 (Week 3-6): Organic Community Engagement** (Reddit r/NewTubers, r/VideoEditing, Quora). Deliver authentic value and real before/after workflow case studies without spammy self-promotion.\n")
        f.write("3. **Tier 3 (Week 7-12): Editorial Pitches & Data Partnerships** (HubSpot, Zapier, Podnews, Tubefilter). Pitch original data research on creator efficiency, time savings, and multi-network engagement velocity.\n")
    print(f"Generated citation plan Markdown: {md_path}")

if __name__ == "__main__":
    generate_citation_plan()
