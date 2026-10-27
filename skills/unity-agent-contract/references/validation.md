# Validation, visuals and demonstrations

## Check coherent changes

An interface, implementation, callers and DI wiring are one change when they must evolve together. Batch related edits that are incomplete in isolation, then compile, inspect Console errors and run the focused check. Fix task-created errors before moving to unrelated behavior. Do not accumulate several unrelated systems into one unchecked final batch.

Calibrate check cadence using measured overhead and failure-feedback time. One grouped check can reduce compile/reload overhead; this alone does not measure fault-localization cost or prove a universal optimal batch size. Retain early checks for independent or risky behavior and integration/PlayMode checks at stable feature boundaries.

Before handoff, run relevant available checks: C# compilation, no new relevant Unity errors, applicable EditMode tests and relevant PlayMode/integration tests. Broaden for shared/core changes or an unresolved concern. Distinguish pre-existing blockers from task-created errors. Do not repeat unchanged broad suites merely to accumulate results.

Use Editor tests where appropriate. Some test modes build a Player or require closing an Editor; inspect the selected mode first and preserve explicit-build and session-ownership rules. A compilation check is not a Player build.

Documentation-only work needs document checks, not Unity startup. A relevant unavailable runtime check remains a reported gap rather than an invented pass.

## Prove a playable flow

Start the task-owned Editor and verify its project/PID/endpoint. Enter PlayMode, wait for reload/reconnection, then prove frames advance. A paused frame-step proves only the stepped behavior. Artificial auto-tick cadence does not establish device performance.

Exercise actual supported input and legal state transitions: onboarding where affected, core action, outcome, retry, progress and restoration. Include repeated/interrupted input and lifecycle boundaries relevant to the change. Use isolated save/progress data, never the user's real progress for automated tests.

Inspect Console errors and runtime state. A screenshot can capture a frozen frame; successful capture and successful gameplay are different claims. Persist accepted runtime tuning in project files and validate the persisted revision.

Temporary Editor/background settings need their original values recorded and restored. Do not change shipping PlayerSettings merely to keep a validation session ticking. Stop only task-owned sessions.

## Visual quality and interaction

Inspect the current game and supplied references before editing its interface. Preserve its visual language for local changes. For new UI, choose a coherent small set of typography, color, spacing, shapes, icons and states. Working buttons and compilation do not establish visual acceptance.

For substantial multi-screen work, finish one representative screen inside the engine before extending its components. Use real copy and native interactive labels/controls; a generated mockup does not prove the implementation.

Open actual captures from the current running revision. Check hierarchy, composition, proportions, contrast, edges and consistency. Correct defects and recapture the affected states. Test supported viewports, safe areas, busy/bright gameplay backgrounds, camera boundaries and actual touch behavior. Keep controls clear of the subject and contact point; update tutorials/copy when control behavior changes.

Capture source matters: a composited screen capture may include Screen Space Overlay UI; an offscreen camera capture often omits it. Locked desktops can yield invalid captures. Try an available alternative and report exactly what could not be inspected. Source inspection, component values and pixel statistics do not substitute for viewing the image.

Tie evidence to revision, scene/state, resolution, insets and capture source. Never reuse an old screenshot as proof of a newer revision. Use the project's maintained visual guidance and relevant references; do not copy another game's art direction as a universal rule.

## Showroom

When selected, maintain one dedicated demonstration-only Showroom worktree and a standard launcher. A user request to show/open/update it should run that script directly. Avoid narrating routine successful preparation; keep acknowledgement minimal.

The script must verify the registered absolute Showroom path, verify it is a dedicated Git worktree, reject canonical/feature paths, clean its tracked and untracked changes, check out the exact requested branch/commit and open that project. Validate resolved paths before recursive cleanup. Never use a name substring such as "showroom" as sufficient deletion authorization. Keep useful implementation work elsewhere.

Repair missing/broken reusable tooling within an authorized Showroom task instead of repeatedly improvising manual cleanup. If the disposable designation cannot be established, resolve that blocker before deleting anything. Do not add unrequested builds or gameplay changes to a demonstration.

Ordinary implementation validation stays in the task workspace; Showroom is for presenting the chosen revision to the user.
