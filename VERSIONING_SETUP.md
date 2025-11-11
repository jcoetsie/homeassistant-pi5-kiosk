# Conventional Commits & Semantic Versioning Setup

This document summarizes the conventional commits, changelog, and automated semantic versioning setup for this project.

## 📦 What Was Set Up

### 1. **Package Configuration** (`package.json`)
- Project metadata and version management
- NPM scripts for commits and releases
- Dependencies: commitizen, commitlint, standard-version

### 2. **Commit Message Enforcement** (`.commitlintrc.json`)
- Validates commit message format
- Enforces conventional commits specification
- Custom scopes for this project (system, network, kiosk, etc.)
- Rules for type, scope, subject format

### 3. **Changelog Generation** (`.versionrc.json`)
- Configuration for `standard-version`
- Defines which commit types appear in changelog
- Emoji prefixes for better readability
- Auto-generates `CHANGELOG.md` on each release

### 4. **Initial Changelog** (`CHANGELOG.md`)
- Started with v1.0.0 baseline
- Documents all existing features from the monolithic refactoring
- Will be automatically updated on each release

### 5. **Pre-commit Validation** (`.pre-commit-config.yaml`)
- Added `commitlint` hook
- Validates commit messages before they're created
- Runs on `commit-msg` git hook stage

### 6. **GitHub Actions Workflows**

#### Release Workflow (`.github/workflows/release.yml`)
- Manual trigger with release type selection (auto/patch/minor/major)
- Automatically bumps version based on conventional commits
- Updates `CHANGELOG.md`
- Creates git tags
- Publishes GitHub releases

#### CI Workflow (`.github/workflows/ci-lint.yml`)
- Added `commitlint` job for PR validation
- Validates all commits in a PR follow conventions
- Only runs on pull requests

### 7. **Documentation**

#### CONTRIBUTING.md
- Comprehensive development workflow guide
- Commit message format examples
- Release process explanation
- Pre-commit hooks documentation
- Tips for contributors

#### .github/COMMIT_CONVENTION.md
- Quick reference for commit types and scopes
- Version bumping rules
- Common examples
- Cheat sheet format

#### .github/PULL_REQUEST_TEMPLATE.md
- Standardized PR template
- Reminds contributors about conventional commits
- Includes checklist for code quality
- Links to commit convention documentation

### 8. **README Updates**
- Added release and conventional commits badges
- Added comprehensive "Conventional Commits & Releases" section
- Updated contributing section with workflow links
- Fixed broken badge URLs

### 9. **Git Ignore** (`.gitignore`)
- Added Node.js related ignores (node_modules, package-lock.json, etc.)

## 🚀 How to Use

### For Contributors

#### Making Commits

**Option 1: Interactive (Recommended)**
```bash
npm run commit
```

**Option 2: Manual**
```bash
git commit -m "feat(keyboard): Add Spanish keyboard layout"
```

#### Creating a Release

**Automated (via GitHub Actions)**
1. Go to Actions → Release → Run workflow
2. Select release type (auto/patch/minor/major)
3. Workflow automatically creates release

**Manual (local)**
```bash
npm run release          # Auto-detect version bump
npm run release:patch    # Force patch (0.0.X)
npm run release:minor    # Force minor (0.X.0)
npm run release:major    # Force major (X.0.0)
git push --follow-tags origin main
```

### For Maintainers

#### Setting Up Local Development

```bash
# Install dependencies
npm install

# Install pre-commit hooks
pre-commit install --hook-type commit-msg
pre-commit install
```

#### Reviewing Pull Requests

All PRs are automatically validated:
- ✅ Commit messages follow conventional format
- ✅ All CI checks pass
- ✅ No secrets detected
- ✅ Code passes linting

## 📊 Version Bumping Rules

