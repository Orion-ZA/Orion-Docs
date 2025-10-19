# Development Guide  

## 🗃 Database Setup

> This guide uses **Cloud Firestore** (not Realtime Database) and the **Web v9 modular SDK**.

---

### 1) Create a Firebase project
1. Go to the [Firebase Console](https://console.firebase.google.com) and **Add project**.
2. Give it a name → (optional) enable Analytics → **Create project**.

---

### 2) Enable Firestore
1. In your project, go to **Build → Firestore Database**.
2. Click **Create database**.
3. **Start in production test mode**.
4. Chose a **location/region** close to our users → **Enable**.

---

### 3) Register a Web App & get config
1. In **Project settings → Your apps**, click **Web** (`</>`).
2. Give the app a nickname → **Register app**.
3. Copy the **Firebase config** (apiKey, authDomain, projectId, etc.).

---

### 4) Install Firebase SDK
```bash
npm install firebase
# or
yarn add firebase
```

---

### 5) Initialize Firebase & Firestore
Create `src/lib/firebase.ts` (or `.js`):

```ts
// src/lib/firebase.ts
import { initializeApp, getApps, getApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";

const firebaseConfig = {
  apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY,
  authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
  projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
  storageBucket: process.env.NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: process.env.NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID,
  appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID,
};

const app = !getApps().length ? initializeApp(firebaseConfig) : getApp();
export const db = getFirestore(app);
```

Add these to `.env.local`:

```env
NEXT_PUBLIC_FIREBASE_API_KEY=xxxxx
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=yourapp.firebaseapp.com
NEXT_PUBLIC_FIREBASE_PROJECT_ID=yourapp
NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=yourapp.appspot.com
NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=1234567890
NEXT_PUBLIC_FIREBASE_APP_ID=1:1234567890:web:abcdef123456
```

---

### 6) Do a quick read/write (CRUD)

#### Add a document
```ts
import { collection, addDoc } from "firebase/firestore";
import { db } from "@/lib/firebase";

await addDoc(collection(db, "users"), {
  name: "Spongebob",
  createdAt: Date.now()
});
```

#### Read documents
```ts
import { collection, getDocs, query, where, orderBy, limit } from "firebase/firestore";
import { db } from "@/lib/firebase";

const q = query(
  collection(db, "users"),
  where("name", "==", "Spongebob"),
  orderBy("createdAt", "desc"),
  limit(10)
);

const snap = await getDocs(q);
const users = snap.docs.map(d => ({ id: d.id, ...d.data() }));
```

#### Update / Delete
```ts
import { doc, updateDoc, deleteDoc } from "firebase/firestore";

await updateDoc(doc(db, "users", "DOC_ID"), { name: "Ada L." });
await deleteDoc(doc(db, "users", "DOC_ID"));
```

---

### 7) Secure your database (Rules)
Go to **Firestore → Rules** and set rules like:

```rules
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {

    // Require authentication
    function isSignedIn() {
      return request.auth != null;
    }

    // Example: per-user data
    match /users/{uid} {
      allow read, write: if isSignedIn() && request.auth.uid == uid;
    }

    // Public, read-only collection
    match /public/{document=**} {
      allow read: if true;
      allow write: if false;
    }
  }
}
```

---

### Minimal Example (React Component)
```tsx
import { useEffect, useState } from "react";
import { collection, addDoc, getDocs } from "firebase/firestore";
import { db } from "@/lib/firebase";

export default function Demo() {
  const [items, setItems] = useState<any[]>([]);

  useEffect(() => {
    (async () => {
      const snap = await getDocs(collection(db, "items"));
      setItems(snap.docs.map(d => ({ id: d.id, ...d.data() })));
    })();
  }, []);

  const addItem = async () => {
    await addDoc(collection(db, "items"), { text: "Hello Firestore", ts: Date.now() });
  };

  return (
    <div>
      <button onClick={addItem}>Add item</button>
      <ul>{items.map(i => <li key={i.id}>{i.text}</li>)}</ul>
    </div>
  );
}
```

## ⚛ React Development Site Setup
### 🚀 Project Setup

1) Create a React Project

  ```bash
  npx create-react-app Orion --template typescript
  cd Orion
  ```

2) Install Dependencies

  ```bash
  npm install firebase react-router-dom @types/react-router-dom
  # or
  yarn add firebase react-router-dom @types/react-router-dom
  ```

### ⚙️ Application Setup

1) Create Firebase Configuration File

  Create `src/firebase.ts`:

  ```typescript
  import { initializeApp, getApps, getApp } from "firebase/app";
  import { getFirestore } from "firebase/firestore";

  const firebaseConfig = {
    apiKey: process.env.REACT_APP_FIREBASE_API_KEY,
    authDomain: process.env.REACT_APP_FIREBASE_AUTH_DOMAIN,
    projectId: process.env.REACT_APP_FIREBASE_PROJECT_ID,
    storageBucket: process.env.REACT_APP_FIREBASE_STORAGE_BUCKET,
    messagingSenderId: process.env.REACT_APP_FIREBASE_MESSAGING_SENDER_ID,
    appId: process.env.REACT_APP_FIREBASE_APP_ID,
  };

  // Initialize Firebase
  const app = !getApps().length ? initializeApp(firebaseConfig) : getApp();
  const db = getFirestore(app);

  export { db };
  ```

2) Set Up Environment Variables

  Create `.env` file in your project root:

  ```env
  REACT_APP_FIREBASE_API_KEY=your-api-key
  REACT_APP_FIREBASE_AUTH_DOMAIN=your-project.firebaseapp.com
  REACT_APP_FIREBASE_PROJECT_ID=your-project-id
  REACT_APP_FIREBASE_STORAGE_BUCKET=your-bucket.appspot.com
  REACT_APP_FIREBASE_MESSAGING_SENDER_ID=your-sender-id
  REACT_APP_FIREBASE_APP_ID=your-app-id
  ```

### 📖 Basic CRUD Operations

