# Database Schema and Deployment for Crowdsourced Hiking Information

## Database Schema Overview

The following UML diagram illustrates the complete database schema and relationships for the Orion hiking application:

![Database Schema UML Diagram](../images/UML.png)

*Figure 1: Complete database schema showing all collections, their attributes, and relationships*

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
    - `id`: String (UUID generated client-side)
    - `userId`: String (Firebase Auth UID)
    - `userName`: String (display name or email, can be "Anonymous")
    - `userEmail`: String (user's email address for reference)
    - `rating`: Number (1-5)
    - `comment`: String (review text content)
    - `message`: String (alternative field name for comment, used in some components)
    - `timestamp`: String (ISO 8601 timestamp)
    - `photos`: Array of Strings (URLs to Firebase Storage) - *Note: Currently not implemented in submission*
  - **Purpose**: Captures user reviews and ratings linked to specific trails. Supports both authenticated and anonymous submissions.

- **Users Collection**
  - **Document Fields:**
    - `submittedTrails`: Array of References to Trail documents (trails created by this user)
    - `favourites`: Array of References to Trail documents (user's favorite trails)
    - `completed`: Array of References to Trail documents (trails marked as completed by user)
    - `wishlist`: Array of References to Trail documents (trails user wants to hike)
    - `profileInfo`: Map (optional - e.g., `name`: String, `email`: String, `joinedDate`: Timestamp)
  - **Purpose**: Manages user profiles and their trail interactions.
  - **Note**: Trail references can be stored as either Firestore DocumentReference objects or string paths (e.g., "/Trails/abc123"). The `completed` field replaces the previously planned `completedHikes` field.

- **Alerts Collection**
  - **Document Fields:**
    - `trailId`: String (ID of the associated trail)
    - `message`: String (alert content/description)
    - `type`: String (e.g., "community", "authority", "emergency")
    - `comment`: String (optional additional details)
    - `timestamp`: Timestamp (when the alert was created)
    - `isActive`: Boolean (whether the alert is currently active)
    - `isTimed`: Boolean (whether this is a timed alert with expiration)
    - `expiresAt`: Timestamp (when the alert expires, only present if `isTimed` is true)
    - `duration`: Number (duration in minutes, used during creation but not stored)
  - **Purpose**: Stores real-time alerts and status updates for trails, supporting both permanent and timed alerts with automatic expiration.
  - **Features**:
    - **Timed Alerts**: Automatically expire after a specified duration
    - **Permanent Alerts**: Remain active until manually removed
    - **Client-side Filtering**: Expired alerts are filtered out on the frontend
    - **Real-time Updates**: Alerts update in real-time across all components
    - **Batch Loading**: Optimized for loading multiple trail alerts simultaneously

- **Reports Collection**
  - **Document Fields:**
    - `type`: String (e.g., "trail", "review", "image", "alert", "general")
    - `category`: String (specific category based on report type, e.g., "inaccurate_info", "safety_concern", "spam", "bug_report")
    - `description`: String (detailed description of the issue being reported)
    - `priority`: String (e.g., "low", "medium", "high", "urgent")
    - `additionalDetails`: String (optional additional information)
    - `targetId`: String (ID of the specific item being reported - review, image, alert, etc.)
    - `trailId`: String (ID of the associated trail, if applicable)
    - `trailName`: String (name of the trail for reference)
    - `reporterId`: String (Firebase Auth UID of the user who submitted the report)
    - `status`: String (e.g., "pending", "reviewed", "resolved", "dismissed")
    - `createdAt`: Timestamp (when the report was created)
    - `updatedAt`: Timestamp (when the report status was last updated)
    - `timestamp`: String (ISO 8601 timestamp, alternative to createdAt)
  - **Purpose**: Manages user-submitted reports for content moderation, safety concerns, and general feedback.
  - **Report Types and Categories**:
    - **Trail Reports**: inaccurate_info, safety_concern, accessibility, maintenance, inappropriate_content, duplicate, other
    - **Review Reports**: inappropriate_content, spam, harassment, false_information, off_topic, other
    - **Image Reports**: inappropriate_content, not_trail_related, poor_quality, duplicate, copyright_violation, other
    - **Alert Reports**: false_information, outdated, inappropriate, spam, other
    - **General Reports**: bug_report, feature_request, inappropriate_content, spam, other
  - **Features**:
    - **Admin Management**: Full CRUD operations via ReportsManagement component
    - **Status Tracking**: Reports progress through pending → reviewed → resolved/dismissed workflow
    - **Priority Levels**: Four-tier priority system (low, medium, high, urgent)
    - **Filtering**: Reports can be filtered by status and type in admin interface
    - **Real-time Updates**: Status changes update immediately across admin interface

### Relationships
- **Trails to Users**: `createdBy` references the creating User; `submittedTrails` in Users links back.
- **Trails to Reviews**: Nested subcollection with `userId` containing Firebase Auth UID (not document reference).
- **Users to Trails**: Arrays (`favourites`, `completed`, `wishlist`, `submittedTrails`) hold Trail references.
- **Trails to Alerts**: `trailId` references the associated Trail.
- **Trails to Reports**: `trailId` references the associated Trail (when report is trail-related).
- **Users to Reports**: `reporterId` contains Firebase Auth UID of the user who submitted the report.
- **Reports to Content**: `targetId` references specific content being reported (reviews, images, alerts, etc.).

## Alert System Architecture

### Frontend Components
- **AlertModal**: Universal modal for creating alerts (used on Trail Detail and Reviews & Media pages)
- **AlertsPopup**: Displays active alerts with countdown timers for timed alerts
- **useTrailAlerts Hook**: Manages alert state, caching, and provides batch loading functionality
- **AlertsManagement**: Admin panel for managing all alerts
- **AlertsUpdates**: User page showing alerts for saved trails

## Reports System Architecture

### Frontend Components
- **ReportModal**: Universal modal for creating reports (supports trail, review, image, alert, and general reports)
- **ReportsManagement**: Admin panel for managing all reports with filtering and status updates
- **useTrailModals Hook**: Manages report submission and modal state
- **ReportModal Integration**: Used across Trail Detail, Reviews & Media, and general feedback pages

### Report Types
1. **Trail Reports**: Issues with trail information, safety concerns, accessibility, maintenance needs
2. **Review Reports**: Inappropriate content, spam, harassment, false information in reviews
3. **Image Reports**: Inappropriate content, poor quality, copyright violations, off-topic images
4. **Alert Reports**: False information, outdated alerts, inappropriate content in alerts
5. **General Reports**: Bug reports, feature requests, general feedback, spam

### Report Lifecycle
1. **Creation**: Users create reports via ReportModal with specific categories and priority levels
2. **Storage**: Reports stored in Firestore with `pending` status and server timestamp
3. **Admin Review**: Admins view reports in ReportsManagement with filtering by status and type
4. **Status Updates**: Reports progress through pending → reviewed → resolved/dismissed workflow
5. **Management**: Admins can update status, delete reports, and track resolution progress

### Alert Types
1. **Community Alerts**: User-submitted alerts about trail conditions
2. **Authority Alerts**: Official alerts from park authorities
3. **Emergency Alerts**: Critical safety information

### Alert Lifecycle
1. **Creation**: Users create alerts via AlertModal with optional duration
2. **Storage**: Alerts stored in Firestore with `isTimed` and `expiresAt` fields
3. **Display**: Active alerts shown in popups with real-time countdown timers
4. **Expiration**: Timed alerts automatically filtered out when expired
5. **Management**: Admins can view and delete alerts via AlertsManagement

### Performance Optimizations
- **Batch Loading**: `fetchMultipleTrailAlerts()` loads alerts for multiple trails in parallel
- **Client-side Caching**: Alerts cached to prevent redundant Firestore queries
- **Expired Alert Filtering**: Client-side filtering removes expired alerts without server calls
- **Real-time Updates**: Components update automatically when alerts change

## Cloud Functions (Firebase Functions)

### Alert Management Functions
- **`addAlert`** (Deprecated): Legacy function for adding alerts via API
  - **Note**: Now deprecated in favor of direct Firestore access from frontend
  - **Purpose**: Backward compatibility for existing integrations
  - **Body Parameters**: `{ trailId, message, type, duration }`
  - **Response**: `{ success: boolean, message: string }`

- **`cleanupExpiredAlerts`** (Scheduled): Automated cleanup of expired alerts
  - **Schedule**: Runs every hour via Firebase Scheduler
  - **Purpose**: Removes expired alerts from Firestore to maintain database efficiency
  - **Process**: Queries for alerts where `expiresAt < now()` and deletes them
  - **Logging**: Logs cleanup statistics for monitoring

### Function Configuration
```javascript
// functions/index.js
exports.addAlert = functions.https.onRequest((req, res) => {
  // Legacy alert creation endpoint
});

exports.cleanupExpiredAlerts = functions.pubsub.schedule('every 1 hours').onRun(async (context) => {
  // Automated cleanup of expired alerts
});
```

## Recent System Improvements

### Performance Optimizations (December 2024)
- **Parallel Alert Loading**: Replaced sequential `for` loops with `Promise.all()` for 10x faster alert loading
- **Batch State Updates**: Single state updates instead of multiple individual updates
- **Enhanced Caching**: Improved cache utilization in `useTrailAlerts` hook
- **Client-side Filtering**: Expired alerts filtered on frontend to reduce server load

### CSS Architecture Improvements
- **Unique Class Naming**: All MyTrails components use `my-trails-` prefix to prevent global CSS conflicts
- **Modal System**: Universal AlertModal with proper visibility control
- **Responsive Design**: Optimized for mobile, tablet, and desktop layouts
- **Theme Support**: Dark/light mode compatibility maintained

### Alert System Features
- **Timed vs Permanent**: Visual distinction with badges (Clock icon for timed, AlertCircle for permanent)
- **Real-time Countdown**: Live countdown timers for timed alerts
- **Automatic Expiration**: Client-side filtering removes expired alerts
- **Admin Management**: Full CRUD operations for alerts in admin panel
- **User Experience**: Non-scrollable popups showing all active alerts

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
