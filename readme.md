# Pre-commit Hooks Setup

This repository uses pre-commit hooks to ensure code quality and consistency. The hooks include:

- Code formatting (Black, isort)
- Linting (Flake8, Pylint)
- YAML validation
- Dockerfile linting (Hadolint)
- File checks (size, merge conflicts, etc.)
- Security checks (detect-private-key, safety, git-secrets)
- Jupyter notebook output cleaning
- Commit message formatting

## Installation

1. Install pre-commit:
```bash
pip install pre-commit commitizen
```

2. Install git-secrets:
```bash
# For Windows (requires Git Bash or similar)
git clone https://github.com/awslabs/git-secrets.git
cd git-secrets
make install
```

3. Install the git hook scripts:
```bash
pre-commit install
pre-commit install --hook-type commit-msg  # Enable commit message hooks
git secrets --install
git secrets --register-aws  # Register AWS patterns
```

4. (Optional) Run against all files:
```bash
pre-commit run --all-files
```

## Hook Details

- **black**: Python code formatter (128 char line length, 4 space indent, 3-line multi-line)
- **isort**: Python import sorter (Black-compatible, 4 space indent)
- **flake8**: Python linter with additional plugins (max complexity: 3)
- **pylint**: Python code analysis (max branches: 3)
- **hadolint**: Dockerfile linter
- **check-yaml**: YAML file validator
- **check-added-large-files**: Prevents large files (>2MB)
- **detect-private-key**: Prevents committing private keys
- **python-safety**: Checks for known security vulnerabilities
- **nbstripout**: Clears Jupyter notebook outputs
- **git-secrets**: Scans for sensitive information (AWS keys, passwords, etc.)
- **commitizen**: Enforces conventional commit message format
- **gitlint**: Additional commit message linting

## Configuration

The hooks are configured in `.pre-commit-config.yaml`. You can modify the settings or disable specific hooks by editing this file.

### Code Style Settings
- Line Length: 128 characters
- Indentation: 4 spaces
- Multi-line Expressions: 3 lines maximum
- Complexity: Maximum of 3 (branches/complexity)

### Security Scanning
Git-secrets will scan for:
- AWS access keys
- Private keys
- Common password patterns
- Other sensitive information

To add custom patterns:
```bash
git secrets --add 'pattern'
```

### Commit Message Format
Commits must follow the Conventional Commits format:
```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

Types:
- feat: New feature
- fix: Bug fix
- docs: Documentation changes
- style: Code style changes (formatting, etc.)
- refactor: Code refactoring
- test: Adding tests
- chore: Maintenance tasks

Example:
```
feat(auth): add user authentication system

- Implement JWT token generation
- Add login/logout endpoints
- Set up user session management
```
