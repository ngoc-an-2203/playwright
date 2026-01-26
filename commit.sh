#!/bin/bash

if [ -n "$1" ]; then
  commit_name="$1"
else
  # Prompt for commit name
  echo "Please enter commit name:"
  read commit_name
fi

# If commit name is empty, exit
if [ -z "$commit_name" ]; then
  echo "Commit name cannot be empty."
  exit 1
fi

# Add all changes
git add .

# Commit with the entered message
git commit -m "$commit_name"

# Get current branch
current_branch=$(git branch --show-current)

# Push to origin on current branch
git push origin $current_branch