# Failure-First YouTube Content System Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the approved design into a usable 90-day editorial system that produces evidence-led English videos and qualified automation reliability calls.

**Architecture:** Keep this repository documentation-first. Stable commercial decisions live in `strategy/`; each planned video lives in its own folder; the roadmap and scorecard connect production to commercial outcomes. Build the first API-503 example end-to-end before expanding the remaining eleven briefs.

**Tech Stack:** Markdown; deterministic demo artifacts or instructions; GitHub for versioned scripts, evidence, and publishing workflow. No application framework or paid SaaS is required.

**Spec:** `docs/superpowers/specs/2026-09-29-failure-first-youtube-content-system-design.md`

## Global Constraints

- Primary success metric: qualified client calls attributed to the videos.
- Initial audience: companies with an automation or AI agent already in development or production.
- Positioning: “I help companies diagnose and stabilize automations and AI agents that work in a demo but fail in real operations.”
- Main language: English, with clear B2 delivery supported by a complete script.
- Long-form target: 6–9 minutes; Short-form derivative: 45–60 seconds.
- Each video uses one commercial CTA: request a review conversation about an existing automation.
- Every video follows the failure-first sequence and includes repeatable evidence of corrected behavior.
- Do not expose confidential employer or client information; do not make claims beyond demo evidence.
- Keep videos multi-industry in the first 90 days and tool-led content out of the editorial structure.

## Review Focus

- A brief with no identifiable buyer or vague business consequence must be held from production; validate required brief fields in the template and first brief.
- A demo that cannot reproduce the same failure on demand must not be treated as proof; include setup, injection, reset, and expected evidence in demo instructions.
- Retries, duplicate events, or repeated requests can accidentally make the example nondeterministic or hide data loss; specify stable inputs and observable outcomes.
- Logs may expose credentials, personal data, or employer/client information; include a pre-recording redaction check and use synthetic data.
- A script may exceed the time target or sound unnatural at B2 delivery; include a timed read-through and plain-language review for the first episode.

---

## File Structure

- Create `README.md`: channel purpose, positioning, failure-first method, paths into the repo, and the single qualified-conversation CTA.
- Create `strategy/positioning.md`: positioning, audience, exclusions, proof boundaries, and language principles.
- Create `strategy/ideal-client.md`: target-company profile and observable qualifying signals.
- Create `strategy/offer-and-cta.md`: review conversation, fixed-scope reliability review, deliverables, and CTA wording.
- Create `strategy/publishing-workflow.md`: weekly production, review, distribution, and feedback loop.
- Create `templates/video-brief-template.md`: the seven-question brief contract and production gate.
- Create `videos/roadmap.md`: the ordered 12-video season and per-video status.
- Create `videos/01-api-failure/brief.md`: buyer, HTTP 503 failure, business consequence, detection, control, evidence, CTA.
- Create `videos/01-api-failure/demo-plan.md`: deterministic success/failure scenario, injection, control, reset, synthetic data, and expected evidence.
- Create `videos/01-api-failure/script.md`: complete 6–9 minute English script with screen directions and one CTA.
- Create `demos/README.md`: how demo artifacts are organized and how to run/reset them without secrets.
- Create `metrics/scorecard.md`: per-video publishing data and qualified conversations, calls, reviews, and paid opportunities.

## Task 1: Establish the Commercial and Editorial Foundation

**Files:**
- Create: `README.md`
- Create: `strategy/positioning.md`
- Create: `strategy/ideal-client.md`
- Create: `strategy/offer-and-cta.md`
- Create: `strategy/publishing-workflow.md`

**Interfaces:**
- Consumes: approved design in the spec.
- Produces: shared positioning, buyer signals, single CTA, and weekly workflow used by all video briefs.

- [ ] **Step 1: Draft and review positioning**
  Record the approved positioning, target problem, 90-day multi-industry constraint, English delivery standard, and explicit exclusions. Verify the wording does not position the channel as general AI education or as a tool tutorial channel.

- [ ] **Step 2: Define buyer qualification**
  Describe companies already running or building automations/agents, the operational failure signals they can recognize, and when a viewer is not a fit. Verify each signal connects to a possible reliability review.

