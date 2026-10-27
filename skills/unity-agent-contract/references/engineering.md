# Engineering and knowledge ownership

Adopt only the selected capabilities and applicable existing project conventions. This reference does not authorize migrating an unrelated system.

## Domain and presentation

Authoritative domain state changes when its domain prerequisites are satisfied. Animation progress must not decide logical availability or reverse a committed transition. Network authorization, simulation and deliberate turn rules can still be real prerequisites; represent those pending states explicitly.

Give stateful services explicit lifetimes. Persistent player state belongs to its persistent owner; a scene consumes it rather than inventing a second copy. Distinguish independent facts with separate predicates. Restore authoritative state before presenting it; reconcile missing/stale objects without replaying unrelated effects.

Prefer small contracts and direct implementations. Establish an interface, event or DTO boundary before multiple independent features need it. Use the project's established DI and presentation architecture. When adopting the author's DI convention, one-time application settings belong in a registered `IStartable`, and project-owned per-frame work in a registered `ITickable`; record the actual DI framework rather than assuming these interfaces exist in every project.

Validate required dependencies at authoring/setup boundaries. Do not hide a broken required serialized reference or DI registration behind a silent return. Handle absence where it is valid: optional content, empty collections, external responses, imported data or old saves.

## Async lifecycle

Preserve an established async stack unless migration is requested. For a new first-party Unity async stack, the author's preference is UniTask. Keep third-party Task/coroutine APIs at their boundary and adapt them; do not rewrite vendor code. Avoid mixing unrelated async styles throughout one feature.

Every operation needs an owner, cancellation lifetime, exception handling, Unity main-thread access and resource disposal. Repeated requests need an explicit concurrency policy: reject, join, queue or supersede as the domain requires. Prevent a canceled or older result from overwriting the current request, and prevent callbacks from accessing destroyed views.

Await real completion signals rather than guessed delays. Independent operations can run concurrently; state transitions and visible sequencing retain their required order. Test interrupted/repeated requests and teardown where the change affects them.

## Shared modules

Before implementing a capability, inspect the user's actual shared-module catalog and maintained sources. A catalog can point to code in several repositories; an empty catalog project folder does not prove no implementation exists. Never invent a repository URL from a display name.

Prefer the ready maintained implementation over a local duplicate. Keep game rules, content, tuning, configuration and adapters in the consumer. Read the module's API and installation contract, preserve licenses/provenance and pin the dependency.

General improvements with a plausible second consumer belong in the shared owner as well. Use an isolated module task branch/worktree, preserve public contracts/GUIDs, validate the module and consumer integration, and update the consumer pin deliberately. Do not turn every local helper into a universal package.

For a new private module used by a project, inspect collaborators, teams and inherited access. Apply equivalent access, preferably through existing teams, without broader privileges. Verify access and report pending invitations or blocked grants with the remaining action. Do not assume a successful repository creation gives every consumer access.

## Knowledge and instruction ownership

Keep a small knowledge map pointing to maintained owners: global execution rules, engineering topics, module catalog, design, interface references and build delivery. Read the owning project's instructions before changes, then only the relevant topic. A neighboring folder is not an inherited instruction source.

Keep game mechanics, schemas, tuning, local commands and justified exceptions in their project. Keep module APIs, notices and version pins with their module. Change a cross-project rule at its global owner first, then reconcile affected child guidance; do not copy the entire baseline into each game.

Update current guidance directly and concisely. Preserve important user corrections, required provenance and dependency contracts. Do not add chat inventories, evidence appendices or historical validation logs by default. Link the actual evidence when needed for the task; keep temporary logs outside maintained knowledge.

Documentation is in English; conversation follows the user's language. Preserve real identifiers, paths and numerical data when translating an existing document. Public editions should deliberately replace private setup values with documented parameters rather than exposing their original contents.
