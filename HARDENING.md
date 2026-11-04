<!-- markdownlint-disable -->

# Hardening Report: rtCamp--action-slack-notify/v2.3.3

> This file was generated automatically by the hardening agent.

**Policy SHA:** `374911c4be584df24e6da57af2d990570ef0f859`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **rtCamp--action-slack-notify/v2.3.3** was hardened automatically. 2 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### unpinned-uses (severity: high)

Two composite steps reference a container image by a mutable tag instead of a sha256 digest: `uses: "docker://ghcr.io/rtcamp/action-slack-notify:v2.3.3"` in the 'Slack Notification (Formatted)' step and again in the 'Slack Notification (Unformatted)' step. Pin each to ghcr.io/rtcamp/action-slack-notify@sha256:<digest>.

Locations:

- `action.yml:45`
- `action.yml:49`

### prior-fix (severity: high)

Carried forward from this version's previous harden, which fixed it; fix it again unless the code no longer has the problem. The previous harden changed action.yml without recording a finding for it, and this analysis reported nothing there. Re-apply its security changes unless the code no longer needs them. The previous patch:
```diff
diff --git a/action.yml b/action.yml
index 1dcc45b..acb24cf 100644
--- a/action.yml
+++ b/action.yml
@@ -2,52 +2,64 @@ name: 'Slack Notify'
 description: 'This action will send a notification to Slack'
 author: 'rtCamp'
 runs:
-    using: 'composite'
-    steps:
-      - name: "Slack-Markdown Message Conversion"
-        if: env.SLACKIFY_MARKDOWN == 'true' && env.SLACK_MESSAGE != ''
-        id: slackify_message
         uses: LoveToKnow/slackify-markdown-action@698a1d4d0ff1794152a93c03ee8ca5e03a310d4e #v1.1.1
-        with:
-          text: '${{ env.SLACK_MESSAGE }}'
-
-      - name: "Slack-Markdown Success Message Conversion"
-        if: env.SLACKIFY_MARKDOWN == 'true' && env.SLACK_MESSAGE_ON_SUCCESS != ''
-        id: slackify_success_message
         uses: LoveToKnow/slackify-markdown-action@698a1d4d0ff1794152a93c03ee8ca5e03a310d4e #v1.1.1
-        with:
-          text: '${{ env.SLACK_MESSAGE_ON_SUCCESS }}'
-
-      - name: "Slack-Markdown Failure Message Conversion"
-        if: env.SLACKIFY_MARKDOWN == 'true' && env.SLACK_MESSAGE_ON_FAILURE != ''
-        id: slackify_failure_message
         uses: LoveToKnow/slackify-markdown-action@698a1d4d0ff1794152a93c03ee8ca5e03a310d4e #v1.1.1
-        with:
-          text: '${{ env.SLACK_MESSAGE_ON_FAILURE }}'
-
-      - name: "Slack-Markdown Cancel Message Conversion"
-        if: env.SLACKIFY_MARKDOWN == 'true' && env.SLACK_MESSAGE_ON_CANCEL != ''
-        id: slackify_cancel_message
         uses: LoveToKnow/slackify-markdown-action@698a1d4d0ff1794152a93c03ee8ca5e03a310d4e #v1.1.1
-        with:
-          text: '${{ env.SLACK_MESSAGE_ON_CANCEL }}'
-
-      - name: "Slack Notification (Formatted)"
-        if: env.SLACKIFY_MARKDOWN == 'true'
-        env:
-          SLACK_MESSAGE: "${{ steps.slackify_message.outputs.text || env.SLACK_MESSAGE }}"
-          SLACK_MESSAGE_ON_SUCCESS: "${{ steps.slackify_success_message.outputs.text || env.SLACK_MESSAGE_ON_SUCCESS }}"
-          SLACK_MESSAGE_ON_FAILURE: "${{ steps.slackify_failure_message.outputs.text || env.SLACK_MESSAGE_ON_FAILURE }}"
-          SLACK_MESSAGE_ON_CANCEL: "${{ steps.slackify_cancel_message.outputs.text || env.SLACK_MESSAGE_ON_CANCEL }}"
-          GITHUB_RUN: "${{ github.event.repository.html_url }}/actions/runs/${{ github.run_id }}"
-          ENABLE_ESCAPES: "true"
-        uses: "docker://ghcr.io/rtcamp/action-slack-notify:v2.3.3"
-
-      - name: "Slack Notification (Unformatted)"
-        if: env.SLACKIFY_MARKDOWN != 'true'
-        uses: "docker://ghcr.io/rtcamp/action-slack-notify:v2.3.3"
-        env:
-          GITHUB_RUN: "${{ github.event.repository.html_url }}/actions/runs/${{ github.run_id }}"
+  using: 'composite'
+  steps:
+    - name: "Slack-Markdown Message Conversion"
+      if: env.SLACKIFY_MARKDOWN == 'true' && env.SLACK_MESSAGE != ''
+      id: slackify_message
+      with:
+        text: '${{ env.SLACK_MESSAGE }}'
+    - name: "Slack-Markdown Success Message Conversion"
+      if: env.SLACKIFY_MARKDOWN == 'true' && env.SLACK_MESSAGE_ON_SUCCESS != ''
+      id: slackify_success_message
+      with:
+        text: '${{ env.SLACK_MESSAGE_ON_SUCCESS }}'
+    - name: "Slack-Markdown Failure Message Conversion"
+      if: env.SLACKIFY_MARKDOWN == 'true' && env.SLACK_MESSAGE_ON_FAILURE != ''
+      id: slackify_failure_message
+      with:
+        text: '${{ env.SLACK_MESSAGE_ON_FAILURE }}'
+    - name: "Slack-Markdown Cancel Message Conversion"
+      if: env.SLACKIFY_MARKDOWN == 'true' && env.SLACK_MESSAGE_ON_CANCEL != ''
+      id: slackify_cancel_message
+      with:
+        text: '${{ env.SLACK_MESSAGE_ON_CANCEL }}'
+    - name: "Slack Notification (Formatted)"
+      if: env.SLACKIFY_MARKDOWN == 'true'
+      env:
+        SLACK_MESSAGE: "${{ steps.slackify_message.outputs.text || env.SLACK_MESSAGE }}"
+        SLACK_MESSAGE_ON_SUCCESS: "${{ steps.slackify_success_message.outputs.text || env.SLACK_MESSAGE_ON_SUCCESS }}"
+        SLACK_MESSAGE_ON_FAILURE: "${{ steps.slackify_failure_message.outputs.text || env.SLACK_MESSAGE_ON_FAILURE }}"
+        SLACK_MESSAGE_ON_CANCEL: "${{ steps.
... (truncated)
```

Locations:

- `action.yml`

## Iteration Notes

### Iteration 1

**Fixes applied:** unpinned-uses, prior-fix

**Notes:**

Pinned both `docker://ghcr.io/rtcamp/action-slack-notify:v2.3.3` references to `@sha256:acc1c430721b27030d3dacf4273eec569388ad650e127bb9f1292f33cd9cd9bd`. I got the digest from the registry and kept the `docker://` prefix and the tag in place. The LoveToKnow/slackify-markdown-action references were already pinned to a commit SHA. The visible part of the prior patch only re-indented the file, so I applied the security change (the image pin) and left the formatting alone. That diff was cut off, so I couldn't confirm the rest of it. There are no `run:` steps, so nothing here can be script-injected.

