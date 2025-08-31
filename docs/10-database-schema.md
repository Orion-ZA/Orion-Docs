# Database Schema and Deployment for Crowdsourced Hiking Information

## Database Schema (Firebase Firestore)

### Collections and Documents

- **Trails Collection**
  - **Document Fields:**
    - `name`: String
    - `location`: GeoPoint (latitude, longitude)
    - `distance`: Number
    - `elevationGain`: Number
    - `difficulty`: String (e.g., "Easy", "Moderate", "Hard")
    - `tags`: Array of Strings (e.g., ["waterfall", "forest"])
    - `gpsRoute`: Array of GeoPoint objects
    - `description`: String
    - `photos`: Array of Strings (URLs to Firebase Storage)
    - `status`: String (e.g., "open", "closed")
    - `createdBy`: Reference to User document (e.g., `/users/{userId}`)
    - `createdAt`: Timestamp
    - `lastUpdated`: Timestamp
    - `reviews`: Subcollection (see below)
  - **Purpose**: Stores trail data with real-time updates and user-submitted content.

- **Reviews Subcollection (under each Trail document)**
  - **Document Fields:**
    - `userId`: Reference to User document
    - `rating`: Number (1-5)
    - `comment`: String
    - `photos`: Array of Strings (URLs to Firebase Storage)
    - `timestamp`: Timestamp
  - **Purpose**: Captures user reviews and media linked to specific trails.

- **Users Collection**
  - **Document Fields:**
    - `profileInfo`: Map (e.g., `name`: String, `email`: String, `joinedDate`: Timestamp)
    - `submittedTrails`: Array of References to Trail documents
    - `favourites`: Array of References to Trail documents
    - `completedHikes`: Array of References to Trail documents
    - `wishlist`: Array of References to Trail documents
  - **Purpose**: Manages user profiles and their trail interactions.

- **Alerts Collection**
  - **Document Fields:**
    - `trailId`: Reference to Trail document
    - `message`: String
    - `type`: String (e.g., "community", "authority")
    - `timestamp`: Timestamp
    - `isActive`: Boolean
  - **Purpose**: Stores real-time alerts and status updates for trails.

### Relationships
- **Trails to Users**: `createdBy` references the creating User; `submittedTrails` in Users links back.
- **Trails to Reviews**: Nested subcollection with `userId` referencing Users.
- **Users to Trails**: Arrays (`favorites`, `completedHikes`, `wishlist`) hold Trail references.
- **Trails to Alerts**: `trailId` references the associated Trail.

## Deployment Information (Firebase Hosting)

### Steps to Deploy
1. **Install Firebase CLI**:
   - Run `npm install -g firebase-tools` to install the Firebase CLI.
2. **Initialize Firebase in Your Project**:
   - Navigate to your project directory and run `firebase login` to authenticate.
   - Run `firebase init` to set up Firebase Hosting:
     - Select Hosting and follow prompts.
     - Specify the public directory (e.g., `public` or `build`).
     - Choose to configure as a single-page app (recommended for React/Vue apps).
3. **Build Your App**:
   - Ensure your app is built (e.g., `npm run build` for React apps) to generate static files.
4. **Deploy to Firebase Hosting**:
   - Run `firebase deploy` to upload your app to Firebase Hosting.
   - Note the deployed URL (e.g., `https://your-project-id.web.app`) as of 10:32 PM SAST on Friday, August 29, 2025.
5. **Monitor and Update**:
   - Use `firebase deploy --only hosting` for future updates.
   - Check deployment status in the Firebase Console under Hosting.

### Configuration File (`firebase.json`)
```json
{
  "hosting": {
    "public": "build",
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ],
    "rewrites": [
      {
        "source": "**",
        "destination": "/index.html"
      }
    ]
  }
}
```
## Choice Justification

### Firebase as Database
- **Real-Time Updates**: Firebase's real-time capabilities align with the need for instant trail status and alert updates, enhancing user experience for hikers.
- **Scalability**: Firestore's serverless architecture scales automatically, supporting community contributions and growing trail data.
- **Ease of Integration**: Built-in authentication and Storage simplify user management and media handling, reducing development overhead.
- **Hosting Compatibility**: Firebase Hosting pairs seamlessly with Firestore, offering a unified platform for both data and delivery.

### Firebase Hosting
- **Simplicity**: Firebase Hosting provides a straightforward deployment process with CDN support, ideal for a web-based hiking app launched today.
- **Performance**: Global CDN and SSL ensure fast, secure access for users across regions.
- **Cost-Effectiveness**: Free tier with generous limits suits a prototype or small-scale project, with pay-as-you-go scaling for growth.
