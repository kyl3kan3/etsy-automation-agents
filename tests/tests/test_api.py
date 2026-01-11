"""
Unit tests for ArtFlow API endpoints
Tests all Flask endpoints with mocked external dependencies
"""

import pytest
import json
from unittest.mock import patch, MagicMock
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Mock external dependencies before importing app
sys.modules['leonardo_sdk'] = MagicMock()
sys.modules['anthropic'] = MagicMock()

from app import app, init_db


@pytest.fixture
def client():
      """Create test client"""
      app.config['TESTING'] = True
      app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():
              init_db()

    with app.test_client() as client:
              yield client


@pytest.fixture
def sample_artwork():
      """Sample artwork data"""
      return {
          'title': 'Test Artwork',
          'description': 'Test description',
          'style': 'Modern',
          'image_url': 'https://example.com/test.jpg'
      }


@pytest.fixture
def sample_listing():
      """Sample listing data"""
      return {
          'title': 'Test Listing',
          'description': 'Test listing description',
          'price': 29.99,
          'stock': 10,
          'category': 'Art Prints'
      }


class TestDashboardEndpoints:
      """Test dashboard data endpoints"""

    def test_get_dashboard_data(self, client):
              """Test GET /api/dashboard"""
              response = client.get('/api/dashboard')
              assert response.status_code == 200
              data = json.loads(response.data)
              assert 'sales' in data
              assert 'listings' in data
              assert 'artworks' in data

    def test_get_dashboard_with_date_range(self, client):
              """Test dashboard with date filtering"""
              response = client.get('/api/dashboard?start_date=2024-01-01&end_date=2024-12-31')
              assert response.status_code == 200
              data = json.loads(response.data)
              assert data is not None


class TestArtworkEndpoints:
      """Test artwork endpoints"""

    @patch('agents.art_generator.generate_artworks')
    def test_generate_artworks(self, mock_generate, client, sample_artwork):
              """Test POST /api/artworks/generate"""
              mock_generate.return_value = [sample_artwork]

        payload = {
                      'prompt': 'beautiful landscape',
                      'style': 'impressionist',
                      'count': 1
        }

        response = client.post('/api/artworks/generate',
                                                             data=json.dumps(payload),
                                                             content_type='application/json')

        assert response.status_code in [200, 201]
        mock_generate.assert_called_once()

    def test_get_artworks(self, client):
              """Test GET /api/artworks"""
              response = client.get('/api/artworks')
              assert response.status_code == 200
              data = json.loads(response.data)
              assert isinstance(data, list)

    def test_get_artwork_by_id(self, client, sample_artwork):
              """Test GET /api/artworks/<id>"""
              response = client.get('/api/artworks/1')
              assert response.status_code in [200, 404]


class TestListingEndpoints:
      """Test listing management endpoints"""

    def test_create_listing(self, client, sample_listing):
              """Test POST /api/listings"""
              response = client.post('/api/listings',
                                    data=json.dumps(sample_listing),
                                    content_type='application/json')

        assert response.status_code in [201, 200]
        data = json.loads(response.data)
        assert data.get('title') == sample_listing['title']

    def test_get_listings(self, client):
              """Test GET /api/listings"""
              response = client.get('/api/listings')
              assert response.status_code == 200
              data = json.loads(response.data)
              assert isinstance(data, list)

    def test_update_listing(self, client, sample_listing):
              """Test PUT /api/listings/<id>"""
              updated_data = {**sample_listing, 'price': 39.99}
              response = client.put('/api/listings/1',
                                   data=json.dumps(updated_data),
                                   content_type='application/json')

        assert response.status_code in [200, 404]

    def test_delete_listing(self, client):
              """Test DELETE /api/listings/<id>"""
              response = client.delete('/api/listings/1')
              assert response.status_code in [200, 204, 404]


class TestOrderEndpoints:
      """Test order tracking endpoints"""

    def test_get_orders(self, client):
              """Test GET /api/orders"""
              response = client.get('/api/orders')
              assert response.status_code == 200
              data = json.loads(response.data)
              assert isinstance(data, list)

    def test_get_order_by_id(self, client):
              """Test GET /api/orders/<id>"""
              response = client.get('/api/orders/1')
              assert response.status_code in [200, 404]

    def test_update_order_status(self, client):
              """Test PUT /api/orders/<id>/status"""
              payload = {'status': 'shipped'}
              response = client.put('/api/orders/1/status',
                                   data=json.dumps(payload),
                                   content_type='application/json')

        assert response.status_code in [200, 404]


class TestAnalyticsEndpoints:
      """Test analytics endpoints"""

    def test_get_analytics(self, client):
              """Test GET /api/analytics"""
              response = client.get('/api/analytics')
              assert response.status_code == 200
              data = json.loads(response.data)
              assert 'sales' in data or 'revenue' in data

    def test_get_sales_by_period(self, client):
              """Test GET /api/analytics/sales"""
              response = client.get('/api/analytics/sales?period=monthly')
              assert response.status_code == 200

    def test_get_engagement_metrics(self, client):
              """Test GET /api/analytics/engagement"""
              response = client.get('/api/analytics/engagement')
              assert response.status_code == 200


class TestSettingsEndpoints:
      """Test settings endpoints"""

    def test_get_settings(self, client):
              """Test GET /api/settings"""
              response = client.get('/api/settings')
              assert response.status_code == 200

    def test_update_settings(self, client):
              """Test PUT /api/settings"""
              payload = {
                  'api_key': 'test-key-123',
                  'notifications_enabled': True
              }
              response = client.put('/api/settings',
                                   data=json.dumps(payload),
                                   content_type='application/json')

        assert response.status_code in [200, 400]


class TestHealthCheck:
      """Test health check endpoint"""

    def test_health_endpoint(self, client):
              """Test GET /health"""
              response = client.get('/health')
              assert response.status_code == 200
              data = json.loads(response.data)
              assert 'status' in data


class TestErrorHandling:
      """Test error handling"""

    def test_invalid_json(self, client):
              """Test invalid JSON request"""
              response = client.post('/api/listings',
                                    data='invalid json',
                                    content_type='application/json')

        assert response.status_code in [400, 415]

    def test_missing_required_field(self, client):
              """Test missing required fields"""
              payload = {'title': 'Test'}  # Missing other required fields
        response = client.post('/api/listings',
                                                             data=json.dumps(payload),
                                                             content_type='application/json')

        assert response.status_code in [400, 422]

    def test_not_found(self, client):
              """Test 404 Not Found"""
              response = client.get('/api/nonexistent/123')
              assert response.status_code == 404


if __name__ == '__main__':
      pytest.main([__file__, '-v', '--cov=agents', '--cov=src'])
