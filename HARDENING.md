<!-- markdownlint-disable -->

# Hardening Report: rtCamp--action-slack-notify/v2.3.3

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `1`

Action **rtCamp--action-slack-notify/v2.3.3** was hardened automatically. 1 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### unpinned-uses (severity: high)

Two `uses:` steps in action.yml reference the Docker image `ghcr.io/rtcamp/action-slack-notify` by a mutable tag (`:v2.3.3`) rather than an immutable SHA digest. If the tag is moved or the registry is compromised, a different image could be silently substituted. These should be pinned to a full SHA256 digest, e.g. `docker://ghcr.io/rtcamp/action-slack-notify@sha256:<64-hex-char-digest> # v2.3.3`.

Failing references:
- `uses: "docker://ghcr.io/rtcamp/action-slack-notify:v2.3.3"` (line 44, "Slack Notification (Formatted)" step)
- `uses: "docker://ghcr.io/rtcamp/action-slack-notify:v2.3.3"` (line 48, "Slack Notification (Unformatted)" step)

Locations:

- `action.yml:44`
- `action.yml:48`

## Iteration Notes

### Iteration 1

**Fixes applied:** unpinned-uses

**Notes:**

Replaced both mutable tag references `docker://ghcr.io/rtcamp/action-slack-notify:v2.3.3` (lines 44 and 48 in action.yml) with the immutable SHA256 digest `docker://ghcr.io/rtcamp/action-slack-notify@sha256:acc1c430721b27030d3dacf4273eec569388ad650e127bb9f1292f33cd9cd9bd` (with `# v2.3.3` comment outside the quoted string). The digest was resolved via the Docker Registry HTTP API v2.

