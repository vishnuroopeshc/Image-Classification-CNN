#!/usr/bin/env python3
"""
Helper script to move files from a subfolder to the root directory.
Usage: python move_files.py <subfolder_name>
"""

import sys
import shutil
from pathlib import Path


def move_files_to_root(subfolder_name):
    """
    Move all files from the specified subfolder to the root directory.
    
    Args:
        subfolder_name (str): Name of the subfolder to move files from
    """
    # Get the current directory (should be repository root)
    root_dir = Path.cwd()
    subfolder_path = root_dir / subfolder_name
    
    # Check if subfolder exists
    if not subfolder_path.exists():
        print(f"Error: Subfolder '{subfolder_name}' does not exist in {root_dir}")
        print(f"\nAvailable directories:")
        for item in root_dir.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                print(f"  - {item.name}")
        sys.exit(1)
    
    if not subfolder_path.is_dir():
        print(f"Error: '{subfolder_name}' is not a directory")
        sys.exit(1)
    
    # Get list of files to move
    files_to_move = [f for f in subfolder_path.iterdir() if f.is_file()]
    
    if not files_to_move:
        print(f"No files found in '{subfolder_name}' to move")
        sys.exit(0)
    
    # Display files that will be moved
    print(f"Files to be moved from '{subfolder_name}' to root directory:")
    for file in files_to_move:
        print(f"  - {file.name}")
    
    # Ask for confirmation
    try:
        response = input(f"\nDo you want to move these {len(files_to_move)} file(s)? (yes/no): ")
    except (EOFError, KeyboardInterrupt):
        print("\nOperation cancelled")
        sys.exit(0)
        
    if response.lower() not in ['yes', 'y']:
        print("Operation cancelled")
        sys.exit(0)
    
    # Move files
    moved_count = 0
    skipped_count = 0
    errors = []
    
    for file in files_to_move:
        destination = root_dir / file.name
        
        # Check if file already exists in root
        if destination.exists():
            print(f"  Skipping {file.name} - already exists in root directory")
            skipped_count += 1
            continue
        
        try:
            shutil.move(str(file), str(destination))
            print(f"  Moved: {file.name}")
            moved_count += 1
        except Exception as e:
            error_msg = f"  Error moving {file.name}: {str(e)}"
            print(error_msg)
            errors.append(error_msg)
    
    # Summary
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Files moved: {moved_count}")
    print(f"  Files skipped: {skipped_count}")
    print(f"  Errors: {len(errors)}")
    
    if errors:
        print(f"\nErrors encountered:")
        for error in errors:
            print(error)
    
    # Check if subfolder is now empty
    remaining_items = list(subfolder_path.iterdir())
    if not remaining_items:
        print(f"\nThe subfolder '{subfolder_name}' is now empty.")
        try:
            remove = input(f"Do you want to remove it? (yes/no): ")
            if remove.lower() in ['yes', 'y']:
                subfolder_path.rmdir()
                print(f"  Removed empty subfolder '{subfolder_name}'")
        except (EOFError, KeyboardInterrupt):
            print("\n  Keeping the empty subfolder")
    else:
        print(f"\nThe subfolder '{subfolder_name}' still contains:")
        for item in remaining_items:
            item_type = "directory" if item.is_dir() else "file"
            print(f"  - {item.name} ({item_type})")
    
    print(f"\n{'='*60}")
    print("Next steps:")
    print("  1. Review the moved files in the root directory")
    print("  2. Add changes to git: git add .")
    print("  3. Commit changes: git commit -m 'Move files from subfolder to root'")
    print("  4. Push to repository: git push")
    print(f"{'='*60}")


def main():
    """Main entry point for the script."""
    if len(sys.argv) != 2:
        print("Usage: python move_files.py <subfolder_name>")
        print("\nExample:")
        print("  python move_files.py src")
        print("  python move_files.py my_project_files")
        sys.exit(1)
    
    subfolder_name = sys.argv[1]
    
    # Validate subfolder name
    if subfolder_name.startswith('.'):
        print("Error: Hidden directories (starting with '.') are not supported")
        sys.exit(1)
    
    if '/' in subfolder_name or '\\' in subfolder_name:
        print("Error: Please provide only the subfolder name, not a path")
        print("Example: 'subfolder' not 'path/to/subfolder'")
        sys.exit(1)
    
    move_files_to_root(subfolder_name)


if __name__ == "__main__":
    main()
