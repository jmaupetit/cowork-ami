# Co-working Mond'Arverne communauté

Ce projet vise à gérer un appel à manifestation d'intérêt pour la création d'un
espace de co-working localisé dans la communauté de commune Mond'Arverne (Puy
de Dôme, France).

## Prérequis

- GNU Make
- Docker
- Docker compose
- Python 3.9

## Démarrer le projet

Pour installer le projet et ses dépendances de développement, nous allons créer
un environnement virtuel python, une configuration de l'environnement de
l'application, démarrer la base de données et appliquer les migrations
courantes :

```bash
$ make bootstrap
```

Pour créer un utilisateur d'administration, lancer :

```bash
$ make superuser
```

And voilà.

## Licence

Ce projet est sous licence MIT, voir le fichier [`LICENSE`](./LICENSE) du
projet.