1) Create a Data Service
  Create `src/services/firestoreService.ts`:
  ```bash
  import { 
    collection, 
    addDoc, 
    getDocs, 
    doc, 
    updateDoc, 
    deleteDoc,
    query,
    where,
    orderBy,
    limit
  } from "firebase/firestore";
  import { db } from "../firebase";

  // Add a new document
  export const addDocument = async (collectionName: string, data: any) => {
    try {
      const docRef = await addDoc(collection(db, collectionName), data);
      return docRef.id;
    } catch (error) {
      console.error("Error adding document: ", error);
      throw error;
    }
  };

  // Get all documents
  export const getDocuments = async (collectionName: string) => {
    try {
      const querySnapshot = await getDocs(collection(db, collectionName));
      return querySnapshot.docs.map(doc => ({ id: doc.id, ...doc.data() }));
    } catch (error) {
      console.error("Error getting documents: ", error);
      throw error;
    }
  };

  // Update a document
  export const updateDocument = async (
    collectionName: string,
    docId: string,
    data: any
  ) => {
    try {
      await updateDoc(doc(db, collectionName, docId), data);
    } catch (error) {
      console.error("Error updating document: ", error);
      throw error;
    }
  };

  // Delete a document
  export const deleteDocument = async (collectionName: string, docId: string) => {
    try {
      await deleteDoc(doc(db, collectionName, docId));
    } catch (error) {
      console.error("Error deleting document: ", error);
      throw error;
    }
  };

  // Query documents
  export const queryDocuments = async (
    collectionName: string,
    field: string,
    operator: any,
    value: any
  ) => {
    try {
      const q = query(
        collection(db, collectionName),
        where(field, operator, value)
      );
      const querySnapshot = await getDocs(q);
      return querySnapshot.docs.map(doc => ({ id: doc.id, ...doc.data() }));
    } catch (error) {
      console.error("Error querying documents: ", error);
      throw error;
    }
  };
```

### Example React Component

Create `src/components/ItemsList.tsx`:

```typescript
import React, { useState, useEffect } from 'react';
import { 
  getDocuments, 
  addDocument, 
  updateDocument, 
  deleteDocument 
} from '../services/firestoreService';

interface Item {
  id: string;
  name: string;
  description?: string;
  createdAt: number;
}

const ItemsList: React.FC = () => {
  const [items, setItems] = useState<Item[]>([]);
  const [newItemName, setNewItemName] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchItems = async () => {
      try {
        const itemsData = await getDocuments('items');
        setItems(itemsData as Item[]);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching items:', error);
        setLoading(false);
      }
    };

    fetchItems();
  }, []);

  const handleAddItem = async () => {
    if (!newItemName.trim()) return;

    try {
      setLoading(true);
      const newItem = {
        name: newItemName,
        createdAt: Date.now()
      };
      await addDocument('items', newItem);
      const updatedItems = await getDocuments('items');
      setItems(updatedItems as Item[]);
      setNewItemName('');
      setLoading(false);
    } catch (error) {
      console.error('Error adding item:', error);
      setLoading(false);
    }
  };

  const handleDeleteItem = async (id: string) => {
    try {
      setLoading(true);
      await deleteDocument('items', id);
      setItems(items.filter(item => item.id !== id));
      setLoading(false);
    } catch (error) {
      console.error('Error deleting item:', error);
      setLoading(false);
    }
  };

  if (loading) return <div>Loading...</div>;

  return (
    <div>
      <h2>Items List</h2>
      <div>
        <input
          type="text"
          value={newItemName}
          onChange={(e) => setNewItemName(e.target.value)}
          placeholder="New item name"
        />
        <button onClick={handleAddItem}>Add Item</button>
      </div>
      <ul>
        {items.map((item) => (
          <li key={item.id}>
            <h3>{item.name}</h3>
            <p>Created: {new Date(item.createdAt).toLocaleString()}</p>
            <button onClick={() => handleDeleteItem(item.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ItemsList;
```

### 🔒 Security Rules

Go to Firestore → Rules and set up proper security:

```js
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read, write: if false;
    }
    
    // Example rules for an items collection
    match /items/{itemId} {
      allow read: if true;
      allow create: if request.auth != null;
      allow update, delete: if request.auth != null && 
                             request.resource.data.userId == request.auth.uid;
    }
  }
}
```

### 🏁 Final Steps

1. Set up routing in `src/App.tsx`:

  ```js
  import React from 'react';
  import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
  import ItemsList from './components/ItemsList';
  import './App.css';

  function App() {
    return (
      <Router>
        <div className="App">
          <Routes>
            <Route path="/" element={<ItemsList />} />
            <Route path="/items" element={<ItemsList />} />
          </Routes>
        </div>
      </Router>
    );
  }

  export default App;
  ```
2. Run your app:
  ```bash
  npm start
  ```

## ⚙️ API Setup

### 🚀 Firebase Functions Setup

1) Install Firebase CLI
  ```bash
  npm install -g firebase-tools
  # or
  yarn global add firebase-tools
  ```
2) Login to Firebase
  ```bash
  firebase login
  ```
3) Initialize Firebase in your project
  ```bash
  cd Orion
  firebase init
  ```

Select:
- Functions (using spacebar to select)
- TypeScript
- Install dependencies now

### ⚙️ Project Structure

Your project will now have:

  ```text
  your-react-project/
    ├── public/
    ├── src/
    ├── functions/  # <-- New Firebase Functions folder
    │   ├── src/
    │   │   ├── index.ts
    │   ├── package.json
    ├── firebase.json
  ```

### 🔥 Basic API Endpoint Setup

1) Create your first API endpoint

  Edit `functions/src/index.ts`:

    ```js
    import * as functions from "firebase-functions";
    import * as admin from "firebase-admin";

    admin.initializeApp();

    // Simple ping endpoint
    export const ping = functions.https.onRequest((req, res) => {
      res.status(200).send({ message: "Pong!", timestamp: Date.now() });
    });

    // Example CRUD endpoints
    export const createItem = functions.https.onRequest(async (req, res) => {
      try {
        if (req.method !== "POST") {
          return res.status(405).send("Method Not Allowed");
        }

        const { name, description } = req.body;
        
        if (!name) {
          return res.status(400).send("Name is required");
        }

        const docRef = await admin.firestore().collection("items").add({
          name,
          description: description || "",
          createdAt: admin.firestore.FieldValue.serverTimestamp(),
          updatedAt: admin.firestore.FieldValue.serverTimestamp()
        });

        return res.status(201).send({ id: docRef.id });
      } catch (error) {
        functions.logger.error("Error creating item:", error);
        return res.status(500).send("Internal Server Error");
      }
    });

    export const getItems = functions.https.onRequest(async (req, res) => {
      try {
        if (req.method !== "GET") {
          return res.status(405).send("Method Not Allowed");
        }

        const snapshot = await admin.firestore().collection("items")
          .orderBy("createdAt", "desc")
          .get();

        const items = snapshot.docs.map(doc => ({
          id: doc.id,
          ...doc.data()
        }));

        return res.status(200).send(items);
      } catch (error) {
        functions.logger.error("Error getting items:", error);
        return res.status(500).send("Internal Server Error");
      }
    });
    ```

2) Deploy your functions
  ```bash
  firebase deploy --only functions
  ```

After deployment, you'll get URLs like:

  ```text
  Function URLs:
    - ping: https://us-central1-your-project.cloudfunctions.net/ping
    - createItem: https://us-central1-your-project.cloudfunctions.net/createItem
    - getItems: https://us-central1-your-project.cloudfunctions.net/getItems
  ```

