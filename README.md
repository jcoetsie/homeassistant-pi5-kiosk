# Raspberry Pi 5 Kiosk for Home Assistant

[![CI Lint](https://github.com/jcoetsie/homeassistant-pi5-kiosk/actions/workflows/ci-lint.yml/badge.svg)](https://github.com/jcoetsie/homeassistant-pi5-kiosk/actions/workflows/ci-lint.yml)
[![Kiosk Maintenance](https://github.com/jcoetsie/homeassistant-pi5-kiosk/actions/workflows/kiosk-maintenance.yml/badge.svg)](https://github.com/jcoetsie/homeassistant-pi5-kiosk/actions/workflows/kiosk-maintenance.yml)
[![Release](https://img.shields.io/github/v/release/jcoetsie/homeassistant-pi5-kiosk)](https://github.com/jcoetsie/homeassistant-pi5-kiosk/releases)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)
[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/jcoetsie/homeassistant-pi5-kiosk)

Ansible playbook to configure a Raspberry Pi 5 as a dedicated touchscreen kiosk for Home Assistant.

## Features

- 🖥️ **Full-screen kiosk mode** with Chromium
- 👆 **Touch support** with multi-touch gestures (swipe, pinch-to-zoom)
- ⌨️ **On-screen keyboard** with configurable layout (default: Belgian French AZERTY)
- 🔘 **Floating keyboard button** for easy access
- 🔄 **Auto-recovery** with network retry logic
- 🔐 **VNC remote access** for maintenance
- 📊 **Log rotation** to prevent SD card filling
- 🤖 **GitHub Actions runner** (optional)
- 🕐 **Automatic weekly maintenance** via GitHub Actions

## Hardware Used

This kiosk setup is tested and running with the following hardware:

- **Single Board Computer**: Raspberry Pi 5 (4GB or 8GB RAM recommended)
- **Touchscreen**: ILITEK ILITEK-TP 10" Multi-touch Display
  - Driver: hid-multitouch
  - Supports multi-touch gestures (swipe, pinch-to-zoom)
- **Storage**: MicroSD card (32GB or larger recommended)
- **Power Supply**: Official Raspberry Pi 5 USB-C Power Supply (27W)
- **Network**: Ethernet (preferred) or WiFi

**Note:** This playbook should work with other touchscreen displays supported by Raspberry Pi OS, though the ILITEK touchscreen is specifically tested with multi-touch gesture support.

## Prerequisites

- Raspberry Pi 5 with Raspberry Pi OS (Debian 12 bookworm)
- Touchscreen display
- Ansible 11.6.0+ on your control machine
- Home Assistant instance

## Quick Start

### Option A: Using DevContainer (Recommended)

The easiest way to get started with all tools pre-installed:

**VS Code:**
1. Install the "Dev Containers" extension
2. Open this repository in VS Code
3. Click "Reopen in Container" when prompted

**GitHub Codespaces:**
1. Click "Code" → "Codespaces" → "Create codespace on main"

The devcontainer includes:
- ✅ Ansible & ansible-lint pre-installed
- ✅ All linting tools (yamllint, markdownlint, shellcheck, gitleaks)
- ✅ Commitizen & conventional commits tools
- ✅ Pre-commit hooks auto-configured
- ✅ Your SSH keys mounted for easy deployment

See [.devcontainer/README.md](.devcontainer/README.md) for details.

### Option B: Manual Setup

### 1. Clone the repository

```bash
git clone https://github.com/jcoetsie/homeassistant-pi5-kiosk.git
cd homeassistant-pi5-kiosk
```

### 2. Set up secrets

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your actual values
nano .env
```

**Required variables:**
- `KIOSK_PASSWORD` - Password for the kiosk user and VNC access

**Optional variables:**
- `KIOSK_URL` - Full URL to your Home Assistant dashboard
- `HOME_ASSISTANT_IP` - IP address of Home Assistant
- `KEYBOARD_LAYOUT` - Keyboard layout code (default: `be` for Belgian French)
  - Common layouts: `us` (US), `uk` (UK), `fr` (French), `de` (German), `es` (Spanish), `it` (Italian), `nl` (Dutch), `be` (Belgian)
- `WIFI_SSID` - WiFi network name
- `WIFI_PASSWORD` - WiFi password
- `GITHUB_RUNNER_TOKEN` - GitHub Actions runner token
- `GITHUB_REPO` - Your GitHub repository (format: owner/repo)

### 3. Configure inventory

```bash
# Copy the example inventory file
cp inventory.ini.example inventory.ini

# Edit with your actual Pi hostname/IP and credentials
nano inventory.ini
```

**Important:** The `inventory.ini` file contains your WiFi password and should NOT be committed to git. It's already in `.gitignore`.

Example `inventory.ini`:
```ini
[kiosk]
keuken.local ansible_user=jcoetsie

[kiosk:vars]
ansible_python_interpreter=/usr/bin/python3
wifi_ssid="YOUR_WIFI_SSID"
wifi_password="YOUR_WIFI_PASSWORD"
wifi_country="BE"
```

### 4. Run the playbook

```bash
# Source your environment variables
export $(cat .env | xargs)

# Run the playbook
ansible-playbook -i inventory.ini playbook.yaml
```

**Note:** The playbook is organized into modular roles for better maintainability. See [ANSIBLE_STRUCTURE.md](ANSIBLE_STRUCTURE.md) for details on the role-based organization.

## GitHub Actions Setup

The repository includes automatic weekly maintenance via GitHub Actions.

### Setting up the runner

1. Get a runner registration token:
   - Go to `Settings → Actions → Runners → New self-hosted runner`
   - Copy the token from the config command

2. Set environment variables and run playbook:
   ```bash
   export GITHUB_RUNNER_TOKEN="your-token-here"
   export GITHUB_REPO="yourusername/yourrepo"
   ansible-playbook -i inventory.ini kiosk.yaml
   ```

3. Add secrets to your GitHub repository:
   - Go to `Settings → Secrets and variables → Actions`
   - **Required secrets:**
     - `KIOSK_PASSWORD` - Kiosk user password
   - **Optional secrets** (will use defaults from playbook if not set):
     - `KIOSK_URL` - Home Assistant dashboard URL
     - `HOME_ASSISTANT_IP` - Home Assistant IP address (also used for failure webhook notifications)
     - `WIFI_SSID` - WiFi network name
     - `WIFI_PASSWORD` - WiFi password
     - `GH_RUNNER_TOKEN` - GitHub runner token (for re-registration)

The workflow runs every Saturday at 2:00 AM and can be triggered manually.

### Home Assistant Webhook (Optional)

The workflow can send failure notifications to Home Assistant via webhook. To enable this:

1. **Create a webhook automation in Home Assistant:**

   ```yaml
   automation:
     - id: kiosk_maintenance_failed_notification
       alias: "Kiosk Maintenance Failed Alert"
       trigger:
         - platform: webhook
           webhook_id: kiosk_maintenance_failed
       action:
         - service: notify.mobile_app  # Or notify.persistent_notification
           data:
             title: "⚠️ Kiosk Maintenance Failed"
             message: "Kitchen kiosk maintenance failed at {{ trigger.json.time }}"
             data:
               priority: high
   ```
2. **Add `HOME_ASSISTANT_IP` to GitHub Secrets** (if not already set)

3. **The webhook URL** is automatically created:
   - `http://YOUR_HA_IP:8123/api/webhook/kiosk_maintenance_failed`
   - No authentication required

When the Saturday maintenance fails, you'll receive an instant notification through Home Assistant!

## Usage

### Accessing the kiosk

- **Physical access**: Touch the keyboard button (⌨️) in the bottom-right corner
- **VNC access**: Connect to `<pi-hostname>:5900` with the kiosk password
- **SSH access**: `ssh kiosk@<pi-hostname>` (uses your SSH key)

### On-screen keyboard

- Tap the floating ⌨️ button in bottom-right corner
- Or run: `/home/kiosk/toggle-keyboard.sh`
- Belgian French AZERTY layout with accented characters

### Logs

View kiosk startup logs:
```bash
tail -f /home/kiosk/kiosk.log
```

Logs are automatically rotated weekly and kept for 2 weeks.

## Customization

### Change the displayed URL

Set `KIOSK_URL` environment variable or edit `kiosk.yaml`:
```yaml
kiosk_url: "{{ lookup('env', 'KIOSK_URL') | default('http://192.168.1.5:8123/lovelace/0', true) }}"
```

### Adjust screen blanking

Edit the `.xinitrc` section in `kiosk.yaml`:
```bash
xset s 600 600        # 600 seconds = 10 minutes
xset dpms 0 0 600
```

### Change keyboard layout

Set the `KEYBOARD_LAYOUT` environment variable to your desired layout code (default is `be` for Belgian French):

```bash
export KEYBOARD_LAYOUT=us  # For US keyboard
# or
export KEYBOARD_LAYOUT=fr  # For French keyboard
```

Common keyboard layout codes:
- `us` - US English
- `uk` - UK English
- `fr` - French
- `de` - German
- `es` - Spanish
- `it` - Italian
- `nl` - Dutch
- `be` - Belgian French (AZERTY)

**Note:** The matchbox on-screen keyboard comes with a Belgian French layout by default. To customize the on-screen keyboard layout,
you'll need to create or edit `/usr/share/matchbox-keyboard/keyboard-<layout>.xml` on the Pi and modify the toggle script to use it.

## Troubleshooting

### Browser not starting

Check the logs:
```bash
tail -50 /home/kiosk/kiosk.log
```

### Keyboard not showing

Toggle manually:
```bash
/home/kiosk/toggle-keyboard.sh
```

### VNC connection refused

Ensure VNC is enabled:
```bash
sudo raspi-config nonint do_vnc 0
sudo systemctl restart vncserver-x11-serviced
```

### Network issues

Check network status:
```bash
nmcli connection show
```

## CI/CD Pipeline

This project includes comprehensive continuous integration checks to ensure code quality, security, and best practices.

### Automated Checks

Every push and pull request triggers the following checks:

| Check | Description | Tool |
|-------|-------------|------|
| **Ansible Lint** | Validates Ansible best practices and detects common issues | `ansible-lint` |
| **YAML Lint** | Ensures YAML files are properly formatted and valid | `yamllint` |
| **Markdown Lint** | Checks documentation formatting and consistency | `markdownlint` |
| **Syntax Check** | Validates Ansible playbook syntax and inventory | `ansible-playbook --syntax-check` |
| **Shell Check** | Lints all shell scripts for common errors | `shellcheck` |
| **Security Scan** | Scans for vulnerabilities in dependencies and config | `trivy` |
| **Secret Detection** | Prevents accidental commits of secrets and credentials | `gitleaks` |

### Running Checks Locally

#### Install Pre-commit Hooks

The easiest way to run all checks locally is using pre-commit:

```bash
# Install pre-commit (if not already installed)
pip install pre-commit

# Install the git hooks
pre-commit install

# Run checks on all files
pre-commit run --all-files

# Run checks on staged files only
pre-commit run
```

#### Run Individual Checks

You can also run specific checks manually:

```bash
# Ansible lint
ansible-lint playbook.yaml roles/

# YAML lint
yamllint .

# Markdown lint
markdownlint '**/*.md'

# Ansible syntax check
ansible-playbook playbook.yaml -i inventory.ini --syntax-check

# Shell check
find roles -name "*.sh" -type f -exec shellcheck {} +

# Security scan
trivy config .

# Check for secrets
gitleaks detect --source . --verbose
```

#### Install Linting Tools

If you prefer to run checks manually without pre-commit:

```bash
# Install Ansible linting tools
pip install ansible-lint yamllint

# Install shellcheck (macOS)
brew install shellcheck

# Install markdownlint (requires Node.js)
npm install -g markdownlint-cli

# Install trivy (macOS)
brew install aquasecurity/trivy/trivy

# Install gitleaks (macOS)
brew install gitleaks
```

### CI Configuration Files

- `.github/workflows/ci-lint.yml` - GitHub Actions workflow
- `.ansible-lint` - Ansible linting rules
- `.yamllint.yaml` - YAML linting configuration
- `.markdownlint.json` - Markdown linting rules
- `.gitleaks.toml` - Secret detection configuration
- `.pre-commit-config.yaml` - Pre-commit hook configuration

### Pull Request Requirements

All checks must pass before merging:
- ✅ All linters pass with no errors
- ✅ No security vulnerabilities detected
- ✅ No secrets committed
- ✅ Playbook syntax is valid

## Conventional Commits & Releases

This project uses [Conventional Commits](https://www.conventionalcommits.org/) for consistent commit messages and automated versioning.

### Commit Message Format

Commits must follow this format:

```
<type>(<scope>): <subject>

[optional body]

[optional footer]
```

**Types:**
- `feat` - New feature (triggers minor version bump)
- `fix` - Bug fix (triggers patch version bump)
- `docs` - Documentation changes
- `style` - Code style changes (formatting, etc.)
- `refactor` - Code refactoring
- `perf` - Performance improvements
- `test` - Adding or updating tests
- `build` - Build system changes
- `ci` - CI/CD changes
- `chore` - Other changes (dependencies, etc.)
- `revert` - Revert a previous commit

**Breaking Changes:** Add `BREAKING CHANGE:` in the footer or `!` after type/scope to trigger major version bump.

**Scopes:**
- `system` - System configuration (user, SSH, updates)
- `network` - Network configuration (Ethernet, WiFi)
- `packages` - Package management
- `vnc` - VNC server configuration
- `kiosk` - Kiosk/browser configuration
- `keyboard` - Keyboard configuration
- `logs` - Log management
- `github-runner` - GitHub Actions runner
- `ci` - CI/CD pipeline
- `docs` - Documentation
- `deps` - Dependencies

### Using Commitizen (Recommended)

Install and use Commitizen for interactive commit message creation:

```bash
# Install dependencies
npm install

# Create a commit using Commitizen
npm run commit
```

This will guide you through creating a properly formatted commit message.

### Manual Commits

If you prefer manual commits, ensure they follow the format:

```bash
# Example: New feature
git commit -m "feat(keyboard): Add support for German keyboard layout"

# Example: Bug fix
git commit -m "fix(vnc): Resolve authentication timeout issue"

# Example: Breaking change
git commit -m "feat(kiosk)!: Change default browser to Firefox

BREAKING CHANGE: Chromium is no longer the default browser. Update your configuration to specify browser preference."
```

### Automated Releases

Releases are automated via GitHub Actions workflow:

1. **Automatic Version Bumping**: Based on conventional commit types
   - `fix:` → patch version (1.0.0 → 1.0.1)
   - `feat:` → minor version (1.0.0 → 1.1.0)
   - `BREAKING CHANGE:` → major version (1.0.0 → 2.0.0)

2. **Changelog Generation**: Automatically generated from commit messages

3. **GitHub Release**: Creates a GitHub release with changelog

#### Trigger a Release

Use the GitHub Actions workflow:

```bash
# Via GitHub UI
# Go to Actions → Release → Run workflow → Select release type

# Or trigger via GitHub CLI
gh workflow run release.yml -f release-type=auto
```

#### Manual Release (Local)

```bash
# Install dependencies
npm install

# Generate release (auto-detects version bump)
npm run release

# Or specify version bump
npm run release:patch  # 1.0.0 → 1.0.1
npm run release:minor  # 1.0.0 → 1.1.0
npm run release:major  # 1.0.0 → 2.0.0

# Push tags
git push --follow-tags origin main
```

### Pre-commit Validation

Commit messages are validated automatically via pre-commit hooks:

```bash
# Install pre-commit hooks (includes commitlint)
npm install
pre-commit install --hook-type commit-msg

# Now all commits will be validated
git commit -m "feat(kiosk): Add new feature"  # ✅ Valid
git commit -m "updated stuff"                  # ❌ Invalid - will be rejected
```

### Viewing the Changelog

The `CHANGELOG.md` file is automatically maintained with all notable changes:

```bash
# View changelog
cat CHANGELOG.md

# Changelog is updated on each release
```

## Security Notes

⚠️ **Never commit secrets to git!**

### Protected Files (in .gitignore)
- `.env` - Contains passwords, tokens, and sensitive configuration
- `inventory.ini` - Contains WiFi passwords and hostnames
- `.ansible/` - Ansible cache directory

### Templates (safe to commit)
- `.env.example` - Template for environment variables
- `inventory.ini.example` - Template for Ansible inventory

### Best Practices
- Use `.env.example` as a template for `.env`
- Use `inventory.ini.example` as a template for `inventory.ini`
- Store secrets in GitHub Secrets for Actions workflows
- Never commit actual WiFi passwords, API tokens, or credentials
- Consider using Ansible Vault for additional security

## License

MIT

## Contributing

Contributions are welcome! This project uses [Conventional Commits](https://www.conventionalcommits.org/) for commit messages and automated versioning.

### Getting Started

**Option 1: DevContainer (Recommended)**

1. **Fork and clone** the repository
2. **Open in VS Code** and click "Reopen in Container" (or use GitHub Codespaces)
3. Environment is automatically configured with all tools!
4. **Make your changes** in a feature branch
5. **Commit using Commitizen**: `npm run commit`
6. **Push and create a PR**

**Option 2: Manual Setup**

1. **Fork and clone** the repository
2. **Install dependencies**: `npm install`
3. **Install pre-commit hooks**: `pre-commit install --hook-type commit-msg && pre-commit install`
4. **Make your changes** in a feature branch
5. **Commit using Commitizen**: `npm run commit` (or follow [commit conventions](.github/COMMIT_CONVENTION.md))
6. **Push and create a PR**

### Resources

- [Contributing Guide](CONTRIBUTING.md) - Detailed development workflow
- [Commit Convention](.github/COMMIT_CONVENTION.md) - Quick reference for commit messages
- [Pull Request Template](.github/PULL_REQUEST_TEMPLATE.md) - PR checklist

### Branch Protection

The `main` branch is protected to ensure code quality:

- 🔒 **Direct pushes blocked** - All changes must go through Pull Requests
- ✅ **Required CI checks** - All linting and security scans must pass
- 💬 **Conversation resolution** - All PR discussions must be resolved before merging
- 🚫 **Force pushes disabled** - Prevents accidental history rewriting

All PRs must:
- ✅ Follow conventional commit format
- ✅ Pass all CI checks (linting, security, tests)
- ✅ Include relevant documentation updates
- ✅ Be tested on actual hardware when possible
