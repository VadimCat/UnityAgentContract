# Feature selection

Read this catalog during initial adoption. Ask about capabilities, rather than making the user choose package names they do not understand. Use their conversation language.

## Suggested selections

**Start small:** `compact-context`, `unity-cli`, `validation-cadence`. This helps an agent ask Unity precise questions and verify changes without a large infrastructure migration.

**Daily development:** the starting selection plus `roslyn`, `task-isolation`, `autonomous-delivery` and `knowledge-ownership`. Useful when the agent implements C# features and should own its environment and Git handoff.

**Full workflow:** offer every feature for discussion. Explain the graphics preset and design conventions as product choices. Full documentation access does not mean every tool or project setting should be installed.

Existing project rules still apply to any selection. For example, an existing worktree requirement is not disabled by choosing a smaller preset.

## Feature IDs and routing

| ID | Explain to the user | Cost / prerequisite | Read after selection |
| --- | --- | --- | --- |
| `compact-context` | Narrow queries and concise summaries keep irrelevant text out of the agent's context. | Requires complete failure reporting and retrieval of omitted detail when necessary. | [contract.md](contract.md) |
| `unity-cli` | Ask the live Editor about scenes, components, assets, compilation and Console state. | Compatible CLI, exact project Editor, Pipeline package and verified session. | [tooling.md](tooling.md) |
| `roslyn` | Navigate C# by symbols rather than scanning entire folders. | Task-local backend; full references need real project assemblies and defines. | [tooling.md](tooling.md) |
| `task-isolation` | Separate branch/worktree, Editor, Library/Temp, ports and services protect concurrent work. | Disk, import and process overhead; setup script is preferable. | [contract.md](contract.md), [delivery.md](delivery.md) |
| `validation-cadence` | Compile and check a coherent behavior change, rather than every saved file. | Focused checks and terminal completion signals. | [validation.md](validation.md) |
| `gameplay-validation` | Prove input, outcomes, retry, progress and restoration in a running game. | Test scenarios, running frames and isolated save data. | [validation.md](validation.md) |
| `visual-quality` | Review actual UI renders and touch behavior at the supported sizes and insets. | Capture/view tools and iteration; optional art sources stay separate. | [validation.md](validation.md) |
| `showroom` | Demonstrate an exact commit through one dedicated disposable worktree and launcher. | Explicitly disposable location; script verifies ownership before cleaning. | [validation.md](validation.md) |
| `async-lifecycle` | Prevent work from outliving its screen/scene and stale results from overwriting new state. | Integrate the established async stack; no automatic framework migration. | [engineering.md](engineering.md) |
| `shared-modules` | Reuse a maintained package and keep game-specific adapters in the game. | Discoverable catalog, source ownership, access and dependency pins. | [engineering.md](engineering.md), [delivery.md](delivery.md) |
| `knowledge-ownership` | Read a small current map and update the owner instead of copying handbooks everywhere. | Maintained topic owners and a concise project profile. | [engineering.md](engineering.md) |
| `final-build` | Produce the requested build only after final changes and relevant checks. | Explicit build request and the configured build service, if present. | [delivery.md](delivery.md) |
| `mobile-graphics` | Start from a concrete portrait, 60 FPS and URP configuration. | Changes appearance/device support; measure in the target game. | [design-and-graphics.md](design-and-graphics.md) |
| `game-design` | Use the game's legal actions and test questions for levels, progression and feel. | Project vocabulary, authoring tools and actual playtests. | [design-and-graphics.md](design-and-graphics.md) |
| `autonomous-delivery` | Let the agent bootstrap, check, commit, prepare review and clean its resources. | Sufficient access and known boundaries; respect enforced restrictions. | [delivery.md](delivery.md) |

## A useful first conversation

Briefly explain the loop, then ask one bundled selection question. For example:

> The agent can query the Editor and C# symbols directly, keep the answers small, then validate a finished behavior change. I suggest starting with compact context, Unity CLI and checks at behavior boundaries. Would you like that starting set, daily development with Roslyn and isolated workspaces, or a custom selection? Gameplay checks, visual review, Showroom demos, async ownership, shared modules, design guidance, final builds and the mobile preset are additional options; I can explain the ones you need.

Adapt this to the user's experience. For an experienced user, offer IDs. For a beginner, explain Editor access, isolated development and verification in ordinary language. Explain any newly considered feature's benefit and cost before adopting it; do not make a giant questionnaire mandatory.

Before applying the selection, identify the project, its actual remote default branch, existing instructions and working infrastructure. Only ask for facts that cannot be discovered. Record the decision once; subsequent tasks use it until the user changes it.

When no answer has arrived, continue useful read-only inspection and explain the recommendation. Do not treat silence as a feature choice. When a user already says "use the daily development set", proceed without another selection question.

Record each feature as selected and verified, selected but blocked, or omitted. Report an unavailable backend separately from a configured profile. A host without native skill support can follow the same Markdown entry point manually.
