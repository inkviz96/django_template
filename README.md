# Template Django Project

- [Getting Started](#getting-started)
- [Project Features](#project-features)
    - [Project technologies](#project-technologies)
    - [Project structure](#project-structure)
    - [Makefile](#makefile)
    - [Pre Commit](#pre-commit)


## Getting Started
After clone or init git repo you need to call init command.
```
make init
```
This command will:
 - create ```.env``` and ```config.yaml``` files based on the example file.
 - install pre-commit and init hooks.

The next step is to set the missing environment variables in the ```.env``` and ```config.yaml``` files.

After that you can build and setup the project.
```
make up_build       # parallel build and up all services
make_migrations     # migrations
make migrate_all    # migrate
make build          # Parallel ONLY build all services
```

Run tests:
```
make test
```

## Project Features
### Project technologies
| Service | Description |
| --- | ----------- |
| Django | web app |
| PostgreSQL | main db |

### Project structure
```
src/
├── src/                         # django project
│   ├── logging_settings/
│   │   ├── logging_config.py    # logging config for unicorn and runserver
│   │
│   │
├── gunicorn.config.py           # gunicorn settings config
```

### Makefile
This project uses **Makefile**. List of make commands with description:
```
make help
```

### Pre-Commit
This project uses [pre-commit](https://pre-commit.com/). List of base linters:
- black
- flake8
- isort
