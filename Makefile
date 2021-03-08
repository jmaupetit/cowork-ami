ACTIVATE = source venv/bin/activate
MANAGE   = $(ACTIVATE) && cd src/survey && python manage.py
PIP      = $(ACTIVATE) && pip

.env:
	cp src/survey/.env.dist src/survey/.env

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
	$(PIP) install --upgrade pip
	$(PIP) install -e .[dev]
.PHONY: install

lint:
lint: \
  lint-isort \
  lint-black \
  lint-flake8 \
  lint-pylint \
  lint-bandit
.PHONY: lint

lint-black:
	@echo 'lint:black started…'
	$(ACTIVATE) && black src/survey
.PHONY: lint-black

lint-flake8:
	@echo 'lint:flake8 started…'
	$(ACTIVATE) && flake8 src/survey
.PHONY: lint-flake8

lint-isort:
	@echo 'lint:isort started…'
	$(ACTIVATE) && isort --atomic src/survey
.PHONY: lint-isort

lint-pylint:
	@echo 'lint:pylint started…'
	$(ACTIVATE) && pylint src/survey
.PHONY: lint-pylint

lint-bandit:
	@echo 'lint:bandit started…'
	$(ACTIVATE) && bandit -qr src/survey
.PHONY: lint-bandit

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

test: run-db
	$(ACTIVATE) && pytest
.PHONY: test

venv:
	python -m venv venv
