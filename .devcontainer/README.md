# Development Container for Raspberry Pi Kiosk

This devcontainer provides a complete development environment with all tools pre-installed.

## What's Included

### Tools & Languages
- **Python 3.11** - For Ansible
- **Node.js 20** - For commitizen, standard-version, and linting tools
- **GitHub CLI** - For GitHub operations
- **Git** - Version control

### Ansible Tools
- ansible
- ansible-core
- ansible-lint
- yamllint

### Linting & Formatting
- shellcheck - Shell script linting
- markdownlint - Markdown linting
- prettier - Code formatting
- gitleaks - Secret detection (via pre-commit)
- commitlint - Commit message validation

### VS Code Extensions
- Ansible - Syntax highlighting and IntelliSense
- YAML - YAML support with schema validation
- Markdownlint - Markdown linting
- ShellCheck - Shell script linting
- GitHub Actions - Workflow syntax highlighting
- GitHub Pull Requests - PR management
- Prettier - Code formatting

### Pre-configured Settings
- Format on save enabled
- Ansible Python interpreter configured
- YAML schemas for Ansible playbooks and GitHub Actions
- Pre-commit hooks installed automatically

## Getting Started

### 1. Open in DevContainer

**VS Code:**
1. Install "Dev Containers" extension
2. Open this repository in VS Code
3. Click "Reopen in Container" when prompted (or use Command Palette: "Dev Containers: Reopen in Container")

**GitHub Codespaces:**
1. Click "Code" → "Codespaces" → "Create codespace on main"

### 2. Configure Your Environment

The setup script automatically creates `.env` and `inventory.ini` from examples. Edit them:

```bash
# Edit environment variables
nano .env

# Edit Ansible inventory
nano inventory.ini
```

### 3. Start Developing

```bash
# Make changes to code

# Commit using conventional commits
npm run commit

# Run linting checks
pre-commit run --all-files

# Deploy to Raspberry Pi (if accessible)
ansible-playbook -i inventory.ini playbook.yaml
```

## SSH Key Access

Your host SSH keys are mounted read-only at `~/.ssh`, so you can:
- Deploy to your Raspberry Pi using existing SSH keys
- Push to GitHub using your existing credentials

## Development Workflow

### Making Changes

1. **Create a feature branch**
   ```bash
   git checkout -b feat/my-feature
   ```

2. **Make your changes**

3. **Commit using Commitizen**
   ```bash
   npm run commit
   ```

4. **Push and create PR**
   ```bash
   git push origin feat/my-feature
   gh pr create
   ```

### Testing Changes

```bash
# Lint Ansible files
ansible-lint playbook.yaml roles/

# Check YAML syntax
yamllint .

# Check Markdown
markdownlint '**/*.md'

# Run all checks
pre-commit run --all-files

# Syntax check playbook
ansible-playbook -i inventory.ini playbook.yaml --syntax-check
```

### Creating Releases

```bash
# Auto-detect version bump
npm run release

# Or force specific version
npm run release:patch  # 1.0.0 → 1.0.1
npm run release:minor  # 1.0.0 → 1.1.0
npm run release:major  # 1.0.0 → 2.0.0

# Push tags
git push --follow-tags origin main
```

## Troubleshooting

### Pre-commit hooks not running

```bash
pre-commit clean
pre-commit install --install-hooks
pre-commit install --hook-type commit-msg
```

### Ansible can't connect to Raspberry Pi

1. Check `inventory.ini` has correct hostname/IP
2. Verify SSH key is working:
   ```bash
   ssh kiosk@your-pi-hostname
   ```
3. Check network connectivity from container

### Node modules issues

```bash
rm -rf node_modules package-lock.json
npm install
```

## Container Customization

To customize the devcontainer, edit `.devcontainer/devcontainer.json`:

- Add more VS Code extensions in `customizations.vscode.extensions`
- Add more system packages in `.devcontainer/setup.sh`
- Add port forwards in `forwardPorts`
- Change Python/Node versions in `features`

After changes, rebuild the container:
- Command Palette → "Dev Containers: Rebuild Container"

## Resources

- [VS Code Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers)
- [GitHub Codespaces](https://github.com/features/codespaces)
- [Contributing Guide](../CONTRIBUTING.md)
- [Commit Convention](../.github/COMMIT_CONVENTION.md)