### 🔄 Connect React to Your API

  1) Create an API service in your React app
    
    Create `src/services/api.ts`:

      ```ts
      const API_BASE_URL = 'https://us-central1-your-project.cloudfunctions.net';

      export const pingApi = async () => {
        const response = await fetch(`${API_BASE_URL}/ping`);
        return response.json();
      };

      export const createItem = async (itemData: { name: string; description?: string }) => {
        const response = await fetch(`${API_BASE_URL}/createItem`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(itemData),
        });
        return response.json();
      };

      export const getItems = async () => {
        const response = await fetch(`${API_BASE_URL}/getItems`);
        return response.json();
      };
      ```
  2) Update your React component to use the API

    Modify `src/components/ItemsList.tsx`:
      ```ts
      import React, { useState, useEffect } from 'react';
      import { getItems, createItem } from '../services/api';

      interface Item {
        id: string;
        name: string;
        description?: string;
        createdAt: string;
      }

      const ItemsList: React.FC = () => {
        const [items, setItems] = useState<Item[]>([]);
        const [newItemName, setNewItemName] = useState('');
        const [loading, setLoading] = useState(true);
        const [error, setError] = useState<string | null>(null);

        useEffect(() => {
          const fetchItems = async () => {
            try {
              const data = await getItems();
              setItems(data);
              setLoading(false);
            } catch (err) {
              setError('Failed to load items');
              setLoading(false);
            }
          };

          fetchItems();
        }, []);

        const handleAddItem = async () => {
          if (!newItemName.trim()) return;

          try {
            setLoading(true);
            const newItem = await createItem({ name: newItemName });
            setItems(prev => [{ ...newItem, name: newItemName }, ...prev]);
            setNewItemName('');
            setLoading(false);
          } catch (err) {
            setError('Failed to add item');
            setLoading(false);
          }
        };

        if (loading) return <div>Loading...</div>;
        if (error) return <div>Error: {error}</div>;

        return (
          <div>
            <h2>Items List</h2>
            <div>
              <input
                type="text"
                value={newItemName}
                onChange={(e) => setNewItemName(e.target.value)}
                placeholder="New item name"
              />
              <button onClick={handleAddItem}>Add Item</button>
            </div>
            <ul>
              {items.map((item) => (
                <li key={item.id}>
                  <h3>{item.name}</h3>
                  {item.description && <p>{item.description}</p>}
                  <p>Created: {new Date(item.createdAt).toLocaleString()}</p>
                </li>
              ))}
            </ul>
          </div>
        );
      };

      export default ItemsList;
      ```

### 🔒 Secure Your API with Authentication

1) Update your Firebase Function to check authentication

  Modify `functions/src/index.ts`:

    ```ts
    export const createItem = functions.https.onRequest(async (req, res) => {
      // Check for authentication
      if (!req.headers.authorization) {
        return res.status(401).send('Unauthorized');
      }

      const token = req.headers.authorization.split('Bearer ')[1];
      
      try {
        const decodedToken = await admin.auth().verifyIdToken(token);
        const { name, description } = req.body;
        
        if (!name) {
          return res.status(400).send("Name is required");
        }

        const docRef = await admin.firestore().collection("items").add({
          name,
          description: description || "",
          createdAt: admin.firestore.FieldValue.serverTimestamp(),
          updatedAt: admin.firestore.FieldValue.serverTimestamp(),
          userId: decodedToken.uid
        });

        return res.status(201).send({ id: docRef.id });
      } catch (error) {
        if (error.code === 'auth/id-token-expired' || error.code === 'auth/id-token-invalid') {
          return res.status(401).send('Unauthorized');
        }
        functions.logger.error("Error creating item:", error);
        return res.status(500).send("Internal Server Error");
      }
    });
    ```

2) Update your React app to send auth tokens
  Modify `src/services/api.ts`:
    ```ts
    import { getAuth } from "firebase/auth";

    const API_BASE_URL = 'https://us-central1-your-project.cloudfunctions.net';

    const getAuthToken = async () => {
      const auth = getAuth();
      const user = auth.currentUser;
      if (!user) throw new Error('User not authenticated');
      return user.getIdToken();
    };

    export const createItem = async (itemData: { name: string; description?: string }) => {
      const token = await getAuthToken();
      const response = await fetch(`${API_BASE_URL}/createItem`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify(itemData),
      });
      return response.json();
    };
    ```

### 🛠 Testing Your API Locally

1. Start the Firebase emulator:

  ```bash
  firebase emulators:start
  ```

2. Test endpoints with cURL:

  ```bash
  # Public endpoint
  curl http://localhost:5001/your-project/us-central1/api/ping

  # Authenticated endpoint (after getting a token)
  curl -H "Authorization: Bearer YOUR_ID_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{"name":"Test Item"}' \
    http://localhost:5001/your-project/us-central1/api/items
  ```

### 🚀 Deployment

Deploy your updated functions:

```bash
firebase deploy --only functions
```

## 🚀 Express.js API Setup

### 🏗️ Project Structure

Create a new Express.js API project:

```bash
mkdir orion-api
cd orion-api
npm init -y
```

### 📦 Install Dependencies

```bash
# Core dependencies
npm install express firebase-admin cors helmet express-rate-limit joi dotenv express-validator multer compression morgan

# Development dependencies
npm install --save-dev nodemon jest supertest eslint

# Documentation
npm install swagger-jsdoc swagger-ui-express
```

### ⚙️ Project Structure

```
orion-api/
├── src/
│   ├── app.js                 # Main application file
│   ├── config/
│   │   ├── database.js        # Firebase configuration
│   │   └── swagger.js         # Swagger documentation
│   ├── controllers/
│   │   ├── trailController.js # Trail CRUD operations
│   │   ├── userController.js  # User management
│   │   ├── alertController.js # Trail alerts
│   │   ├── reviewController.js # Trail reviews
│   │   └── reportController.js # Trail reports
│   ├── middleware/
│   │   └── errorHandler.js    # Error handling middleware
│   ├── models/
│   │   ├── Trail.js          # Trail model and validation
│   │   └── User.js           # User model and validation
│   ├── routes/
│   │   ├── trailRoutes.js    # Trail API routes
│   │   ├── userRoutes.js     # User API routes
│   │   ├── alertRoutes.js    # Alert API routes
│   │   ├── reviewRoutes.js   # Review API routes
│   │   └── reportRoutes.js   # Report API routes
│   └── validation/
│       └── trailValidation.js # Joi validation schemas
├── tests/
│   └── trail.test.js         # API tests
├── package.json
├── .env                      # Environment variables
├── .gitignore
├── Procfile                  # For Render deployment
├── Dockerfile               # For containerized deployment
└── README.md
```

