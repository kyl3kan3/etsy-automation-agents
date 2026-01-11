# Testing Guide for ArtFlow

## Overview

This guide covers the complete testing strategy for the ArtFlow project, including unit tests, integration tests, and CI/CD testing.

## Quick Start

### Installation

```bash
# Install test dependencies
pip install pytest pytest-cov pytest-mock pytest-xdist

# Run tests with coverage
pytest --cov=agents --cov=src -v

# Run with coverage report
pytest --cov=agents --cov=src --cov-report=html
```

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_api.py

# Run specific test class
pytest tests/test_api.py::TestDashboardEndpoints

# Run specific test
pytest tests/test_api.py::TestDashboardEndpoints::test_get_dashboard_data

# Run with markers
pytest -m unit   # Only unit tests
pytest -m api    # Only API tests

# Run in parallel (faster)
pytest -n auto   # Use all CPU cores
```

## Test Structure

```
tests/
├── test_api.py          # API endpoint tests
├── test_agents.py       # Agent tests (to be created)
├── test_integration.py  # Integration tests (to be created)
└── conftest.py          # Pytest fixtures and configuration
```

## Test Categories

### Unit Tests
Test individual functions and classes in isolation with mocked dependencies.

**Location:** `tests/test_api.py`

**Run Unit Tests:**
```bash
pytest -m unit
```

**Example:**
```python
def test_create_listing(client, sample_listing):
    response = client.post('/api/listings',
                          data=json.dumps(sample_listing),
                          content_type='application/json')
    assert response.status_code in [201, 200]
