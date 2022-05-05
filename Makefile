compose_file := docker-compose.yaml
compose := docker-compose -f $(compose_file)

init: init-envs pre-commit
init-envs:	## Generate '.env' and 'config.yaml' files based on example files.
	cp env.example .env
	cp config.example.yaml config.yaml

pre-commit:	## Install and use pre-commit config.
	pip install pre-commit --upgrade
	pre-commit install

build: ## Parallel build all project services
	$(compose) build --parallel

up_db: ## Up with flag d only database
	$(compose) up -d db

up: ## Up with flag d all services
	$(compose) up -d

up_service: ## Up with flag d choices service
	$(compose) up -d $(service)

up_build: build ## Up and build all project services
	$(compose) up -d

up_service_build: build ## Up and build choices project service
	$(compose) up -d $(service)

down: ## Down all project services
	$(compose) down

make_migrations: ## Make migrations file for django project
	$(compose) exec web python manage.py makemigrations

migrate_all: ## Migrate all into to database
	$(compose) exec web python manage.py migrate

shell: ## Launch shell plus
	$(compose) exec web python manage.py shell_plus

ps: ## Display all images information
	$(compose) ps -s -a $(service)

logs: ## Display all logs for choices project service
	$(compose) logs --timestamps -f $(service)

test: ## Run tests for all project or for choices tag
	$(compose) exec web python manage.py test --verbosity=3 --exclude-tag=skip --force-color --tag=$(tag)

help: ## Help description for all make commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'