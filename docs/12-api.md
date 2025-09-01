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
