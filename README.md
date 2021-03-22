# Survey

A basic survey engine for Django developers.

## Prérequis

- GNU Make
- Docker
- Docker compose
- Python 3.9

## Démarrer le projet

To install the project along with its dependencies, we will create a python
virtual environment, a dot env configuration file, start the database and apply
current migrations:

```bash
$ make bootstrap
```

Now create a super user using the following command:

```bash
$ make superuser
```

And voilà.

## Licence

This project is released under the MIT License, See the bundled
[`LICENSE`](./LICENSE) file for details..
