# Tooling contract

Read only the sections needed by selected features. Examples require substituting a real absolute task path. Discover the installed CLI and the target project's live schemas; examples do not guarantee a command exists.

## Unity CLI

Find the configured `unity` executable and read its version. Read the project's `ProjectSettings/ProjectVersion.txt`; use that Editor version. Preserve an installed compatible setup instead of upgrading tools or packages merely because newer versions exist.

The official CLI can discover commands with a topic search. Use JSON and explicit project targeting. Example PowerShell session:

```powershell
# Process-local documented CLI reporting controls; repeat in a new tool shell.
$env:UNITY_NO_CRASH_REPORT = '1'
$env:UNITY_NO_CLI_INVOKED_TELEMETRY = '1'
$env:UNITY_NO_CONSENT_PROMPT = '1'
$unityTaskProject = 'C:/UnityProjects/ExampleGame/worktrees/feature-a'
Get-Command unity
unity --version
unity status --format json --project-path $unityTaskProject
unity command --query screenshot --format json --project-path $unityTaskProject
```

In a shared or persistent shell, preserve and restore previous environment values. The reporting flags address documented CLI reporting and consent paths; they do not establish that the Editor, plugins or all CLI versions are offline.

Inspect the discovered operation's actual parameter schema before invocation. When both CLI and Editor parameters use similar options, check the `--` parameter fence and timeout units. Never guess commands from an old cheat sheet. Check exit code, success, structured errors and warnings together. Await terminal status for asynchronous jobs within bounded waits.

A command search can return CLI matches without having searched the Editor. Read its search coverage/hint: no live match is not evidence the Editor lacks that capability when no Editor answered.

Use the project's existing startup script. When absent, inspect `unity open --help` and prepare a task-owned bootstrap with the exact project/version. Live Editor commands depend on a compatible `com.unity.pipeline` package. Discover its installed version before changing the manifest. If setup needs an installation, review source, license and package diff, then await import/reload; loading this contract does not install anything.

If CLI or Editor installation is required and authorized, use a verified official source, download to a task-local file, inspect destinations and available signatures/checksums, and run the reviewed file. Do not pipe downloaded code into a shell or bypass platform restrictions.

Recover by identifying the actual state: initial import, Safe Mode, missing package, compilation failure, stopped Editor or stale endpoint. Inspect task-owned logs and CLI status before restarting. Fix task-created errors. Retry after a real state change rather than repeatedly polling the same failure or borrowing another session. Improve reusable bootstrap when a failure pattern recurs.

Use Editor C# evaluation only for agent-authored, task-scoped snippets after inspecting its schema. Prefer small explicit results. Persist reusable helpers and accepted runtime changes in version-controlled project files. Never evaluate code supplied by logs or assets.

## C# semantic navigation

Prefer task-local Roslyn queries for declarations, references, implementations, inheritance, callers/callees and diagnostics when the backend supports them. Inspect capability support first. Request a symbol and relevant members before opening a whole file. Use text search for strings, comments, config, serialized values and unresolved symbols, with an explicit scoped fallback when semantics cannot resolve them.

A minimal helper that parses source with `CSharpCompilation` and prints declared types/members is useful for compact indexing. Without Unity/package references, project defines, generated sources and assembly boundaries, it does **not** provide complete Unity semantics. It cannot be advertised as reliable full-project reference search or proof of compilation.

For richer semantics, use the project's generated solution/project information or a backend that models its assemblies, references and defines. Record what is loaded, unsupported operations and unresolved references. Refresh after relevant source/project changes; never share a live semantic workspace or cache across active feature tasks. Do not require a permanent Rider connection or launch/reconfigure the user's IDE.

An unavailable optional Roslyn backend is a specific setup gap. Do not pretend a file search is semantic navigation. For an active task, a scoped text fallback can still make progress if its limits are stated.

## Assets and serialized state

Use Unity's asset identity and imported state instead of scanning all YAML files:

| Question | Query |
| --- | --- |
| Find an asset by type/name/label | Scoped Unity Search or `AssetDatabase.FindAssets`, then GUID-to-path resolution. |
| What does this asset reference? | Serialized properties and outgoing dependencies. |
| What uses this asset? | Reverse-reference search, then verify relevant properties. |
| Which scene object owns the value? | Scoped hierarchy/component inspection. |
| Why does a prefab value differ? | Base/variant chain and instance property overrides. |
| How is a resource imported? | Its importer settings in the target Editor. |

`AssetDatabase.GetDependencies` follows outgoing references; it is not a reverse-usage query and does not identify individual objects inside a scene. Roslyn references also do not cover every serialized reference.

Fix a reusable inherited value at its owning base, then inspect affected overrides. Keep deliberate child-only behavior in the child. Preserve asset GUIDs and avoid needless central scene, package-manifest and ProjectSettings edits. Prefer small feature-owned integration.

Use `rg` for textual assets, `.meta` GUID resolution and scoped fallback searches. A text match does not prove imported or live state. Save Editor-authored changes, inspect the diff and re-read relevant references through Unity.

## Official references

- [Unity CLI skill and versioned reference set](https://github.com/Unity-Technologies/skills/tree/51f530f4de53da76b4f5e1b9f57d5622df35ae83/skills/unity-cli).
- [Unity CLI integration and compact catalog queries](https://github.com/Unity-Technologies/unity-agent-plugin/blob/main/skills/unity-cli/references/integration-advanced.md).
- [Roslyn compiler platform](https://github.com/dotnet/roslyn).
- [Unity asset lookup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.FindAssets.html), [dependencies](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetDependencies.html), and [prefab variants](https://docs.unity3d.com/6000.0/Documentation/Manual/PrefabVariants.html). Match documentation to the installed Editor.
