#!/usr/bin/env python3
"""
Parse markdownlint output and fix remaining errors that can't be auto-fixed.
"""

import re
from pathlib import Path


def parse_errors(output_file: str) -> list[tuple[str, int, str, str]]:
    """Parse markdownlint output file and extract errors."""
    errors = []

    # Read the file as UTF-16-LE (Windows encoding)
    with open(output_file, 'rb') as f:
        content = f.read()
        # Check for BOM
        if content.startswith(b'\xff\xfe'):  # UTF-16 LE BOM
            text = content[2:].decode('utf-16-le')
        elif content.startswith(b'\xfe\xff'):  # UTF-16 BE BOM
            text = content[2:].decode('utf-16-be')
        else:
            # Try to decode as UTF-16-LE
            try:
                text = content.decode('utf-16-le')
            except UnicodeDecodeError:
                # Fallback to UTF-8
                text = content.decode('utf-8', errors='replace')

    # Parse error lines
    for line in text.split('\n'):
        line = line.strip()
        if not line or 'error' not in line.lower():
            continue

        # Pattern: file:line error MD###/rule-name Description [Context: "..."]
        # Handle both formats: file:line error and file:line:col error
        match = re.match(r'^([^:]+):(\d+)(?::(\d+))?\s+error\s+(MD\d+/\S+)\s+(.+?)(?:\s+\[Context:\s+"(.+?)"\])?$', line)
        if match:
            filepath, line_num, col_num, rule, desc, context = match.groups()
            errors.append((filepath, int(line_num), rule, desc))

    return errors


def fix_md041_first_line_heading(filepath: str) -> bool:
    """Fix MD041: First line should be a top-level heading."""
    path = Path(filepath)
    if not path.exists():
        return False

    content = path.read_text(encoding='utf-8')
    lines = content.split('\n')

    # Check if first non-empty line is not an h1
    first_line_idx = 0
    for i, line in enumerate(lines):
        if line.strip():
            first_line_idx = i
            break

    if first_line_idx >= len(lines):
        return False

    first_line = lines[first_line_idx]

    # If it's already an h1, nothing to do
    if first_line.strip().startswith('# '):
        return False

    # If it's a heading but not h1, convert to h1
    if first_line.strip().startswith('#'):
        # Count leading #
        level = len(first_line) - len(first_line.lstrip('#'))
        if level > 1:
            # Convert to h1
            new_line = '# ' + first_line.lstrip('#').lstrip()
            lines[first_line_idx] = new_line
            path.write_text('\n'.join(lines), encoding='utf-8')
            return True

    # If it's not a heading at all, add an h1
    # Extract a title from the first line or use filename
    if first_line.strip():
        title = first_line.strip().rstrip('#').strip()
        # Remove markdown formatting
        title = re.sub(r'^#+\s*', '', title)
        title = re.sub(r'\*\*([^*]+)\*\*', r'\1', title)
        title = title.strip()

        if title:
            lines.insert(first_line_idx, f'# {title}')
            path.write_text('\n'.join(lines), encoding='utf-8')
            return True

    return False


def fix_md001_heading_increment(filepath: str, line_num: int, expected: str) -> bool:
    """Fix MD001: Heading levels should only increment by one level at a time."""
    path = Path(filepath)
    if not path.exists():
        return False

    content = path.read_text(encoding='utf-8')
    lines = content.split('\n')

    if line_num < 1 or line_num > len(lines):
        return False

    line_idx = line_num - 1
    line = lines[line_idx]

    if not line.strip().startswith('#'):
        return False

    # Extract expected level (h2, h3, h4, etc.)
    expected_level = int(expected[1]) if expected.startswith('h') else 2

    # Count current level
    current_level = len(line) - len(line.lstrip('#'))

    if current_level != expected_level:
        # Fix the heading level
        new_line = '#' * expected_level + ' ' + line.lstrip('#').lstrip()
        lines[line_idx] = new_line
        path.write_text('\n'.join(lines), encoding='utf-8')
        return True

    return False


