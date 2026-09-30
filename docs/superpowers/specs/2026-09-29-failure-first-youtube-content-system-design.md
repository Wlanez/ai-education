# Failure-First YouTube Content System — Design

**Date:** 2026-09-29  
**Repository:** `Wlanez/ai-education`  
**Status:** Approved design

## Purpose

Build a 90-day YouTube content system that generates qualified calls with companies whose business automations or AI agents are unreliable.

The repository is an execution system for producing evidence-led videos, not a general collection of AI lessons.

## Primary outcome

The primary success metric is **qualified client calls attributed to the videos**.

Secondary metrics:

- Relevant conversations started
- Requests for an automation review
- Paid diagnostics
- Repair or implementation opportunities
- Viewer retention and qualified comments

Views and subscriber growth are supporting indicators, not the main objective.

## Audience

The initial audience is companies that already have an automation or AI agent in development or production and experience failures such as:

- Lost or duplicated records
- Silent integration failures
- Incorrect or unsupported answers
- Excessive retries and API costs
- Missing audit evidence
- Weak authorization boundaries
- No human approval for sensitive actions
- Insufficient logs for incident investigation

The content will use examples from multiple industries without committing the channel to one vertical during the first 90 days.

## Positioning

> I help companies diagnose and stabilize automations and AI agents that work in a demo but fail in real operations.

Supporting message:

> Your automation works—until something unexpected happens. I help find and fix those failure points before they cost you customers, money, or trust.

## Editorial strategy

The channel follows a **failure-first** approach.

Each video begins with an observable failure and follows this sequence:

1. Show the workflow operating normally.
2. Introduce a realistic failure.
3. Show the business consequence.
4. Diagnose the failure.
5. Add a bounded control.
6. Repeat the scenario.
7. Show evidence that the behavior is now safe.
8. Invite the viewer to request a diagnostic call.

Tool tutorials are permitted only when a tool supports the business problem. The channel will not be organized around n8n, Claude, OpenAI, Kubernetes, or another tool.

## Channel and language

- Primary channel: YouTube
- Main language: English
- English level: clear B2 delivery supported by a complete script
- Long-form target: 6–9 minutes
- Short-form derivative: 45–60 seconds
- Secondary distribution: LinkedIn and YouTube Shorts

Scripts use short sentences, necessary technical vocabulary, explicit screen directions, and natural pauses.

## Repository structure

```text
ai-education/
├── README.md
├── strategy/
│   ├── positioning.md
│   ├── ideal-client.md
│   ├── offer-and-cta.md
│   └── publishing-workflow.md
├── videos/
│   ├── roadmap.md
│   ├── 01-api-failure/
│   │   ├── brief.md
│   │   ├── script.md
│   │   └── demo-plan.md
│   └── ...
├── templates/
│   └── video-brief-template.md
├── demos/
│   └── README.md
├── metrics/
│   └── scorecard.md
└── docs/
    └── superpowers/
        └── specs/
```

## Component responsibilities

### README

Explains the problem Jorge solves, shows the failure-first approach, points to published cases, and invites qualified companies to request a conversation.

### Strategy

Contains stable decisions:

- Positioning and exclusions
- Ideal client and qualifying signals
- Diagnostic offer and single call to action
- Weekly production and distribution workflow

### Video roadmap

Prioritizes the 12 videos for the 90-day season and records their production state.

### Video folder

Each video receives one folder containing:

- `brief.md`: buyer, failure, consequence, evidence, and CTA
- `script.md`: complete English narration and screen directions
- `demo-plan.md`: deterministic setup, success path, failure injection, controls, and expected evidence

### Templates

Provides one reusable brief format so every video remains commercially focused.

### Demos

Holds reproducible supporting code when a video requires it. Demo code is separate from scripts and editorial material.

### Metrics

Tracks publication and commercial outcomes by video. The scorecard records qualified conversations, calls, review requests, and paid opportunities.

## Video brief contract

Every video must answer:

1. Which company or decision-maker has this problem?
2. What failure is being introduced?
3. What is the business consequence?
4. How is the failure detected?
5. Which control limits the damage?
6. What evidence proves the corrected behavior?
7. What single action should the viewer take?

A video should not enter production if these answers are vague.

## First 90-day season

One long-form video will be published each week:

1. Essential API returns HTTP 503
2. Duplicate leads enter the CRM
3. Webhook is received but processing is lost
4. Automation invoices the same transaction twice
5. Agent exposes data outside the user's authorization
6. Retries increase cost and worsen an incident
7. Sensitive action executes without human approval
8. n8n workflow succeeds intermittently
9. Agent lacks logs required for investigation
10. Stale source data produces an unsupported answer
11. Integration fails silently
12. Full pre-production automation review

The order moves from understandable operational failures to a complete diagnostic, progressively demonstrating Jorge's reliability expertise.

## Conversion flow

```text
Visible failure
    ↓
YouTube demonstration
    ↓
Failure checklist
    ↓
Request for review
    ↓
Qualified diagnostic call
    ↓
Paid diagnostic, repair, or implementation
```

Each video uses one CTA: request a review conversation about an existing automation. Educational CTAs such as “follow for more” may appear only after the commercial CTA and must not replace it.

## Initial service path

The content supports a simple service progression:

1. Fit conversation
2. Fixed-scope automation reliability review
3. Written findings and prioritized remediation plan
4. Repair or controlled pilot
5. Optional monitoring and operational support

Specific pricing is intentionally kept outside the editorial design so it can be tested without rewriting the content system.

## Publishing workflow

1. Select the next failure from the roadmap.
2. Complete and review the commercial brief.
3. Build a deterministic demo with a repeatable failure.
4. Write the English script.
5. Rehearse for clarity and timing.
6. Record the success and failure paths.
7. Publish the YouTube video.
8. Produce one Short and one LinkedIn post.
9. Record conversations, calls, and opportunities in the scorecard.
10. Use evidence from results to reprioritize later videos.

## Quality controls

Before publication, verify:

- The failure can be reproduced.
- The business consequence is stated in plain language.
- The control is proportional to the risk.
- Logs or other evidence support the conclusion.
- No confidential employer or client information is exposed.
- Claims match what the demo proves.
- English narration is easy to deliver naturally.
- The CTA matches the target audience.

## Scope exclusions

The first 90 days will not prioritize:

- General AI news
- Model benchmark commentary
- Prompt collections without a business workflow
- Tool tutorials without a failure scenario
- A paid course or community
- Multiple unrelated calls to action
- Building a large SaaS product before validating client demand

## Review after 90 days

Evaluate:

- Number and quality of calls
- Problems mentioned repeatedly by buyers
- Industries producing the strongest response
- Videos responsible for commercial conversations
- Which diagnostic work can become a repeatable offer
- Whether a focused vertical should replace the multi-industry approach
