# 4. Tech Stack  

## Backend  
- **Framework**: Express.js
    - Why? This is a popular and robust choice for building RESTful APIs. It's JavaScript-based, which allows for seamless integration with our React frontend.
- **Database**: Firebase
    - Why Firebase? Its real-time database capabilities, which enable instant updates for trail statuses, community contributions, and alerts—perfect for hikers needing up-to-date information. Its built-in user authentication and cloud functions streamline user management and API operations like Trail and User Contribution APIs, reducing development time. Additionally, Firebase Storage handles photos and media efficiently, while its scalability supports growing trail data and user interactions, making it ideal for a dynamic, community-driven platform hosted on AWS.
- **Auth**: Firebase Authentication
    - Why? Because Firebase. It just makes sense.

## Frontend  
- **Framework**: React
- **Styling**: TailwindCSS
- **Why?** React is a powerful library for building dynamic user interfaces, and Tailwind CSS allows for rapid, utility-first styling. This combination will help us create a responsive design that works across all devices. We are all just very comfortable with React so it was a no brainer. 

## APIs  
- **Approach**: Since Firebase is the DB what is the best options? 
1. Firebase Cloud Functions (Serverless)

    **Best for**: Simple, event-driven APIs (REST or GraphQL) that scale automatically.

    **Pros**:

    - Tightly integrated with Firebase
    - No server management
    - Auto-scaling

    **Cons**:

    - Cold starts can add latency.
    - Limited execution time (9 min max per function).

    **Languages**: JavaScript/TypeScript (Node.js). And we are using JS / TS so perfect!

2. Node.js + Express (Traditional Server)

    **Best for**: More complex APIs needing long-running processes.

    **Pros**:
    - Full control over server logic.
    - Works well with Firebase Admin SDK.
    - Can be deployed on Cloud Run (serverless containers) or App Engine.

    **Cons**:
    - Requires manual scaling (unless using Cloud Run).

    **Deployment**:
    - Google Cloud Run (serverless containers)
    - Render / Railway (PaaS)

- **Decision**: As of 12/08/2025 we have chosen to use Firebase Cloud Functions however it is a pay as you go service so if this doesn't suit sour needs and becomes expensive we will ultimately switch to the classic Node.js and Express.