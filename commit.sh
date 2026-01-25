#!/bin/bash

# Prompt for commit name
echo "Please enter commit name:"
read commit_name

# Add all changes
git add .

# Commit with the entered message
git commit -m "$commit_name"

# Get current branch
current_branch=$(git branch --show-current)

# Push to origin on current branch
git push origin $current_branch