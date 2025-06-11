#!/bin/bash

set -e  # Stop the script if any command fails

echo ">> Updating package list..."
sudo apt update

echo ">> Installing Git if not already installed..."
if ! command -v git &> /dev/null; then
    sudo apt install -y git
else
    echo "Git is already installed: $(git --version)"
fi

echo ">> Installing Ansible if not already installed..."
if ! command -v ansible &> /dev/null; then
    sudo apt install -y ansible
else
    echo "Ansible is already installed: $(ansible --version | head -n 1)"
fi

# Change this to your own repository URL
REPO_URL="https://github.com/KissGe83/converter.git"
REPO_DIR="converter"

echo ">> Checking if repository exists..."
if [ ! -d "../../$REPO_DIR" ]; then
    echo "Repository not found, cloning..."
    git clone "$REPO_URL"
else
    echo "Repository already exists: $REPO_DIR"
fi

echo ">> Done ✅"

