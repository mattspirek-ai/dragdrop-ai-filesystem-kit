---
name: seo-brief-generator
description: Use when the user needs an SEO content brief for a target keyword before writing an article. Triggers on "SEO brief", "content brief", "outline for keyword", "help me rank for".
---

# SEO Brief Generator

## When to use
The user has a target keyword and wants a brief a writer can execute without guessing.

## Inputs you need
- Target keyword
- Audience + their awareness stage
- The unique angle/POV the brand can bring (so the piece beats existing results)
If the angle is missing, propose 2-3 and ask which to use.

## Steps
1. Infer search intent (informational / commercial / transactional) and state it.
2. Propose 3 titles with the keyword near the front.
3. Build an H2/H3 outline that fully satisfies intent.
4. List the real questions readers ask (People-Also-Ask style).
5. Recommend word-count range and 2-3 internal links to include.
6. Name the single differentiator that makes this rank over the current top pages.

## Output format
```
Keyword: ... | Intent: ...
Titles: 1) 2) 3)
Outline:
  H2 ...
    H3 ...
Questions to answer: - ...
Word count: ...
Internal links: ...
Winning angle: ...
```

## Quality bar
- The outline must cover everything a top result covers PLUS the unique angle.
- No keyword stuffing. Headings read like a human wrote them.

## Example
**Input:** keyword "AI receptionist for dentists", audience = practice owners, angle = "HIPAA-safe setup in a day".
**Output:** Commercial-intent brief with titles, a 7-section outline, 6 PAA questions, 1200-1600 words, 2 internal links, differentiator = the HIPAA-in-a-day angle.
