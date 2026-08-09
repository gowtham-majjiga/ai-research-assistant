# Design Decisions

## Why separate planning from retrieval?

The planner determines what should be searched; retrieval only knows how to talk to a provider. This separation makes provider integrations independently testable.

## Why deterministic ranking?

The portfolio version keeps ranking inspectable. A recruiter can understand why a document was promoted instead of relying on an opaque score.

## Why cache?

Research questions often repeat during development. A small TTL cache reduces duplicate network calls and improves iteration speed.

## Why return errors instead of swallowing them?

The UI can still show successful evidence while retaining enough diagnostic information to understand which provider failed.
