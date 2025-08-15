# 2. Development Guide  

## 🗃 Database Setup  
1. **Install PostgreSQL**:  
   ```bash
   brew install postgresql  # macOS
   sudo apt install postgresql  # Linux
   ```  
2. **Create DB**:  
   ```sql
   CREATE DATABASE hiking_db;
   \c hiking_db
   CREATE TABLE trails (
     id SERIAL PRIMARY KEY,
     name VARCHAR(255),
     difficulty VARCHAR(50)
   );
   ```  

## 🌐 API Endpoints  
| Endpoint          | Description                |  
|-------------------|----------------------------|  
| `GET /trails`     | Fetch all trails           |  
| `POST /reviews`   | Submit a trail review      |  