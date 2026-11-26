---
name: schedule-meeting
description: Find calendar availability and book or update meetings when the user asks to arrange a meeting or respond to an invitation.
---

# Schedule a meeting

Read [team rules](../friday/references/team.md). Run this workflow in the current context.

## Connect and verify Google Calendar

Discover Calendar tools/schemas; verify the intended account and accessible calendars through a small read. Use request/profile scope or an unambiguous primary calendar; ask if unclear. Missing tools or access means unavailable Calendar, not free availability. Read [connection setup](../friday/references/connections.md) on failure and reverify afterward. Never create a test event to verify access.

## Find a time

Resolve title/purpose, attendee email addresses, date/window, duration, timezone, calendar, and any needed agenda/preparation. Ask only for missing essentials. Never invent addresses or treat a name match as recipient confirmation. Add conferencing only when requested or established by preference.

Check the user's and accessible participant/room calendars with timezone-aware boundaries. Inaccessible calendars mean unknown availability; mark unverified participants in proposals. For an explicitly requested booking time, inaccessible calendars alone do not require renewed approval. Do not silently change accounts or time, or book across known conflicts.

## Book and verify

An explicit booking request with resolved details authorizes the event and specified invitations. Finding availability, scanning mail, or proposing times does not. Do not seek redundant approval unless the host requires it.

Before writing, search for an existing event/invitation with the same purpose and participants. Reuse or modify it only as requested; accepting an invitation uses the response action, not a new event.

Use the provider's timed-event schema with timezone-aware start/end, title, calendar, and attendees. Set `notify=true` when exposed unless a silent event was requested; do not send a separate Gmail invitation.

Read back the event when possible; verify time, timezone, attendees, calendar, and conference link. Recheck pending conference provisioning before claiming a final link. Reconcile timeouts/ambiguous writes through reads before retrying; never create another event while the first result is unresolved.

Return the event link, date/time/timezone, attendees, actions, unverified availability, and pending details. Claim booking only from a successful write and supporting result; creation does not prove notification delivery or acceptance.
