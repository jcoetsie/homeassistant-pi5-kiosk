# Development Workflow Guide

This document explains the development workflow for this project, including commit conventions, versioning, and release processes.

## Quick Start for Contributors

### 1. Install Dependencies

```bash
# Install Node.js dependencies (commitizen, commitlint, standard-version)
npm install

# Install pre-commit hooks
pre-commit install --hook-type commit-msg
pre-commit install
```

### 2. Make Your Changes

Work on your feature or bug fix as usual:

```bash
# Create a feature branch
git checkout -b feat/my-new-feature

# Make your changes
# ... edit files ...
```

### 3. Commit Your Changes

**Option A: Using Commitizen (Recommended)**

```bash
# Stage your changes
git add .

# Use commitizen for interactive commit
npm run commit
```

This will prompt you with questions to build a proper conventional commit message.

**Option B: Manual Commit**

```bash
git commit -m "feat(keyboard): Add German keyboard layout support"
```

The pre-commit hook will validate your commit message format automatically.

### 4. Push and Create PR

```bash
# Push your branch
git push origin feat/my-new-feature

# Create a pull request via GitHub UI or CLI
gh pr create
```

**Important:** The `main` branch is protected and requires:
- ✅ All CI checks must pass (Ansible lint, YAML lint, security scans, etc.)
- ✅ Changes must be submitted via Pull Request
- ✅ All PR conversations must be resolved
- ⚠️ Direct pushes to `main` are blocked

## Commit Message Format

### Structure

```
<type>(<scope>): <subject>

[optional body]

[optional footer]
```

### Examples

#### Feature Addition
```
feat(keyboard): Add German keyboard layout support

Add de.xml keyboard layout file and configuration option.
Users can now set KEYBOARD_LAYOUT=de in their .env file.
```

#### Bug Fix
```
fix(vnc): Resolve authentication timeout issue

The VNC server was timing out during authentication.
Increased timeout to 30 seconds and added retry logic.

Closes #123
```

#### Breaking Change
```
feat(kiosk)!: Change default browser to Firefox

BREAKING CHANGE: Chromium is no longer the default browser.
Users must now explicitly set BROWSER=chromium in .env if they
want to continue using Chromium.
```

#### Documentation
```
docs(readme): Update installation instructions

Add troubleshooting section for common network issues.
```

#### CI/CD Changes
```
ci(github): Add automated security scanning

Add Trivy security scanning to CI pipeline.
Runs on every push and PR.
```

## Version Bumping Rules

| Commit Type | Version Bump | Example |
|-------------|--------------|---------|
| `fix:` | Patch (0.0.X) | 1.0.0 → 1.0.1 |
| `feat:` | Minor (0.X.0) | 1.0.0 → 1.1.0 |
| `BREAKING CHANGE:` or `!` | Major (X.0.0) | 1.0.0 → 2.0.0 |
| `docs:`, `chore:`, etc. | No bump | 1.0.0 → 1.0.0 |

## Release Process

### Automated Release (Recommended)

Releases are handled automatically via GitHub Actions:

1. **Merge to main**: When PRs are merged to `main`, no release happens yet
2. **Trigger release**: Manually trigger the release workflow
3. **Automatic steps**:
   - Analyzes commits since last release
   - Determines version bump (patch/minor/major)
   - Updates version in `package.json`
   - Generates/updates `CHANGELOG.md`
   - Creates git tag
   - Pushes to GitHub
   - Creates GitHub Release

#### Trigger via GitHub UI

1. Go to **Actions** tab
2. Click **Release** workflow
3. Click **Run workflow**
4. Select release type:
   - `auto` - Let conventional commits determine version
   - `patch` - Force patch version (1.0.0 → 1.0.1)
   - `minor` - Force minor version (1.0.0 → 1.1.0)
   - `major` - Force major version (1.0.0 → 2.0.0)

#### Trigger via GitHub CLI

```bash
# Auto-detect version bump
gh workflow run release.yml -f release-type=auto

# Force specific version bump
gh workflow run release.yml -f release-type=patch
gh workflow run release.yml -f release-type=minor
gh workflow run release.yml -f release-type=major
```

### Manual Release (Local)

If needed, you can create releases locally:

