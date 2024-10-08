.PHONY: install
install:
	poetry install

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: boot
boot:
	poetry run python -m web.core.scripts.boot

.PHONY: reboot
reboot:
	poetry run python -m web.core.scripts.boot --clean

.PHONY: test
test:
	poetry run pytest -v -rs -n auto --show-capture=no

.PHONY: migrate
migrate:
	poetry run python -m web.core.manage migrate

.PHONY: migrations
migrations:
	poetry run python -m web.core.manage makemigrations

.PHONY: runserver
runserver:
	poetry run python -m web.core.manage runserver

.PHONY: superuser
superuser:
	poetry run python -m web.core.manage createsuperuser

.PHONY: dev-db
dev-db:
	poetry run python -m web.core.scripts.boot
	docker compose -f web/docker-compose.dev.yml up --force-recreate db

.PHONY: update
update: install migrate install-pre-commit ;
