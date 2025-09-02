# 📑 Project Meeting Minutes

## 1. Sprint Planning Meeting
**Date:** 21/08 
**Attendees:** Everyone  
**Sprint Goal:** Implement the core browsing, contribution, and trail-saving features.  

### Agenda
- Review backlog  
- Prioritize user stories  
- Define sprint goal  
- Assign tasks  

### Key Points
- **Backlog Review:**  
  1. **Browse Trails** – Search by location, difficulty, distance, terrain; view descriptions, photos, reviews, maps.  
  2. **Community Contributions** – Users can submit new trails, update existing ones, upload photos, rate, and review.  
  3. **Favourites & Wishlists** – Save trails, mark completed, maintain wishlist.  
  4. **Safety & Alerts** – Show trail closures, conditions, alerts; notify users on saved trails.  

- **Decisions:**  
  - Sprint Goal: *“Enable users to browse and search trails, contribute reviews/photos, save trails, and receive safety alerts.”*  
  - Assignments:  
    - Browse & Search functionality → Dev A  
    - Trail descriptions/photos/reviews UI → Dev B  
    - Community Contributions (form & DB link) → Dev C  
    - Favourites & Wishlists → Dev D  
    - Safety & Alerts (data + notifications) → Dev E  

- **Dependencies:** Firebase backend, Mapbox maps, push notification system.  

### Action Items
- [ ] Confirm schema for trails, reviews, and alerts.  
- [ ] Share mockups for contribution form.  
- [ ] Set up notification service integration.  

---

## 2. Sprint Retrospective
**Date:** 22/08
**Attendees:** Everyone 

### What Went Well ✅
- Core browsing features worked smoothly with Mapbox integration.  
- Community contributions feature successfully linked to database.  
- Favourites & Wishlists synced well across sessions.  

### What Could Improve ⚠️
- Safety & Alerts took longer due to external data sourcing.  
- Contribution form UI had multiple redesigns.  

### Action Items 🎯
- Research more reliable trail alert data sources.  
- Prototype form layouts before coding.  

---

## 3. Scrum Meeting 1
**Date:** 22/08  

### Yesterday
- Search filter framework created (location, difficulty, distance, terrain).  
- Trail schema finalized in database.  

### Today
- Connect search filters to database.  
- Begin work on trail detail pages (description, photos, reviews).  

### Blockers
- None.  

---

## 4. Scrum Meeting 2
**Date:** 25/08  

### Yesterday
- Trail detail page set up with description and photo display.  
- Contribution form skeleton created.  

### Today
- Add reviews + rating system.  
- Connect contribution form to backend.  

### Blockers
- Validation for photo uploads still unclear.  

---

## 5. Scrum Meeting 3
**Date:** 28/08  

### Yesterday
- Reviews + ratings completed.  
- Contribution form connected to database.  
- Wishlist UI completed.  

### Today
- Implement “mark as completed” functionality.  
- Begin Safety & Alerts prototype (closures + conditions).  

### Blockers
- Need a reliable source/API for official alerts.  

---

## 6. Scrum Meeting 4
**Date:** 30/08 

### Yesterday
- Safety alerts prototype working with test data.  
- Wishlist and completed trail features tested.  

### Today
- Integrate alerts with saved trails notifications.  
- Final testing + demo preparation.  

### Blockers
- Push notification setup delayed by Firebase configuration.  