```

### Integration Tests
Test interactions between multiple components (database, API, external services).

**Location:** `tests/test_integration.py` (to be created)

**Run Integration Tests:**
```bash
pytest -m integration
```

### API Tests
Test all Flask API endpoints for correct behavior and error handling.

**Location:** `tests/test_api.py`

**Run API Tests:**
```bash
pytest -m api
```

## Coverage

### Viewing Coverage Reports

**Terminal Report:**
```bash
pytest --cov=agents --cov=src --cov-report=term-missing
```

**HTML Report:**
```bash
pytest --cov=agents --cov=src --cov-report=html
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
start htmlcov/index.html  # Windows
```

### Coverage Goals
- Overall: 80%+ code coverage
- - Critical paths: 90%+ coverage
  - - Utils: 70%+ coverage (less critical)
   
    - ## Fixtures
   
    - ### Available Fixtures
   
    - **client**: Flask test client
    - ```python
      def test_endpoint(client):
          response = client.get('/api/endpoint')
      ```

      **sample_artwork**: Sample artwork data
      ```python
      def test_create_artwork(client, sample_artwork):
          # Use sample_artwork fixture
      ```

      **sample_listing**: Sample listing data
      ```python
      def test_create_listing(client, sample_listing):
          # Use sample_listing fixture
      ```

      ## Mocking

      ### Mocking External Services

      ```python
      from unittest.mock import patch, MagicMock

      @patch('agents.art_generator.generate_artworks')
      def test_generate_artworks(mock_generate, client):
          mock_generate.return_value = [sample_artwork]
          # Test with mocked external service
      ```

      ### Mocking Database

      ```python
      @patch('models.Artwork.query')
      def test_artwork_query(mock_query):
          mock_query.filter_by.return_value.first.return_value = artwork
          # Test with mocked database
      ```

      ## Markers

      Custom pytest markers for organizing tests:

      ```bash
      # Run only unit tests
      pytest -m unit

      # Run only API tests
      pytest -m api

      # Run only integration tests
      pytest -m integration

      # Run only slow tests
      pytest -m slow

      # Run everything except slow tests
      pytest -m "not slow"
      ```

      ## Test Examples

      ### Testing API Endpoints

      ```python
      class TestListingEndpoints:
          def test_create_listing(self, client, sample_listing):
              response = client.post('/api/listings',
                                    data=json.dumps(sample_listing),
                                    content_type='application/json')
              assert response.status_code in [201, 200]
              data = json.loads(response.data)
              assert data.get('title') == sample_listing['title']

          def test_get_listings(self, client):
              response = client.get('/api/listings')
              assert response.status_code == 200
              data = json.loads(response.data)
              assert isinstance(data, list)
      ```

      ### Testing Error Handling

      ```python
      class TestErrorHandling:
          def test_invalid_json(self, client):
              response = client.post('/api/listings',
                                    data='invalid json',
                                    content_type='application/json')
              assert response.status_code in [400, 415]

          def test_not_found(self, client):
              response = client.get('/api/nonexistent/123')
              assert response.status_code == 404
      ```

      ## CI/CD Testing

      Tests run automatically on every push via GitHub Actions:

      ```bash
      # Runs in .github/workflows/deploy.yml
      pytest --cov=agents --cov=src --cov-report=xml
      ```

      ### Coverage Report Upload
      Coverage is automatically uploaded to Codecov for tracking over time.

      ## Performance Testing

      ### Running Performance Tests

      ```bash
      # Time test execution
      pytest --durations=10 --durations-min=1.0

      # Profile with pytest-profile
      pytest --profile

      # Memory profiling
      pip install pytest-memprof
      pytest --memprof
      ```

      ### Load Testing

      Use **locust** for load testing:

      ```bash
      # Install locust
      pip install locust

      # Create locustfile.py
      # Run load tests
      locust -f locustfile.py --host=http://localhost:5000
      ```

      **Example locustfile.py:**
      ```python
      from locust import HttpUser, task, between

      class APIUser(HttpUser):
          wait_time = between(1, 3)

          @task
          def list_artworks(self):
              self.client.get("/api/artworks")

          @task(3)
          def create_listing(self):
              self.client.post("/api/listings",
                  json={"title": "Test", "price": 29.99})
      ```

      ## Troubleshooting

      ### Common Issues

      **Tests fail with import errors:**
      ```bash
      # Make sure requirements are installed
      pip install -r requirements.txt

      # Add project to Python path
      export PYTHONPATH="${PYTHONPATH}:/path/to/etsy-automation-agents"
      ```

      **Database locked error:**
      ```bash
      # Use in-memory SQLite for testing
      app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
      ```

      **Mocking not working:**
      ```python
      # Patch where it's used, not where it's defined
      @patch('app.external_service.call')  # Wrong
      @patch('module.using.external_service')  # Correct
      ```

      ## Best Practices

      1. **Test Isolation:** Each test should be independent
      2. 2. **Clear Names:** Test names should describe what they test
         3. 3. **Arrange-Act-Assert:** Organize tests with setup, action, verification
            4. 4. **Mock External:** Mock API calls, databases, external services
               5. 5. **Cover Edge Cases:** Test success, failure, and edge cases
                  6. 6. **Keep Tests Fast:** Mock slow operations, use in-memory databases
                     7. 7. **Document Fixtures:** Explain what each fixture provides
                        8. 8. **Review Coverage:** Aim for 80%+ code coverage
                          
                           9. ## Resources
                          
                           10. - **Pytest Documentation:** https://docs.pytest.org/
                               - - **Coverage Documentation:** https://coverage.readthedocs.io/
                                 - - **Mocking Guide:** https://docs.python.org/3/library/unittest.mock.html
                                   - - **Flask Testing:** https://flask.palletsprojects.com/testing/
                                    
                                     - ## Adding More Tests
                                    
                                     - ### Template for New Test File
                                    
                                     - ```python
                                       """
                                       Tests for [Module Name]
                                       """

                                       import pytest
                                       from unittest.mock import patch, MagicMock

                                       @pytest.fixture
                                       def sample_data():
                                           return {...}

                                       class TestModule:
                                           def test_function(self, sample_data):
                                               # Arrange
                                               # Act
                                               # Assert
                                               pass
                                       ```

                                       ---

                                       **Last Updated:** January 11, 2026
                                       **Version:** 1.0.0
