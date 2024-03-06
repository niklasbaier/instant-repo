# project-template

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

ideas

- CICD
