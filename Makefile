.PHONY: api-run api-test api-lint web-run web-build

api-run:
	cd apps/api && uv run uvicorn app.main:app --reload --port 8000

api-test:
	cd apps/api && uv run pytest

api-lint:
	cd apps/api && uv run ruff check .

web-run:
	cd apps/web && npm run dev

web-build:
	cd apps/web && npm run build