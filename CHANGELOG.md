# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
