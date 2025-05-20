# FastAPI Microservice Template

A modern, production-ready template for building microservices with FastAPI.

## Features

- 🚀 FastAPI framework with modern Python features
- 📝 Pydantic for data validation and settings management
- 🧪 Comprehensive test suite with pytest
- 🔍 Code quality tools (black, isort, mypy, flake8)
- 🔄 Pre-commit hooks for code quality
- 🐳 Docker support
- 🔐 Environment-based configuration
- 📚 API documentation with Swagger UI

## Prerequisites

- Python 3.10+
- Git
- Docker (optional)

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/dmsierra11/fantasy-fastapi-template.git
   cd fantasy-fastapi-template
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up pre-commit hooks:
   ```bash
   pip install pre-commit
   pre-commit install
   ```

5. Run the development server:
   ```bash
   uvicorn main:app --reload
   ```

The API will be available at http://localhost:8000

## API Documentation

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Development

### Setup

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install dependencies and pre-commit hooks:
   ```bash
   make install
   ```

### Development Workflow

1. Format code:
   ```bash
   make format
   ```

2. Run linters:
   ```bash
   make lint
   ```

3. Run tests:
   ```bash
   make test
   ```

4. Clean up:
   ```bash
   make clean
   ```

### Code Style

This project follows strict code style guidelines:

- Line length: 88 characters (Black's default)
- Type hints: Required for all functions and methods
- Docstrings: Required for all modules, classes, and functions
- Imports: Sorted using isort with Black profile
- Formatting: Black for code formatting
- Linting: Flake8 with docstring checks
- Type checking: MyPy with strict settings

The pre-commit hooks will automatically enforce these guidelines on each commit.

### Best Practices

1. Always run `make format` before committing to ensure consistent code style
2. Write tests for new features and bug fixes
3. Keep docstrings up to date
4. Use type hints consistently
5. Run `make lint` to catch issues before committing

### Running Tests

```bash
pytest
```

### Code Quality

The project uses several tools to maintain code quality:

- **black** (>=23.10.1): Code formatting
- **isort** (>=5.12.0): Import sorting
- **mypy** (>=1.6.1): Static type checking
- **flake8** (>=6.1.0): Python linter

Run all checks:

```bash
pre-commit run --all-files
```

### Project Configuration

The project uses `pyproject.toml` for configuration of various tools:
- Black formatting settings
- isort import sorting
- MyPy type checking
- pytest configuration

### Docker Support

Build the Docker image locally:

```bash
docker build -t fastapi-microservice .
```

Run the container from the local image:

```bash
docker run -p 8000:8000 fastapi-microservice
```

Or, run the container directly from DockerHub (replace `yourusername` with your DockerHub username):

```bash
docker run -p 8000:8000 yourusername/fastapi-microservice
```

> **Note:** Replace `yourusername` with your DockerHub username if you want to pull the image from DockerHub.

## Project Structure

```
fantasy-fastapi-template/
├── app/
│   ├── routers/         # API routes
│   │   └── example_router.py
│   ├── services/        # Business logic
│   │   └── example_service.py
│   └── __init__.py
├── tests/
│   ├── routers/         # Route tests
│   │   └── test_example_router.py
│   ├── services/        # Service tests
│   │   └── test_example_service.py
│   └── __init__.py
├── .github/
│   └── workflows/       # GitHub Actions workflows
│       └── ci.yml
├── .pre-commit-config.yaml
├── Dockerfile
├── main.py             # Application entry point
├── pyproject.toml      # Project configuration
└── requirements.txt    # Project dependencies
```

## Dependencies

Key dependencies and their minimum versions:
- FastAPI >= 0.104.0
- Uvicorn >= 0.24.0
- Pydantic >= 2.4.2
- Pydantic-settings >= 2.0.3
- Python-dotenv >= 1.0.0
- Pytest >= 7.4.3
- HTTPX >= 0.25.0

For a complete list of dependencies, see `requirements.txt`.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
