# Video 01 — An API Returns HTTP 503: What Happens to the Order?

**Target duration:** 6–9 minutes  
**Delivery:** Read naturally at a calm pace. Keep sentences short.  
**Primary CTA:** Request a review conversation about an existing automation.

## Opening

[SCREEN: Show a synthetic order, ORDER-1000, waiting to be sent to a fulfillment service.]

Your customer places an order. Your system sends it to another service. The service is unavailable for a moment and returns HTTP 503.

What happens next?

In this example, the order is still in your system, but the fulfillment service has not accepted it. If nobody sees the failure, the customer may wait, your team may follow up manually, and the order may be delayed.

Today I’ll show the normal request, the failure, and a small control that makes the result easier to trust.

## The normal path

[SCREEN: Run python3 demo.py. Point to healthy_path.]

First, the service is available. We send ORDER-0999. The API returns HTTP 201, which means the order was created. We made one attempt, and the demo shows one accepted order.

That is the path we expect. But production systems also see short outages, network problems, and services that are temporarily overloaded.

## Failure before the control

[SCREEN: Point to single_attempt_503.]

Now the same kind of request receives HTTP 503. The number 503 means the service is temporarily unable to handle the request. The request was not accepted in this simulation.

The workflow makes one attempt. It records needs_attention and stops. That is safer than pretending the order succeeded, but the order is still waiting. Someone must notice the problem and decide what to do.

A log line by itself may not be enough. If the team has no alert, no queue view, or no follow-up process, this can become a customer delay that people discover later.

This is our business failure: the order submission did not reach the service, and the workflow needs a clear recovery path.

## What the response can tell us

Before changing anything, separate three states: request sent, request accepted, and order fulfilled. They are different. A network call may finish while the response says the service did not accept the work.

A successful response may confirm only that another system received the request. It does not always prove that a person or a later process completed the order. This demo measures accepted_orders because that is the boundary it can observe. In a real workflow, you may need a later fulfillment event or a reconciliation check to confirm the full business outcome.

We also need to decide when to retry. This example retries only HTTP 503, a temporary service error. A 400 means something about the request is invalid; repeating the same request will not correct it. Other statuses, such as a rate limit, need a policy based on the receiving service's guidance. We keep this episode focused on one status.

## Add a bounded control

[SCREEN: Show the retry function and highlight max_attempts=3, the HTTP 503 check, and the order idempotency key.]

We will add three limits.

First, retry only the temporary service error shown here: HTTP 503. A bad request, such as HTTP 400, should not be repeated without a change.

Second, stop after three attempts. A retry limit prevents one request from continuing forever.

Third, use the same idempotency key for every attempt. An idempotency key is a stable identifier for this order. It helps the receiving service recognize a repeated request as the same order, instead of creating it again.

This local demo does not wait between attempts. A production system should use a suitable delay, often with jitter, and follow the service’s retry guidance. The right policy depends on the service and the business process.

## Test a short outage

[SCREEN: Point to transient_503.]

Here, the first attempt returns 503. The second returns 201. The workflow now reports completed after two attempts, and the receiving service accepted one order.

The evidence is visible in the output: attempt one returned 503; attempt two returned 201; accepted_orders is one.

We can also replay the same order in the tests. The stable idempotency key prevents a duplicate in this simulated service. That does not prove every real API supports idempotency. Before using this pattern, confirm how the receiving service handles repeated requests.

## Test a longer outage

[SCREEN: Point to persistent_503.]

What if all three attempts return 503?

The workflow stops after the third attempt and reports pending_review. No order was accepted. This is not a successful recovery, and the system does not claim that it is.

A real workflow should send this item to a visible queue or alert an owner. The owner can check the service and decide when it is safe to try again. The exact follow-up belongs to the business process.

The control has a clear limit: it recovers from a short temporary failure in this example. It does not fix a long outage, incorrect data, or every network problem.

## What to check in your own workflow

[SCREEN: Display three labels: response status, attempt count, accepted record.]

When you review an automation, ask three questions.

Does it check the API response, or does it mark work complete after sending a request?

Does it retry only errors that may recover, and does it stop after a defined limit?

Can the receiving service safely recognize the same request if it arrives again?

Then check what happens after the retry limit. Is the item visible to an owner? Is there an alert? Can the team tell whether the order was accepted?

These questions help separate a request that was sent from work that was actually completed.

## Close and CTA

[SCREEN: Return to the order output. Highlight one accepted order on recovery and pending_review after repeated failure.]

A 503 does not always mean the whole system is broken. But a workflow needs to handle the response honestly.

In this demo, a short outage recovered with a limited retry and one accepted order. A longer outage stopped safely and left the order for review. Those outcomes are visible and repeatable.

If your company already has an automation or AI agent in development or production and you are seeing failures like this, request a review conversation. We can discuss the workflow and the evidence at a high level. Please do not send credentials or confidential production data.

Thanks for watching.