### 🔥 Firebase Admin SDK Setup

1) **Create Firebase Service Account**

   - Go to [Firebase Console](https://console.firebase.google.com/)
   - Select your project → Project Settings → Service Accounts
   - Click "Generate new private key"
   - Download the JSON file

2) **Set up Environment Variables**

   Create `.env` file:

   ```env
   # Server Configuration
   PORT=3000
   NODE_ENV=development

   # Firebase Configuration
   FIREBASE_PROJECT_ID=your-firebase-project-id
   FIREBASE_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\nYOUR_PRIVATE_KEY_HERE\n-----END PRIVATE KEY-----\n"
   FIREBASE_CLIENT_EMAIL=your-service-account@your-project.iam.gserviceaccount.com
   FIREBASE_STORAGE_BUCKET=your-firebase-storage-bucket.appspot.com

   # Security
   JWT_SECRET=your-super-secret-jwt-key-here
   API_RATE_LIMIT=100

   # CORS
   ALLOWED_ORIGINS=http://localhost:3000,http://localhost:3001,https://orion-sdp.web.app
   ```

3) **Create Database Configuration**

   Create `src/config/database.js`:

   ```javascript
   const admin = require('firebase-admin');

   let db = null;

   const connectDB = async () => {
     try {
       // Initialize Firebase Admin SDK
       if (!admin.apps.length) {
         const serviceAccount = {
           projectId: process.env.FIREBASE_PROJECT_ID,
           privateKey: process.env.FIREBASE_PRIVATE_KEY?.replace(/\\n/g, '\n'),
           clientEmail: process.env.FIREBASE_CLIENT_EMAIL,
         };

         admin.initializeApp({
           credential: admin.credential.cert(serviceAccount),
           storageBucket: process.env.FIREBASE_STORAGE_BUCKET,
         });
       }

       // Get Firestore instance
       db = admin.firestore();
       
       // Test connection
       await db.collection('Trails').limit(1).get();
       
       console.log('🔥 Firebase Firestore Connected');
     } catch (error) {
       console.error('❌ Firebase connection error:', error.message);
       process.exit(1);
     }
   };

   // Get Firestore instance
   const getDB = () => {
     if (!db) {
       throw new Error('Database not initialized. Call connectDB() first.');
     }
     return db;
   };

   // Get Firebase Admin instance
   const getAdmin = () => {
     return admin;
   };

   // Graceful shutdown
   process.on('SIGINT', async () => {
     console.log('🔌 Firebase connection closed through app termination');
     process.exit(0);
   });

   module.exports = { connectDB, getDB, getAdmin };
   ```

### 🚀 Express Application Setup

Create `src/app.js`:

```javascript
const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const compression = require('compression');
const morgan = require('morgan');
const rateLimit = require('express-rate-limit');
require('dotenv').config();

const { connectDB } = require('./config/database');
const trailRoutes = require('./routes/trailRoutes');
const userRoutes = require('./routes/userRoutes');
const alertRoutes = require('./routes/alertRoutes');
const reviewRoutes = require('./routes/reviewRoutes');
const reportRoutes = require('./routes/reportRoutes');
const errorHandler = require('./middleware/errorHandler');
const swaggerSpecs = require('./config/swagger');
const swaggerUi = require('swagger-ui-express');

const app = express();

// Connect to Firebase Firestore
connectDB();

// Security middleware
app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      connectSrc: ["'self'", "https://*.onrender.com"],
      scriptSrc: ["'self'", "'unsafe-inline'"],
      styleSrc: ["'self'", "'unsafe-inline'", "https://fonts.googleapis.com"],
      fontSrc: ["'self'", "https://fonts.gstatic.com"],
      imgSrc: ["'self'", "data:", "https:"],
      objectSrc: ["'none'"],
      upgradeInsecureRequests: [],
    },
  },
  crossOriginEmbedderPolicy: false
}));
app.use(compression());

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: process.env.API_RATE_LIMIT || 100, // limit each IP to 100 requests per windowMs
  message: 'Too many requests from this IP, please try again later.'
});
app.use('/api/', limiter);

// CORS configuration
const corsOptions = {
  origin: function (origin, callback) {
    // Allow requests with no origin (like mobile apps or curl requests)
    if (!origin) return callback(null, true);
    
    const allowedOrigins = process.env.ALLOWED_ORIGINS?.split(',') || [
      'http://localhost:3000',
      'https://orion-sdp.web.app'
    ];
    
    if (allowedOrigins.indexOf(origin) !== -1) {
      callback(null, true);
    } else {
      // For development, allow any origin
      if (process.env.NODE_ENV === 'development') {
        callback(null, true);
      } else {
        callback(new Error('Not allowed by CORS'));
      }
    }
  },
  credentials: true,
  optionsSuccessStatus: 200,
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Authorization', 'Accept', 'Origin', 'X-Requested-With']
};
app.use(cors(corsOptions));

// Handle preflight requests
app.options('*', cors(corsOptions));

// Logging
if (process.env.NODE_ENV === 'development') {
  app.use(morgan('dev'));
} else {
  app.use(morgan('combined'));
}

// Body parsing middleware
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true, limit: '10mb' }));

// Health check endpoints
app.get('/health', (req, res) => {
  res.status(200).json({
    status: 'OK',
    timestamp: new Date().toISOString(),
    uptime: process.uptime()
  });
});

app.get('/health/db', async (req, res) => {
  try {
    const { getDB } = require('./config/database');
    const db = getDB();
    
    // Test database connection
    const testDoc = await db.collection('Trails').limit(1).get();
    
    res.status(200).json({
      status: 'OK',
      database: 'Connected',
      timestamp: new Date().toISOString(),
      trailsCount: testDoc.size,
      message: 'Successfully connected to Trails collection'
    });
  } catch (error) {
    console.error('Database health check failed:', error);
    res.status(500).json({
      status: 'ERROR',
      database: 'Disconnected',
      error: error.message,
      timestamp: new Date().toISOString()
    });
  }
});

// API Documentation
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerSpecs, {
  explorer: true,
  customCss: '.swagger-ui .topbar { display: none }',
  customSiteTitle: 'Orion Trail API Documentation',
  swaggerOptions: {
    url: '/api-docs/swagger.json',
    validatorUrl: null,
    tryItOutEnabled: true
  }
}));

// API routes
app.use('/api/trails', trailRoutes);
app.use('/api/users', userRoutes);
app.use('/api/alerts', alertRoutes);
app.use('/api/reviews', reviewRoutes);
app.use('/api/reports', reportRoutes);

// 404 handler
app.use('*', (req, res) => {
  res.status(404).json({
    success: false,
    message: 'Route not found'
  });
});

// Error handling middleware
app.use(errorHandler);

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`🚀 Server running on port ${PORT}`);
  console.log(`📚 API Documentation: http://localhost:${PORT}/api-docs`);
});

