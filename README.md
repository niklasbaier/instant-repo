# Project Template

> Choose a self-explaining name for your project.

## Description

> Let people know what your project can do specifically.Provide context and add a link to any reference visitors might be unfamiliar with. A list of **Features** or a **Background** subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.>

This is a template repository that can be cloned/forked to easily create new projects from a good starting basis. It includes best practices that I have learned, including

- dependency management via [Poetry](https://python-poetry.org/docs/)
- pre-commit hooks for formatters & linters via [Ruff](https://docs.astral.sh/ruff/) and `mypy`
- [Semantic Versioning](https://semver.org/), [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) & automated [changelog](https://keepachangelog.com/en/1.1.0/) releases via `commitizen`
- automated documenation via `mkdocs` following the [Diátaxis documentation framework](https://diataxis.fr/) best practices
- a proper project structure / skeleton
- a proper README following <https://www.makeareadme.com/>
- proper logging for dev & prod environment, for terminal & into logfiles (/logs), following <https://engineeringfordatascience.com/posts/python_logging/>
- a proper CICD skeleton via GitHub Actions (<https://hackernoon.com/how-to-integrate-github-actions-and-cicd-with-your-next-python-project>)
- proper testing suite, also with codecov (free Teamscale alternative for personal use & OS!)

If cloned/forked, delete the `CHANGELOG.md`, and reset the `[tool.poetry]/version` and `[tool.commitizen]/version` back to `0.1.0` in the `pyproject.toml`, as well as in `src/app/__init__.py`.

## Badges

> On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use [Shields](https://shields.io/) to add some to your README. Many services also have instructions for adding a badge.

## Visuals

> Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like [ttygif](https://github.com/icholy/ttygif) can help, but check out [Asciinema](https://asciinema.org/) for a more sophisticated method.

## Installation

> Within a particular ecosystem, there may be a common way of installing things, such as using [Yarn](https://yarnpkg.com/), [NuGet](https://www.nuget.org/), or [Homebrew](https://brew.sh/). However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

This projects assumes a generic development setup on your machine, most notably:

- homebrew
- XCode development kit

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

Restart your shell and install the appropriate version of Python (set it before in the `.pythion-version` file):

```
pyenv install <.python-version
```

Install `pipx`:

```
brew install pipx
pipx ensurepath
sudo pipx ensurepath --global # optional to allow pipx actions in global scope
```

Install `poetry`:

```
POETRY_VERSION=$(cat .poetry-version)
pipx install "poetry==$POETRY_VERSION"
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
poetry run pre-commit install
```

or simply

```
pre-commit install
``
if in the poetry shell

Run the documentation locally via:

```

mkdocs serve

```

The documentation is also hosted via GitHub pages through the `.github/workflows/ci.yaml`. This has to be initialized in the repo settings > pages > Build and deployment > Source > Deploy from a branch, > Branch > gh-pages > / (root) > Save

## Usage

> Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support

> Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap

> If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing

> State if you are open to contributions and what your requirements are for accepting them.

> For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

> You can also document commands to [lint the code](https://stackoverflow.com/questions/8503559/what-is-linting) or [run tests](https://en.wikipedia.org/wiki/Test_automation). These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a [Selenium](https://www.selenium.dev/) server for testing in a browser.

## Authors and acknowledgment

> Show your appreciation to those who have contributed to the project.

## License

> For open source projects, say how it is [licensed](https://choosealicense.com/).

## Project status

> If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
```
