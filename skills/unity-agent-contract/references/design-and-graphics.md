# Optional design and mobile configuration

These are explicit feature choices, not requirements for adopting compact context or Editor tooling. Preserve an established game's mechanics, visual language and justified exceptions.

## Design decisions

Bind level actions to the game's own vocabulary, legal transitions and authoring tools. Separate learning, mental difficulty, duration, level size and variety. A larger level is not automatically a better or harder one. Use the project's maintained level guidance and playtests.

Give each progression unlock, booster or recovery feature a test question. Scope the first prototype to answering those questions, rather than automatically adding a full meta-game. Treat observed timing ranges, size curves and unlock schedules as conditional priors; validate them in the target game.

For feel, identify the action and observed problem before adding effects. Prioritize responsive input and clear state changes, then coordinate motion, camera, animation, audio, particles and haptics. Keep domain availability independent of delayed presentation. Validate the interaction in the running game; use visual-quality guidance when HUD or controls change.

Separate source observations from recommendations. Keep target-specific tuning and exceptions in the game; put reusable guidance with its topic owner. If an adopter has no maintained guides, record that gap rather than inventing a claim that a source has been reviewed.

## Author's portrait mobile preset

Use only when `mobile-graphics` is selected and appropriate to the product. Explain appearance and device-support tradeoffs before applying it to an existing project. Do not change settings during an unrelated task. Match API/property names to installed Editor and URP versions.

| Area | Chosen baseline |
| --- | --- |
| Orientation | Fixed portrait; disable upside-down and both landscape orientations. |
| Startup | `QualitySettings.vSyncCount = 0`; `Application.targetFrameRate = 60` once in the DI startup entry point (`IStartable` where used), not a per-frame setter. Disable VSync in every quality tier. |
| Android pacing | Optimized frame pacing (Swappy) enabled. |
| Color and sampling | Gamma; URP render scale 0.9; HDR off; MSAA disabled (1 sample). |
| Textures | Depth texture off; opaque texture on with 2x bilinear downsampling. |
| Renderer | URP Forward; SRP Batcher on; dynamic batching off. Retain project-local renderer references. |
| Lighting | Main-light shadows, additional lights/shadows, soft shadows, reflection-probe blending/box projection, light layers, SSAO and lens flares off. |
| Android threading | Multithreaded rendering on; graphics jobs off; static/dynamic batching off. |
| Memory | Incremental GC and unused mip stripping on. |
| Graphics APIs | Android automatic graphics APIs (Vulkan/OpenGLES3). The source preset also requires ES3.1, ES3.1 AEP and ES3.2; these reduce compatibility and need an explicit recorded product decision. |
| Mobile quality | Full textures; anisotropic per-texture; LOD bias 0.7; particle raycast budget 64. |
| Desktop quality | LOD bias 2; forced anisotropic; particle raycast budget 4096. |

URP overrides corresponding built-in lighting/shadow settings. The named quality tiers in a source project are not a reason to copy another project's entire configuration.

Preserve application IDs, signing, icons, versions, SDK requirements, scene lists, shader inclusion, pipeline GUIDs and gameplay assets. Inspect and edit the target project's own settings and renderer assets. Verify imported/live settings through its task-owned Editor and check portrait gameplay after color-space/pipeline changes.

This preset is a starting configuration, not a measured optimization or a 60 FPS guarantee. Performance investigations need a reproducible workload, frame-time/memory/GC measurements and target-device observations where relevant. Rendering correctness in the Editor does not prove sustained mobile performance. Player builds still require a user build request.
