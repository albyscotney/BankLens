# Formatting tools
FORMATTERS = poetry run black . && poetry run isort .

# Format code
format:
	$(FORMATTERS)

# Check code formatting without making changes
check-format:
	poetry run black . --check && poetry run isort . --check

# Lint code with pylint
lint:
	poetry run pylint .

# Check formatting and linting together
quality:
	make check-format && make lint

# Run tests
test:
	poetry run pytest

# Install dependencies
install:
	poetry install