module.exports = app;
```

### 📝 Package.json Scripts

Update your `package.json`:

```json
{
  "scripts": {
    "start": "node src/app.js",
    "dev": "nodemon src/app.js",
    "test": "jest",
    "lint": "eslint src/",
    "build": "echo 'No build step required'",
    "heroku-postbuild": "npm install"
  },
  "engines": {
    "node": ">=16.0.0"
  }
}
```

### 🧪 Testing Your API

1) **Start the development server:**

   ```bash
   npm run dev
   ```

2) **Test with curl:**

   ```bash
   # Health check
   curl http://localhost:3000/health

   # Create a trail
   curl -X POST http://localhost:3000/api/trails \
     -H "Content-Type: application/json" \
     -d '{
       "name": "Test Trail",
       "location": {"latitude": 40.7128, "longitude": -74.0060},
       "distance": 3.5,
       "elevationGain": 500,
       "difficulty": "Easy",
       "description": "A test trail",
       "createdBy": "test-user"
     }'

   # Get all trails
   curl http://localhost:3000/api/trails
   ```

3) **Access API Documentation:**

   Visit: `http://localhost:3000/api-docs`

## 🚀 Render Deployment

### 📋 Prerequisites

1. **GitHub Repository**: Push your code to GitHub
2. **Render Account**: Sign up at [render.com](https://render.com)
3. **Environment Variables**: Prepare your production environment variables

### 🔧 Render Setup

1) **Create New Web Service**

   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select your `orion-api` repository

2) **Configure Service Settings**

   ```
   Name: orion-api
   Environment: Node
   Region: Oregon (US West)
   Branch: main (or your default branch)
   Root Directory: (leave empty)
   Build Command: npm install
   Start Command: npm start
   ```

3) **Set Environment Variables**

   In the Render dashboard, go to Environment tab and add:

   ```
   NODE_ENV=production
   PORT=10000
   FIREBASE_PROJECT_ID=your-firebase-project-id
   FIREBASE_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\nYOUR_PRIVATE_KEY_HERE\n-----END PRIVATE KEY-----\n"
   FIREBASE_CLIENT_EMAIL=your-service-account@your-project.iam.gserviceaccount.com
   FIREBASE_STORAGE_BUCKET=your-firebase-storage-bucket.appspot.com
   JWT_SECRET=your-super-secret-jwt-key-here
   API_RATE_LIMIT=100
   ALLOWED_ORIGINS=https://orion-sdp.web.app,https://your-render-url.onrender.com
   ```

4) **Deploy**

   - Click "Create Web Service"
   - Render will automatically build and deploy your application
   - You'll get a URL like: `https://orion-api-xyz.onrender.com`

### 🔒 Production Security

1) **Update CORS Settings**

   Update your `src/app.js` CORS configuration:

   ```javascript
   const corsOptions = {
     origin: function (origin, callback) {
       if (!origin) return callback(null, true);
       
       const allowedOrigins = process.env.ALLOWED_ORIGINS?.split(',') || [
         'https://orion-sdp.web.app',
         'https://your-render-url.onrender.com'
       ];
       
       if (allowedOrigins.indexOf(origin) !== -1) {
         callback(null, true);
       } else {
         callback(new Error('Not allowed by CORS'));
       }
     },
     credentials: true,
     optionsSuccessStatus: 200,
     methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
     allowedHeaders: ['Content-Type', 'Authorization', 'Accept', 'Origin', 'X-Requested-With']
   };
   ```

2) **Environment-Specific Configuration**

   Create `src/config/environment.js`:

   ```javascript
   const config = {
     development: {
       port: 3000,
       cors: {
         origin: true, // Allow all origins in development
         credentials: true
       },
       logging: 'dev'
     },
     production: {
       port: process.env.PORT || 10000,
       cors: {
         origin: process.env.ALLOWED_ORIGINS?.split(',') || [],
         credentials: true
       },
       logging: 'combined'
     }
   };

   module.exports = config[process.env.NODE_ENV || 'development'];
   ```

### 📊 Monitoring & Health Checks

1) **Health Check Endpoints**

   Your API includes these health check endpoints:

   ```bash
   # Basic health check
   curl https://your-api.onrender.com/health

   # Database health check
   curl https://your-api.onrender.com/health/db
   ```

2) **Render Monitoring**

   - Render provides built-in monitoring
   - Check logs in the Render dashboard
   - Set up uptime monitoring
   - Monitor response times and error rates

### 🔄 Continuous Deployment

1) **Automatic Deployments**

   - Render automatically deploys when you push to your main branch
   - Each deployment gets a unique URL for testing
   - Production URL remains stable

2) **Manual Deployments**

   - Use Render dashboard to trigger manual deployments
   - Rollback to previous versions if needed
   - Preview deployments for pull requests

### 🧪 Testing Your Live API

1) **Test with curl:**

   ```bash
   # Health check
   curl https://your-api.onrender.com/health

   # Create a trail
   curl -X POST https://your-api.onrender.com/api/trails \
     -H "Content-Type: application/json" \
     -d '{
       "name": "Live Test Trail",
       "location": {"latitude": 40.7128, "longitude": -74.0060},
       "distance": 3.5,
       "elevationGain": 500,
       "difficulty": "Easy",
       "description": "Testing live API!",
       "createdBy": "live-test-user"
     }'

   # Get all trails
   curl https://your-api.onrender.com/api/trails
   ```

2) **Access Live Documentation:**

   Visit: `https://your-api.onrender.com/api-docs`

### 🚨 Troubleshooting

1) **Common Issues:**

   - **Build Failures**: Check your `package.json` scripts and dependencies
   - **Environment Variables**: Ensure all required variables are set
   - **CORS Errors**: Update `ALLOWED_ORIGINS` with your frontend URL
   - **Database Connection**: Verify Firebase service account credentials

2) **Debugging:**

   - Check Render logs in the dashboard
   - Use health check endpoints to verify connectivity
   - Test locally with production environment variables

### 📈 Performance Optimization

1) **Enable Compression**

   ```javascript
   app.use(compression());
   ```

2) **Rate Limiting**

   ```javascript
   const limiter = rateLimit({
     windowMs: 15 * 60 * 1000, // 15 minutes
     max: 100, // limit each IP to 100 requests per windowMs
     message: 'Too many requests from this IP, please try again later.'
   });
   app.use('/api/', limiter);
   ```

3) **Caching Headers**

   ```javascript
   app.use((req, res, next) => {
     if (req.path.startsWith('/api/')) {
       res.set('Cache-Control', 'no-cache');
     }
     next();
   });
   ```

Your Express.js API is now deployed and ready to serve your React application!

## 🔗 Connecting React App to Express API

