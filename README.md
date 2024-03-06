# Project Template

This is a template repository that can be cloned to easily create new projects from a good starting basis. It includes best practices that I have learned, including

- dependency management via `poetry`
- pre-commit hooks such as `black`, `flake8`, `mypy`
- semantic versioning & changelog releases via `commitizen`
- documenation via `mkdocs`
- a proper project structure / skeleton

if cloned, delete the changelog.md, and reset the versions back to 0.1.0 in pyproject.toml and `src/app/__init__.py`

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

Restart your shell and install the appropriate version of python:

```
pyenv install <.python-version
```

Install poetry

```
curl -sSL https://install.python-poetry.org | python3 -
```

confirm it has worked

```
poetry --version
```

install dependencies via

```
poetry install
```

install pre-commit hooks via

```
pre-commit install
```

the documentation can be run locally via

```
mkdocs serve
```

but is also hosted via GitHub pages through the `.github/workflows/ci.yaml`
Has to be initialized in the repo settings > pages > Build and deployment

> Source > Deploy from a branch
> Branch > gh-pages > / (root) > Save

# Roadmap

- proper README
- mkdocstrings to automatically populate the documentation
- logging via https://engineeringfordatascience.com/posts/python_logging/
- maybe: https://github.com/folke/devmoji
- maybe: proper CICD
- maybe: releases?
