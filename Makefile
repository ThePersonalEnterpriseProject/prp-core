.PHONY: test-unit test-int test-e2e

test-unit:
	docker build --target test ./backend

test-int:
	docker compose run --rm -e TESTING=1 backend pytest tests/integration

test-e2e:
	docker build --target test ./frontend

screenshots:
	docker compose run --rm e2e
