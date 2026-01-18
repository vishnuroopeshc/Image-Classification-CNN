# Guide: Moving Files from Subfolder to Root Directory

This guide explains how to move files from a subfolder to the root directory of your Image Classification CNN project.

## Option 1: Using Git (Recommended)

If you want to move files and preserve Git history:

```bash
# Move all files from a subfolder to root
git mv subfolder/* .

# Commit the changes
git add .
git commit -m "Move files from subfolder to root"

# Push to repository
git push
```

## Option 2: Using Command Line (Linux/Mac)

```bash
# Navigate to repository root
cd /path/to/Image-Classification-CNN

# Move all files from subfolder to current directory
mv subfolder/* .

# Remove empty subfolder (optional)
rmdir subfolder

# Add and commit changes
git add .
git commit -m "Move files from subfolder to root"
git push
```

## Option 3: Using Command Line (Windows)

```cmd
# Navigate to repository root
cd C:\path\to\Image-Classification-CNN

# Move all files from subfolder to current directory
move subfolder\*.* .

# Remove empty subfolder (optional)
rmdir subfolder

# Add and commit changes
git add .
git commit -m "Move files from subfolder to root"
git push
```

## Option 4: Using the Helper Script

We've provided a Python script to make this easier:

```bash
# Run the helper script
python move_files.py subfolder

# The script will move files and show you what was moved
# Then commit and push:
git add .
git commit -m "Move files from subfolder to root"
git push
```

## Common Scenarios

### Moving Only Python Files
```bash
# Move only .py files
mv subfolder/*.py .
git add *.py
git commit -m "Move Python files to root"
git push
```

### Moving Only Specific Files
```bash
# Move specific files
git mv subfolder/model.py .
git mv subfolder/train.py .
git mv subfolder/dataset.py .
git add .
git commit -m "Move model files to root"
git push
```

### Moving and Keeping Folder Structure for Some Files
```bash
# Move some files to root, keep others in subfolder
git mv subfolder/*.py .
# Leave data files in subfolder
git add .
git commit -m "Reorganize project structure"
git push
```

## Important Notes

1. **Backup First**: Before moving files, consider creating a backup or working on a new branch
2. **Git History**: Using `git mv` preserves file history, while using regular `mv` does not
3. **Hidden Files**: The `*` wildcard doesn't match hidden files (starting with `.`). Use `.*` or list them explicitly
4. **Verify Changes**: After moving, check that all files are in the correct location before committing

## Troubleshooting

**Error: "No such file or directory"**
- Make sure you're in the repository root directory
- Verify the subfolder name is correct
- Check if files exist in the subfolder: `ls subfolder/`

**Error: "pathspec did not match any files"**
- The subfolder might be empty or have different files than expected
- List contents: `ls -la subfolder/`

**Files not showing in git status**
- Add them explicitly: `git add .`
- Check .gitignore isn't excluding them: `cat .gitignore`

## Need More Help?

If you're still having trouble, please provide:
1. The name of your subfolder
2. What files you want to move
3. Any error messages you're seeing
