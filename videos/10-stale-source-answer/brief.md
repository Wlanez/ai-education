# Video 10 Brief — Stale source data produces an unsupported answer

**Status:** Brief  
**Buyer:** Product or operations owner of an agent that answers from changing policies, procedures, or product documentation.  
**Failure:** Retrieval returns an old document version, and the agent answers without checking the source date or validity.  
**Business consequence:** Staff or customers may act on an outdated price, process, or policy.  
**Detection:** Display source version, effective date, retrieval timestamp, and the answer's cited source.  
**Control:** Define freshness metadata and a maximum age for the use case; exclude or flag stale sources and abstain or escalate when no current source is available.  
**Evidence:** Provide one current and one stale synthetic document; show the current answer is sourced and the stale-only request is flagged or withheld.  
**CTA:** Request a review conversation about an automation or AI agent already in development or production.

## Production note

Use synthetic examples, verify that the failure is reproducible, and limit claims to the evidence captured. Complete a demo plan and English script before recording.
