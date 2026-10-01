# Video 08 Brief — n8n workflow succeeds intermittently

**Status:** Brief  
**Buyer:** Operations owner maintaining an n8n workflow that supports a real business process.  
**Failure:** A downstream node intermittently returns an error, while workflow error handling does not make the failed run visible or recoverable.  
**Business consequence:** Some records complete and others remain unfinished; staff may assume the workflow is dependable because many runs succeed.  
**Detection:** Correlate execution ID, node status, input record ID, and final business outcome; alert when the expected completion record is missing.  
**Control:** Make the failing path explicit, retry only safe transient errors with a bounded policy, preserve failed items for review, and use an idempotency key for any repeated write.  
**Evidence:** Inject a deterministic downstream failure on one run and success on another; show the failed item is visible and the successful item is written once.  
**CTA:** Request a review conversation about an automation or AI agent already in development or production.

## Production note

Use synthetic examples, verify that the failure is reproducible, and limit claims to the evidence captured. Complete a demo plan and English script before recording.
