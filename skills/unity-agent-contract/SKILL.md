---
name: unity-agent-contract
description: Help a user adopt a compact Unity agent workflow by explaining and selecting Editor tooling, semantic navigation, isolation, validation and delivery features. Use for workflow setup or adaptation, rather than unrelated Unity gameplay implementation.
---

# Unity Agent Contract

Help the user choose and adopt the parts of this workflow that solve their problem. This is an instruction package; it does not install or start any tool by being read.

## First adoption

1. Read [features.md](references/features.md). Explain the narrow-query, compact-result, coherent-change, focused-verification loop in the user's language.
2. Inspect the available project's instructions, existing bootstrap, actual tools and versions with read-only actions. If no project is available, discuss the feature selection first; ask for the project location before project configuration.
3. Ask which features are needed. Offer the recommended starting selection, explain what each relevant option does and its setup or runtime cost, and allow a custom selection. If the user already made the choice, use it. Do not silently adopt everything or assume a recommendation was accepted.
4. After selection, read [contract.md](references/contract.md) and only the references mapped to those features. Preserve existing project rules and authorization; resolve actual conflicts explicitly. Do not import the author's machine paths, private services or game-specific defaults.
5. In an isolated task workspace, create or update a short project-owned profile with selected feature IDs, concrete paths/versions/commands, validation requirements and unavailable prerequisites. Add a small pointer to existing project instructions. Do not overwrite unrelated instructions or install global agent configuration without authorization.
6. Configure selected capabilities within the task's scope. Verify each enabled capability with its actual tool and record unresolved limitations. A profile or a skill file alone is not an implemented integration. Continue authorized routine work autonomously.

Do not launch Unity or semantic services for a documentation-only adoption. Do not build a Player, publish, message others or sign up for services merely because the contract describes those actions. Existing explicit authorization remains valid; ask only for missing choices or enforced restrictions.

## After adoption

Use the saved selection for follow-ups; do not repeat the questionnaire each task. Start with the small project profile and consult detail only when relevant. Before code or serialized-state changes, verify task environment ownership. Keep large outputs on disk, preserve failure information and report exact validation gaps.

| Need | Read when selected or required by the active task |
| --- | --- |
| Context, ownership and evidence | [contract.md](references/contract.md) |
| Editor, Roslyn, assets and recovery | [tooling.md](references/tooling.md) |
| Async, modules and knowledge ownership | [engineering.md](references/engineering.md) |
| Check cadence, gameplay, visuals and Showroom | [validation.md](references/validation.md) |
| Levels, progression, feel or optional mobile preset | [design-and-graphics.md](references/design-and-graphics.md) |
| Autonomous setup, Git, builds and cleanup | [delivery.md](references/delivery.md) |

Do not turn this reference set into mandatory context for every Unity question. The selected project profile and the current task determine what to load.
