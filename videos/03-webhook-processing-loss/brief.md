# Video 03 Brief — Webhook is received but processing is lost

**Status:** Brief  
**Buyer:** Engineering or operations owner responsible for an event-driven workflow that receives webhooks.  
**Failure:** The endpoint returns HTTP 200 before the event is durably queued; the process crashes before handling the event.  
**Business consequence:** The sender believes delivery succeeded, but the business action never happens and may not be retried.  
**Detection:** Compare received event IDs with completed processing records and show the missing completion.  
**Control:** Persist the event to a durable queue or inbox before acknowledging receipt; track queued, processing, completed, and dead-letter states.  
**Evidence:** Crash after receipt but before processing; show the event remains queued and completes after restart, with one business action.  
**CTA:** Request a review conversation about an automation or AI agent already in development or production.

## Production note

Use synthetic examples, verify that the failure is reproducible, and limit claims to the evidence captured. Complete a demo plan and English script before recording.
