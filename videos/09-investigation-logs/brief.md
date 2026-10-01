# Video 09 Brief — Agent lacks logs required for investigation

**Status:** Brief  
**Buyer:** Engineering or compliance owner who may need to investigate an AI agent's decision or action.  
**Failure:** An agent returns an incorrect result, but logs omit the correlation ID, tool outcome, source/version, or decision status needed to reconstruct the run.  
**Business consequence:** A customer receives a wrong delivery status, but the support team cannot tell which agent run produced it. They cannot send a targeted correction, and repeat support tickets arrive while they investigate.  
**Detection:** Attempt to trace a synthetic request from user input through retrieval/tool calls to final outcome; identify missing links.  
**Control:** Emit structured, correlated events for the workflow stage, tool name/result, source reference, model/config version, and final action status; redact secrets and unnecessary personal data.  
**Evidence:** Compare a sparse log with a redacted event timeline that reconstructs one synthetic run without exposing sensitive content.  
**CTA:** Request a review conversation about an automation or AI agent already in development or production.

## Production note

Use synthetic examples, verify that the failure is reproducible, and limit claims to the evidence captured. Complete a demo plan and English script before recording.

