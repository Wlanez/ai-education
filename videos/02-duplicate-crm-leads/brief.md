# Video 02 Brief — Duplicate leads enter the CRM

**Status:** Brief  
**Buyer:** Sales operations or CRM owner whose lead intake automation is already in use.  
**Failure:** A provider redelivers the same lead event after a timeout, and the workflow creates a new CRM record each time.  
**Business consequence:** Sales staff contact the same person more than once, waste time, and may distrust lead counts.  
**Detection:** Compare the incoming provider event ID with CRM records and show a duplicate-record count.  
**Control:** Use the stable provider event ID as an idempotency key and upsert the CRM record; do not rely on name or email alone to identify an event.  
**Evidence:** Deliver the same synthetic event twice; show two delivery attempts but one CRM lead record.  
**CTA:** Request a review conversation about an automation or AI agent already in development or production.

## Production note

Use synthetic examples, verify that the failure is reproducible, and limit claims to the evidence captured. Complete a demo plan and English script before recording.
