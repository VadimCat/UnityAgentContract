# Third-party references

This repository contains an original portable description of VadimCat's Unity agent workflow. It does not redistribute third-party skill files, executables, Unity packages or Roslyn libraries. Its MIT license applies to the original repository material.

Unity CLI command patterns and Pipeline concepts were checked against [Unity Technologies' official Unity CLI skill](https://github.com/Unity-Technologies/skills/tree/51f530f4de53da76b4f5e1b9f57d5622df35ae83/skills/unity-cli) at revision `51f530f4de53da76b4f5e1b9f57d5622df35ae83`, the [official integration reference](https://github.com/Unity-Technologies/unity-agent-plugin/blob/main/skills/unity-cli/references/integration-advanced.md), and locally available CLI help. These links are references, not bundled dependencies. Unity's software and upstream materials retain their respective licenses and trademarks. This repository is not an official Unity product.

Roslyn is Microsoft's .NET compiler platform. Use its [official repository](https://github.com/dotnet/roslyn) and the licenses of any separately installed packages. The workflow does not ship a semantic backend or promise that a lightweight declaration index provides full project semantics.

The graphics preset records the author's selected project configuration, not a Unity performance guarantee. Verify setting names and behavior for the target Editor and render-pipeline versions.