| Commit Type | Example | Version Change |
|-------------|---------|----------------|
| `fix:` | `fix(vnc): Resolve timeout` | 1.0.0 → 1.0.1 |
| `feat:` | `feat(keyboard): Add layout` | 1.0.0 → 1.1.0 |
| `BREAKING CHANGE:` or `!` | `feat(kiosk)!: Change browser` | 1.0.0 → 2.0.0 |
| Other (`docs:`, `chore:`, etc.) | `docs: Update readme` | No change |

## 📝 Changelog Sections

The generated changelog includes these sections:

| Emoji | Section | Commit Types |
|-------|---------|--------------|
| ✨ | Features | `feat:` |
| 🐛 | Bug Fixes | `fix:` |
| ⚡ | Performance | `perf:` |
| ♻️ | Refactoring | `refactor:` |
| 📚 | Documentation | `docs:` |
| 📦 | Build System | `build:` |
| 👷 | CI/CD | `ci:` |

Hidden (not in changelog): `style:`, `test:`, `chore:`

## 🔧 Configuration Files Reference

| File | Purpose |
|------|---------|
| `package.json` | NPM package config, scripts, dependencies |
| `.commitlintrc.json` | Commit message validation rules |
| `.versionrc.json` | Changelog generation configuration |
| `CHANGELOG.md` | Auto-generated changelog (don't edit manually) |
| `.pre-commit-config.yaml` | Git hooks configuration |
| `.github/workflows/release.yml` | Automated release workflow |
| `.github/workflows/ci-lint.yml` | CI with commit validation |
| `CONTRIBUTING.md` | Detailed contributor guide |
| `.github/COMMIT_CONVENTION.md` | Quick reference guide |
| `.github/PULL_REQUEST_TEMPLATE.md` | PR template |

## 🎯 Benefits

### For the Project
- ✅ Consistent commit history
- ✅ Automated versioning (no manual version bumps)
- ✅ Auto-generated changelog
- ✅ Clear release notes
- ✅ Better collaboration

### For Developers
- ✅ Clear contribution guidelines
- ✅ Interactive commit tool (commitizen)
- ✅ Automatic validation (pre-commit hooks)
- ✅ Standardized workflow

### For Users
- ✅ Clear release notes
- ✅ Predictable versioning (semantic versioning)
- ✅ Easy to track changes
- ✅ Professional project management

## 🔗 Resources

- [Conventional Commits](https://www.conventionalcommits.org/)
- [Semantic Versioning](https://semver.org/)
- [Keep a Changelog](https://keepachangelog.com/)
- [Commitizen](https://github.com/commitizen/cz-cli)
- [Commitlint](https://commitlint.js.org/)
- [Standard Version](https://github.com/conventional-changelog/standard-version)

## 📋 Next Steps

1. **Install dependencies**: `npm install`
2. **Install hooks**: `pre-commit install --hook-type commit-msg && pre-commit install`
3. **Test it**: `npm run commit` to create your first conventional commit
4. **Create first release**: Use GitHub Actions workflow or `npm run release`

## 🆘 Troubleshooting

### Commit Rejected
- Ensure format: `type(scope): subject`
- Check valid types: feat, fix, docs, etc.
- Check valid scopes: system, network, kiosk, etc.
- Subject must be lowercase and under 100 chars

### Release Failed
- Ensure all commits follow conventional format
- Check GitHub Actions logs for details
- Verify you have write permissions
- Try manual release locally to debug

### Pre-commit Not Running
```bash
# Reinstall hooks
pre-commit install --hook-type commit-msg
pre-commit install

# Test manually
pre-commit run --all-files
```

## ✅ Verification

To verify everything is working:

```bash
# 1. Check package.json
cat package.json | grep version

# 2. Try commitizen
npm run commit
# (then cancel with Ctrl+C)

# 3. Verify pre-commit hooks
pre-commit run --all-files

# 4. Check workflow files
ls -la .github/workflows/

# 5. Review docs
cat CONTRIBUTING.md
cat .github/COMMIT_CONVENTION.md
```

---

**Status:** ✅ Setup Complete

All conventional commits, changelog, and semantic versioning infrastructure is now in place and ready to use!
