# Pre-commit Hooks Setup

This repository uses pre-commit hooks to ensure code quality and consistency. The hooks include:

- Code formatting (Black, isort)
- Linting (Flake8, Pylint)
- YAML validation
- Dockerfile linting (Hadolint)
- File checks (size, merge conflicts, etc.)
- Security checks (detect-private-key, safety)

## Installation

1. Install pre-commit:
```bash
pip install pre-commit
```

2. Install the git hook scripts:
```bash
pre-commit install
```

3. (Optional) Run against all files:
```bash
pre-commit run --all-files
```

## Hook Details

- **black**: Python code formatter
- **isort**: Python import sorter
- **flake8**: Python linter with additional plugins
- **pylint**: Python code analysis
- **hadolint**: Dockerfile linter
- **check-yaml**: YAML file validator
- **check-added-large-files**: Prevents large files (>500KB)
- **detect-private-key**: Prevents committing private keys
- **python-safety**: Checks for known security vulnerabilities

## Configuration

The hooks are configured in `.pre-commit-config.yaml`. You can modify the settings or disable specific hooks by editing this file.
