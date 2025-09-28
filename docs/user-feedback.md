# User Feedback System

## Overview
This document describes the user feedback collection system implemented in the Orion trail discovery platform. All user feedback is collected through our in-app feedback system accessible via the Feedback page.

## Feedback Collection Method

### In-App Feedback System
Orion uses a comprehensive in-app feedback system that allows users to submit feedback directly from within the application. This system is accessible through the **Feedback** page and provides multiple feedback types with detailed categorization.

**Access:** Navigate to the Feedback page in the app or use the feedback button in the application interface.

## Feedback Types

The in-app feedback system supports four distinct feedback categories:

### 💬 General Feedback
- **Purpose**: Overall user experience and general thoughts
- **Use Case**: General suggestions, overall satisfaction, user experience feedback
- **Prompt**: "Share your thoughts with us"

### 🐛 Bug Report
- **Purpose**: Report technical issues and bugs encountered
- **Use Case**: Application errors, functionality problems, technical issues
- **Features**: 
  - Screenshot upload capability
  - Detailed bug description field
  - Steps to reproduce section
- **Prompt**: "Describe the bug you encountered"

### 💡 Feature Suggestion
- **Purpose**: Request new features or improvements
- **Use Case**: New functionality requests, enhancement ideas, feature improvements
- **Prompt**: "Tell us about your idea"

### 👍 Praise
- **Purpose**: Positive feedback and appreciation
- **Use Case**: Highlighting what works well, positive experiences, appreciation
- **Prompt**: "What did you love about Orion?"

## Feedback System Features

### Rating System
- **5-Star Rating**: Users can rate their experience from 1 to 5 stars
- **Interactive Stars**: Hover effects and visual feedback
- **Rating Labels**: "Not satisfied" to "Very satisfied" scale

### Message System
- **Dynamic Prompts**: Context-aware prompts based on feedback type
- **Text Area**: Large text area for detailed feedback
- **Character Limits**: Appropriate limits for different feedback types

### Screenshot Upload (Bug Reports)
- **File Upload**: Image file upload capability for bug reports
- **File Validation**: Only image files accepted
- **Preview**: Screenshot preview with remove option
- **File Management**: Easy removal of uploaded screenshots

### Contact Permission
- **Opt-in Contact**: Users can choose whether to allow follow-up contact
- **Privacy Respect**: Clear indication of contact preferences
- **User Control**: Easy toggle for contact permission

### User Context Capture
- **Automatic Data**: User ID, email, user agent, current page
- **Anonymous Support**: Works for both authenticated and anonymous users
- **Technical Details**: Browser and device information for debugging

## Feedback Data Structure

### Database Storage
All feedback is stored in the `feedback` collection in Firestore with the following structure:

```javascript
{
  rating: Number,           // 1-5 star rating
  message: String,          // User's feedback message
  type: String,             // "general", "bug", "suggestion", "praise"
  contactAllowed: Boolean,  // Whether user allows follow-up contact
  createdAt: Timestamp,     // When feedback was submitted
  userId: String,           // User ID (null for anonymous)
  email: String,            // User email or "Anonymous"
  userAgent: String,        // Browser/device information
  page: String,             // Page where feedback was submitted
  screenshot: File          // Screenshot file (for bug reports)
}
```

### Admin Management
Feedback is managed through the **Admin Dashboard** where administrators can:
- View all submitted feedback
- Filter by feedback type (bug, suggestion, general, praise)
- Review user ratings and messages
- Access user contact information (if permission granted)
- View technical context (browser, page, timestamp)
- Download screenshots for bug reports

## Feedback Processing Workflow

### 1. Submission
- User navigates to Feedback page
- Selects feedback type and provides rating
- Writes detailed message
- Optionally uploads screenshot (bug reports)
- Sets contact permission preference
- Submits feedback

### 2. Storage
- Feedback data saved to Firestore
- Automatic timestamp and user context added
- Screenshot files stored (if provided)

### 3. Admin Review
- Feedback appears in Admin Dashboard
- Administrators can filter and review submissions
- Contact information available for follow-up (if permitted)

### 4. Response (Optional)
- Administrators can contact users for clarification
- Follow-up only if user granted permission
- Feedback used for product improvement decisions

## Success Confirmation

### User Experience
After successful submission, users see a confirmation screen with:
- **Success Message**: "Thank you for your feedback!"
- **Appreciation Note**: "Your input helps us improve the app for everyone."
- **Action Options**: 
  - Send another feedback
  - Go back to previous page

### Loading States
- **Submission Process**: Loading spinner during feedback submission
- **Form Validation**: Real-time validation for required fields
- **Error Handling**: Clear error messages for failed submissions

## Integration with Bug Tracking

### Bug Reports
- Bug reports submitted through the feedback system are automatically categorized
- Screenshots and technical context help with debugging
- Integration with GitHub Issues for developer workflow (as documented in [Bug Tracking Guide](bugs.md))

### Feature Requests
- Feature suggestions are collected and prioritized
- User demand and business impact assessment
- Integration with product roadmap planning

## Privacy & Data Protection

### User Privacy
- **Contact Permission**: Users explicitly opt-in for follow-up contact
- **Anonymous Support**: Feedback can be submitted without user account
- **Data Minimization**: Only necessary information is collected

### Data Security
- **Secure Storage**: All feedback stored securely in Firestore
- **Access Control**: Only authorized administrators can view feedback
- **Data Retention**: Feedback data retained according to privacy policy

## Analytics & Insights

### Feedback Metrics
- **Submission Volume**: Track feedback submission rates
- **Type Distribution**: Monitor feedback type distribution
- **Rating Trends**: Analyze user satisfaction trends over time
- **Response Rates**: Track admin response to user feedback

### Continuous Improvement
- **Regular Review**: Scheduled feedback review meetings
- **Trend Analysis**: Identify common issues and requests
- **Product Impact**: Measure impact of feedback on product development

---

*Last updated: September 2025*
*Next review: October 2025*
