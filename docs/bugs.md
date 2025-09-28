# Bug Tracking Guide

This document explains how our team tracks, manages, and resolves bugs using both **GitHub Issues** and our **in-app feedback system**.  
Please follow this process so that all bug reports are clear, consistent, and easy to resolve.

---

## 1. Reporting a Bug

### Option A: In-App Feedback System (Recommended for Users)
We've implemented a comprehensive feedback system accessible through the app:
1. Navigate to the **Feedback** page in the app
2. Select **"Bug Report"** as the feedback type
3. Provide a rating and detailed description
4. Include steps to reproduce the issue
5. Optionally attach a screenshot
6. Submit the feedback - it will be stored in our database

### Option B: GitHub Issues (For Developers)
When you find a bug:
1. Go to the **Issues** tab → click **New Issue** → select **Bug Report**.
2. Fill in the bug template completely:
   - **Describe the bug** clearly.
   - Provide **steps to reproduce**.
   - Include **expected vs. actual behavior**.
   - Add **screenshots/logs** if possible.
   - Specify **environment** (OS, browser, version, etc.).

⚠️ **Tip:** Before creating a new issue, search the existing issues to avoid duplicates.

---

## 2. Labels
We use labels to organize bugs:

- `bug` → confirmed bug
- `needs-triage` → new issue, not yet reviewed
- `critical` → blocks major functionality
- `high` → serious, but workaround exists
- `low` → minor issue, cosmetic
- `duplicate` → already reported
- `wontfix` → acknowledged but won’t be fixed
- `in progress` → actively being worked on

---

## 3. Workflow
Bugs move through the following stages:

1. **New** – bug is reported and given `needs-triage`.
2. **Acknowledged** – team confirms the bug and adds severity labels (`critical`, `high`, `low`).
3. **In Progress** – assigned to a developer, marked with `in progress`.
4. **Review** – a pull request (PR) is created and linked to the issue.
5. **Done** – issue is closed automatically when the PR is merged.

---

## 4. Viewing and Managing Feedback

### Admin Dashboard Access
All user feedback (including bug reports) submitted through the in-app feedback system can be viewed and managed through the **Admin Dashboard**:

1. **Access the Admin Dashboard** - Navigate to the admin section of the app
2. **View Feedback** - All submitted feedback is stored in the `feedback` collection in Firestore
3. **Filter by Type** - Bug reports can be filtered from other feedback types (general, suggestions, praise)
4. **Review Details** - Each feedback entry includes:
   - User rating and message
   - Feedback type (bug, suggestion, general, praise)
   - User information (if contact is allowed)
   - Timestamp and page location
   - Screenshots (for bug reports)
   - Browser/device information

### Feedback Data Structure
The feedback system captures:
- **Rating**: 1-5 star rating
- **Message**: Detailed description
- **Type**: bug, suggestion, general, or praise
- **Contact Permission**: Whether user allows follow-up
- **User Context**: User ID, email, user agent, current page
- **Screenshots**: Optional image attachments for bug reports
- **Timestamp**: When the feedback was submitted

---

## 5. Assignments
- Each bug must have **one assignee** responsible for fixing it.  
- If you start working on a bug, assign yourself (or ask a lead to assign you).  
- Always link your PR to the issue with:  
```bash
Closes #<issue_number>
```