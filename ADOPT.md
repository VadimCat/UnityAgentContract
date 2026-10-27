# Adopt the Unity Agent Contract

Instructions for an AI agent helping a user adopt this workflow. Read the [skill entry point](skills/unity-agent-contract/SKILL.md) and the [feature catalog](skills/unity-agent-contract/references/features.md), then follow the onboarding procedure. Do not read every reference before knowing what is relevant.

Your first useful response should explain the context-saving loop and ask which capabilities the user needs. Offer the recommended starting selection and briefly explain the additional options and their costs. Use the user's conversation language. Write resulting documentation in English.

Inspect existing project instructions, tools and versions with read-only actions when a project is available. Reuse existing working infrastructure. If the user has already specified the selection, do not ask the same question again. An unavailable optional feature should be marked unavailable with its exact prerequisite, rather than silently treated as installed.

After selection, create a small project-owned profile and scoped instruction pointer, following the [profile template](examples/UNITY_AGENT_PROFILE.template.md) and [instructions template](examples/AGENTS.template.md). Reconcile existing instructions instead of replacing them. Configure only selected capabilities within the user's task and permissions, in an isolated workspace. Read the matching references and verify the capabilities actually enabled.

Adopting instructions does not authorize an unrelated game refactor, a Player build, publishing, external messages, new legal commitments, or replacing another agent's setup. Continue routine authorized setup without repeated permission requests. Ask only for a real missing choice or an enforced restriction.
