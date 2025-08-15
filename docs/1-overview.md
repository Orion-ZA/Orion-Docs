# 1. Overview  

## 🛠 Version Control  
- **GitHub Repo:** [Orion](https://github.com/Orion-ZA/Orion)  
- **Branch Strategy:**  
  - `main`: Production  
  - `develop`: Staging  
  - `feature/*`: New features (e.g., `feature/trail-search`)  

## 📂 Repository Structure  
```
backend/
├── models/ # Trail, User schemas
├── routes/ # API endpoints
frontend/
├── public/ # Static assets
├── src/ # React components
docs/ # This documentation
```

## ✅ Sprint 1 Goals  
- [x] Set up PostgreSQL + Trail schema.  
- [x] Implement user auth (OAuth).  
- [x] Draft UI wireframes.  