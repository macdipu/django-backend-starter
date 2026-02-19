COMPOSE = docker compose -f docker/compose/local.yml

.PHONY: up down rebuild migrate shell logs test superuser clean

up:
	$(COMPOSE) up --build

down:
	$(COMPOSE) down

rebuild:
	$(COMPOSE) build --no-cache

migrate:
	$(COMPOSE) run --rm web python manage.py migrate

shell:
	$(COMPOSE) run --rm web python manage.py shell

logs:
	$(COMPOSE) logs -f

test:
	$(COMPOSE) run --rm web pytest

superuser:
	$(COMPOSE) run --rm web python manage.py createsuperuser

clean:
	$(COMPOSE) down -v
