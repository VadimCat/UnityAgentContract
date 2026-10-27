# Autonomous delivery

## Prepare an isolated task

Read existing instructions, current knowledge and bootstrap commands. Locate the canonical repository and actual remote default branch. Fetch the current default when a remote exists and create a dedicated task branch/worktree. For a new repository, the author's default is `master`; preserve an existing repository's configured default unless a rename is requested.

Use the user's configured project/worktree root. Do not import the author's workstation location into an adopter's machine. Continue a task's branch for follow-ups rather than losing its context. Keep one independent feature per task workspace; do not edit the canonical checkout or use Showroom for implementation.

Set up required tools autonomously within scope and available access. Prefer existing create/start/test/destroy scripts. Each Unity task owns its Editor, Library/Temp, logs, ports and on-demand semantic state. Do not wait for another task's Editor to become available or restart its services. Work against explicit contracts when unfinished features have a genuine dependency.

Documentation and Git-only work do not need an Editor or semantic server. Keep background startup unobtrusive. Never launch, configure or close a user-owned interactive IDE as automatic bootstrap.

If a recurring environment failure needs manual recovery twice, improve reusable tooling instead of repeating the workaround. Record task-owned runtime metadata outside version control; important feature state belongs in committed files.

## Reviewable handoff

Keep scope small; isolate any necessary supporting refactor. Before completion:

1. Run the relevant compilation, tests, serialized-state/gameplay/visual checks for the change. Report exact gaps and distinguish existing blockers.
2. Inspect the diff and remove accidental generated, machine-specific or unrelated changes. Exclude credentials, Library/Temp/Logs, runtime metadata and IDE state.
3. Fetch again and inspect material changes on the remote default. Integrate according to repository policy and rerun affected checks if needed. Never overwrite newer canonical work.
4. Commit intentional changes, push the task branch when access exists, and create/update an appropriate PR. Keep the title/description about the final behavior, relevant validation and limitations.
5. Follow repository merge policy. A reviewable pushed branch is a durable handoff; do not treat every task as permission to bypass review and merge it.

Report the result, revision/PR, relevant checks and material remaining limitations. Do not call generated but uncompiled/unverified Unity code complete.

## Final build delivery

Build only when the user explicitly requests a build. That request authorizes invoking the project's configured build bot for that task; do not ask again for the same action. Compile/test checks that do not build a Player remain normal validation.

Treat the build as the final artifact: finish every requested change, including additions received during the task, then complete relevant checks and diff review before starting/queuing it. Use the configured build service and exact published revision. Do not substitute local builds or manual uploads when the project's workflow requires its bot.

Follow the build to terminal completion and verify the delivered artifact includes the final changes and requested format. Queue acceptance is not delivery. If failure or later changes require a retry, finish remaining fixes/checks before retrying and deliver the final revision's artifact.

Preserve application identity, signing, versions and SDK requirements unless the task changes them explicitly. Keep credentials in established credential tooling, not command arguments, output or Git. Do not infer permission to publish a store release or message a third party from a request for a build.

## Cleanup and restrictions

After durable commit/push and when no further local verification is needed, stop only verified task-owned processes and release its temporary resources. Check resolved absolute targets before recursive deletion/moving. On Windows, use one shell end-to-end and literal-path filesystem operations; do not feed enumerated paths to another shell for deletion.

Remove a disposable task worktree when appropriate; retain it if local review artifacts are still needed or work is not safely preserved. Never terminate another workspace's Editor, semantic service, build worker or IDE.

When access, pending invitations, OS/provider restrictions or missing tools block progress, identify the exact restriction, affected capability/participants and remaining action. Do useful independent work meanwhile. Do not bypass enforced restrictions or represent a blocked check as passed.