### 📡 API Service Setup

1) **Create API Service in React App**

   Create `src/services/api.js`:

   ```javascript
   const API_BASE_URL = process.env.REACT_APP_API_URL || 'https://your-api.onrender.com';

   class ApiService {
     constructor() {
       this.baseURL = API_BASE_URL;
     }

     async request(endpoint, options = {}) {
       const url = `${this.baseURL}${endpoint}`;
       const config = {
         headers: {
           'Content-Type': 'application/json',
           ...options.headers,
         },
         ...options,
       };

       try {
         const response = await fetch(url, config);
         const data = await response.json();

         if (!response.ok) {
           throw new Error(data.message || 'Something went wrong');
         }

         return data;
       } catch (error) {
         console.error('API request failed:', error);
         throw error;
       }
     }

     // Trail endpoints
     async getTrails(params = {}) {
       const queryString = new URLSearchParams(params).toString();
       return this.request(`/api/trails${queryString ? `?${queryString}` : ''}`);
     }

     async getTrail(id) {
       return this.request(`/api/trails/${id}`);
     }

     async createTrail(trailData) {
       return this.request('/api/trails', {
         method: 'POST',
         body: JSON.stringify(trailData),
       });
     }

     async updateTrail(id, trailData) {
       return this.request(`/api/trails/${id}`, {
         method: 'PUT',
         body: JSON.stringify(trailData),
       });
     }

     async deleteTrail(id) {
       return this.request(`/api/trails/${id}`, {
         method: 'DELETE',
       });
     }

     async searchTrails(query, filters = {}) {
       const params = { q: query, ...filters };
       const queryString = new URLSearchParams(params).toString();
       return this.request(`/api/trails/search?${queryString}`);
     }

     async getTrailsNear(latitude, longitude, maxDistance = 10000) {
       const params = { latitude, longitude, maxDistance };
       const queryString = new URLSearchParams(params).toString();
       return this.request(`/api/trails/near?${queryString}`);
     }

     // Health check
     async healthCheck() {
       return this.request('/health');
     }
   }

   export default new ApiService();
   ```

2) **Set Environment Variables**

   Create `.env` file in your React app root:

   ```env
   REACT_APP_API_URL=https://your-api.onrender.com
   REACT_APP_FIREBASE_API_KEY=your-api-key
   REACT_APP_FIREBASE_AUTH_DOMAIN=your-project.firebaseapp.com
   REACT_APP_FIREBASE_PROJECT_ID=your-project-id
   REACT_APP_FIREBASE_STORAGE_BUCKET=your-bucket.appspot.com
   REACT_APP_FIREBASE_MESSAGING_SENDER_ID=your-sender-id
   REACT_APP_FIREBASE_APP_ID=your-app-id
   ```

### 🎣 Custom Hooks for API Integration

1) **Create Trail Hooks**

   Create `src/hooks/useTrails.js`:

   ```javascript
   import { useState, useEffect } from 'react';
   import apiService from '../services/api';

   export const useTrails = (params = {}) => {
     const [trails, setTrails] = useState([]);
     const [loading, setLoading] = useState(true);
     const [error, setError] = useState(null);
     const [pagination, setPagination] = useState(null);

     const fetchTrails = async (newParams = {}) => {
       try {
         setLoading(true);
         setError(null);
         const response = await apiService.getTrails({ ...params, ...newParams });
         setTrails(response.data);
         setPagination(response.pagination);
       } catch (err) {
         setError(err.message);
       } finally {
         setLoading(false);
       }
     };

     useEffect(() => {
       fetchTrails();
     }, []);

     return {
       trails,
       loading,
       error,
       pagination,
       refetch: fetchTrails,
     };
   };

   export const useTrail = (id) => {
     const [trail, setTrail] = useState(null);
     const [loading, setLoading] = useState(true);
     const [error, setError] = useState(null);

     useEffect(() => {
       if (!id) return;

       const fetchTrail = async () => {
         try {
           setLoading(true);
           setError(null);
           const response = await apiService.getTrail(id);
           setTrail(response.data);
         } catch (err) {
           setError(err.message);
         } finally {
           setLoading(false);
         }
       };

       fetchTrail();
     }, [id]);

     return { trail, loading, error };
   };

   export const useTrailActions = () => {
     const [loading, setLoading] = useState(false);
     const [error, setError] = useState(null);

     const createTrail = async (trailData) => {
       try {
         setLoading(true);
         setError(null);
         const response = await apiService.createTrail(trailData);
         return response.data;
       } catch (err) {
         setError(err.message);
         throw err;
       } finally {
         setLoading(false);
       }
     };

     const updateTrail = async (id, trailData) => {
       try {
         setLoading(true);
         setError(null);
         const response = await apiService.updateTrail(id, trailData);
         return response.data;
       } catch (err) {
         setError(err.message);
         throw err;
       } finally {
         setLoading(false);
       }
     };

     const deleteTrail = async (id) => {
       try {
         setLoading(true);
         setError(null);
         await apiService.deleteTrail(id);
       } catch (err) {
         setError(err.message);
         throw err;
       } finally {
         setLoading(false);
       }
     };

     return {
       createTrail,
       updateTrail,
       deleteTrail,
       loading,
       error,
     };
   };
   ```

2) **Create Search Hook**

   Create `src/hooks/useTrailSearch.js`:

   ```javascript
   import { useState, useCallback } from 'react';
   import apiService from '../services/api';

   export const useTrailSearch = () => {
     const [results, setResults] = useState([]);
     const [loading, setLoading] = useState(false);
     const [error, setError] = useState(null);

     const searchTrails = useCallback(async (query, filters = {}) => {
       if (!query.trim()) {
         setResults([]);
         return;
       }

       try {
         setLoading(true);
         setError(null);
         const response = await apiService.searchTrails(query, filters);
         setResults(response.data);
       } catch (err) {
         setError(err.message);
         setResults([]);
       } finally {
         setLoading(false);
       }
     }, []);

     const searchNearby = useCallback(async (latitude, longitude, maxDistance = 10000) => {
       try {
         setLoading(true);
         setError(null);
         const response = await apiService.getTrailsNear(latitude, longitude, maxDistance);
         setResults(response.data);
       } catch (err) {
         setError(err.message);
         setResults([]);
       } finally {
         setLoading(false);
       }
     }, []);

     return {
       results,
       loading,
       error,
       searchTrails,
       searchNearby,
     };
   };
   ```

### 🎨 React Components Using API

