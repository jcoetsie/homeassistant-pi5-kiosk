# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

### 1.0.1 (2025-11-12)


### 📚 Documentation

* Add branch protection information to documentation ([#1](https://github.com/jcoetsie/homeassistant-pi5-kiosk/issues/1)) ([34e3403](https://github.com/jcoetsie/homeassistant-pi5-kiosk/commit/34e34033d2c363d9e577c672444e85d76a6e6f87))


### 🐛 Bug Fixes

* **ci:** Add security-events write permission for CodeQL SARIF upload ([5ef322c](https://github.com/jcoetsie/homeassistant-pi5-kiosk/commit/5ef322cd0b7658fe3d121a9045fdafc0061c73b8))
* **ci:** Remove npm cache requirement from release workflow ([241b232](https://github.com/jcoetsie/homeassistant-pi5-kiosk/commit/241b232e3813e4bd25a1c0e5d75deebd1ddbcdfe))
* **ci:** Resolve ansible-lint yamllint config and variable naming issues ([192a9f2](https://github.com/jcoetsie/homeassistant-pi5-kiosk/commit/192a9f210aac202b3a660c204f6b8388e41ebb45))
* **ci:** Resolve pre-commit hook issues with ansible-lint and shellcheck ([293343f](https://github.com/jcoetsie/homeassistant-pi5-kiosk/commit/293343fd7f001989f0d4a82b3626e52b3d630f08))
* **ci:** Update release workflow to work with protected main branch ([#2](https://github.com/jcoetsie/homeassistant-pi5-kiosk/issues/2)) ([f20e1ff](https://github.com/jcoetsie/homeassistant-pi5-kiosk/commit/f20e1ff8ed91c067b8c0eca0f836e5fec3dd49c1))

## [1.0.0] - 2025-11-11

### ✨ Features

- **kiosk**: Full-screen kiosk mode with Chromium browser
- **kiosk**: Multi-touch gestures support (swipe, pinch-to-zoom)
- **keyboard**: On-screen keyboard with configurable layout (Belgian French AZERTY default)
- **keyboard**: Floating keyboard button for easy access
- **network**: Ethernet and WiFi failover configuration
- **vnc**: Remote VNC access on port 5900
- **logs**: Log rotation for kiosk and system logs
- **logs**: Journald log size management
- **github-runner**: Self-hosted GitHub Actions runner
- **ci**: Comprehensive CI pipeline with linting and security checks
- **ci**: Automated weekly maintenance workflow

### 📚 Documentation

- **docs**: Complete hardware documentation for ILITEK touchscreen
- **docs**: Comprehensive README with setup instructions
- **docs**: Ansible role structure documentation
- **docs**: CI/CD pipeline documentation

### ♻️ Code Refactoring

- **system**: Split monolithic playbook into 8 modular roles
- **ci**: Modular role-based Ansible structure

### 👷 CI/CD

- **ci**: Added ansible-lint, yamllint, markdownlint checks
- **ci**: Added shellcheck for shell script validation
- **ci**: Added Trivy security scanning
- **ci**: Added gitleaks secret detection
- **ci**: Pre-commit hooks for local development

[1.0.0]: https://github.com/jcoetsie/homeassistant-pi5-kiosk/releases/tag/v1.0.0
