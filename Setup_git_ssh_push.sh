#!/bin/bash

# Ask for user input
read -p "GitHub username: " username
read -p "Repository name: " repo
read -p "Your email for SSH key: " email

# Step 1: Generate SSH key
ssh-keygen -t ed25519 -C "$email" -f ~/.ssh/id_ed25519 -N ""

# Step 2: Start SSH agent and add the key
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Step 3: Show public key
echo "🔑 Your SSH public key:"
cat ~/.ssh/id_ed25519.pub
echo "➡️  Copy the above key and add it to GitHub at https://github.com/settings/keys"
read -p "Press Enter after adding the SSH key..."

# Step 4: Set up git repo
git init
git add .
git commit -m "Initial commit"
git branch -M main

# Step 5: Set remote to SSH
git remote add origin git@github.com:$username/$repo.git

# Step 6: Push code
git push -u origin main

echo "✅ All done! Code pushed to GitHub via SSH."


# Permission To Run
# chmod +x setup_git_ssh_push.sh

# Run Inside workspace
# ./setup_git_ssh_push.sh
