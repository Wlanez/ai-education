# Video 01 Brief — Essential API Returns HTTP 503

**Buyer:** An operations, engineering, or automation owner at a company that submits business orders through an API already in development or production.  
**Failure:** The fulfillment API returns HTTP 503, and the workflow makes one attempt without a bounded recovery path.  
**Business consequence:** The request is not accepted. The order waits for manual follow-up, which can delay fulfillment and create customer support work.  
**Detection:** Capture the HTTP status, attempt count, accepted-order state, and whether the workflow leaves the order in a visible attention state.  
**Control:** Retry only the temporary HTTP 503 response, cap attempts at three, reuse a stable idempotency key, and leave the item pending review after repeated failure. Production systems should add suitable delay/jitter, honor service guidance, and surface the pending item to an owner.  
**Evidence:** Healthy path returns 201 and accepts one order; one-shot 503 returns needs_attention and accepts none; transient 503 returns 503 then 201 with one accepted order; persistent 503 stops after three attempts, reports pending_review, and accepts none.  
**CTA:** Request a review conversation about an automation or AI agent already in development or production.

## Why this case matters

A request being sent does not prove that the receiving service accepted the work. The video demonstrates an order-submission failure in a synthetic local simulator; it does not claim that all 503 errors are transient or that retries solve every outage.

## Production readiness

The demo is deterministic and resettable. Use synthetic order IDs only. The control is limited to this scenario, and narration must call out the limitations of production retry timing and real API idempotency support.
