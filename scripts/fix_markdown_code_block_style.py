#!/usr/bin/env python3
"""
Fix MD046: Code block style.

Converts indented code blocks (4+ spaces) to fenced code blocks (```).
"""

import re
from pathlib import Path


def is_indented_code_line(line: str) -> bool:
    """Check if a line is part of an indented code block."""
    stripped = line.rstrip()
    # Empty lines are not code lines
    if not stripped:
        return False
    # Indented code blocks start with 4+ spaces or a tab
    if stripped.startswith("    ") or stripped.startswith("\t"):
        return True
    return False


def detect_code_language(content: str) -> str:
    """
    Try to detect the language of a code block from its content.
    Returns empty string if language cannot be determined.
    """
    # Simple heuristics for common languages
    if re.search(r"^(def|class|import|from|if|for|while|async|await)\s", content, re.MULTILINE):
        return "python"
    if re.search(r"(function|const|let|var|=>|import\s+.*from)", content):
        return "javascript"
    if re.search(r"(SELECT|INSERT|UPDATE|DELETE|CREATE|ALTER)\s", content, re.IGNORECASE):
        return "sql"
    if re.search(r"(<html|<div|<script|<!DOCTYPE)", content, re.IGNORECASE):
        return "html"
    if re.search(r"(\{|\}|@media|\.class|#id)", content) and re.search(r"color|margin|padding", content):
        return "css"
    if re.search(r"(#!/bin/bash|#!/bin/sh|echo\s|export\s)", content):
        return "bash"
    if re.search(r"(package|import|public\s+class|private\s+class)", content):
        return "java"
    return ""


def fix_code_block_style(content: str) -> tuple[str, int]:
    """
    Convert indented code blocks to fenced code blocks.

    Returns:
        (new_content, blocks_converted)
    """
    lines = content.split("\n")
    new_lines = []
    blocks_converted = 0
    i = 0
    in_code_block = False
    code_block_lines = []

    while i < len(lines):
        line = lines[i]

        # Check if we're already in a fenced code block
        if line.strip().startswith("```"):
            # If we were in an indented code block, close it first
            if in_code_block and code_block_lines:
                # Convert accumulated indented code to fenced
                code_content = "\n".join(code_block_lines)
                language = detect_code_language(code_content)
                lang_suffix = f"{language}\n" if language else "\n"
                new_lines.append("```" + lang_suffix + code_content + "\n```")
                blocks_converted += 1
                code_block_lines = []
                in_code_block = False

            new_lines.append(line)
            i += 1
            continue

        # Check if current line is indented code
        if is_indented_code_line(line):
            if not in_code_block:
                # Start of new indented code block
                in_code_block = True
                code_block_lines = []

            # Remove leading indentation (4 spaces or tab)
            if line.startswith("    "):
                code_line = line[4:]
            elif line.startswith("\t"):
                code_line = line[1:]
            else:
                code_line = line.lstrip()

            code_block_lines.append(code_line)
            i += 1
        else:
            # Not a code line
            if in_code_block and code_block_lines:
                # End of indented code block - convert it
                code_content = "\n".join(code_block_lines)
                language = detect_code_language(code_content)
                lang_suffix = f"{language}\n" if language else "\n"
                new_lines.append("```" + lang_suffix + code_content + "\n```")
                blocks_converted += 1
                code_block_lines = []
                in_code_block = False

            new_lines.append(line)
            i += 1

    # Handle case where file ends with indented code block
    if in_code_block and code_block_lines:
        code_content = "\n".join(code_block_lines)
        language = detect_code_language(code_content)
        lang_suffix = f"{language}\n" if language else "\n"
        new_lines.append("```" + lang_suffix + code_content + "\n```")
        blocks_converted += 1

    return "\n".join(new_lines), blocks_converted


def parse_markdownlint_output(output_file: Path) -> list[Path]:
    """Parse markdownlint output to get files with MD046 issues."""
    files_to_fix = set()

    try:
        with open(output_file, encoding="utf-16-le") as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            with open(output_file, encoding="utf-8") as f:
                content = f.read()
        except Exception:
            return []

    # Pattern for MD046 errors
    # Handles both "Errors: file.md:123 error MD046" and "file.md:123 error MD046"
    pattern = r"(?:^Errors:\s+)?([^:]+):\d+.*error\s+MD046"
    for line in content.split("\n"):
        match = re.search(pattern, line)
        if match:
            file_path = Path(match.group(1))
            files_to_fix.add(file_path)

    return list(files_to_fix)


def fix_markdown_file(file_path: Path) -> tuple[bool, int]:
    """
    Fix code block style in a single markdown file.

    Returns:
        (changed, blocks_converted)
    """
    try:
        with open(file_path, encoding="utf-8") as f:
            original_content = f.read()

        new_content, blocks_converted = fix_code_block_style(original_content)

        if new_content != original_content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            return True, blocks_converted

        return False, 0

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False, 0


def main():
    """Main function to fix MD046 issues."""
    project_root = Path(__file__).parent.parent

    # Parse markdownlint output to get files with MD046 issues
    output_file = None
    for filename in [
        "markdownlint-out-8.txt",
        "markdownlint-out-7.txt",
        "markdownlint-out-6.txt",
        "markdownlint-out-5.txt",
        "markdownlint-out-4.txt",
        "markdownlint-out-3.txt",
    ]:
        candidate = project_root / filename
        if candidate.exists():
            output_file = candidate
            break

    if output_file:
        print(f"Parsing markdownlint output from {output_file}...")
        files_with_issues = parse_markdownlint_output(output_file)
        print(f"Found {len(files_with_issues)} files with MD046 issues in output")

        files_to_fix = files_with_issues
    else:
        print("No markdownlint output file found.")
        print("Processing all markdown files...")
        # Fallback: process all markdown files
        ignore_dirs = {".git", "node_modules", "__pycache__", ".venv", "venv", "dist", "build", ".venv-ci"}
        files_to_fix = []
        for md_file in project_root.rglob("*.md"):
            if any(ignore_dir in md_file.parts for ignore_dir in ignore_dirs):
                continue
            files_to_fix.append(md_file)

    total_changed = 0
    total_blocks_converted = 0

    for file_path in sorted(files_to_fix):
        # Make path absolute if relative
        if not file_path.is_absolute():
            file_path = project_root / file_path

        if not file_path.exists():
            print(f"Warning: {file_path} does not exist, skipping")
            continue

        changed, blocks_converted = fix_markdown_file(file_path)
        if changed:
            total_changed += 1
            total_blocks_converted += blocks_converted
            print(f"[OK] {file_path.relative_to(project_root)} ({blocks_converted} code block(s) converted)")

    print(f"\nSummary: {total_changed} files changed, {total_blocks_converted} total code blocks converted")


if __name__ == "__main__":
    main()