- [ ] **Step 3: Define offer and CTA**
  Describe the fit conversation, fixed-scope review, written findings, remediation plan, and optional repair/support path. Add exactly one primary CTA for every video: request a review conversation about an existing automation.

- [ ] **Step 4: Define weekly workflow**
  Specify selection, brief gate, deterministic demo, script/rehearsal, recording, publication, Short and LinkedIn derivative, scorecard update, and roadmap feedback.

- [ ] **Step 5: Write the repo README**
  Summarize the business problem, failure-first method, entry points to strategy/videos/demos/metrics, and CTA. Verify linked paths exist.

- [ ] **Step 6: Review foundation for contradictions**
  Check all five strategy files against the spec. Verify that views are secondary, English is the primary video language, the CTA is consistent, and unsupported claims or pricing commitments were not introduced.

- [ ] **Step 7: Commit the foundation**
  `git add README.md strategy && git commit -m "docs: establish failure-first content strategy"`

## Task 2: Add the Reusable Brief, 90-Day Roadmap, Demo Guide, and Scorecard

**Files:**
- Create: `templates/video-brief-template.md`
- Create: `videos/roadmap.md`
- Create: `demos/README.md`
- Create: `metrics/scorecard.md`

**Interfaces:**
- Consumes: Task 1 positioning, qualification, offer, and publishing workflow.
- Produces: a production gate, canonical video sequence, demo safety conventions, and outcome tracking format.

- [ ] **Step 1: Write the brief template**
  Include the seven required questions verbatim in meaning: buyer; failure; business consequence; detection; damage-limiting control; evidence; one viewer action. Add a hold-from-production rule when an answer is vague.

- [ ] **Step 2: Write the 12-video roadmap**
  Preserve the approved order and titles from the spec. Track each video as `Not started`, `Brief`, `Demo`, `Script`, `Recorded`, `Published`, or `Reviewed`; include target format and result link/date fields without inventing publication dates.

- [ ] **Step 3: Define demo conventions**
  Require synthetic data, repeatable setup and reset steps, isolated credentials, visible failure injection, observable business outcome, control behavior, and evidence capture. State that no secrets or confidential employer/client data may be committed.

- [ ] **Step 4: Create the scorecard**
  Provide one row per video and fields for publication date, long-form/Short/LinkedIn links, qualified conversations, calls, review requests, paid diagnostics, repair/implementation opportunities, and notes. Keep views and retention as supporting indicators.

- [ ] **Step 5: Validate completeness**
  Check the 12 items and order against the spec. Verify each brief-template field has a matching scorecard or production artifact where applicable; ensure blank metrics are clearly distinguishable from zero.

- [ ] **Step 6: Commit the operating system**
  `git add templates videos/roadmap.md demos/README.md metrics/scorecard.md && git commit -m "docs: add content workflow and measurement"`

## Task 3: Build the First Repeatable Case — Essential API Returns HTTP 503

**Files:**
- Create: `videos/01-api-failure/brief.md`
- Create: `videos/01-api-failure/demo-plan.md`
- Create: `videos/01-api-failure/script.md`
- Modify: `videos/roadmap.md`
- Optional create: `demos/01-api-failure/*` only if a small runnable demo materially improves repeatability.

**Interfaces:**
- Consumes: Task 1 buyer/CTA/workflow; Task 2 brief contract, roadmap status, and demo conventions.
- Produces: first complete video package that can be rehearsed, recorded, and measured.

- [ ] **Step 1: Complete the commercial brief**
  Fill every template field for an essential API returning HTTP 503. State a concrete business impact in plain language, name how failure is detected, specify a bounded control, define evidence, and use the shared CTA. Keep industry details generic.

- [ ] **Step 2: Design the deterministic demo**
  Document a healthy request, a repeatable 503 injection, the observable failed business outcome, the control (bounded retry/circuit-breaker or safe failure path appropriate to the scenario), and a rerun proving corrected behavior. Specify stable synthetic inputs, reset steps, and expected logs/metrics. Do not imply one control solves all outage conditions.

