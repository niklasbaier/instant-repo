# Project Template

This is a template repository that can be cloned/forked to easily create new projects from a good starting basis. It includes best practices that I have learned, including

- dependency management via `poetry`
- pre-commit hooks for formatters & linters via `ruff` and `mypy`
- semantic versioning & changelog releases via `commitizen`
- automatic documenation via `mkdocs` following the [Diátaxis documentation framework](https://diataxis.fr/) best practices
- a proper project structure / skeleton

If cloned/forked, delete the `CHANGELOG.md`, and reset the `[tool.poetry]/version` and `[tool.commitizen]/version` back to `0.1.0` in the `pyproject.toml`, as well as in and `src/app/__init__.py`.

## Installation

Install pyenv:

```
brew install pyenv
```

Set your shell environment for pyenv:

```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

Restart your shell and install the appropriate version of Python (set it before in the `.pythion-version` file:

```
pyenv install <.python-version
```

Install `poetry`:

```
curl -sSL https://install.python-poetry.org | python3 -
```

Confirm it has worked:

```
poetry --version
```

Install project dependencies from the `pyproject.toml` via:

```
poetry install
```

Install pre-commit hooks from the `.pre-commit-config.yaml` via:

```
pre-commit install
```

Run the documentation locally via:

```
mkdocs serve
```

The documentation is also hosted via GitHub pages through the `.github/workflows/ci.yaml`. This has to be initialized in the repo settings > pages > Build and deployment > Source > Deploy from a branch, > Branch > gh-pages > / (root) > Save

## Roadmap

- proper README
- logging via https://engineeringfordatascience.com/posts/python_logging/
- maybe: https://github.com/folke/devmoji
- maybe: proper CICD
- maybe: releases?
