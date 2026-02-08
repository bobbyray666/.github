# Copilot Instructions for Fleek .github

## Repository Purpose
This is the **organization profile repository** for fleek-sh on GitHub. The `profile/README.md` displays on the organization's main page and serves as the primary marketing/messaging surface for Fleek to developers and the broader community.

## Key Messaging Framework
Fleek's core positioning focuses on making **AI inference production-ready**: latency, scale, cost efficiency, and reliability. Any updates should reinforce these themes:

- **"Making inference boring"** - Fleek abstracts infrastructure complexity
- **Operational guarantees** - Predictable performance, not fragile scaling demos
- **Value proposition** - Pay for work, not idle capacity; lower tail latency, higher utilization
- **Audience** - ML teams shipping to production, not researchers or notebook users

## Content Structure (profile/README.md)
The README follows this pattern:
1. **Epigraph** (`### Coda: After the Model Boom`) - Sets the thesis
2. **Problem Definition** - Infrastructure gravity that teams lose time to
3. **Core Value Propositions** - Three pillars (boring, lower latency, higher utilization)
4. **Section Headers** with supporting details (`## Making inference boring`, `## Simple by design`, etc.)
5. **Target Audience** - Teams that care about specific outcomes (latency distributions, operational invariants, cost proportionality, APIs that survive production)
6. **Call to Action** - Reference to https://www.fleek.sh

## Writing Guidelines
- **Tone**: Direct, systems-thinking, production-focused (avoid hype, marketing-speak)
- **Metaphors**: Infrastructure, systems design, and operations language (e.g., "bin-packing", "scheduling", "execution layer")
- **Comparisons**: Frame Fleek's approach against competitor/legacy patterns (e.g., "experiments vs systems", "launch threads vs production")
- **Length**: Keep sections concise; density trumps elaboration
- **Links**: Cross-reference https://www.fleek.sh for details and external resources

## Common Editing Tasks
- **Update value propositions**: Ensure claims reflect current product capabilities
- **Add new sections**: Maintain the constraint-and-clarity format (problem → solution → benefit)
- **Refine messaging**: Test that language aligns with the "boring infrastructure" thesis
- **Update links**: Keep https://www.fleek.sh and any external references current

## External References & Link Policy
Currently, this repo contains only one external link: `https://www.fleek.sh`. When adding additional links, follow this hierarchy:
- **Primary**: https://www.fleek.sh (main landing)
- **Product docs** (if established): Point to canonical documentation site
- **GitHub**: Link to main Fleek repos only if showcasing implementation details
- **Social/community**: Only add if officially endorsed (Discord, Twitter, etc.)

**Rule**: Every external link should forward readers toward a clear action or learning goal—avoid link bloat.

## Governance & Updates
- This README is the **organization's face**—changes should align with overall messaging strategy
- Before adding claims about product capabilities or performance, verify they're live
- Document new sections in this `copilot-instructions.md` so future agents understand the rationale

## Scope Boundaries
This is **not** the place for:
- Detailed technical architecture (that belongs in main Fleek repos)
- Integration guides or API references (link to docs site instead)
- Contributor guidelines (use CONTRIBUTING.md in product repos)
- Troubleshooting or support channels (unless official)

## Technical Context
- Single markdown file; no complex build process
- GitHub renders this automatically on https://github.com/fleek-sh
- Markdown formatting: Keep `###` for subsections, code formatting for technical terms
