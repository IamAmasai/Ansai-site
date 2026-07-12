# Ansai Technologies — Pivot Strategy & Site Roadmap

**Compiled:** July 2026 (v2 — updated with resolved terminology, positioning framework, and direct build instructions)
**Purpose:** Single reference document for the infrastructure pivot thesis, locked terminology, build sequencing, current site audit, and design resources — so nothing discussed gets lost or re-litigated from scratch. **Section 12 is written as direct, imperative instruction for whichever model actually builds the site — read that section as a spec, not commentary.**

---

## 1. Executive Summary — The Pivot, in One Paragraph

Ansai is not becoming "an AI agent company." Ansai builds the **structural layer underneath an organization** — the part that captures how it actually operates — so that any tool, current or future, can act on it intelligently. AI is not the product. AI is the current, most useful **tenant** sitting on top of a structure that will outlast it. We integrate with what an organization already uses (spreadsheets, paper records, existing habits) rather than replacing it, make those tools quietly better, and let anything new — including whatever succeeds AI — stand on the same ground without a rebuild. We prove this in one organization, prove it generalizes in a second, different one, and only then let it grow toward the larger, tool-agnostic ecosystem it's ultimately capable of becoming.

> **Core belief, stated plainly, because it governs every downstream decision in this document:**
> **AI is an enabler, not a destination.** It does not stay in its own category. It permeates into every other layer of technology the way electricity or networking did before it — quietly present everywhere, the headline nowhere. Ansai's structure is built so that today's tenant (AI) and whatever technology succeeds it can both stand on the same ground without a rebuild. This is not a hedge against AI. It's a recognition that betting the company's entire identity on the current loudest tenant is exactly how a company ages badly.

---

## 2. Locked Terminology — The Ledger

This is the language discipline. Anything external-facing gets checked against this table before it ships. Drift has happened repeatedly in this process itself — logged in Section 11 — so treat this table as authoritative over any earlier draft.

| Term | Locked to | Explicitly NOT this | Status |
|---|---|---|---|
| Category (external, public-facing) | **"digital infrastructure"** | operational infrastructure, agentic infra, AI agent company, data structure company | **LOCKED (final)** |
| Who it serves | **organizations** | institutions | Locked |
| What AI is | one tenant / enabler among others, that **permeates** every layer rather than staying in its own lane; named plainly only in technical depth | the leading category word, the headline | Locked |
| Internal engineering codename | *(deliberately not yet decided)* | ~~Kiini~~ (rejected by founder) | Parked |
| Mechanism-level terms (fine in technical appendix, never in the opening line) | "agentic," "data structure," "agent-core" | — | Locked |

**Resolution of the open question from the prior draft:** the founder has confirmed — **"digital infrastructure" is the final category term.** The live site's current hero line ("the operational infrastructure platform for Africa") is now out of date and must be rewritten to match. This is listed explicitly as a required copy change in Section 12.

**Locked one-liner:**
> "Ansai builds digital infrastructure for African organizations — schools, businesses, and enterprises — making their data queryable and actionable through AI."

