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