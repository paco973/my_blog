ifneq (,$(wildcard ./.env))
include .env
export
ENV_FILE_PARAM = --env-file .env

endif

# Les services sont construits une fois, puis étiquetés, par défaut en tant que project_service.
build:
	docker-compose up --build -d --remove-orphans

# Construit, (re)crée, démarre et s'attache à des conteneurs pour un service.
up:
	docker-compose up -d

# Arrête les conteneurs et supprime les conteneurs, les réseaux, les volumes et les images créés par up
down:
	docker-compose down

# Récupère par lots les journaux présents au moment de l'exécution.
show-logs:
	docker-compose logs
# Applique les migrations
migrate:
	docker-compose exec web_app python manage.py migrate

# Crée des migrations
makemigrations:
	docker-compose exec web_app python manage.py makemigrations
#Crée un super user
superuser:
	docker-compose exec web_app python manage.py createsuperuser

#collecte les fichiers statiques de chacune de vos applications (et de tout autre endroit que vous spécifiez) dans un emplacement unique qui peut facilement être servi en production.
collectstatic:
	docker-compose exec web_app python manage.py collectstatic --no-input --clear

down-v:
	docker-compose down -v

volume:
	docker volume inspect logistics_postgres_data

hexa-db:
	docker compose exec postgres-db psql --username=paco --dbname=logistics

test:
	docker compose exec web_app pytest -p no:warnings --cov=.

test-html:
	docker compose exec web_app pytest -p no:warnings --cov=. --cov-report html

flake8:
	docker compose exec web_app flake8 .

black-check:
	docker compose exec web_app black --check --exclude=migrations .

black-diff:
	docker compose exec web_app black --diff --exclude=migrations .

black:
	docker compose exec web_app black --exclude=migrations .

isort-check:
	docker compose exec web_app isort . --check-only --skip env --skip migrations

isort-diff:
	docker compose exec web_app isort . --diff --skip env --skip migrations

isort:
	docker compose exec web_app isort . --skip env --skip migrations

.PHONY: help

# help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'