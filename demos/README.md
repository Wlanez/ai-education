# Demo Safety and Reproducibility

Use demonstrations to show one business failure, a proportional control, and evidence of the resulting behavior.

## Each demo must document

- **Purpose:** the workflow and consequence being demonstrated.
- **Requirements:** local tools and versions, with no paid external service required unless the video brief justifies it.
- **Setup:** deterministic synthetic input and initial state.
- **Healthy path:** expected request and business outcome before fault injection.
- **Failure injection:** exact action that creates the observable failure.
- **Control:** what behavior changes and what risk remains.
- **Reset:** exact steps to restore the initial state and rerun.
- **Evidence:** expected logs, metrics, records, or screen state for both failure and controlled outcome.

## Data and access rules

- Use synthetic data by default. If a real example is necessary, redact it and confirm it is safe to publish.
- Never commit secrets, tokens, credentials, personal data, production payloads, or confidential employer/client information.
- Use least privilege and local-only credentials for any runnable demo.
- Inspect terminal output, browser tabs, logs, and screen recordings for accidental disclosure before publishing.

## Evidence standard

A demo supports only the behavior actually observed in its stated scenario. A successful rerun does not prove that every outage or edge case is solved. State assumptions, control limits, and remaining failure paths plainly.

Keep reusable code under a video-specific folder such as demos/01-api-failure/; keep briefs and narration under videos/.
