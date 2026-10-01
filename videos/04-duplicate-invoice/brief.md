# Video 04 Brief — Automation invoices the same transaction twice

**Status:** Brief  
**Buyer:** Finance or billing operations owner using an automation to create invoices or payment requests.  
**Failure:** The billing provider accepts an invoice request, but the response times out. The automation retries without checking whether the first request succeeded.  
**Business consequence:** The same transaction can create a second invoice or payment request, requiring correction and risking duplicate collection.  
**Detection:** Compare transaction ID, provider invoice IDs, request attempts, and final ledger state.  
**Control:** Use a stable transaction idempotency key where supported; after an ambiguous timeout, query or reconcile provider state before resending.  
**Evidence:** Simulate provider acceptance followed by a timeout; retry and show one provider invoice ID and one ledger entry.  
**CTA:** Request a review conversation about an automation or AI agent already in development or production.

## Production note

Use synthetic examples, verify that the failure is reproducible, and limit claims to the evidence captured. Complete a demo plan and English script before recording.
