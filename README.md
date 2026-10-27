# Unity Agent Contract

A practical contract for working with Unity through an AI agent while keeping its context small. Created by [VadimCat](https://github.com/VadimCat).

**Give your agent [ADOPT.md](ADOPT.md). It explains the available features, asks which ones you want, and adapts only those to your project.** You can also give it this prompt:

> Read ADOPT.md in this repository. Explain how the workflow saves context, then ask which features I need and what each would do for my project. Inspect my existing setup before recommending changes. Do not install everything by default. Speak my language; write project documentation in English.

The central idea is to ask a tool a narrow question, receive a small structured answer, make one coherent change, and verify it in the right environment. Keep large logs and captures on disk; bring relevant facts into the conversation. Load detailed instructions only when their subject matters.

## What you can adopt

| Feature | Why use it? | Cost or prerequisite |
| --- | --- | --- |
| Compact context | Query symbols, assets and command schemas instead of dumping repositories and logs. | Requires deliberate query scope; smaller output must retain failures. |
| Unity CLI | Inspect and control the actual Editor, including serialized state and diagnostics. | Compatible CLI, Editor and project Pipeline package; discover versions first. |
| Roslyn navigation | Find C# declarations and, with a suitable backend, references and implementations. | Task-local tooling with the appropriate project/assembly context. |
| Task isolation | Keep task branches, Editors, caches and ports independent. | More disk space and initial import time. |
| Validation cadence | Catch errors at complete behavior boundaries without recompiling after every file save. | Focused tests and a way to await compilation completion. |
| Gameplay validation | Exercise input, outcomes, retry and restoration in a running game. | Reproducible scenarios and isolated test progress. |
| Visual quality | Inspect real renders and interaction at the supported screen sizes. | Captures, image viewing and iteration time. |
| Showroom | Open an exact revision for a demonstration in a disposable worktree. | Dedicated script; its local contents are intentionally discarded. |
| Async lifecycle | Own cancellation, stale results, exceptions and resources. | Integrates with the project's existing async stack. |
| Shared modules | Reuse maintained capabilities instead of inventing local duplicates. | A discoverable module catalog, explicit ownership and dependency pins. |
| Knowledge ownership | Keep stable rules at their owner and game facts in the game. | Small maintained documentation and conditional references. |
| Final build delivery | Build only on request, after all changes and relevant checks. | Project build service where configured. |
| Mobile graphics preset | Adopt a specific portrait/60 FPS/URP starting point deliberately. | Product and device tradeoffs; verify in the target game. |
| Game design | Tie levels, progression and feedback to explicit hypotheses. | The game's own vocabulary, authoring tools and playtests. |
| Autonomous delivery | Let the agent own setup, checks, Git handoff and cleanup. | Defined scope, access and repository review policy. |

The [feature catalog](skills/unity-agent-contract/references/features.md) contains stable feature IDs, suggested starting selections and the onboarding procedure. The complete contract is available even when you adopt only a subset.

## Where to start

- [ADOPT.md](ADOPT.md): entry point to give another agent.
- [Portable skill](skills/unity-agent-contract/SKILL.md): onboarding and progressive loading. Its folder is self-contained; copy it to your agent's supported skill directory if desired. No installer or global configuration change is required to read it.
- [Core contract](skills/unity-agent-contract/references/contract.md): context budget, ownership, verification and handoff.
- [Tooling](skills/unity-agent-contract/references/tooling.md): Unity CLI discovery, Roslyn limits, asset identity and recovery.
- [Engineering](skills/unity-agent-contract/references/engineering.md): domain state, async, module reuse and instruction ownership.
- [Validation and presentation](skills/unity-agent-contract/references/validation.md): behavior checks, visual evidence and Showroom.
- [Design and mobile configuration](skills/unity-agent-contract/references/design-and-graphics.md): explicitly optional product choices.
- [Delivery](skills/unity-agent-contract/references/delivery.md): Git, build, access and task cleanup.
- [Project profile template](examples/UNITY_AGENT_PROFILE.template.md): record selected features, actual tools and limitations.
- [Project instructions template](examples/AGENTS.template.md): a small pointer to the selected project profile.

## Scope and evidence

This repository publishes a workflow and adoption skill, not a Unity CLI binary, Roslyn server, Unity package, workspace manager or build bot. Its examples are command shapes, not a claim that your installation exposes those commands. It has no automatic installation, telemetry or tool execution. Tools you separately choose have their own behavior and terms.

The workflow aims to reduce unnecessary context. **There is no measured universal token saving or speedup claim.** Compare equivalent completed tasks and their validation, rather than comparing a checked task with an unchecked one. The CLI patterns were checked against a local `unity` 1.0.0-beta.14 installation on 2026-10-27; live Editor commands must still be discovered for each project.

For broader Unity and design guidance, see the companion [UnityGameDesignKnowledge](https://github.com/VadimCat/UnityGameDesignKnowledge) repository. Read only the relevant topic; do not import an entire handbook into every task.

## Maintenance

Documentation is in English. Preserve existing project contracts and license notices. Run `python scripts/validate.py` before submitting a change. This checks local Markdown links, the portable skill entry point and accidental machine-specific references; it does not validate Unity execution or the behavior of an adopting agent.

Original material is available under the [MIT license](LICENSE). Unity tooling is owned and licensed separately; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
