# Workflow: Topic → Published + Distributed

**Outcome:** One topic becomes a search-optimized article plus a week of channel posts.
**Trigger:** A topic from the content calendar.
**Owner:** Content / marketing · **Runs:** per topic
**Time:** ~30 min with the kit vs a half-day manually.

## Assets used
- Prompt: [Keyword Cluster Builder](../01-prompts/seo.md), [Headline Doctor](../01-prompts/content.md)
- Skill: [seo-brief-generator](../02-skills/seo-brief-generator/SKILL.md), [content-repurposer](../02-skills/content-repurposer/SKILL.md)
- Agent: [SEO Agent](../03-agents/seo-agent.md), [Content Agent](../03-agents/content-agent.md)

## Steps
| # | Step | Asset | Output |
|---|------|-------|--------|
| 1 | Place the topic in a cluster + pick the keyword | SEO Agent / Keyword Cluster Builder | Target keyword + intent |
| 2 | Generate the content brief | seo-brief-generator skill | Outline, questions, angle |
| 3 | Draft the article in brand voice | Content Agent | Full draft + TL;DR |
| 4 | Sharpen the headline + metadata | Headline Doctor + SEO Agent | Title, meta, FAQ schema |
| 5 | Repurpose into channel posts | content-repurposer skill | Newsletter, LinkedIn, video, tweets, carousel |

## Definition of done
Article published with metadata, and a week of distribution posts queued.

## Metrics to track
Time-to-publish · Organic impressions/rankings for the keyword · Engagement on distribution posts.
