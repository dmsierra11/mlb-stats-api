.PHONY: install format lint test clean run

install:
	pip install -r requirements.txt
	pre-commit install

format:
	black --line-length 88 .
	isort --profile black --line-length 88 .

lint:
	flake8 --max-line-length 88 --extend-ignore=E203 .
	mypy .

test:
	pytest

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type d -name ".pytest_cache" -exec rm -r {} +
	find . -type d -name ".mypy_cache" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -r {} +
	find . -type d -name "*.egg" -exec rm -r {} +
	find . -type d -name ".coverage" -exec rm -r {} +
	find . -type d -name "htmlcov" -exec rm -r {} +
	find . -type d -name "dist" -exec rm -r {} +
	find . -type d -name "build" -exec rm -r {} +

run:
	. .venv/bin/activate && uvicorn main:app --reload --host 0.0.0.0 --port 8000
