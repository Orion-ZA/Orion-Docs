# 4. Tech Stack  

## Backend  
- **Framework**: Express.js
    - Why? This is a popular and robust choice for building RESTful APIs. It's JavaScript-based, which allows for seamless integration with our React frontend.
- **Database**: Firebase
    - Why Firebase? Its real-time database capabilities, which enable instant updates for trail statuses, community contributions, and alerts—perfect for hikers needing up-to-date information. Its built-in user authentication and cloud functions streamline user management and API operations like Trail and User Contribution APIs, reducing development time. Additionally, Firebase Storage handles photos and media efficiently, while its scalability supports growing trail data and user interactions, making it ideal for a dynamic, community-driven platform hosted on AWS.
- **Auth**: Auth0
    - Why? This will handle secure user authentication, allowing users to sign in with existing accounts from providers like Google or Facebook.

## Frontend  
- **Framework**: React
- **Styling**: TailwindCSS
- **Why?**: React is a powerful library for building dynamic user interfaces, and Tailwind CSS allows for rapid, utility-first styling. This combination will help us create a responsive design that works across all devices.

## APIs  
- **External**: Mapbox API (trail maps).  
- **Internal**: RESTful endpoints for trails/reviews.  