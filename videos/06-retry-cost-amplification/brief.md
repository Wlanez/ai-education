# Video 06 Brief — Retries increase cost and worsen an incident

**Status:** Brief  
**Buyer:** Operations or engineering owner of an automation that calls a paid or rate-limited service.  
**Failure:** A failing call is retried immediately by multiple workflow runs, multiplying requests during a provider slowdown.  
**Business consequence:** API or model costs rise while the provider is least able to respond; useful work is delayed.  
**Detection:** Show attempts per job, retry rate, response status, and estimated request cost over the same synthetic interval.  
**Control:** Set a retry budget, cap attempts, use exponential backoff with jitter for retryable failures, and pause or shed load when the budget is exhausted.  
**Evidence:** Compare unbounded/immediate retries with a bounded schedule; show fewer calls during the same simulated outage and an explicit pending state.  
**CTA:** Request a review conversation about an automation or AI agent already in development or production.

## Production note

Use synthetic examples, verify that the failure is reproducible, and limit claims to the evidence captured. Complete a demo plan and English script before recording.
