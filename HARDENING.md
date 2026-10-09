<!-- markdownlint-disable -->

# Hardening Report: rtCamp--action-slack-notify/v2.3.3

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **rtCamp--action-slack-notify/v2.3.3** was hardened automatically. 1 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### unpinned-uses (severity: high)

Two `uses:` steps in action.yml reference the Docker image `ghcr.io/rtcamp/action-slack-notify` using a mutable version tag (`:v2.3.3`) instead of an immutable SHA digest. This means the image could be silently replaced with a different (potentially malicious) version without any change to the workflow. Both occurrences are: `uses: "docker://ghcr.io/rtcamp/action-slack-notify:v2.3.3"`. These should be replaced with a pinned digest reference such as `docker://ghcr.io/rtcamp/action-slack-notify@sha256:<64-hex-char-digest>`.

Locations:

- `action.yml:44`
- `action.yml:52`

## Iteration Notes

### Iteration 1

**Fixes applied:** unpinned-uses

**Notes:**

Replaced both mutable tag references `docker://ghcr.io/rtcamp/action-slack-notify:v2.3.3` in action.yml (lines 44 and 52) with pinned digest references `docker://ghcr.io/rtcamp/action-slack-notify:v2.3.3@sha256:acc1c430721b27030d3dacf4273eec569388ad650e127bb9f1292f33cd9cd9bd`. The docker:// scheme and :v2.3.3 tag are preserved inline, with the immutable SHA digest appended to prevent silent image replacement.

