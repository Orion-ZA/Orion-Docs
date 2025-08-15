# 8. Implementation  

## ✅ Completed (Sprint 1)  
- **Google OAuth**:  
  ```javascript
  passport.use(new GoogleStrategy({ /* ... */ })); 
  ```  
- **Trail Schema**:  
  ```sql
  CREATE TABLE trails (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location GEOGRAPHY(POINT)
  ); 
  ```  