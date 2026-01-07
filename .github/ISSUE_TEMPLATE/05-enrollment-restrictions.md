name: "Enrollment restrictions"
about: "Server-side enforcement for activity capacity and rules"
title: "Enforce enrollment restrictions server-side"
labels: backend,validation

# Enrollment restrictions

Implement server-side checks:

- Block signup when `max_participants` reached.
- Optionally add eligibility rules (grade-level, prerequisites).
- Return clear error messages for failed signups.

Acceptance criteria:
- Cannot exceed `max_participants`.
- Error codes/messages documented.