- [ ] **Step 3: Decide whether runnable code is needed**
  Prefer explicit reproducible instructions if they are enough to record the scenario. If code is needed, keep the demo isolated, small, and free of third-party services and secrets; document exact run/reset commands in `demos/01-api-failure/README.md`.

- [ ] **Step 4: Write the full English narration**
  Create a 6–9 minute script using short, natural B2 sentences, with explicit on-screen directions, pauses, failure and recovery evidence, and one CTA. Do not claim a fix unless the planned rerun demonstrates it.

- [ ] **Step 5: Rehearse and quality-check**
  Read aloud with a timer; revise for 6–9 minutes and natural delivery. Confirm technical terms are explained, the consequence is clear, the failure is repeatable, evidence matches the narration, the CTA is single, and all displayed data are synthetic/redacted.

- [ ] **Step 6: Update roadmap status**
  Mark only artifacts actually completed. Keep recording/publication fields empty until those events occur.

- [ ] **Step 7: Commit the first case**
  `git add videos/01-api-failure videos/roadmap.md demos && git commit -m "content: prepare first API failure case"`

## Task 4: Extend the Roadmap into the Remaining 11 Briefs

**Files:**
- Create: `videos/02-duplicate-crm-leads/brief.md`
- Create: `videos/03-webhook-processing-loss/brief.md`
- Create: `videos/04-duplicate-invoice/brief.md`
- Create: `videos/05-agent-authorization-boundary/brief.md`
- Create: `videos/06-retry-cost-amplification/brief.md`
- Create: `videos/07-sensitive-action-approval/brief.md`
- Create: `videos/08-intermittent-n8n-workflow/brief.md`
- Create: `videos/09-investigation-logs/brief.md`
- Create: `videos/10-stale-source-answer/brief.md`
- Create: `videos/11-silent-integration-failure/brief.md`
- Create: `videos/12-preproduction-reliability-review/brief.md`
- Modify: `videos/roadmap.md`

**Interfaces:**
- Consumes: approved template, qualification, CTA, demo safety conventions, and first case as quality example.
- Produces: twelve commercially qualified briefs with production readiness visible.

- [ ] **Step 1: Draft remaining briefs in roadmap order**
  For each video, specify buyer, observable failure, plain-language consequence, detection, proportional control, proof to capture, and the shared CTA. A brief that cannot state these concretely stays marked `Brief` and must not be represented as production-ready.

- [ ] **Step 2: Check overlap and progression**
  Verify the episodes build from operational failures toward a complete review, while each has a distinct failure and business consequence. Keep tool names subordinate to the problem.

- [ ] **Step 3: Review safety and claims**
  Verify synthetic examples, least-privilege framing where authorization is involved, human approval where sensitive actions are involved, and no unsupported guarantee language.

- [ ] **Step 4: Validate roadmap consistency**
  Compare folder names, titles, brief status, and order. Verify all 12 roadmap entries resolve to the intended brief path.

- [ ] **Step 5: Commit the remaining briefs**
  `git add videos && git commit -m "content: define remaining reliability video briefs"`

## Task 5: Run a 90-Day Review and Reprioritize from Evidence

**Files:**
- Modify: `metrics/scorecard.md`
- Modify: `videos/roadmap.md`
- Optional create: `metrics/review-YYYY-MM-DD.md` for each completed review.

**Interfaces:**
- Consumes: published-video metrics and actual conversations/opportunities.
- Produces: documented decisions about buyer demand, strongest problems, and next production priorities.

- [ ] **Step 1: Record actual outcomes**
  Update the scorecard after each publishing cycle. Use `0` only for a measured zero and `—` for not yet measured; record qualified conversations and attribution evidence.

- [ ] **Step 2: Review commercial signal**
  At the 90-day point, summarize call count and quality, repeated buyer problems, industries responding, videos linked to commercial conversations, and diagnostic work that could become repeatable.

- [ ] **Step 3: Reprioritize**
  Adjust later topics or select a vertical only when the recorded evidence supports it. Record the reason and keep original outcomes intact.

- [ ] **Step 4: Commit the review**
  `git add metrics videos/roadmap.md && git commit -m "docs: review first content season outcomes"`
