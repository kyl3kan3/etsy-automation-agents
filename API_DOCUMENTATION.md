# ArtFlow API Documentation

## Overview
This document describes the Flask API endpoints for the Etsy Print Art Automation System (ArtFlow). The API provides endpoints for dashboard metrics, listings management, analytics, and configuration.

## Base URL
```
http://localhost:5000/api
```

## Authentication
Currently, no authentication is required. In production, implement JWT or API key authentication.

## Endpoints

### Dashboard Metrics

#### GET /dashboard/metrics
Returns key business metrics for the dashboard.

**Response:**
```json
{
  "totalRevenue": 12847,
  "totalViews": 48200,
  "activeListing": 24,
  "favorites": 1847,
  "recentOrders": 3,
  "lastUpdated": "2024-01-11T17:36:00Z"
}
```

---

### Listings Management

#### GET /listings
Returns all product listings.

**Query Parameters:**
- `search` (optional): Search term for listing titles
- - `status` (optional): Filter by status (active, draft, paused)
  - - `page` (optional): Page number (default: 1)
    - - `limit` (optional): Items per page (default: 10)
     
      - **Response:**
      - ```json
        {
          "listings": [
            {
              "id": "list_001",
              "title": "Abstract Ocean Waves",
              "price": 450,
              "status": "active",
              "views": 1200,
              "favorites": 89,
              "created": "2024-01-05T10:30:00Z"
            }
          ],
          "total": 24,
          "page": 1,
          "totalPages": 3
        }
        ```

        #### POST /listings
        Create a new listing.

        **Request Body:**
        ```json
        {
          "title": "New Artwork",
          "description": "Beautiful art piece",
          "price": 299.99,
          "tags": ["art", "abstract"],
          "imageUrl": "https://..."
        }
        ```

        **Response:** Returns created listing object

        #### GET /listings/{id}
        Get specific listing details.

        #### PUT /listings/{id}
        Update a listing.

        #### DELETE /listings/{id}
        Delete a listing.

        ---

        ### Analytics

        #### GET /analytics/sales
        Returns sales analytics data.

        **Query Parameters:**
        - `startDate` (optional): ISO date string
        - - `endDate` (optional): ISO date string
          - - `period` (optional): day, week, month
           
            - **Response:**
            - ```json
              {
                "totalSales": 24580,
                "averagePrice": 425.50,
                "conversionRate": 4.8,
                "customerGrowth": 156,
                "chartData": [
                  {"date": "2024-01-01", "sales": 450, "views": 1500},
                  {"date": "2024-01-02", "sales": 520, "views": 1800}
                ]
              }
              ```

              #### GET /analytics/engagement
              Returns engagement metrics.

              **Response:**
              ```json
              {
                "views": 48200,
                "favorites": 1847,
                "conversionRate": 4.8,
                "byDate": [
                  {"date": "2024-01-01", "views": 1500, "favorites": 125}
                ]
              }
              ```

              ---

              ### Configuration

              #### GET /settings
              Returns current settings.

              **Response:**
              ```json
              {
                "shopName": "Artisan Gallery",
                "email": "artist@example.com",
                "apiKeys": {
                  "etsy": "configured",
                  "openai": "configured",
                  "leonardo": "configured"
                },
                "preferences": {
                  "notifications": true,
                  "autoPublish": false
                }
              }
              ```

              #### PUT /settings
              Update settings.

              **Request Body:**
              ```json
              {
                "shopName": "New Shop Name",
                "email": "newemail@example.com",
                "preferences": {
                  "notifications": true,
                  "autoPublish": true
                }
              }
              ```

              ---

              ### Image Generation

              #### POST /generate/batch
              Generate batch of images using Leonardo.AI.

              **Request Body:**
              ```json
              {
                "theme": "abstract",
                "count": 50,
                "style": "modern"
              }
              ```

              **Response:**
              ```json
              {
                "batchId": "batch_001",
                "status": "processing",
                "estimatedTime": 300,
                "generatedImages": []
              }
              ```

              #### GET /generate/batch/{id}
              Get batch generation status and results.

              ---

              ## Error Responses

              All errors follow this format:

              ```json
              {
                "error": "Error message",
                "code": "ERROR_CODE",
                "details": {}
              }
              ```

              ### Common Error Codes:
              - `400`: Bad Request - Invalid parameters
              - - `404`: Not Found - Resource doesn't exist
                - - `500`: Internal Server Error
                 
                  - ---

                  ## Rate Limiting
                  Currently no rate limiting. Implement in production:
                  - 1000 requests per hour per IP
                  - - 100 requests per minute per IP
                   
                    - ---

                    ## Pagination
                    List endpoints support pagination:
                    - `limit`: Items per page (default: 10, max: 100)
                    - - `page`: Page number (default: 1)
                      - - Response includes: `total`, `page`, `totalPages`
                       
                        - ---

                        ## CORS
                        CORS is enabled for development. Configure in production.

                        ---

                        ## Environment Variables
                        ```
                        FLASK_ENV=development
                        FLASK_PORT=5000
                        DATABASE_URL=sqlite:///etsy_automation.db
                        ETSY_API_KEY=your_key
                        OPENAI_API_KEY=your_key
                        LEONARDO_API_KEY=your_key
                        ```

                        ---

                        ## Testing
                        ```bash
                        # Test dashboard endpoint
                        curl http://localhost:5000/api/dashboard/metrics

                        # Test listings endpoint
                        curl http://localhost:5000/api/listings

                        # Create new listing
                        curl -X POST http://localhost:5000/api/listings \
                          -H "Content-Type: application/json" \
                          -d '{"title":"Test","price":99.99}'
                        ```

                        ---

                        ## Deployment Notes
                        - Use HTTPS in production
                        - - Implement proper authentication
                          - - Add rate limiting
                            - - Enable CORS properly
                              - - Use environment variables for secrets
                                - - Add request logging
                                  - - Implement monitoring and alerting
