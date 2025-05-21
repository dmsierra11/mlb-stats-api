# MLB Stats API

A modern, production-ready API for fetching MLB statistics and player information.

## Features

- 🚀 FastAPI framework with modern Python features
- 📊 Comprehensive MLB statistics and player data
- 🔍 Player search functionality
- 📈 Detailed player statistics (hitting, pitching, fielding)
- 👥 Team information and rosters
- 📝 Pydantic for data validation and settings management
- 🧪 Comprehensive test suite with pytest and coverage reporting
- 🔍 Code quality tools (black, isort, mypy, flake8)
- 🔄 Pre-commit hooks for code quality
- 🐳 Docker support
- 🔐 Environment-based configuration
- 📚 API documentation with Swagger UI
- 📊 Test coverage reporting with pytest-cov

## API Endpoints

### Players

- `GET /api/v1/mlb/players/search` - Search for players by name
- `GET /api/v1/mlb/players/{player_id}` - Get player information
- `GET /api/v1/mlb/players/{player_id}/stats` - Get player statistics
  - Query parameters:
    - `season`: The season year (e.g., 2024)
    - `stats_type`: Type of stats (season, career)
    - `group`: Stats group (hitting, pitching, fielding)

### Teams

- `GET /api/v1/mlb/teams` - Get all MLB teams
- `GET /api/v1/mlb/teams/{team_id}` - Get team information (team_id must be a numeric ID, not a team abbreviation)
- `GET /api/v1/mlb/teams/{team_id}/roster` - Get team roster (team_id must be a numeric ID, not a team abbreviation)

## Prerequisites

- Python 3.10+
- Git
- Docker (optional)

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/dmsierra11/mlb-stats-api.git
   cd mlb-stats-api
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

## Running the Project

### Local Development

1. Make sure you have all prerequisites installed and the virtual environment activated:

   ```bash
   # Activate virtual environment if not already activated
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Start the development server:

   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

3. Access the API:
   - API Base URL: http://localhost:8000
   - Interactive API Documentation: http://localhost:8000/docs
   - Alternative API Documentation: http://localhost:8000/redoc

### Using Docker

1. Build the Docker image:

   ```bash
   docker build -t mlb-stats-api .
   ```

2. Run the container:

   ```bash
   docker run -p 8000:8000 mlb-stats-api
   ```

3. Access the API using the same URLs as local development.

### Environment Variables

The following environment variables can be configured (create a `.env` file in the project root):

```env
# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=True

# Add other environment variables as needed
```

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

3. Run tests with coverage:

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
- Test coverage: Maintained with pytest-cov

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
docker build -t mlb-stats-api .
```

Run the container from the local image:

```bash
docker run -p 8000:8000 mlb-stats-api
```

## Project Structure

```
mlb-stats-api/
├── app/
│   ├── routers/         # API routes
│   │   └── mlb_router.py
│   ├── services/        # Business logic
│   │   └── mlb_service.py
│   ├── models/         # Data models
│   │   └── mlb_models.py
│   ├── main.py         # App initialization
│   └── __init__.py
├── tests/
│   ├── routers/         # Route tests
│   │   └── test_mlb_router.py
│   ├── services/        # Service tests
│   │   └── test_mlb_service.py
│   └── __init__.py
├── .github/
│   └── workflows/       # GitHub Actions workflows
│       └── ci.yml
├── .mypy_cache/        # MyPy type checking cache
├── .pytest_cache/      # Pytest cache directory
├── .venv/              # Python virtual environment
├── .coverage           # Test coverage data
├── .gitignore         # Git ignore rules
├── .pre-commit-config.yaml
├── Dockerfile
├── Makefile           # Development commands
├── main.py            # Application entry point
├── pyproject.toml     # Project configuration
└── requirements.txt   # Project dependencies
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
- Requests >= 2.31.0
- Pytest-cov >= 4.1.0
- Black >= 23.10.1
- isort >= 5.12.0
- mypy >= 1.6.1
- flake8 >= 6.1.0
- pre-commit >= 3.5.0

For a complete list of dependencies, see `requirements.txt`.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
