# Video 07 Brief — Sensitive action executes without human approval

**Status:** Brief  
**Buyer:** Business owner responsible for an AI-enabled workflow that can send refunds, change records, or trigger another consequential action.  
**Failure:** The agent chooses and executes a synthetic refund without a human approval step.  
**Business consequence:** An incorrect or unauthorized action can move money or alter a customer record before a person can intervene.  
**Detection:** Show the proposed action, policy decision, approval state, and action log.  
**Control:** Separate recommendation from execution; require an authorized human to approve the exact action and amount, then validate the approval server-side before execution.  
**Evidence:** The same proposed refund is blocked before approval, then executes once after an authorized approval; rejected or expired approval remains blocked.  
**CTA:** Request a review conversation about an automation or AI agent already in development or production.

## Production note

Use synthetic examples, verify that the failure is reproducible, and limit claims to the evidence captured. Complete a demo plan and English script before recording.
