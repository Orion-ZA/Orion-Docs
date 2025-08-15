# 5. Design Decisions  

## 🗺 UI Wireframes  
![Trail Search](assets/wireframes/trail-search.png)  
- **Key Pages**:  
  - Trail Explorer (map/list view).  
  - Review Submission Form.  

## 🏗 Architecture  
```mermaid
graph LR  
  A[React Frontend] --> B[Express API]  
  B --> C[PostgreSQL]  
  B --> D[Mapbox API]
```