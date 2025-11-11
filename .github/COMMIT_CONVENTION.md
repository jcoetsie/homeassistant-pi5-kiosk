# Conventional Commits Quick Reference

## Commit Format

```
<type>(<scope>): <subject>
```

## Types

| Type | Description | Version Bump | Changelog Section |
|------|-------------|--------------|-------------------|
| `feat` | New feature | Minor (0.X.0) | ✨ Features |
| `fix` | Bug fix | Patch (0.0.X) | 🐛 Bug Fixes |
| `perf` | Performance improvement | Patch | ⚡ Performance |
| `refactor` | Code refactoring | - | ♻️ Refactoring |
| `docs` | Documentation only | - | 📚 Documentation |
| `style` | Code style/formatting | - | Hidden |
| `test` | Tests only | - | Hidden |
| `build` | Build system changes | - | 📦 Build |
| `ci` | CI/CD changes | - | 👷 CI/CD |
| `chore` | Other changes | - | Hidden |
| `revert` | Revert previous commit | - | - |

## Scopes

| Scope | Description |
|-------|-------------|
| `system` | User creation, SSH, system updates |
| `network` | Ethernet, WiFi, locale configuration |
| `packages` | Package installation and management |
| `vnc` | VNC server configuration |
| `kiosk` | Browser and kiosk mode setup |
| `keyboard` | Keyboard layout and on-screen keyboard |
| `logs` | Log rotation and management |
| `github-runner` | GitHub Actions runner |
| `ci` | CI/CD pipeline |
| `docs` | Documentation |
| `deps` | Dependency updates |

## Examples

### Adding a Feature
```bash
git commit -m "feat(keyboard): Add German keyboard layout"
```

### Fixing a Bug
```bash
git commit -m "fix(vnc): Resolve authentication timeout"
```

### Breaking Change
```bash
git commit -m "feat(kiosk)!: Change default browser to Firefox

BREAKING CHANGE: Chromium is no longer the default browser."
```

### Documentation
```bash
git commit -m "docs(readme): Update installation instructions"
```

### CI/CD
```bash
git commit -m "ci(github): Add security scanning workflow"
```

### Dependency Update
```bash
git commit -m "chore(deps): Update ansible-lint to v24.3.0"
```

## Using Commitizen

```bash
# Interactive commit creation
npm run commit
```

## Rules

✅ **Do:**
- Use present tense ("Add feature" not "Added feature")
- Start with lowercase after colon
- Keep subject under 100 characters
- Use body for detailed explanation
- Reference issues with "Fixes #123"

❌ **Don't:**
- End subject with period
- Use past tense
- Make vague commits ("updated stuff")
- Skip scope when relevant
- Forget breaking change notation

## Release Versions

```
1.0.0
│ │ │
│ │ └─ Patch - fix:
│ └─── Minor - feat:
└───── Major - BREAKING CHANGE: or !
```

## Quick Commands

```bash
# Create commit with Commitizen
npm run commit

# Create release
npm run release

# Install hooks
pre-commit install --hook-type commit-msg
```

## Resources

- [Conventional Commits](https://www.conventionalcommits.org/)
- [Semantic Versioning](https://semver.org/)
- Full guide: [CONTRIBUTING.md](CONTRIBUTING.md)