1) **Trail List Component**

   Create `src/components/TrailList.js`:

   ```javascript
   import React, { useState } from 'react';
   import { useTrails } from '../hooks/useTrails';

   const TrailList = () => {
     const [filters, setFilters] = useState({
       difficulty: '',
       status: 'open',
       page: 1,
       limit: 10,
     });

     const { trails, loading, error, pagination, refetch } = useTrails(filters);

     const handleFilterChange = (key, value) => {
       setFilters(prev => ({
         ...prev,
         [key]: value,
         page: 1, // Reset to first page when filters change
       }));
     };

     const handlePageChange = (newPage) => {
       setFilters(prev => ({ ...prev, page: newPage }));
     };

     if (loading) return <div>Loading trails...</div>;
     if (error) return <div>Error: {error}</div>;

     return (
       <div>
         <h2>Trails</h2>
         
         {/* Filters */}
         <div className="filters">
           <select
             value={filters.difficulty}
             onChange={(e) => handleFilterChange('difficulty', e.target.value)}
           >
             <option value="">All Difficulties</option>
             <option value="Easy">Easy</option>
             <option value="Moderate">Moderate</option>
             <option value="Hard">Hard</option>
             <option value="Expert">Expert</option>
           </select>

           <select
             value={filters.status}
             onChange={(e) => handleFilterChange('status', e.target.value)}
           >
             <option value="open">Open</option>
             <option value="closed">Closed</option>
             <option value="maintenance">Maintenance</option>
             <option value="seasonal">Seasonal</option>
           </select>
         </div>

         {/* Trail List */}
         <div className="trail-list">
           {trails.map((trail) => (
             <div key={trail.id} className="trail-card">
               <h3>{trail.name}</h3>
               <p>{trail.description}</p>
               <div className="trail-meta">
                 <span>Distance: {trail.distance}km</span>
                 <span>Elevation: {trail.elevationGain}m</span>
                 <span>Difficulty: {trail.difficulty}</span>
                 <span>Status: {trail.status}</span>
               </div>
             </div>
           ))}
         </div>

         {/* Pagination */}
         {pagination && (
           <div className="pagination">
             <button
               disabled={pagination.page <= 1}
               onClick={() => handlePageChange(pagination.page - 1)}
             >
               Previous
             </button>
             <span>
               Page {pagination.page} of {pagination.pages}
             </span>
             <button
               disabled={pagination.page >= pagination.pages}
               onClick={() => handlePageChange(pagination.page + 1)}
             >
               Next
             </button>
           </div>
         )}
       </div>
     );
   };

   export default TrailList;
   ```

2) **Trail Search Component**

   Create `src/components/TrailSearch.js`:

   ```javascript
   import React, { useState } from 'react';
   import { useTrailSearch } from '../hooks/useTrailSearch';

   const TrailSearch = () => {
     const [query, setQuery] = useState('');
     const [filters, setFilters] = useState({
       difficulty: '',
       tags: '',
     });

     const { results, loading, error, searchTrails } = useTrailSearch();

     const handleSearch = (e) => {
       e.preventDefault();
       searchTrails(query, filters);
     };

     return (
       <div>
         <h2>Search Trails</h2>
         
         <form onSubmit={handleSearch}>
           <input
             type="text"
             value={query}
             onChange={(e) => setQuery(e.target.value)}
             placeholder="Search trails..."
             required
           />
           
           <select
             value={filters.difficulty}
             onChange={(e) => setFilters(prev => ({ ...prev, difficulty: e.target.value }))}
           >
             <option value="">All Difficulties</option>
             <option value="Easy">Easy</option>
             <option value="Moderate">Moderate</option>
             <option value="Hard">Hard</option>
             <option value="Expert">Expert</option>
           </select>

           <input
             type="text"
             value={filters.tags}
             onChange={(e) => setFilters(prev => ({ ...prev, tags: e.target.value }))}
             placeholder="Tags (comma-separated)"
           />

           <button type="submit" disabled={loading}>
             {loading ? 'Searching...' : 'Search'}
           </button>
         </form>

         {error && <div className="error">Error: {error}</div>}

         {results.length > 0 && (
           <div className="search-results">
             <h3>Search Results ({results.length})</h3>
             {results.map((trail) => (
               <div key={trail.id} className="trail-card">
                 <h4>{trail.name}</h4>
                 <p>{trail.description}</p>
                 <div className="trail-meta">
                   <span>Distance: {trail.distance}km</span>
                   <span>Difficulty: {trail.difficulty}</span>
                 </div>
               </div>
             ))}
           </div>
         )}
       </div>
     );
   };

   export default TrailSearch;
   ```

### 🔧 Error Handling & Loading States

1) **Create Error Boundary**

   Create `src/components/ErrorBoundary.js`:

   ```javascript
   import React from 'react';

   class ErrorBoundary extends React.Component {
     constructor(props) {
       super(props);
       this.state = { hasError: false, error: null };
     }

     static getDerivedStateFromError(error) {
       return { hasError: true, error };
     }

     componentDidCatch(error, errorInfo) {
       console.error('Error caught by boundary:', error, errorInfo);
     }

     render() {
       if (this.state.hasError) {
         return (
           <div className="error-boundary">
             <h2>Something went wrong</h2>
             <p>Please try refreshing the page or contact support if the problem persists.</p>
             <button onClick={() => window.location.reload()}>
               Refresh Page
             </button>
           </div>
         );
       }

       return this.props.children;
     }
   }

   export default ErrorBoundary;
   ```

2) **Create Loading Component**

   Create `src/components/LoadingSpinner.js`:

   ```javascript
   import React from 'react';

   const LoadingSpinner = ({ size = 'medium', message = 'Loading...' }) => {
     const sizeClass = `spinner-${size}`;
     
     return (
       <div className="loading-container">
         <div className={`spinner ${sizeClass}`}></div>
         <p className="loading-message">{message}</p>
       </div>
     );
   };

   export default LoadingSpinner;
   ```

### 🎯 Usage in App.js

Update your `src/App.js`:

```javascript
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import ErrorBoundary from './components/ErrorBoundary';
import TrailList from './components/TrailList';
import TrailSearch from './components/TrailSearch';
import './App.css';

function App() {
  return (
    <ErrorBoundary>
      <Router>
        <div className="App">
          <header>
            <h1>Orion Trail App</h1>
          </header>
          
          <main>
            <Routes>
              <Route path="/" element={<TrailList />} />
              <Route path="/trails" element={<TrailList />} />
              <Route path="/search" element={<TrailSearch />} />
            </Routes>
          </main>
        </div>
      </Router>
    </ErrorBoundary>
  );
}

export default App;
```

### 🧪 Testing the Integration

1) **Test API Connection**

   ```bash
   # In your React app directory
   npm start
   ```

2) **Verify API Calls**

   - Open browser dev tools → Network tab
   - Navigate through your app
   - Check that API calls are being made to your Render URL
   - Verify responses are coming back correctly

3) **Test Error Handling**

   - Temporarily change `REACT_APP_API_URL` to an invalid URL
   - Verify error states are displayed properly
   - Restore correct URL