```bash
# Ensure you're on main and up to date
git checkout main
git pull

# Generate release (auto-detects version)
npm run release

# Or force specific version bump
npm run release:patch  # 1.0.0 → 1.0.1
npm run release:minor  # 1.0.0 → 1.1.0
npm run release:major  # 1.0.0 → 2.0.0

# Push changes and tags
git push --follow-tags origin main
```

This will:
1. Bump version in `package.json`
2. Update `CHANGELOG.md`
3. Create a git commit with message: `chore(release): X.Y.Z [skip ci]`
4. Create a git tag `vX.Y.Z`

## Changelog

The `CHANGELOG.md` is automatically maintained and includes:

- ✨ **Features** - New functionality (`feat:` commits)
- 🐛 **Bug Fixes** - Bug fixes (`fix:` commits)
- ⚡ **Performance** - Performance improvements (`perf:` commits)
- ♻️ **Refactoring** - Code refactoring (`refactor:` commits)
- 📚 **Documentation** - Documentation changes (`docs:` commits)
- 📦 **Build System** - Build changes (`build:` commits)
- 👷 **CI/CD** - CI/CD changes (`ci:` commits)

Hidden sections (not in changelog):
- 💎 Styles (`style:`)
- ✅ Tests (`test:`)
- 🔧 Chores (`chore:`)

## Pre-commit Hooks

Pre-commit hooks run automatically before each commit:

### Installed Hooks

1. **Trailing whitespace** - Removes trailing whitespace
2. **End of file fixer** - Ensures files end with newline
3. **YAML check** - Validates YAML syntax
4. **Large files check** - Prevents committing large files
5. **Merge conflict check** - Detects merge conflict markers
6. **Private key detection** - Prevents committing private keys
7. **Ansible lint** - Validates Ansible best practices
8. **YAML lint** - Comprehensive YAML validation
9. **Shell check** - Validates shell scripts
10. **Gitleaks** - Detects secrets
11. **Markdown lint** - Validates markdown formatting
12. **Commitlint** - Validates commit message format

### Bypassing Hooks (Not Recommended)

In rare cases, you can skip hooks:

```bash
# Skip all hooks (not recommended)
git commit --no-verify -m "fix(urgent): Emergency fix"

# Better: Fix the issues flagged by hooks
```

## CI/CD Pipeline

All commits and PRs trigger CI checks:

- ✅ Ansible linting
- ✅ YAML validation
- ✅ Markdown linting
- ✅ Syntax checking
- ✅ Shell script validation
- ✅ Security scanning
- ✅ Secret detection

See the [CI/CD Pipeline section in README](README.md#cicd-pipeline) for details.

## Tips for Contributors

### Good Commit Messages

✅ **Good:**
```
feat(keyboard): Add support for French AZERTY layout

Implement fr.xml keyboard layout configuration.
Users can now set KEYBOARD_LAYOUT=fr in environment variables.
```

❌ **Bad:**
```
updated keyboard stuff
```

### Commit Often

- Make small, focused commits
- Each commit should represent one logical change
- This makes the changelog more readable and useful

### Reference Issues

Link commits to issues when applicable:

```
fix(vnc): Resolve connection timeout

Increased connection timeout from 10s to 30s.

Fixes #42
```

### Test Before Committing

```bash
# Run pre-commit checks manually
pre-commit run --all-files

# Run CI checks locally (if you have tools installed)
ansible-lint playbook.yaml
yamllint .
markdownlint '**/*.md'
```

## Troubleshooting

### Commit Message Rejected

If your commit message is rejected:

1. Check the format matches: `type(scope): subject`
2. Use one of the valid types: `feat`, `fix`, `docs`, etc.
3. Use one of the valid scopes (see README)
4. Keep subject under 100 characters
5. Don't end subject with a period

### Pre-commit Hook Failed

1. Read the error message carefully
2. Fix the issues (e.g., trailing whitespace, YAML syntax)
3. Stage the fixes: `git add .`
4. Commit again

### Release Failed

If automated release fails:

1. Check GitHub Actions logs
2. Ensure all commits follow conventional format
3. Verify you have write permissions to the repository
4. Try manual release locally to debug

## Resources

- [Conventional Commits](https://www.conventionalcommits.org/)
- [Semantic Versioning](https://semver.org/)
- [Keep a Changelog](https://keepachangelog.com/)
- [Commitizen](https://github.com/commitizen/cz-cli)
- [Standard Version](https://github.com/conventional-changelog/standard-version)
