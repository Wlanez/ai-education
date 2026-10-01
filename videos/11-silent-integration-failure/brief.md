# Video 11 Brief — Integration fails silently

**Status:** Brief  
**Buyer:** Integration or operations owner responsible for data moving between two business systems.  
**Failure:** A connector catches and suppresses a downstream write error, then reports the overall workflow as successful.  
**Business consequence:** Source and destination records drift apart; teams discover the gap only during reconciliation or when a customer asks.  
**Detection:** Compare source events against destination acknowledgements and show a missing acknowledgement despite a green workflow status.  
**Control:** Preserve and surface the error, correlate the event across systems, retry only safe failures, and route exhausted items to a visible queue with an owner.  
**Evidence:** Inject a destination failure; show the workflow no longer reports success, the mismatch is counted, and the event is available for controlled recovery.  
**CTA:** Request a review conversation about an automation or AI agent already in development or production.

## Production note

Use synthetic examples, verify that the failure is reproducible, and limit claims to the evidence captured. Complete a demo plan and English script before recording.