Your React app is now fully integrated with your Express.js API deployed on Render!

## 🔍 Code Quality & Linting Tools

### 🛠️ Custom Linter Setup

The Orion project includes a comprehensive custom linter that combines semantic HTML checking with additional code quality, accessibility, performance, and security checks.

#### **📦 Installation**

The linter tools are already installed as dev dependencies:

```bash
npm install --save-dev prettier husky lint-staged
```

#### **⚙️ Configuration Files**

**Prettier Configuration (`.prettierrc`)**
```json
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 100,
  "tabWidth": 2,
  "useTabs": false,
  "bracketSpacing": true,
  "bracketSameLine": false,
  "arrowParens": "avoid",
  "endOfLine": "lf",
  "quoteProps": "as-needed",
  "jsxSingleQuote": true,
  "proseWrap": "preserve",
  "htmlWhitespaceSensitivity": "css",
  "embeddedLanguageFormatting": "auto"
}
```

**Prettier Ignore (`.prettierignore`)**
```
# Ignore artifacts:
build
coverage

# Ignore dependencies:
node_modules

# Ignore other:
.git
.vscode
.env
.DS_Store
```

**Lint-staged Configuration (in `package.json`)**
```json
{
  "lint-staged": {
    "*.{js,jsx,ts,tsx}": [
      "prettier --write"
    ],
    "*.{json,css,md}": [
      "prettier --write"
    ]
  }
}
```

#### **🚀 Available Scripts**

**Prettier Scripts**
```bash
npm run format          # Format all files
npm run format:check    # Check formatting (CI/CD)
npm run format:staged   # Format only staged files
```

**Semantic HTML Checker Scripts**
```bash
npm run semantic-check              # Basic semantic HTML check
npm run semantic-check:verbose     # Detailed check with suggestions
npm run semantic-check:components  # Check only components directory
npm run semantic-check:pages       # Check only pages directory
```

**Comprehensive Linter Scripts**
```bash
npm run lint                    # Run comprehensive linter
npm run lint:verbose           # Detailed linter output
npm run lint:accessibility     # Focus on accessibility issues
npm run lint:performance       # Focus on performance issues
npm run lint:security          # Focus on security issues
npm run lint:file              # Analyze specific file and its test
```

#### **🔍 Custom Linter Features**

**1. Semantic HTML Analysis**
- Detects usage of `<div>` and `<span>` vs semantic HTML elements
- Provides per-file statistics and recommendations
- Identifies accessibility issues with form elements
- Suggests semantic alternatives for better structure

**2. Accessibility Checks**
- Missing `alt` attributes on images
- Missing `label` or `aria-label` for form inputs
- Proper use of semantic elements (`<button>`, `<nav>`, `<main>`, etc.)
- Color contrast and keyboard navigation considerations

**3. Performance Analysis**
- Identifies large bundle sizes
- Detects unused imports and dependencies
- Suggests code splitting opportunities
- Analyzes image optimization needs

**4. Security Checks**
- Detects potential XSS vulnerabilities
- Identifies unsafe DOM manipulation
- Checks for proper input validation
- Analyzes authentication and authorization patterns

**5. Code Quality Rules**
- Console statement detection
- Long line identification
- Missing type definitions
- Inconsistent naming conventions

#### **📊 Usage Examples**

**Basic Semantic Check**
```bash
npm run semantic-check
```

**Detailed Analysis with Suggestions**
```bash
npm run semantic-check:verbose
```

**Check Specific Component**
```bash
npm run lint:file src/components/TrailCard.js
```

**Focus on Accessibility**
```bash
npm run lint:accessibility
```

#### **🔄 Git Integration**

**Pre-commit Hook**
The project uses Husky to automatically run Prettier formatting on staged files before each commit:

```bash
# .husky/pre-commit
npx lint-staged
```

**Workflow**
1. Write code normally
2. Stage files with `git add`
3. Commit with `git commit` (Prettier runs automatically)
4. Code is automatically formatted and consistent

#### **🎯 Best Practices**

**1. Regular Linting**
- Run `npm run lint` before major commits
- Use `npm run semantic-check:verbose` for detailed HTML analysis
- Fix accessibility issues as they're identified

**2. Component Development**
- Use `npm run lint:file ComponentName.js` to analyze specific components
- Check both the component and its test file together
- Focus on semantic HTML structure

**3. Performance Monitoring**
- Run `npm run lint:performance` before releases
- Address bundle size and optimization suggestions
- Monitor for performance regressions

**4. Security Reviews**
- Use `npm run lint:security` for security-focused analysis
- Review authentication and input validation patterns
- Check for potential vulnerabilities

#### **🔧 IDE Integration**

**VS Code Setup**
Install the Prettier extension and add to settings:

```json
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "editor.formatOnPaste": true
}
```

**Other IDEs**
- **WebStorm**: Built-in Prettier support
- **Sublime Text**: Install JsPrettier package
- **Atom**: Install prettier-atom package

#### **📈 Continuous Integration**

**GitHub Actions Integration**
Add to your workflow:

```yaml
- name: Run Linter
  run: |
    npm run format:check
    npm run lint:accessibility
    npm run semantic-check
```

**Pre-commit Checks**
The pre-commit hook ensures:
- All staged files are properly formatted
- Code style consistency across the team
- No formatting issues in the repository

#### **🚨 Troubleshooting**

**Common Issues**

1. **ESLint Errors Blocking Commits**
   - The lint-staged config only runs Prettier (not ESLint) to avoid blocking commits
   - Run `npm run lint` manually to see ESLint issues
   - Fix ESLint errors gradually without blocking development

2. **Prettier Conflicts**
   - Ensure all team members use the same `.prettierrc` configuration
   - Run `npm run format` to resolve formatting conflicts
   - Check `.prettierignore` for excluded files

3. **Semantic HTML Issues**
   - Use `npm run semantic-check:verbose` for detailed suggestions
   - Focus on high-priority recommendations first
   - Gradually improve HTML structure over time

#### **📚 Related Documentation**

- **Prettier Setup**: See `PRETTIER_SETUP.md` for detailed Prettier configuration
- **Testing**: See `src/__tests__/TESTING.md` for testing guidelines
- **API Documentation**: See API docs for backend integration

#### **🎉 Benefits**

1. **Consistent Code Style**: All team members write code in the same format
2. **Better Accessibility**: Automatic detection of accessibility issues
3. **Improved Performance**: Identification of performance bottlenecks
4. **Enhanced Security**: Detection of potential security vulnerabilities
5. **Semantic HTML**: Better HTML structure and SEO optimization
6. **Team Productivity**: Reduced code review time and fewer style discussions

The custom linter ensures high code quality, accessibility compliance, and consistent development practices across the entire Orion project.