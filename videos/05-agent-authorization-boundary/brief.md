# Video 05 Brief — Agent exposes data outside the user's authorization

**Status:** Brief  
**Buyer:** Product, security, or operations owner of an AI agent that retrieves information for different users.  
**Failure:** The agent uses a shared service identity and returns a synthetic record belonging to another user after a request with a different user ID.  
**Business consequence:** A support user for Customer A can read Customer B's invoice total and billing address. This exposes confidential billing details, forces support and security teams to investigate, and delays resolving the customer's issue.  
**Detection:** Record the authenticated principal, requested resource owner, authorization decision, and returned record ID using synthetic values.  
**Control:** Enforce authorization in the application/server for every retrieval; scope queries to the authenticated principal and deny by default. Do not rely on a prompt or the model to enforce access.  
**Evidence:** Run User A and User B requests; show the cross-user request is denied and no other user's record is returned.  
**CTA:** Request a review conversation about an automation or AI agent already in development or production.

## Production note

Use synthetic examples, verify that the failure is reproducible, and limit claims to the evidence captured. Complete a demo plan and English script before recording.

