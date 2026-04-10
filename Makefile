.PHONY: test lint format watch build publish

test:
	uv run pytest .

lint:
	uv run ruff check .
	uv run ty check .

format:
	uv run ruff format .

watch:
	uv run uvicorn snek_case.main:app --reload

build:
	uv build

publish:
	uv publish