**Why not "AI agent company" — restated plainly, since this gets re-litigated the moment hype is in the room:** leading with "AI agent" invites a comparison set Ansai cannot win (venture-funded agent startups with capital Ansai doesn't have), and per Gartner's 2026 Hype Cycle, agentic AI is already at the Peak of Inflated Expectations with the industry's own analysts predicting a fast move toward the Trough of Disillusionment and mass project cancellations within roughly 18 months of this writing. "Digital infrastructure" is not a hedge — it is the category that is actually true, ages well past the current hype cycle, and puts Ansai's real differentiator (structure that outlasts any single tool) at the center instead of the one thing every other AI startup is also currently claiming.

---

## 3. The Core Thesis

### 3.1 The Five-Layer Architecture

This is the actual machine, stripped of any product-specific skin. It already maps almost exactly onto packages that exist today inside `ansai-core` — meaning this thesis was discovered from work already done, not invented fresh.

| Layer | What it does | Existing Ansai package |
|---|---|---|
| **1. Ingestion** | Pull in an institution's data wherever it actually lives — PDFs, spreadsheets, scanned forms, legacy databases, WhatsApp exports | `@ansai/pipeline` |
| **2. Structuring** | Turn messy, org-specific data into a coherent internal representation — entities, relationships, schema. Historically the "hard part" — closer to consulting than product at this stage | *(currently manual — the real gap)* |
| **3. Retrieval** | Plain-language question in, grounded answer out, with citations back to source | *(new — this is `agent-core`)* |
| **4. Action** | Not just answer — do things: draft a report, flag a compliance issue, update a record | *(new — the tool-calling layer)* |
| **5. Trust / Tenancy** | Wall off every organization's data from every other organization's, with audit trails | `@ansai/auth`, `@ansai/tenancy`, `@ansai/roles`, `@ansai/audit` |

**The precise sentence, no buzzwords:**
> You are building the layer that sits between an organization's messy, siloed, real-world records and the point where a person can ask a question or trigger an action in plain language — safely, per-organization, regardless of what kind of organization it is.

### 3.2 Governing Reasoning Aids (why this is the right shape, not just an appealing one)

- **Palantir precedent:** Palantir explicitly refuses to call itself an AI company. Its real positioning is the "ontology" — a structured, queryable model of how an organization actually works — with AI as one thing that acts on top of it. The model is the moat; AI is a tenant. This is the same architecture at a different scale, for organizations Palantir will never serve.
- **AWS precedent:** AWS did not start as "cloud infrastructure for the world." It was Amazon's own internal tooling, battle-tested at real operational scale, turned outward only after it had proven itself. **Abstraction is earned through repeated contact with real use, not legislated upfront on a whiteboard.**
- **Endosymbiosis / "become the organelle, not the invader":** Mitochondria were once free-living bacteria that slotted in alongside an existing cell's operations rather than demanding it rebuild — and became indispensable over time. Applied directly: if a school or business already uses Excel, the correct move is not to replace it but to make it quietly smarter from underneath, so the tool they trust gets better without them leaving it.
  - **Cheap, correct version:** ingest what they already use (Excel sheets, paper registers), enrich it back out in a format they already trust (a smarter export, a flagged cell, a WhatsApp summary).
  - **Expensive, premature version:** building a live Excel add-in / Office API integration before a real user is asking for it specifically. Same "don't build adapters for tools you don't have users for" discipline as the plugin-ecosystem question below.
- **Coral reef / fish:** Models and specific AI tools churn on a roughly weekly-to-monthly cycle and will keep being replaced. The structure — the reef — is what compounds and does not decay with each model release. **Ansai is not in the fish business. Ansai is building the reef.**
- **Roman roads:** Infrastructure built to solve one narrow problem well becomes the distribution rail for everything that comes after, almost by accident of physics. Practical implication: the structuring layer built inside one real school **doubles as the go-to-market vehicle** for Internatives, the lesson plan tool, and the CBC toolkit — not a separate sales motion, the same motion.
- **Mycelium:** A single fungal network can serve multiple tree species — but it still grows outward from where it's already rooted, not fed to the whole forest on day one. The ecosystem vision is correct as an eventual property; it must be **earned one connection at a time**, starting from the one school already in hand.
- **Amazon Basics caution (a live design principle, not an urgent fix):** Being simultaneously the neutral infrastructure layer and a vendor selling products on top of it is a real, documented trust tension at scale (Amazon Basics vs. third-party sellers on Amazon's own marketplace). Not a problem today with one school and zero competing tenants — but worth holding as a principle now, while it costs nothing: the structure should be able to honestly serve a tool that isn't Ansai's own, even while Ansai's tools happen to be the best-fitted tenant early on.

### 3.3 Internal vs. External Language (register discipline)

**Internal version (conviction anchor — for the two of you, not for a deck):**
> We build the structure underneath an organization — the part that lets it understand and run itself. We don't ask anyone to abandon what they already trust; we make it work better on its own, and let anything new stand on that same ground without tearing anything up. AI isn't the house. It's the most useful guest currently staying in it.

**External version (investor / partner / enterprise-facing — one metaphor max, no ornament):**
> Ansai builds the digital infrastructure an organization runs on — the layer that captures how it actually works, not a rebuild of its existing tools. We integrate with what an organization already uses — spreadsheets, paper records, existing workflows — rather than replacing them, and make those tools materially more effective as a result. That infrastructure is technology-agnostic by design: today it enables AI-driven insight and automation; tomorrow it will support whatever technology succeeds AI, without requiring the organization to rebuild. We validate this in one organization at a time, confirm it generalizes across a second, different one, and expand from there.

**Rule going forward:** one metaphor maximum in anything that leaves the building. The reef, the mitochondria, the roads — brilliant for internal thinking, a liability in front of anyone deciding whether to trust you with their operations or their money.

---

## 4. Market Sequencing — Scouting vs. Committing

**Ant-colony principle:** scouting is parallel and cheap; committing real build resources is sequential and expensive. Confusing the two either starves the company (never commits) or collapses it (commits everywhere at once, dilutes to nothing).

| Market | Current status | What "scouting" means here | What it does NOT require yet |
|---|---|---|---|
| **Schools** | Active — already in motion via EduManage | — | — |
| **Small business (SME)** | **Held / parked**, per explicit founder decision this conversation | A handful of conversations through existing trust networks, to check whether the old blocker (critical SME data lives "by head," not digitally) still holds | No build |
| **Enterprise** | Scouting only | A handful of conversations through existing network (Safaricom ties, ADK credentials as door-openers) to learn real budget and procurement timelines | No build, no vertical-specific integration |

**The actual build discipline within this sequencing:**
- Extend `ansai-core` with one new package (working label: `agent-core`) — schema contract only, ingestion + retrieval + tool-calling. Do **not** port the full critic/composer verification pipeline from the Kenya Product Safety Agent design by default — that level of adversarial rigor is justified when a wrong answer causes physical harm, not for "which students are behind on fees."
- Ship it first as **EduManage's AI tier**, scoped to the one real school already in a relationship. No new sales motion required.
- **Never let EduManage-specific logic leak into the core schema** — same discipline already correctly applied once to keep EduManage-specific roles out of `@ansai/roles`. If a concept wouldn't also make sense for a small business or a hospital, it's config, not core.
- Pick **one connective thread first**, not "the whole system": e.g., teacher lesson plans ↔ admin CBC compliance visibility, *or* fee records ↔ parent communication. One real, working connection beats an unverifiable claim of total interconnectedness.

---

## 5. Build Sequence — Phase by Phase

| Phase | Timeframe | What you build | What it proves | Explicit guardrail |
|---|---|---|---|---|
| **0 — Define** | Days | A written schema (not code) of universal primitives: entities, relationships, events, policies | Whether the abstraction can be articulated cleanly before touching real data | Don't write implementation code yet |
| **1 — Prove in one** | Weeks | Instantiate the schema against the one real school; attach one narrow agent (retrieval + a couple of actions) | Whether the structure is actually *useful* | No critic/composer overkill at this stage |
| **2 — Prove portability** | Following months | Point the *same* schema at a genuinely different organization (a scouting relationship is enough — doesn't need to be a paying customer yet) | **This is the real test of the moat claim.** Survives with only new instance data + thin config = real. Needs surgery = expensive lesson learned cheap. | Don't chase a third vertical yet — two is the minimum sample size |
| **3 — Tool-agnosticism** | Continuous, from Phase 0 onward | No extra build — a standing constraint: never let one vendor's API shape leak into the core schema | Swapping/adding a model or tool later is a config change, not a rewrite | Don't build adapters for tools you don't have users for yet |
| **4 — Ecosystem** | 1–3+ years out | Opening the structure to third-party tools/organizations, once 2–3 real institutions show the structure getting *more* valuable over time | Whether you have a real platform, not just a well-built product | Name this honestly as **not this quarter's work** |

---

## 6. Positioning & Messaging Discipline

### 6.1 Why "agentic infrastructure" is not the public category (data-backed, not just a hunch)

Per Gartner's 2026 Hype Cycle for Agentic AI: agentic AI currently sits at the **Peak of Inflated Expectations** — only ~17% of organizations have actually deployed AI agents, while 60%+ expect to within two years, and the technology is beginning its move toward the Trough of Disillusionment faster than Gartner initially projected, with over 40% of agentic projects predicted to be cancelled by the end of 2027. Gartner has also coined the term **"agent washing"** — legacy automation rebranded as agentic — meaning the word itself now signals suspicion to a sophisticated buyer, not cutting-edge credibility.

**Conclusion:** "agentic" stays in the technical appendix, for technically fluent audiences only (a CTO, a developer-tool investor). It never leads the public one-liner. The category noun should describe the **outcome**, not the **mechanism** — the same discipline Stripe ("payments infrastructure," not "tokenized ledger reconciliation"), Twilio ("communications infrastructure," not "SMPP/SIP abstraction"), and Salesforce (named after the outcome, not the underlying database architecture) all follow.

### 6.2 Audience-specific entry points (same underlying claim, different opening line)

| Audience | Opening line |
|---|---|
| **Investor / grant panel** | "We build digital infrastructure for African organizations — starting with schools, expanding into any organization that needs its own data made usable through AI." |
| **School principal** | Keep existing framing: "We help you deliver CBC properly" — the AI-native layer is a *feature*, never the headline |
| **Enterprise / NGO** | "We help your organization query and act on its own data — internal documents, records, operations — without hiring a data team to structure it first" |
| **SME (parked, for later)** | Different register entirely: "We help your business run itself better over WhatsApp" — not "digital infrastructure" language at all |

### 6.3 The Dunford Framework, Applied Directly to Ansai (source material verified, not generic)

This section exists because a link was shared and needed to actually be used, not just cited. Source: **"Positioning Secrets for AI Products,"** a Maven lightning lesson taught by **Abhishek Ratna** (Principal, AI Strategy & Technical Marketing at Atlassian's Rovo Studio; ex-Google, ex-Microsoft; led GTM across TensorFlow, Labelbox, Protopia AI, and Atlassian's Agents work). The lesson's actual structure: the problem with "AI-powered" positioning → the one-sentence test → **April Dunford's 5-step positioning framework, applied to AI specifically** → a live positioning teardown of Airtop.ai → overcoming the AI trust problem → applying the framework across the AI stack.

**The underlying methodology is April Dunford's, from *Obviously Awesome*** — the standard positioning framework used at Google, Postman, IBM, and hundreds of B2B/SaaS companies. Its central warning, directly relevant here: most weak positioning happens because a company defaults to the market category it *started* in, rather than deliberately choosing the category that makes its actual strength obvious. **Ansai's "digital infrastructure" decision (Section 2) is exactly this exercise — deliberately refusing the default "AI agent company" category in favor of the one that puts the real differentiator at the center.**

**The 5 steps, run against Ansai directly, right now, so this isn't left abstract:**

1. **Competitive alternatives — what an organization does if Ansai doesn't exist.** Not just other software: **Excel spreadsheets, paper registers, a hired data clerk, WhatsApp groups used as ad-hoc admin systems, or simply doing nothing and living with the chaos.** Dunford's framework explicitly names "Excel" and "doing nothing" as real competitive alternatives, not jokes — this validates the earlier "meet Excel where it lives" instinct directly: Excel isn't a tool to route around, it's the *actual incumbent* Ansai is competing with in most target organizations today.
2. **Unique attributes — what Ansai has that those alternatives don't.** Local-first/offline-first architecture that survives Kenya's real connectivity conditions; native M-PESA Daraja integration; a structural layer that stays tool-agnostic instead of locking an organization to one AI vendor; direct field-level building (the Mshauri model) rather than software designed from outside the context.
3. **Value themes — attributes translated into what the customer actually feels.** "You never lose a week of records to a blackout or a lost notebook." "Your existing spreadsheets get smarter instead of being replaced." "You're not betting your operations on whichever AI vendor is fashionable this year."
4. **Who cares a lot.** Organizations where operational continuity is existential, not a nice-to-have (a school cannot afford to lose fee or attendance records); organizations in genuinely unreliable-connectivity environments; organizations wary of vendor lock-in — which, per the Gartner hype-cycle data in 6.1, is a rational and *growing* fear as agentic-AI projects start failing industry-wide.
5. **Market category — the frame that makes the value obvious.** Not "AI agent company" (a crowded, currently souring category where Ansai loses every capital comparison). Not "SaaS company" (generic, invites feature-list comparison). **"Digital infrastructure"** — a category where durability, structure, and reliability are the entire point, and where being young, African, and differently resourced than Silicon Valley competitors is irrelevant to the comparison, because infrastructure is judged on whether it holds, not on how much funding built it.

**The "one-sentence test" from the same lesson, applied:** if you can't say your positioning line out loud to a real buyer without either of you needing it explained further, it's not done. Test the locked one-liner in Section 2 against this directly, out loud, before it goes on the site.

**The AI trust problem (from the lesson's own framing, directly relevant to Section 8's audit):** AI products fail to earn trust when they lead with the mechanism ("we use agents," "we're AI-powered") instead of demonstrating the outcome first and letting the AI be discovered underneath it. This is the same reasoning already governing Section 2 and 6.1 — now confirmed by a named practitioner's framework rather than resting on this document's judgment alone.

---

## 7. Prior Bets, Reassessed (Profitability Check)

Two ideas were previously bundled under "pivot to agents" and need to stay separated, since they carry very different risk profiles:

- **Bet A — AI-native corporate consulting / "AI implementation":** Profitable *if actually sold*, but structurally boutique consulting, not a scalable product — linear with founder hours, no compounding asset. Real risk: another full workstream added to an already fragmented founder attention span. No client conversations held yet as of this writing.
- **Bet B — Kenya Product Safety Agent:** Excellent, mission-true engineering (the label-vs-lab-testing correction is genuinely sharp work) attached to zero revenue model. Free consumer tier = the "core product" = $0 revenue by design, with real per-query compute cost (3–4+ model calls minimum) and no funding runway to survive the multi-year gap Yuka needed before monetizing. **Fails the founder's own three-question filter, specifically question 3 ("will someone pay before it's finished") and partially question 1 (proximity to the pain is second-hand — Daily Nation reporting and CEJAD studies, not direct lived contact with the informal cosmetics trade).** Not abandoned — just frozen at "concept" until a real conversation with CEJAD happens, since that costs nothing and is the highest-signal action available on this thread.

**Actual conclusion:** neither agent bet is currently a Phase 1 capital engine. **Internatives is the strongest near-term revenue candidate already in hand** — concrete pricing (KES 3,500/teacher; KES 50–80K/school), a TSC CPD accreditation pathway that could convert the whole sales motion from "please attend" to "credentialed pathway you already need," and a validation test (the four-questions sheet, with a specific principal) that was designed but not yet closed.

**Standing action item:** close the loop on the principal test. Highest information-per-cost action currently available — costs nothing beyond what's already been built, and determines whether Internatives' pricing/accreditation push is worth accelerating.

---

## 8. Current Site Audit — ansaitechnologies.co.ke (repo: `Ansai-site`)

### 8.1 Stack, as it actually exists
Vanilla HTML/CSS/JS — `index.html`, `styles.css`, `script.js`, no framework, no build step, no component system. Fonts: DM Sans + DM Mono (Google Fonts), matching the locked brand system. Color tokens confirmed in CSS: `--bg: #111c27`, blue `#1c5cf5`, cyan `#2de8e8` — correct values, but **the variables are misnamed `--gold` and `--gold-soft`** despite holding blue/cyan values — leftover template naming that was never corrected, a real maintainability bug for whoever touches this file next.

### 8.2 What's genuinely good — preserve this
- The written content itself: Utu Engineering, Pamoja, the Mshauri model, constraint-led innovation, ship-to-learn, institutional trust — authentic, lived philosophy, not generic startup copy.
- Brand tokens are correctly implemented once the naming bug is fixed.
- The local-first / sync-always / backup-automated engineering story is a genuine, rare differentiator for a landing page.
- Believable, non-inflated stats: "2026, founded in Nairobi," "8 strategic sectors in the platform vision" — no fabricated social proof.

### 8.3 The "vibecoded" tells — concrete, from the code, not vibes
1. **Emoji used as icons** (📊 🔄 🛠️) inside a floating phone mockup — the single most recognizable "AI-generated demo" signal in the industry right now.
2. **Decorative bar charts with no real data** — `style="height: 52%"` etc., purely implying "growth" or "activity" with nothing backing it.
3. **Stock photography** (Pexels files) behind feature cards and sector tiles — generic aerial-farm/classroom energy, undermines a distinctive brand.
4. **A pricing-table component reused to display the sector roadmap** ("Active / Coming / Future / Horizon / Scale") — the nearest familiar template pattern, reskinned for content it doesn't actually fit. Needs an honest redesign, not a reskin.
5. **Four "View framework →" links that go nowhere** (`href="#"`), despite the actual source documents (Group Identity, Culture Constitution, Engineering Principles, Design Playbook) sitting in the repo as `.docx` files, unrendered. Free, low-effort credibility currently unclaimed.
6. **"Institutions" is baked in at the code level**, not just copy-level — hero, features heading, solution section, principles card labels, FAQ (twice), footer. Needs a deliberate rewrite pass, not a blind find-replace, since some sentences need light rephrasing around the swap to "organizations."
7. **Unoptimized images** — several multi-megabyte JPGs loaded directly as backgrounds, no responsive sizing or modern format, real load-time cost — notably ironic for a company whose entire pitch is performance under poor connectivity.
8. **A stat that doesn't hold up on inspection:** "AI adoption minimum," `data-target="5"` — the displayed "0" is only the pre-animation start state; the real counted-up value is 5, and even then, the label doesn't clearly parse. Needs a rewrite, not a defense.
9. **Footer links to `ansai.co`**, a different domain than the live `ansaitechnologies.co.ke` — worth confirming whether intentional (a shorter forwarding domain) or a leftover mistake.
10. Hardcoded copyright year (`©2026`) — trivial, but easy to auto-generate.

### 8.4 The one real architectural decision this forces
Skiper UI and Vengeance UI (see Section 9) are both React/shadcn-based — they do not drop into the current vanilla stack as-is. Two honest paths:
- **Migrate to React/Next.js** — bigger, real commitment, unlocks the component ecosystem properly.
- **Stay vanilla, hand-build the specific interaction patterns** borrowed from those libraries, without the dependency.

**Necessity check: roughly 90% of what's wrong above is fixable in the current stack with zero framework migration.** The emoji icons, fake charts, stock photos, dead links, and "institutions" language are all fixable today. The framework decision is separate and bigger — don't let it block the fast fixes.

---

## 9. Design Resources — Vetted

| Resource | What it is | Verdict |
|---|---|---|
| **Taste Skill** (tasteskill.dev / `github.com/Leonxlnx/taste-skill`) | Open-source, MIT-licensed, 30.8k stars — `SKILL.md` rule files against generic AI-slop patterns for coding agents (Claude Code, Cursor). Includes a redesign-audit-first mode, motion/density "dials," and a pre-flight checklist. | Legitimate and well-built. Designed to auto-load inside a coding agent's own filesystem — if the actual build happens in Claude Code locally, install it there directly. Inside this chat interface, the same principles can be borrowed manually alongside Anthropic's built-in `frontend-design` skill. |
| **Skiper UI** (skiper-ui.com) | Real, shadcn/ui-based component library — 70+ animated React/Tailwind/Framer Motion components, CLI-installed. | Legitimate, well-regarded, genuinely non-generic components. Requires a React stack. |
| **Vengeance UI** (vengenceui.com) | Real, Radix + Tailwind + Framer Motion animated component library, CLI-installed as editable source files (not an npm black box). | Legitimate, same React requirement as above. |
| **Emil Kowalski** (animations.dev) | Real, widely respected design engineer — built Vaul, Sonner; a genuine reference point for motion/interaction detail. | Worth reading directly, not just name-dropping. |
| **Maven — "Positioning Secrets for AI Products"** (Abhishek Ratna, Atlassian) | Real, free lightning lesson. Full breakdown and direct application to Ansai is in **Section 6.3** — not just cited, actually run against the company. | Directly informed the final "digital infrastructure" category lock via the Dunford 5-step framework. |
| **Claude Fable 5** | Verified via multiple independent reviews (not just marketing) to have a genuinely strong, substantiated reputation specifically for **product UI/UX and dashboard work** — includes an auto-invoked internal "interface design skill." Slightly less differentiated on heavily custom marketing-page art direction. | Real option to switch to for this specific build — a mid-conversation model swap, available whenever the actual build begins. |

---

## 10. Immediate Action Items (in order)

1. **Close the loop on the Internatives principal test** — record the outcome if it already happened; if not, run it exactly as designed (the four-questions sheet, nothing more).
2. **Rebuild the site to Section 12's build instructions** — "digital infrastructure" is now locked; the current live copy ("operational infrastructure platform") is out of date and must be replaced.
3. **Fix the site punch list** (Section 8.3) — none of it requires a framework migration; all of it is currently costing credibility for free.
4. **Sketch the `agent-core` package interface** (Section 5, Phase 0) — contract only, ingest/query/tool-call, no implementation yet.
5. **Ship `agent-core` as EduManage's AI tier**, scoped to the one real school (Phase 1).
6. **Run 2–3 low-cost scouting conversations** in SME and enterprise (Section 4) — no build, information only.
7. **Freeze the Kenya Product Safety Agent at "concept"** until a real CEJAD conversation happens.

---

## 11. Standing Corrections Log (discipline, carried forward)

Worth keeping visible, because the pattern repeats and the fix each time is the same: catch the drift, name it precisely, correct in place.

1. **EduManage overclaimed** in earlier work as a "durable" business — corrected: one school, pre-revenue, an honest early pilot.
2. **Assumed shop/retailer willingness to pay** for the Safety Agent without checking incentive — corrected toward a consumer-first model, with the free-tier revenue gap now honestly flagged in Section 7.
3. **"Institution" language drifted back in three separate times** across this conversation even after being explicitly corrected — now understood as a standing audit item, not a one-time fix.
4. **"Data structure" surfaced once in place of "digital infrastructure"** — logged as the same class of error: the more technically available term crowding out the agreed category term under time pressure.
5. **"Agentic infra" proposed and correctly re-scoped** to the technical appendix rather than the public category, backed by actual Gartner hype-cycle data rather than instinct alone.
6. **A site stat ("0 AI adoption minimum") was misread and praised** before the actual code was checked — corrected once the real `data-target` value was inspected. Lesson restated plainly: check the artifact before praising it.

**Working rule this document exists to enforce:** any external-facing claim, term, or stat should be checked against this document before it ships — not re-derived from memory each time.

---

## 12. BUILD INSTRUCTIONS — Direct Spec for the Implementing Model

**Read this section as a work order, not background reading.** Everything above is reasoning; everything below is what to actually do. If any instruction here conflicts with an earlier section, this section wins — it is the most recently resolved version of every decision.

### 12.1 Non-negotiable copy — use verbatim, do not paraphrase

**Hero headline:**
```
Digital infrastructure for African organizations.
```

**Hero subhead:**
```
Ansai builds software for the organizations that run African life: schools, farms, clinics, transport networks, utilities, and the communities they serve. We start where trust is deepest, then expand through the systems daily life depends on.
```

**Meta description:**
```
Ansai Technologies is digital infrastructure for African organizations, starting with education and expanding across the systems communities depend on.
```

**One-liner, for any pitch context, deck, or about page:**
```
Ansai builds digital infrastructure for African organizations — schools, businesses, and enterprises — making their data queryable and actionable through AI.
```

### 12.2 Global find-and-replace, applied with judgment (not a blind script)

| Find | Replace with | Note |
|---|---|---|
| "operational infrastructure" | "digital infrastructure" | Every instance, hero to FAQ |
| "institutions" / "institutional" | "organizations" / "organizational" | Rewrite the surrounding sentence where a blind swap reads awkwardly (e.g. "institutional trust" → "the trust organizations place in us," not "organizational trust") |
| "AI adoption minimum" stat block | Remove or replace with a real, verifiable metric. Do not ship an unclear stat. If no real number exists yet, remove the metric entirely rather than inventing one. | See Section 8.3 finding — this stat does not currently parse |

### 12.3 Remove — these are the confirmed "vibecoded" tells, delete on sight

- **All emoji used as UI icons** (📊 🔄 🛠️ and similar). Replace with proper SVG icons, hand-drawn or from a real icon set — never emoji, anywhere in the interface.
- **All decorative bar charts with no real data** (`style="height: 52%"` etc. with no labeled axis or source). If a chart is wanted, it must represent a real, labeled number, or it should not exist.
- **All Pexels/stock photography.** Do not replace with different stock photos. Prefer: original photography if available, abstract geometric/brand-color compositions, or no imagery at all over generic stock photography. A strong type-and-color system beats a stock photo every time.
- **The pricing-card component currently displaying the sector roadmap.** Do not reskin it — design a new, distinct visual pattern for "Education → Agriculture → Health → Utilities → Mobility & Cities" that does not resemble a SaaS pricing table (no "tiers," no implied cost comparison). A horizontal timeline, a connected-nodes diagram, or a simple staged list are all better fits than a pricing grid.

### 12.4 Fix — real, concrete engineering corrections

- **Rename CSS variables to match their actual values.** `--gold: #1c5cf5` and `--gold-soft: #2de8e8` are misnamed (both are blue/cyan, not gold). Rename to `--accent-blue: #1c5cf5` and `--accent-cyan: #2de8e8`. Update every reference across `styles.css`.
- **Wire the four "View framework →" links to real destinations.** The source documents already exist in the repo (`Ansai_GID001_Group_Identity`, `Ansai_GCC001_Culture_Constitution`, `Ansai_GEP001_Engineering_Principles`, `Ansai_GDP001_Design_Playbook`). Convert each to a clean rendered page or a linked PDF and point the corresponding link at it. Do not ship a live "View framework →" link that resolves to `#`.
- **Optimize every image before shipping.** No JPG over ~200KB. Convert to WebP/AVIF with responsive `srcset`. This matters specifically for Ansai given the product's own pitch is reliability under poor connectivity — a heavy homepage undercuts the story.
- **Make the copyright year dynamic** (`new Date().getFullYear()`), not hardcoded.
- **Confirm the footer domain.** It currently links to `ansai.co`, a different domain than the live `ansaitechnologies.co.ke`. Verify this is intentional before shipping either way.

### 12.5 Stack decision — default unless told otherwise

**Stay on the current vanilla HTML/CSS/JS stack.** Per Section 8.4, roughly 90% of the identified problems are fixable without a framework migration. Do not introduce React, Next.js, or a build pipeline as a side effect of this pass. If Skiper UI or Vengeance UI components are wanted, hand-port the *specific visual/interaction pattern* (e.g., a particular hover effect or card motion) into vanilla CSS/JS rather than pulling in the dependency and the framework it requires. A full React migration is a separate, deliberate future decision — not something to back into while fixing copy and images.

### 12.6 Design language — apply consistently

- **Typography:** DM Sans (weights 400/500/700/800) for all text, DM Mono for numerals, stats, and technical labels. Already correctly loaded — keep as-is.
- **Color:** navy `#111c27` background, `#ffffff` text, `#8b9bb4` muted text, `--accent-blue: #1c5cf5` and `--accent-cyan: #2de8e8` as the only two accent colors (post-rename per 12.4). Do not introduce additional accent colors without a documented reason.
- **Motion:** subtle, purposeful, never decorative-for-its-own-sake. Reference Emil Kowalski's written work (animations.dev) for the standard to hold interactions to — motion should clarify state changes, not perform activity.
- **Anti-slop discipline:** apply the working principles from Taste Skill (tasteskill.dev / `github.com/Leonxlnx/taste-skill`) even without formally installing it — specifically its redesign-audit-first approach (assess what exists before changing it) and its pre-flight checklist (no shipping a section without checking it against known AI-slop patterns first).
- **One metaphor per section, maximum**, in any user-facing copy. No stacking of reef/mitochondria/road analogies in the same paragraph — those stay internal (Section 3.2), never external.

### 12.7 Pre-ship checklist — run this before anything goes live

- [ ] Zero instances of "institution" or "operational infrastructure" anywhere in shipped copy
- [ ] Zero emoji used as icons
- [ ] Zero decorative charts without real, labeled data
- [ ] Zero stock photography
- [ ] All four framework links resolve to real content
- [ ] All images under ~200KB, modern format, responsive
- [ ] CSS variables named accurately
- [ ] Copyright year generated dynamically
- [ ] The locked one-liner (12.1) appears verbatim somewhere above the fold
- [ ] Nothing on the page describes Ansai as an "AI agent company" or leads with "agentic" anywhere outside a clearly marked technical/engineering section

---

## 13. DESIGN ADDENDUM — July 2026 (supersedes 12.4 token naming and 12.6 design language)

The site was rebuilt to Section 12 in July 2026, then overhauled on the visual layer to a tasteskill v2 spec (`ansai-redesign-prompt.md` in this repo). Where this section conflicts with 12.4 or 12.6, this section wins. Copy, IA, and the locked terminology of Sections 2 and 12.1 are unchanged.

### 13.1 Locked tokens (current)

| Token | Value | Role |
|---|---|---|
| `--navy` | `#111C27` | page background |
| `--blue` | `#1C5CF5` | **sole accent**, used identically everywhere: CTAs, icons, links, featured tiles, data highlights |
| `--teal` | `#2DE8E8` | **logo mark only**, never anywhere else on a page |
| `--white` | `#ffffff` | primary text on dark |
| `--muted` | `#8B98A8` | secondary text |
| `--muted-dim` | `#5A6C82` / `#7A8595` | tertiary text, labels |

The 12.4 instruction to rename variables to `--accent-blue` and `--accent-cyan` is retired: there is no cyan CSS token anymore. The brand gradient is likewise retired from CTAs and surfaces; it survives only inside the logo mark artwork.

### 13.2 Shape, layout, and motion locks

- Radius: 8px buttons, 20px cards, one scale per element type, no exceptions.
- Nav: single line, 64px default height, 80px maximum.
- Hero: asymmetric split, headline and CTA left-aligned, solid blue panel on the right that bleeds past its own column edge. Headline maximum 2 lines on desktop. No tagline, trust strip, or pricing teaser inside the hero.
- Feature grid: bento with exact cell count for the content, one larger tile, at most one fully saturated blue cell, remaining cells tinted (`rgba(28,92,245,0.09)`) or neutral surface.
- Motion budget per page: one scroll-triggered staggered reveal (currently the bento cells), fires once, nothing else animates on load or on a loop, everything wrapped in `prefers-reduced-motion`.
- Zero em-dashes in shipped site copy. The 12.1 one-liner ships in its approved comma form: "Ansai builds digital infrastructure for African organizations: schools, businesses, and enterprises, making their data queryable and actionable through AI." (Terminology unchanged; punctuation adapted by founder decision, July 2026.)
- One CTA label per intent across nav, hero, and footer. Contact intent label: "Start a conversation" (mailto:hello@ansaitechnologies.co.ke).

### 13.3 Document knock-on

GDP-001 (Design Playbook) was updated to v1.1 on its rendered web page (`frameworks/design-playbook.html`) to reflect the single-accent and radius locks; the `.docx` source in this repo remains v1.0 and should be regenerated from the web page when convenient. The rendered page is the current authority.
