"""Validate portable documentation without launching Unity or accessing a network."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    required = (
        "README.md", "ADOPT.md", "LICENSE", "THIRD_PARTY_NOTICES.md",
        "skills/unity-agent-contract/SKILL.md",
        "skills/unity-agent-contract/references/features.md",
    )
    for relative in required:
        if not (root / relative).is_file():
            errors.append(f"Missing required file: {relative}")

    private_path = re.compile(r"[CD]:[/\\](?:Codex|Users)[/\\]", re.IGNORECASE)
    private_catalog = re.compile(r"https://chatgpt\.com/space/page_[a-z0-9]+", re.IGNORECASE)
    markdown_link = re.compile(r"!?\[[^\]\n]*\]\(([^)\n]+)\)")
    files = [p for p in root.rglob("*") if p.is_file()
             and p.suffix in {".md", ".yaml"}
             and not set(p.relative_to(root).parts).intersection(
                 {".git", "worktrees", "work", ".cache", ".venv"})]
    for path in files:
        relative = path.relative_to(root).as_posix()
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeError as exc:
            errors.append(f"{relative}: invalid UTF-8: {exc}")
            continue
        if content.startswith("\ufeff"):
            errors.append(f"{relative}: unexpected byte-order mark")
        if private_path.search(content) or private_catalog.search(content):
            errors.append(f"{relative}: machine-specific path or private catalog URL")
        if path.suffix != ".md":
            continue
        # Ignore illustrative links inside fenced code blocks.
        prose = re.sub(r"^```[^\n]*\n.*?^```[^\n]*$", "", content,
                       flags=re.MULTILINE | re.DOTALL)
        for match in markdown_link.finditer(prose):
            target = match.group(1).strip()
            if target.startswith("<"):
                target = target[1:target.find(">")]
            else:
                target = target.split(' "', 1)[0]
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            linked = (path.parent / unquote(parsed.path)).resolve()
            if not linked.is_relative_to(root):
                errors.append(f"{relative}: link escapes repository: {target}")
            elif not linked.exists():
                errors.append(f"{relative}: missing local link: {target}")

    skill = root / "skills/unity-agent-contract/SKILL.md"
    if skill.is_file():
        content = skill.read_text(encoding="utf-8")
        frontmatter = re.match(r"\A---\n(.*?)\n---\n", content, re.DOTALL)
        if not frontmatter:
            errors.append("SKILL.md: missing frontmatter")
        else:
            metadata = frontmatter.group(1)
            if not re.search(r"^name: unity-agent-contract$", metadata, re.MULTILINE):
                errors.append("SKILL.md: unexpected skill name")
            if not re.search(r"^description: .+", metadata, re.MULTILINE):
                errors.append("SKILL.md: missing description")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    root = parser.parse_args().root.resolve()
    errors = validate(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PASS: portable skill, required files, local links and public path checks")
    print("Not checked: external links, Unity execution or adopting-agent behavior")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
