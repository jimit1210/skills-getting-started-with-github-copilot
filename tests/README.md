# Tests

This directory contains backend tests for the FastAPI application.

## Structure

- `tests/conftest.py` — shared pytest fixtures:
  - `client` creates a `TestClient` for the FastAPI app
  - `reset_activities` restores the in-memory activity state before each test
- `tests/test_app.py` — endpoint tests for the application API
- `tests/utils.py` — helper functions for building API request URLs and sending requests

## Test style

Tests use the Arrange-Act-Assert (AAA) pattern:
- Arrange: set up the activity name, email, and any expected state
- Act: call the API through the shared `client` fixture
- Assert: verify the response status code and body, plus any state changes

## Running tests

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the full test suite:

```bash
pytest
```
