#!/usr/bin/env python3
"""Add PSScriptAnalyzer suppression comments to PowerShell scripts."""

from pathlib import Path

SUPPRESSION = """# Suppress PSAvoidUsingWriteHost: This script uses Write-Host for status/output messages
# PSScriptAnalyzer suppression - Write-Host is appropriate for user-facing status messages
# [Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Status and output messages require Write-Host for proper display')]
"""

def add_suppression_to_file(file_path: Path) -> bool:
    """Add suppression comment to a PowerShell file if it uses Write-Host and doesn't already have suppression."""
    try:
        content = file_path.read_text(encoding='utf-8')

        # Skip if already has suppression
        if 'SuppressMessageAttribute' in content:
            return False

        # Skip if doesn't use Write-Host
        if 'Write-Host' not in content:
            return False

        # Find the insertion point (after first comment block or shebang)
        lines = content.split('\n')
        insert_idx = 0

        # Skip shebang
        if lines[0].startswith('#!'):
            insert_idx = 1

        # Skip initial comment block
        while insert_idx < len(lines) and (lines[insert_idx].strip().startswith('#') or lines[insert_idx].strip() == ''):
            insert_idx += 1

        # Insert suppression
        lines.insert(insert_idx, SUPPRESSION.rstrip())
        new_content = '\n'.join(lines)

        file_path.write_text(new_content, encoding='utf-8')
        return True
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Process all PowerShell scripts in the scripts directory."""
    scripts_dir = Path(__file__).parent
    ps1_files = list(scripts_dir.rglob('*.ps1'))

    fixed_count = 0
    for ps1_file in ps1_files:
        if add_suppression_to_file(ps1_file):
            print(f"Fixed: {ps1_file.relative_to(scripts_dir.parent)}")
            fixed_count += 1

    print(f"\nFixed {fixed_count} files")

if __name__ == '__main__':
    main()
