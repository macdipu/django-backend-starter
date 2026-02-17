.PHONY: up down migrate shell logs test

up:
	docker compose -f docker/compose/local.yml up --build

down:
	docker compose -f docker/compose/local.yml down

migrate:
	docker compose -f docker/compose/local.yml exec web python manage.py migrate

shell:
	docker compose -f docker/compose/local.yml exec web python manage.py shell

logs:
	docker compose -f docker/compose/local.yml logs -f

test:
	docker compose -f docker/compose/local.yml exec web pytest
