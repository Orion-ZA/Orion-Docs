# 🌲 Orion Trails API Documentation

This document provides comprehensive documentation for both the Firebase Cloud Functions API and the new RESTful CRUD API for the Orion hiking trails application.

## 📋 Table of Contents
1. [Firebase Cloud Functions API](#firebase-cloud-functions-api)
2. [RESTful CRUD API](#restful-crud-api)
3. [Error Handling](#error-handling)
4. [Data Models](#data-models)

---

# Firebase Cloud Functions API

**Base URL:** `https://us-central1-orion-sdp.cloudfunctions.net`

This API provides essential trail management functions using Firebase Cloud Functions.

---

## 📌 Core Trail Endpoints

### GET /getTrails
Fetches a list of trails from the database with optional filtering.

**Query Parameters:**
| Parameter       | Type   | Required | Description                                                                 |
|-----------------|--------|----------|-----------------------------------------------------------------------------|
| `latitude`      | Float  | No       | User's latitude. Can be used to filter trails by proximity.                 |
| `longitude`     | Float  | No       | User's longitude. Used together with `latitude` for location-based results. |
| `maxDistance`   | Number | No       | Maximum distance (in km) from user location.                                |
| `difficulty`    | String | No       | Filter trails by difficulty (e.g., `Easy`, `Moderate`, `Hard`).             |
| `limit`         | Number | No       | Maximum number of trails to return.                                         |

**Example Request:**
```http
GET https://us-central1-orion-sdp.cloudfunctions.net/getTrails?difficulty=Easy
```

**Example Response:**
```json
[
  {
    "id": "trail123",
    "name": "Bikini Bottom Trail",
    "location": { "_latitude": -26.2041, "_longitude": 28.0473 },
    "distance": 12,
    "difficulty": "Easy",
    "gpsRoute": [
      { "_latitude": -26.2041, "_longitude": 28.0473 },
      { "_latitude": -26.2050, "_longitude": 28.0500 }
    ],
    "description": "The waterfall is pretty cool.",
    "photos": [
      "https://storage.googleapis.com/trails/trail123/photo1.jpg"
    ],
    "createdBy": "user_abc123"
  }
]
```

### POST /submitTrail
Submit a new trail to the database.

**Request Body:**
```json
{
  "name": "Sunset Peak",
  "location": { "lat": -26.2041, "lng": 28.0473 },
  "distance": 10.5,
  "elevationGain": 800,
  "difficulty": "Moderate",
  "status": "open",
  "tags": ["scenic", "wildlife"],
  "description": "Beautiful sunset views",
  "photos": ["url1", "url2"],
  "gpsRoute": [{ "lat": -26.2, "lng": 28.0 }]
}
```

**Response:**
```json
{
  "message": "Trail submitted successfully",
  "trailId": "trail123",
  "trail": { "id": "trail123", "name": "Sunset Peak", ... }
}
```

---

## 🚨 Alert Management

### GET /getTrailAlerts
Fetch all active alerts for a specific trail.

**Query Parameters:**
- `trailId` (string, required) — ID of the trail.

**Response:**
```json
{
  "alerts": [
    {
      "id": "alertId123",
      "trailId": "<reference>",
      "message": "Flooding near the river",
      "type": "warning",
      "isActive": true,
      "timestamp": "2025-09-02T12:00:00Z"
    }
  ]
}
```

### POST /addAlert
Add a new alert for a trail.

**Body:**
```json
{
  "trailId": "TRAIL_ID",
  "message": "Trail closed due to maintenance",
  "type": "info"
}
```

**Response:**
```json
{ "success": true, "message": "Alert added successfully" }
```

---

## 👤 User Trail Management

### POST /favourites/add
Add a trail to user's favourites.

**Body:**
```json
{ "uid": "user123", "trailId": "trail123" }
```

### POST /favourites/remove
Remove a trail from user's favourites.

**Body:**
```json
{ "uid": "user123", "trailId": "trail123" }
```

### POST /wishlist/add
Add a trail to wishlist.

**Body:**
```json
{ "uid": "user123", "trailId": "trail123" }
```

### POST /wishlist/remove
Remove a trail from wishlist.

**Body:**
```json
{ "uid": "user123", "trailId": "trail123" }
```

### POST /completed
Mark a trail as completed.

**Body:**
```json
{ "uid": "user123", "trailId": "trail123" }
```

### POST /completed/remove
Remove a trail from completed list.

**Body:**
```json
{ "uid": "user123", "trailId": "trail123" }
```

### GET /getSavedTrails
Get all saved trails for a user.

**Query Parameters:**
- `uid` (string, required)

**Response:**
```json
{
  "favourites": [{ "id": "trail1", "name": "Trail One" }],
  "wishlist": [{ "id": "trail2", "name": "Trail Two" }],
  "completed": [{ "id": "trail3", "name": "Trail Three" }]
}
```

---

## 📝 Trail Updates

### POST /trails/update
Update trail information.

**Body:**
```json
{
  "trailId": "trail123",
  "updates": {
    "name": "Updated Trail Name",
    "status": "closed",
    "tags": ["waterfall"]
  }
}
```

### POST /trails/updateImages
Update images for a trail.

**Body:**
```json
{
  "trailId": "trail123",
  "photos": ["url1", "url2"]
}
```

---

## ⭐ Reviews

### GET /getTrailReviews
Fetch reviews for a specific trail.

**Query Parameters:**
- `trailId` (string, required)

**Response:**
```json
{
  "reviews": [
    {
      "id": "review123",
      "user": "user123",
      "rating": 5,
      "comment": "Amazing trail!",
      "timestamp": "2025-09-02T12:00:00Z"
    }
  ]
}
```

### POST /addTrailReview
Add a review to a trail.

**Body:**
```json
{
  "trailId": "trail123",
  "review": {
    "id": "review123",
    "user": "user123",
    "rating": 4,
    "comment": "Nice views, but steep climb",
    "timestamp": "2025-09-02T12:00:00Z"
  }
}
```

---

## 🔧 Utility Endpoints

### GET /helloWorld
Basic test endpoint.

**Response:**
```json
{ "message": "Hello from Firebase!" }
```

### Callable: getUserData
Get user data from Firestore (requires authentication).

**Request (via Firebase SDK):**
```js
const getUserData = firebase.functions().httpsCallable("getUserData");
const res = await getUserData();
console.log(res.data);
```

**Response:**
```json
{
  "data": {
    "favourites": [],
    "wishlist": [],
    "completed": []
  }
}
```

---

# RESTful CRUD API

**Base URL:** `https://orion-api-qeyv.onrender.com`  
**Documentation:** [https://orion-api-qeyv.onrender.com/api-docs/](https://orion-api-qeyv.onrender.com/api-docs/)

This is a comprehensive RESTful API providing full CRUD operations for trail management with advanced features like search, filtering, and geolocation support.

---

## 🏥 Health Check Endpoints

### GET /health
Check if the API service is running and healthy.

**Response:**
```json
{
  "status": "OK",
  "timestamp": "2024-01-15T10:30:00.000Z",
  "uptime": 123.456
}
```

### GET /health/db
Check database connectivity and health.

**Response:**
```json
{
  "status": "OK",
  "database": "Connected",
  "timestamp": "2024-01-15T10:30:00.000Z",
  "trailsCount": 42,
  "message": "Successfully connected to Trails collection"
}
```

---

## 🛤️ Trail CRUD Operations

### POST /api/trails
Create a new trail.

**Request Body:**
```json
{
  "name": "Mountain Peak Trail",
  "location": {
    "latitude": -26.2041,
    "longitude": 28.0473
  },
  "distance": 8.5,
  "elevationGain": 1200,
  "difficulty": "Hard",
  "description": "Challenging trail with stunning mountain views",
  "tags": ["mountain", "challenging", "scenic"],
  "gpsRoute": [
    { "latitude": -26.2041, "longitude": 28.0473 },
    { "latitude": -26.2050, "longitude": 28.0500 }
  ],
  "photos": ["https://example.com/photo1.jpg"],
  "status": "open",
  "createdBy": "user123"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Trail created successfully",
  "data": {
    "id": "trail123",
    "name": "Mountain Peak Trail",
    "location": { "latitude": -26.2041, "longitude": 28.0473 },
    "distance": 8.5,
    "elevationGain": 1200,
    "difficulty": "Hard",
    "description": "Challenging trail with stunning mountain views",
    "tags": ["mountain", "challenging", "scenic"],
    "gpsRoute": [...],
    "photos": ["https://example.com/photo1.jpg"],
    "status": "open",
    "createdBy": "user123",
    "createdAt": "2024-01-15T10:30:00.000Z",
    "lastUpdated": "2024-01-15T10:30:00.000Z"
  }
}
```

### GET /api/trails
Get all trails with pagination and filtering.

**Query Parameters:**
| Parameter       | Type   | Required | Description                                                                 |
|-----------------|--------|----------|-----------------------------------------------------------------------------|
| `page`          | Number | No       | Page number (default: 1)                                                    |
| `limit`         | Number | No       | Items per page (default: 10, max: 100)                                      |
| `sort`          | String | No       | Sort field: `name`, `distance`, `elevationGain`, `createdAt`, `lastUpdated` |
| `order`         | String | No       | Sort order: `asc` or `desc` (default: `desc`)                               |
| `difficulty`    | String | No       | Filter by difficulty: `Easy`, `Moderate`, `Hard`, `Expert`                  |
| `status`        | String | No       | Filter by status: `open`, `closed`, `maintenance`, `seasonal`               |
| `tags`          | String | No       | Comma-separated tags to filter by                                           |
| `minDistance`   | Number | No       | Minimum distance filter                                                     |
| `maxDistance`   | Number | No       | Maximum distance filter                                                     |
| `minElevation`  | Number | No       | Minimum elevation gain filter                                               |
| `maxElevation`  | Number | No       | Maximum elevation gain filter                                               |

**Example Request:**
```http
GET /api/trails?difficulty=Hard&status=open&page=1&limit=10&sort=distance&order=asc
```

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "id": "trail123",
      "name": "Mountain Peak Trail",
      "location": { "latitude": -26.2041, "longitude": 28.0473 },
      "distance": 8.5,
      "elevationGain": 1200,
      "difficulty": "Hard",
      "status": "open",
      "tags": ["mountain", "challenging", "scenic"],
      "description": "Challenging trail with stunning mountain views",
      "photos": ["https://example.com/photo1.jpg"],
      "createdBy": "user123",
      "createdAt": "2024-01-15T10:30:00.000Z",
      "lastUpdated": "2024-01-15T10:30:00.000Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 42,
    "pages": 5
  }
}
```

### GET /api/trails/{id}
Get a specific trail by ID.

**Response:**
```json
{
  "success": true,
  "data": {
    "id": "trail123",
    "name": "Mountain Peak Trail",
    "location": { "latitude": -26.2041, "longitude": 28.0473 },
    "distance": 8.5,
    "elevationGain": 1200,
    "difficulty": "Hard",
    "status": "open",
    "tags": ["mountain", "challenging", "scenic"],
    "description": "Challenging trail with stunning mountain views",
    "photos": ["https://example.com/photo1.jpg"],
    "createdBy": "user123",
    "createdAt": "2024-01-15T10:30:00.000Z",
    "lastUpdated": "2024-01-15T10:30:00.000Z"
  }
}
```

### PUT /api/trails/{id}
Update a trail.

**Request Body:**
```json
{
  "name": "Updated Trail Name",
  "status": "maintenance",
  "description": "Updated description",
  "tags": ["updated", "tags"]
}
```

**Response:**
```json
{
  "success": true,
  "message": "Trail updated successfully",
  "data": {
    "id": "trail123",
    "name": "Updated Trail Name",
    "status": "maintenance",
    "description": "Updated description",
    "tags": ["updated", "tags"],
    "lastUpdated": "2024-01-15T11:00:00.000Z"
  }
}
```

### DELETE /api/trails/{id}
Delete a trail.

**Response:**
```json
{
  "success": true,
  "message": "Trail deleted successfully"
}
```

---

## 🔍 Advanced Search Features

### GET /api/trails/search
Search trails by text content.

**Query Parameters:**
| Parameter       | Type   | Required | Description                                                                 |
|-----------------|--------|----------|-----------------------------------------------------------------------------|
| `q`             | String | Yes      | Search query text                                                            |
| `difficulty`    | String | No       | Filter by difficulty                                                         |
| `status`        | String | No       | Filter by status                                                             |
| `tags`          | String | No       | Comma-separated tags to filter by                                           |

**Example Request:**
```http
GET /api/trails/search?q=mountain&difficulty=Hard&status=open
```

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "id": "trail123",
      "name": "Mountain Peak Trail",
      "description": "Challenging mountain trail with stunning views",
      "difficulty": "Hard",
      "status": "open"
    }
  ],
  "total": 1
}
```

### GET /api/trails/near
Find trails near a specific location.

**Query Parameters:**
| Parameter       | Type   | Required | Description                                                                 |
|-----------------|--------|----------|-----------------------------------------------------------------------------|
| `latitude`      | Number | Yes      | Latitude coordinate (-90 to 90)                                             |
| `longitude`     | Number | Yes      | Longitude coordinate (-180 to 180)                                          |
| `maxDistance`   | Number | No       | Maximum distance in meters (default: 10000, max: 100000)                    |
| `page`          | Number | No       | Page number (default: 1)                                                    |
| `limit`         | Number | No       | Items per page (default: 10, max: 100)                                      |

**Example Request:**
```http
GET /api/trails/near?latitude=-26.2041&longitude=28.0473&maxDistance=5000
```

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "id": "trail123",
      "name": "Nearby Trail",
      "location": { "latitude": -26.2041, "longitude": 28.0473 },
      "distance": 8.5,
      "difficulty": "Moderate",
      "distanceFromLocation": 2500
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 5,
    "pages": 1
  }
}
```

---

## 👤 User Management & Trail Interactions

### POST /api/users/favourites/add
Add a trail to user's favourites.

**Request Body:**
```json
{
  "userId": "user123",
  "trailId": "trail123"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Trail added to favourites successfully"
}
```

### POST /api/users/favourites/remove
Remove a trail from user's favourites.

**Request Body:**
```json
{
  "userId": "user123",
  "trailId": "trail123"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Trail removed from favourites successfully"
}
```

### POST /api/users/wishlist/add
Add a trail to user's wishlist.

**Request Body:**
```json
{
  "userId": "user123",
  "trailId": "trail123"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Trail added to wishlist successfully"
}
```

### POST /api/users/wishlist/remove
Remove a trail from user's wishlist.

**Request Body:**
```json
{
  "userId": "user123",
  "trailId": "trail123"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Trail removed from wishlist successfully"
}
```

### POST /api/users/completed
Mark a trail as completed.

**Request Body:**
```json
{
  "userId": "user123",
  "trailId": "trail123"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Trail marked as completed successfully"
}
```

### POST /api/users/completed/remove
Remove a trail from completed list.

**Request Body:**
```json
{
  "userId": "user123",
  "trailId": "trail123"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Trail removed from completed successfully"
}
```

### GET /api/users/savedTrails
Get all saved trails for a user (favourites, wishlist, completed).

**Query Parameters:**
- `userId` (string, required) - User ID

**Response:**
```json
{
  "success": true,
  "data": {
    "favourites": [
      {
        "id": "trail1",
        "name": "Mountain Trail",
        "distance": 8.5,
        "difficulty": "Hard"
      }
    ],
    "wishlist": [
      {
        "id": "trail2",
        "name": "Forest Trail",
        "distance": 5.2,
        "difficulty": "Easy"
      }
    ],
    "completed": [
      {
        "id": "trail3",
        "name": "Lake Trail",
        "distance": 6.3,
        "difficulty": "Moderate"
      }
    ]
  }
}
```

---

## 🚨 Alert Management

### POST /api/alerts
Create a new alert for a trail.

**Request Body:**
```json
{
  "trailId": "trail123",
  "message": "Trail closed due to flooding",
  "type": "emergency",
  "comment": "Expected to reopen in 2 days",
  "isTimed": true,
  "duration": 2880
}
```

**Response:**
```json
{
  "success": true,
  "message": "Alert created successfully",
  "data": {
    "id": "alert123",
    "trailId": "trail123",
    "message": "Trail closed due to flooding",
    "type": "emergency",
    "comment": "Expected to reopen in 2 days",
    "isActive": true,
    "isTimed": true,
    "expiresAt": "2024-01-17T10:30:00.000Z",
    "timestamp": "2024-01-15T10:30:00.000Z"
  }
}
```

### GET /api/alerts/trail
Get all alerts for a specific trail.

**Query Parameters:**
- `trailId` (string, required) - Trail ID

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "id": "alert123",
      "trailId": "trail123",
      "message": "Trail closed due to flooding",
      "type": "emergency",
      "isActive": true,
      "timestamp": "2024-01-15T10:30:00.000Z"
    }
  ]
}
```

### GET /api/alerts
Get all alerts with pagination and filtering (Admin).

**Query Parameters:**
- `page` (number, optional) - Page number (default: 1)
- `limit` (number, optional) - Items per page (default: 10)
- `status` (string, optional) - Filter by status: `all`, `active`, `inactive`

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "id": "alert123",
      "trailId": "trail123",
      "message": "Trail maintenance in progress",
      "type": "authority",
      "isActive": true,
      "timestamp": "2024-01-15T10:30:00.000Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 25,
    "pages": 3
  }
}
```

### PUT /api/alerts/{alertId}
Update an alert.

**Request Body:**
```json
{
  "message": "Updated alert message",
  "isActive": false
}
```

**Response:**
```json
{
  "success": true,
  "message": "Alert updated successfully"
}
```

### DELETE /api/alerts/{alertId}
Delete an alert.

**Response:**
```json
{
  "success": true,
  "message": "Alert deleted successfully"
}
```

---

## ⭐ Review Management

### POST /api/reviews
Create a new review for a trail.

**Request Body:**
```json
{
  "trailId": "trail123",
  "review": {
    "id": "review123",
    "userId": "user123",
    "userName": "John Doe",
    "userEmail": "john@example.com",
    "rating": 5,
    "comment": "Amazing trail with beautiful views!",
    "photos": ["https://example.com/photo1.jpg"],
    "timestamp": "2024-01-15T10:30:00.000Z"
  }
}
```

**Response:**
```json
{
  "success": true,
  "message": "Review created successfully",
  "data": {
    "id": "review123",
    "userId": "user123",
    "userName": "John Doe",
    "rating": 5,
    "comment": "Amazing trail with beautiful views!",
    "timestamp": "2024-01-15T10:30:00.000Z"
  }
}
```

### GET /api/reviews
Get all reviews for a specific trail.

**Query Parameters:**
- `trailId` (string, required) - Trail ID

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "id": "review123",
      "userId": "user123",
      "userName": "John Doe",
      "rating": 5,
      "comment": "Amazing trail with beautiful views!",
      "timestamp": "2024-01-15T10:30:00.000Z"
    }
  ]
}
```

