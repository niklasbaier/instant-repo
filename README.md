# project-template

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
poetry install
```

the documentation can be run via

```
mkdocs serve
```

can be hosted on GitHub pages via GitHub actions
repo settings > pages > Build and deployment

> Source > Deploy from a branch
> Branch > gh-pages > / (root) > Save

# upcoming (maybe)

- https://engineeringfordatascience.com/posts/python_logging/
- https://github.com/folke/devmoji
- proper CICD
