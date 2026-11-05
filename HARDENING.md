<!-- markdownlint-disable -->

# Hardening Report: rtCamp--action-slack-notify/v2.4.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `374911c4be584df24e6da57af2d990570ef0f859`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **rtCamp--action-slack-notify/v2.4.0** was hardened automatically. 1 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### prior-fix (severity: high)

Carried forward from this version's previous harden, which fixed it; fix it again unless the code no longer has the problem. The previous harden changed action.yml without recording a finding for it, and this analysis reported nothing there. Re-apply its security changes unless the code no longer needs them. The previous patch:
```diff
diff --git a/action.yml b/action.yml
index 664d271..a4ac2b8 100644
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
-        uses: "docker://ghcr.io/rtcamp/action-slack-notify@sha256:17fac87b8ea4ffec1f90b8557f88e8fd69ec8568f690f4ea24d5a408eeee419a" # v2.4.0
-
-      - name: "Slack Notification (Unformatted)"
-        if: env.SLACKIFY_MARKDOWN != 'true'
-        uses: "docker://ghcr.io/rtcamp/action-slack-notify@sha256:17fac87b8ea4ffec1f90b8557f88e8fd69ec8568f690f4ea24d5a408eeee419a" # v2.4.0
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
+        SLACK_ME
... (truncated)
```

Locations:

- `action.yml`

## Iteration Notes

### Iteration 1

**Fixes applied:** prior-fix

**Notes:**

I re-applied the earlier harden to action.yml as far as I could see it. The patch I was given was cut off, so I couldn't tell whether it also changed the two Docker notification steps at the end, where its line count grew from 52 to 64. What I could see only re-indented runs/steps to 2 spaces. I applied that and normalised the '# v1.1.1' comments; nothing else changed.

action.yml has no real security problem left. The LoveToKnow/slackify-markdown-action steps are pinned to a full commit SHA (698a1d4..., v1.1.1). The Docker steps are pinned to the image digest sha256:17fac87b..., which upstream already used. The file has no run: steps, so there is nowhere for shell injection.

One thing doesn't match: looking up the v2.4.0 tag today gives a different digest, sha256:5da2cab1.... The pinned 17fac87b... might be a single-platform image under that tag, or the tag might have been pushed again since. I kept upstream's digest, and I didn't put the tag inline because a tag next to a digest it may not match would be misleading.

