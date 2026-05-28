.PHONY: api-run api-test api-lint db-up db-down db-logs db-psql web-run web-build

api-run:
	cd apps/api && uv run uvicorn app.main:app --reload --port 8000

api-test:
	cd apps/api && uv run pytest

api-lint:
	cd apps/api && uv run ruff check .

db-up:
	docker compose up -d

db-down:
	docker compose down

db-logs:
	docker compose logs -f db

db-psql:
	docker compose exec db psql -U dev -d travel

web-run:
	cd apps/web && npm run dev

web-build:
	cd apps/web && npm run build