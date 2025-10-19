# Tech Stack  

## Backend  
- **Framework**: Express.js
    - Why? This is a popular and robust choice for building RESTful APIs. It's JavaScript-based, which allows for seamless integration with our React frontend.
- **Database**: Firebase
    - Why Firebase? Its real-time database capabilities, which enable instant updates for trail statuses, community contributions, and alerts—perfect for hikers needing up-to-date information. Its built-in user authentication and cloud functions streamline user management and API operations like Trail and User Contribution APIs, reducing development time. Additionally, Firebase Storage handles photos and media efficiently, while its scalability supports growing trail data and user interactions, making it ideal for a dynamic, community-driven platform hosted on AWS.
- **Auth**: Firebase Authentication
    - Why? Because Firebase. It just makes sense.

## Frontend  
- **Framework**: React
- **Styling**: ~~TailwindCSS~~ → Vanilla CSS 
- **Maps**: Mapbox GL JS
  - **Why?** Interactive trail maps with location selection, map controls, and trail discovery capabilities. Provides high-quality mapping with custom styling and real-time data integration.
- **Weather Integration**: Weather API Service
  - **Why?** Real-time weather data for trail locations, multi-day forecasts, and weather-based trail recommendations for hiker safety.
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

## Development Tools & Code Quality

### **Code Formatting & Linting**
- **Prettier**: Code formatter for consistent code style
  - **Why?** Ensures consistent formatting across the entire codebase, reduces code review time, and improves team collaboration.
- **ESLint**: JavaScript/React linting and code quality
  - **Why?** Catches potential bugs, enforces coding standards, and maintains code quality across the project.
- **Custom Linter**: Comprehensive code analysis tool
  - **Why?** Combines semantic HTML checking, accessibility analysis, performance monitoring, and security checks in one tool.

### **Git Integration & Automation**
- **Husky**: Git hooks management
  - **Why?** Automates code quality checks before commits, ensuring only properly formatted and linted code reaches the repository.
- **Lint-staged**: Run linters on staged files
  - **Why?** Optimizes pre-commit hooks by only checking files that are actually being committed, improving performance.

### **Security & Monitoring**
- **Security Audit System**: NPM package vulnerability monitoring
  - **Why?** Prevents supply chain attacks by monitoring package vulnerabilities and ensuring secure dependencies.
- **Package Verification**: Dependency verification process
  - **Why?** Maintains security by verifying package integrity and preventing malicious package installations.

### **Testing Framework**
- **Jest**: JavaScript testing framework
  - **Why?** Comprehensive testing for React components, hooks, and utility functions with excellent React Testing Library integration.
- **React Testing Library**: Component testing utilities
  - **Why?** Encourages testing user behavior rather than implementation details, leading to more reliable tests.

## Changes

### Development Tools & Code Quality Implementation

**Date:** October 2025
**Reason:** Enhanced code quality, security, and development workflow

#### What Was Added
- **Prettier**: Automated code formatting
- **Husky + Lint-staged**: Pre-commit hooks for code quality
- **Custom Linter**: Comprehensive analysis tool for semantic HTML, accessibility, performance, and security
- **Security Audit System**: NPM package vulnerability monitoring
- **Enhanced Testing**: Jest and React Testing Library integration

#### Impact
**Pros:**
- **Consistent Code Style**: All team members now write code in the same format automatically
- **Improved Security**: Proactive monitoring prevents supply chain attacks and vulnerabilities
- **Better Accessibility**: Automatic detection of accessibility issues in HTML components
- **Enhanced Performance**: Identification of performance bottlenecks and optimization opportunities
- **Streamlined Workflow**: Automated formatting and linting reduces manual code review time
- **Quality Assurance**: Comprehensive testing framework ensures reliable code

**Cons:**
- **Initial Setup Time**: Required configuration and team training on new tools
- **Learning Curve**: Team needed to adapt to new linting rules and formatting standards
- **Build Process Complexity**: Additional tools add complexity to the development pipeline

### CSS Framework Switch: TailwindCSS → Vanilla CSS

**Date:** 23/08/2025
**Reason:** Majority Vote on CSS being preferred

#### Why We Switched

**Previous Approach:** TailwindCSS
- Utility-first CSS framework
- Rapid prototyping capabilities
- Large class-based HTML

**New Approach:** Vanilla CSS
- Smaller Bundle Size
- Team was more comfortable
- Easier maintenance for our team

#### Impact

**Pros:**
- Smaller bundle size: Vanilla CSS often results in a smaller overall file size since it doesn't include the entire utility library that TailwindCSS does. This can lead to faster loading times for users.
- Improved team comfort and collaboration: Since the team was more comfortable with Vanilla CSS, the switch likely reduced the learning curve and allowed for more efficient collaboration on styling tasks.
- Familiar workflow: The team can stick to a tried-and-true workflow of writing CSS directly, which can feel more intuitive and natural for those experienced with it.
- No reliance on external frameworks: By not depending on a framework like Tailwind, the project's styling is less tied to a specific ecosystem, which can make it easier to maintain and modify in the long run.

**Cons:**
- **Initial time constraints**: The switch required a period of refactoring the existing Tailwind CSS into Vanilla CSS, which took valuable development time
- **Potential for inconsistency**: Without the enforced structure of a utility-first framework, there's a greater risk of slight inconsistencies in spacing, colors, or typography if the team isn't diligent with documentation or a robust design system
- **Slower development for new features**: While a comfort with the tools makes work easier, the process of writing custom CSS rules for every new component or feature can be more time-consuming than applying existing utility classes from a framework

#### Future Considerations

We will continuously evaluate our styling approach. While Vanilla CSS is the current choice due to team comfort, we may reconsider a CSS preprocessor like Sass or a CSS-in-JS library in the future if the project's complexity increases. This would allow us to benefit from features like variables, nesting, and mixins, which could improve maintainability and scalability without the overhead of a full utility framework.

Additionally, we'll monitor the performance of our CSS bundle to ensure it remains small and efficient as the application grows. This will be a key metric in deciding on any future changes to our frontend styling stack