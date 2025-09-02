# 🌲 Trails API Documentation

This document explains how to use the `getTrails` API for retrieving hiking trail information.  
Base URL:  
```
https://us-central1-orion-sdp.cloudfunctions.net
```

---

## 📌 Endpoint: Get Trails

**URL:**  
```
GET /getTrails
```

**Full URL:**  
```
https://us-central1-orion-sdp.cloudfunctions.net/getTrails
```

**Description:**  
Fetches a list of trails from the database. Each trail includes details such as name, location, distance, difficulty, description, and photos.

---

## 🔑 Query Parameters

| Parameter       | Type   | Required | Description                                                                 |
|-----------------|--------|----------|-----------------------------------------------------------------------------|
| `latitude`      | Float  | No       | User’s latitude. Can be used to filter trails by proximity.                 |
| `longitude`     | Float  | No       | User’s longitude. Used together with `latitude` for location-based results. |
| `maxDistance`   | Number | No       | Maximum distance (in km) from user location.                                |
| `difficulty`    | String | No       | Filter trails by difficulty (e.g., `Easy`, `Moderate`, `Hard`).             |
| `limit`         | Number | No       | Maximum number of trails to return.                                         |

---

## 📥 Request Example

```http
GET https://us-central1-orion-sdp.cloudfunctions.net/getTrails?difficulty=Easy
```

---

## 📤 Response Example

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

---

## ⚠️ Error Responses

| Status Code | Example Response | Meaning                                  |
|-------------|------------------|------------------------------------------|
| `400`       | `{ "error": "Missing required parameters" }` | Request was invalid or incomplete. |
| `404`       | `{ "error": "No trails found" }`             | No trails matched the query.       |
| `500`       | `{ "error": "Internal server error" }`       | Something went wrong on the server.|

---

## ✅ Usage Notes
- If no query parameters are provided, all available trails may be returned.  
- Location-based queries (`latitude`, `longitude`, `maxDistance`) are optional but recommended for performance.  
- Results may vary depending on your database indexing and filtering logic.  

---


## Orion API Documentation

This document provides details about the available Firebase Cloud Functions endpoints for the Hiking Trails app.  
All endpoints are protected with CORS and return JSON responses.

---

### **General Notes**
- **Base URL**: `https://us-central1-orion-sdp.cloudfunctions.net/<function-name>`
- **Methods**: Only the specified HTTP methods are supported; others will return `405 Method Not Allowed`.
- **Authentication**: Some endpoints require Firebase Authentication (`Authorization: Bearer <token>`).

---

### **Alerts**

#### **GET /getAlerts**
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

---

#### **POST /addAlert**
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

### **Trails**

#### **GET /getTrails**
Fetch all trails, optionally filtered by query parameters.

**Query Parameters:**
- Any field in the `Trails` collection (e.g., `difficulty=Hard`).

**Response:**
```json
[
  {
    "id": "trail123",
    "name": "Mountain Hike",
    "distance": 8.9,
    "difficulty": "Hard",
    "status": "open"
  }
]
```

---

#### **POST /submitTrail**
Submit a new trail.

**Body:**
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

#### **POST /trails/update**
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

**Response:**
```json
{ "message": "Trail info updated successfully." }
```

---

#### **POST /trails/updateImages**
Update images for a trail.

**Body:**
```json
{
  "trailId": "trail123",
  "photos": ["url1", "url2"]
}
```

**Response:**
```json
{ "message": "Trail images updated successfully." }
```

---

### **Favourites**

#### **POST /favourites/add**
Add a trail to user’s favourites.

**Body:**
```json
{ "uid": "user123", "trailId": "trail123" }
```

**Response:**
```json
{ "message": "Trail added to favourites." }
```

---

#### **POST /favourites/remove**
Remove a trail from favourites.

**Body:**
```json
{ "uid": "user123", "trailId": "trail123" }
```

**Response:**
```json
{ "message": "Trail removed from favourites." }
```

---

### **Wishlist**

#### **POST /wishlist/add**
Add a trail to wishlist.

**Body:**
```json
{ "uid": "user123", "trailId": "trail123" }
```

**Response:**
```json
{ "message": "Trail added to wishlist." }
```

---

#### **POST /wishlist/remove**
Remove a trail from wishlist.

**Body:**
```json
{ "uid": "user123", "trailId": "trail123" }
```

**Response:**
```json
{ "message": "Trail removed from wishlist." }
```

---

### **Completed Trails**

#### **POST /completed**
Mark a trail as completed.

**Body:**
```json
{ "uid": "user123", "trailId": "trail123" }
```

**Response:**
```json
{ "message": "Trail marked as completed." }
```

---

#### **POST /completed/remove**
Remove a trail from completed list.

**Body:**
```json
{ "uid": "user123", "trailId": "trail123" }
```

**Response:**
```json
{ "message": "Trail removed from completed." }
```

---

### **Saved Trails**

#### **GET /getSavedTrails**
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

### **Reviews**

#### **GET /getTrailReviews**
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

---

#### **POST /addTrailReview**
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

**Response:**
```json
{ "message": "Review added successfully." }
```

---

### **Other**

#### **GET /helloWorld**
Basic test endpoint.

**Response:**
```json
{ "message": "Hello from Firebase!" }
```

---

#### **Callable: getUserData**
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

# **Error Handling**
- `400 Bad Request` → Missing or invalid parameters.
- `401 Unauthorized` → Missing or invalid auth token (for protected routes).
- `404 Not Found` → User or trail not found.
- `405 Method Not Allowed` → Wrong HTTP method.
- `500 Internal Server Error` → Server or Firestore error.

---

# **Collections Structure**
- **Users**
  - `favourites`: [TrailRef]
  - `wishlist`: [TrailRef]
  - `completed`: [TrailRef]

- **Trails**
  - `reviews`: Subcollection of reviews
  - `photos`: Array of URLs

- **Alerts**
  - Linked by `trailId` (reference to a Trail).

---