### PUT /api/reviews/{trailId}/{reviewId}
Update a review.

**Request Body:**
```json
{
  "rating": 4,
  "comment": "Updated review: Great trail but a bit crowded"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Review updated successfully"
}
```

### DELETE /api/reviews/{trailId}/{reviewId}
Delete a review.

**Response:**
```json
{
  "success": true,
  "message": "Review deleted successfully"
}
```

---

## 📋 Report Management

### POST /api/reports
Create a new report.

**Request Body:**
```json
{
  "type": "trail",
  "category": "safety_concern",
  "description": "Loose rocks on the trail pose a safety hazard",
  "priority": "high",
  "additionalDetails": "Located near the 3km marker",
  "trailId": "trail123",
  "trailName": "Mountain Peak Trail",
  "reporterId": "user123"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Report created successfully",
  "data": {
    "id": "report123",
    "type": "trail",
    "category": "safety_concern",
    "description": "Loose rocks on the trail pose a safety hazard",
    "priority": "high",
    "status": "pending",
    "createdAt": "2024-01-15T10:30:00.000Z",
    "updatedAt": "2024-01-15T10:30:00.000Z"
  }
}
```

### GET /api/reports
Get all reports with pagination and filtering (Admin).

**Query Parameters:**
- `page` (number, optional) - Page number (default: 1)
- `limit` (number, optional) - Items per page (default: 10)
- `status` (string, optional) - Filter by status: `all`, `pending`, `reviewed`, `resolved`, `dismissed`
- `type` (string, optional) - Filter by type: `all`, `trail`, `review`, `image`, `alert`, `general`

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "id": "report123",
      "type": "trail",
      "category": "safety_concern",
      "description": "Loose rocks on the trail",
      "priority": "high",
      "status": "pending",
      "trailName": "Mountain Peak Trail",
      "createdAt": "2024-01-15T10:30:00.000Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 15,
    "pages": 2
  }
}
```

### GET /api/reports/{reportId}
Get a specific report by ID.

**Response:**
```json
{
  "success": true,
  "data": {
    "id": "report123",
    "type": "trail",
    "category": "safety_concern",
    "description": "Loose rocks on the trail pose a safety hazard",
    "priority": "high",
    "status": "pending",
    "trailId": "trail123",
    "trailName": "Mountain Peak Trail",
    "reporterId": "user123",
    "createdAt": "2024-01-15T10:30:00.000Z",
    "updatedAt": "2024-01-15T10:30:00.000Z"
  }
}
```

### PUT /api/reports/{reportId}
Update a report.

**Request Body:**
```json
{
  "status": "resolved",
  "priority": "medium"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Report updated successfully"
}
```

### DELETE /api/reports/{reportId}
Delete a report.

**Response:**
```json
{
  "success": true,
  "message": "Report deleted successfully"
}
```

---

# Error Handling

## Firebase Cloud Functions API Errors

| Status Code | Example Response | Meaning                                  |
|-------------|------------------|------------------------------------------|
| `400`       | `{ "error": "Missing required parameters" }` | Request was invalid or incomplete. |
| `404`       | `{ "error": "No trails found" }`             | No trails matched the query.       |
| `405`       | `{ "error": "Method Not Allowed" }`          | Wrong HTTP method used.            |
| `500`       | `{ "error": "Internal server error" }`       | Something went wrong on the server.|

## RESTful CRUD API Errors

| Status Code | Example Response | Meaning                                  |
|-------------|------------------|------------------------------------------|
| `400`       | `{ "success": false, "message": "Validation error", "errors": ["Trail name is required"] }` | Validation failed |
| `404`       | `{ "success": false, "message": "Trail not found" }` | Resource not found |
| `405`       | `{ "success": false, "message": "Method not allowed" }` | Wrong HTTP method |
| `500`       | `{ "success": false, "message": "Internal server error", "error": "Error details" }` | Server error |

---

# Data Models

## Trail Object Structure

```json
{
  "id": "string",
  "name": "string (max 100 chars)",
  "location": {
    "latitude": "number (-90 to 90)",
    "longitude": "number (-180 to 180)"
  },
  "distance": "number (km, >= 0)",
  "elevationGain": "number (meters, >= 0)",
  "difficulty": "string (Easy|Moderate|Hard|Expert)",
  "tags": ["string (max 50 chars each, max 10 tags)"],
  "gpsRoute": [
    {
      "latitude": "number",
      "longitude": "number"
    }
  ],
  "description": "string (max 2000 chars)",
  "photos": ["string (valid URLs, max 20 photos)"],
  "status": "string (open|closed|maintenance|seasonal)",
  "createdBy": "string (user ID)",
  "createdAt": "string (ISO 8601 date-time)",
  "lastUpdated": "string (ISO 8601 date-time)"
}
```

## Alert Object Structure

```json
{
  "id": "string",
  "trailId": "string",
  "message": "string",
  "type": "string (info|warning|error)",
  "isActive": "boolean",
  "timestamp": "string (ISO 8601 date-time)"
}
```

## User Object Structure

```json
{
  "id": "string (user ID)",
  "profileInfo": {
    "name": "string",
    "email": "string (email format)",
    "joinedDate": "string (ISO 8601 date-time)"
  },
  "submittedTrails": ["string (trail IDs)"],
  "favourites": ["string (trail IDs)"],
  "completed": ["string (trail IDs)"],
  "wishlist": ["string (trail IDs)"]
}
```

## Alert Object Structure

```json
{
  "id": "string",
  "trailId": "string",
  "message": "string",
  "type": "string (community|authority|emergency)",
  "comment": "string (optional)",
  "timestamp": "string (ISO 8601 date-time)",
  "isActive": "boolean",
  "isTimed": "boolean",
  "expiresAt": "string (ISO 8601 date-time, only if isTimed is true)",
  "duration": "number (minutes, used during creation but not stored)",
  "lastUpdated": "string (ISO 8601 date-time)"
}
```

## Review Object Structure

```json
{
  "id": "string (UUID)",
  "userId": "string (Firebase Auth UID)",
  "userName": "string (display name or 'Anonymous')",
  "userEmail": "string (email format)",
  "rating": "number (1-5)",
  "comment": "string (review text)",
  "message": "string (alternative field for comment)",
  "timestamp": "string (ISO 8601 date-time)",
  "photos": ["string (photo URLs)"],
  "lastUpdated": "string (ISO 8601 date-time)"
}
```

## Report Object Structure

```json
{
  "id": "string",
  "type": "string (trail|review|image|alert|general)",
  "category": "string (specific category based on type)",
  "description": "string (detailed issue description)",
  "priority": "string (low|medium|high|urgent)",
  "additionalDetails": "string (optional)",
  "targetId": "string (ID of reported item)",
  "trailId": "string (associated trail ID)",
  "trailName": "string (trail name for reference)",
  "reporterId": "string (Firebase Auth UID)",
  "status": "string (pending|reviewed|resolved|dismissed)",
  "createdAt": "string (ISO 8601 date-time)",
  "updatedAt": "string (ISO 8601 date-time)",
  "timestamp": "string (ISO 8601 date-time, alternative field)"
}
```

---

## ✅ Usage Notes

### Firebase Cloud Functions API
- All endpoints are protected with CORS
- Some endpoints require Firebase Authentication (`Authorization: Bearer <token>`)
- Location-based queries are optional but recommended for performance
- Results may vary depending on database indexing and filtering logic

### RESTful CRUD API
- Comprehensive validation with detailed error messages
- Advanced filtering and search capabilities
- Geolocation support with distance calculations
- Pagination for large result sets
- Rate limiting: 100 requests per 15 minutes per IP
- Full Swagger documentation available at `/api-docs/`

### General Notes
- Both APIs use JSON for request/response bodies
- All timestamps are in ISO 8601 format
- Location coordinates use standard latitude/longitude format
- Photos must be valid HTTP/HTTPS URLs
- Trail status affects visibility in search results

