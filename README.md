# hackathon-meteo
Anticiper, prévenir et gérer les risques naturels

![version](https://img.shields.io/badge/version-0.2.0-blue)
![python_version](https://img.shields.io/badge/python-3.12-blue)

![logo](https://cdn.discordapp.com/attachments/1225054185985278016/1227023200622215200/Fichier_3.png?ex=6626e568&is=66147068&hm=f882f5d2cbdcacc0d3d36c5168496e8c5515b95a08da4b160f3602514013934f&)

## Getting started

### Requirements

- [Python 3.12](https://www.python.org/) or higher;
- [PostgreSQL 14](https://www.postgresql.org/) or higher.

### Install

Download this repository and unzip it on your computer. You should rename the folder `hackathon-meteo-main` in `hackathon-meteo`.

Or clone the repository directly on your computer:

```bash
git clone git@github.com:jlebunetel/hackathon-meteo.git
```

You need an accessible _PostgreSQL_ database before starting the application. You can use _Docker Compose_ to get one conveniently:

```bash
docker compose run
```

To start the demo application, please run:

```bash
make quickstart
```

Wait a bit for the application to build, then you can access it with your favorite internet browser to the following address: [http://127.0.0.1:8000](http://localhost:8000).

> :memo: The default superuser login and password are: `demo` / `demo`.

That's all!

### Install a development environment

Create a virtual environment (`make venv`) and install development dependencies in it (`make install-dev`).

Activate your virtual environment (`source venv/bin/activate` with _bash_ or `. venv/bin/activate.fish` with _fish shell_).

Run `pre-commit install` to install _pre-commit_ into your git hooks.

You can update your hooks to the latest version automatically by running `pre-commit autoupdate`.

If you want to manually run all _pre-commit_ hooks on a repository, run `pre-commit run --all-files`.

> :memo: A [Makefile](Makefile) provides helpfull commands to manage this very project. Run `make help` to list available commands.
>
## Tech/framework used

- [Django](https://www.djangoproject.com/): a Python-based free and open-source web framework;
- [Bulma](https://bulma.io/): the modern CSS framework that just works.

## Contributing

For the sake of simplicity, to ease interaction with the community, we use the [GitHub flow](https://guides.github.com/introduction/flow/index.html) for open-source projects. In a few words:
- The `main` branch is always stable and deployable;
- Tags from the `main` branch are considered as releases;
- Contributors have to fork or create a new feature-branch to work on (if they are allowed to in the original repository) and propose a pull request to merge their branch to `main`.

This project follows the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification. You can use `cz commit` to easily write commit messages.

If you'd like to contribute, please raise an issue or fork the repository and use a feature branch. Pull requests are warmly welcome!

## Versioning

We use [SemVer](http://semver.org/) for versioning. See the [CHANGELOG.md](CHANGELOG.md) file for details.

## Licensing

The code in this project is licensed under MIT license. See the [LICENSE](LICENSE) file for details.

## Contributors

- __Benjamin Lion__ - [k4r4c](https://github.com/k4r4c)
- __Julien Lebunetel__ - [jlebunetel](https://github.com/jlebunetel)
- __Philippe Hermant__ - [phgot](https://github.com/phgot)
- __Pierre-Edouard Chaix__ - [pierreedouardchaix](https://github.com/pierreedouardchaix)
- __Thanh Huy Le__ - [Geksmode](https://github.com/Geksmode)
