ACTIVATE = source venv/bin/activate
MANAGE   = $(ACTIVATE) && cd src/cowork && python manage.py
PIP      = $(ACTIVATE) && pip

.env:
	cp src/cowork/.env.dist src/cowork/.env

bootstrap: \
	venv \
	install \
	.env \
	migrate
.PHONY: bootstrap

down:
	docker-compose down
.PHONY: down

install:
	$(PIP) install -e .[dev]
.PHONY: install

migrate: run-db
	$(MANAGE) migrate
.PHONY: migrate

run: run-db
	$(MANAGE) runserver
.PHONY: run

run-db:
	docker-compose up -d postgresql
	docker-compose run --rm dockerize -wait "tcp://postgresql:5432" -timeout 60s
.PHONY: run-db

status:
	docker-compose ps
.PHONY: status

stop:
	docker-compose stop
.PHONY: stop

superuser:
	$(MANAGE) createsuperuser
.PHONY: superuser

venv:
	python -m venv venv
