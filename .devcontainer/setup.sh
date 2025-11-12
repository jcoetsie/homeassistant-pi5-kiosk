#!/bin/bash
set -e

echo "🚀 Setting up development environment..."

# Update package lists
echo "📦 Updating package lists..."
sudo apt-get update

# Install system dependencies
echo "🔧 Installing system dependencies..."
sudo apt-get install -y \
    shellcheck \
    jq \
    git

# Install Python dependencies
echo "🐍 Installing Python dependencies..."
pip install --upgrade pip
pip install \
    ansible \
    ansible-core \
    ansible-lint \
    yamllint \
    pre-commit \
    passlib

# Install Node.js dependencies
echo "📦 Installing Node.js dependencies..."
npm install

# Install pre-commit hooks
echo "🪝 Installing pre-commit hooks..."
pre-commit install --install-hooks
pre-commit install --hook-type commit-msg

# Copy .env.example if .env doesn't exist
if [ ! -f .env ]; then
    echo "📋 Creating .env from .env.example..."
    cp .env.example .env
    echo "⚠️  Please edit .env with your actual values"
fi

# Copy inventory.ini.example if inventory.ini doesn't exist
if [ ! -f inventory.ini ]; then
    echo "📋 Creating inventory.ini from inventory.ini.example..."
    cp inventory.ini.example inventory.ini
    echo "⚠️  Please edit inventory.ini with your Raspberry Pi details"
fi

# Make scripts executable
chmod +x .devcontainer/*.sh 2>/dev/null || true

echo ""
echo "✅ Development environment setup complete!"
echo ""
echo "📝 Next steps:"
echo "  1. Edit .env with your actual values"
echo "  2. Edit inventory.ini with your Raspberry Pi hostname/IP"
echo "  3. Run 'npm run commit' to make conventional commits"
echo "  4. Run 'ansible-playbook -i inventory.ini playbook.yaml' to deploy"
echo ""
echo "🔗 Useful commands:"
echo "  - npm run commit          # Create conventional commit"
echo "  - npm run release         # Generate release"
echo "  - pre-commit run --all    # Run all linting checks"
echo "  - ansible-lint            # Lint Ansible files"
echo ""
