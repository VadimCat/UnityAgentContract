# Unity agent profile

Template: replace example values with discovered project facts after feature selection. Omit unselected details; do not copy every reference into this file.

## Selection

- Contract source: repository URL and adopted commit/tag.
- Selected features: user-confirmed IDs from the feature catalog.
- Selected and verified: IDs plus the actual capability check.
- Selected but blocked: ID, exact prerequisite/restriction and next action.
- Omitted: relevant alternatives intentionally left out.
- Documentation: English. Conversation: the user's language.

## Project facts

- Canonical repository/root and actual remote default branch.
- Task workspace root and create/start/status/test/stop commands.
- Unity version from `ProjectSettings/ProjectVersion.txt`.
- CLI path/version, Pipeline version and discovery command, if selected.
- Editor ownership verification: project path, PID and endpoint source.
- Semantic backend and supported operations, if selected; actual reference/define loading and limitations.
- Test entry points and safe test-progress location.
- Ignored paths for logs, captures and runtime metadata.

## Conditional owners

- Knowledge map and relevant engineering/design/UI guides.
- Shared-module catalog and maintained source locations, if selected.
- Existing async and DI stack, if relevant; no automatic migration.
- Showroom script, registered disposable path and exact-revision argument, if selected.
- Build interface and final-artifact checks, if selected; explicit build request required.
- Mobile preset decision/exceptions and device-support tradeoffs, if selected.

## Validation and handoff

Record relevant compile/test/runtime/visual checks, completion signals and current blockers. Include task cleanup ownership and repository review/merge policy. Keep commands concrete and short; link maintained procedures for detail.