def fix_md013_line_length(filepath: str, line_num: int, max_length: int = 120) -> bool:  # noqa: C901
    """Fix MD013: Line length issues by wrapping long lines."""
    # Suppressed: Complex line wrapping logic requires multiple conditional branches for different markdown contexts
    path = Path(filepath)
    if not path.exists():
        return False

    content = path.read_text(encoding='utf-8')
    lines = content.split('\n')

    if line_num < 1 or line_num > len(lines):
        return False

    line_idx = line_num - 1
    line = lines[line_idx]

    if len(line) <= max_length:
        return False

    # Don't wrap code blocks, links, or special markdown
    if line.strip().startswith('```') or line.strip().startswith('|') or '`' in line:
        # For code blocks and tables, we might want to keep them as-is
        # But for very long lines, we could break them
        if len(line) > max_length * 2:  # Only break extremely long lines
            # Try to break at spaces
            words = line.split(' ')
            if len(words) > 1:
                new_lines = []
                current_line = ''
                for word in words:
                    if len(current_line) + len(word) + 1 <= max_length:
                        current_line += (' ' if current_line else '') + word
                    else:
                        if current_line:
                            new_lines.append(current_line)
                        current_line = word
                if current_line:
                    new_lines.append(current_line)

                if len(new_lines) > 1:
                    # Replace the line with wrapped version
                    lines[line_idx] = '\n'.join(new_lines)
                    path.write_text('\n'.join(lines), encoding='utf-8')
                    return True
        return False

    # For regular text, wrap at spaces
    words = line.split(' ')
    if len(words) > 1:
        new_lines = []
        current_line = ''
        indent = len(line) - len(line.lstrip())

        for word in words:
            test_line = current_line + (' ' if current_line else '') + word
            if len(test_line) <= max_length:
                current_line = test_line
            else:
                if current_line:
                    new_lines.append(' ' * indent + current_line)
                current_line = word

        if current_line:
            new_lines.append(' ' * indent + current_line)

        if len(new_lines) > 1:
            lines[line_idx] = '\n'.join(new_lines)
            path.write_text('\n'.join(lines), encoding='utf-8')
            return True

    return False


def fix_md051_link_fragments(filepath: str, line_num: int) -> bool:
    """Fix MD051: Link fragments should be valid."""
    path = Path(filepath)
    if not path.exists():
        return False

    content = path.read_text(encoding='utf-8')
    lines = content.split('\n')

    if line_num < 1 or line_num > len(lines):
        return False

    line_idx = line_num - 1
    line = lines[line_idx]

    # Find markdown links with fragments
    # Pattern: [text](#fragment)
    pattern = r'\[([^\]]+)\]\(#([^)]+)\)'

    def fix_fragment(match):
        text = match.group(1)
        fragment = match.group(2)

        # Convert fragment to valid format (lowercase, replace spaces with hyphens, remove special chars)
        valid_fragment = re.sub(r'[^\w\s-]', '', fragment.lower())
        valid_fragment = re.sub(r'[-\s]+', '-', valid_fragment)
        valid_fragment = valid_fragment.strip('-')

        return f'[{text}](#{valid_fragment})'

    new_line = re.sub(pattern, fix_fragment, line)

    if new_line != line:
        lines[line_idx] = new_line
        path.write_text('\n'.join(lines), encoding='utf-8')
        return True

    return False


def main():
    """Main function to fix markdownlint errors."""
    output_file = Path('markdownlint-output-1.txt')

    if not output_file.exists():
        print(f"Error: {output_file} not found")
        return

    errors = parse_errors(str(output_file))

    print(f"Found {len(errors)} errors to fix")

    # Group errors by file and rule
    fixes_applied = 0

    for filepath, line_num, rule, desc in errors:
        rule_code = rule.split('/')[0] if '/' in rule else rule

        try:
            fixed = False

            if rule_code == 'MD041':
                fixed = fix_md041_first_line_heading(filepath)
            elif rule_code == 'MD001':
                # Extract expected level from description
                match = re.search(r'Expected:\s*(h\d+)', desc)
                if match:
                    expected = match.group(1)
                    fixed = fix_md001_heading_increment(filepath, line_num, expected)
            elif rule_code == 'MD013':
                fixed = fix_md013_line_length(filepath, line_num)
            elif rule_code == 'MD051':
                fixed = fix_md051_link_fragments(filepath, line_num)

            if fixed:
                fixes_applied += 1
                print(f"Fixed {rule_code} in {filepath}:{line_num}")

        except Exception as e:
            print(f"Error fixing {filepath}:{line_num} - {e}")

    print(f"\nApplied {fixes_applied} fixes")
    print("\nNote: Some errors (like MD024 duplicate headings, MD025 multiple h1) require manual review")


if __name__ == '__main__':
    main()
