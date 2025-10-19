# Testing Documentation

## Overview

The Orion project implements comprehensive testing across both frontend React components and backend Firebase functions, as well as a comprehensive REST API built with Express.js and Firebase Firestore. Our testing strategy ensures code quality, reliability, and maintainability through unit tests, integration tests, and coverage reporting.

## Testing Framework & Tools

### Frontend Testing
- **Jest**: Primary testing framework
- **React Testing Library**: Component testing utilities
- **@testing-library/user-event**: User interaction simulation
- **@testing-library/jest-dom**: Custom Jest matchers for DOM testing

### Backend Testing
- **Jest**: Testing framework for Firebase functions
- **Firebase Admin SDK**: Mocked for function testing
- **CORS**: Mocked for HTTP function testing

### API Testing (Orion-API)
- **Jest**: Primary testing framework for Express.js API
- **Supertest**: HTTP assertion library for API endpoint testing
- **Firebase Admin SDK**: Mocked for Firestore database operations
- **Express**: Test-specific Express app instances for route testing

### Coverage & Reporting
- **Coverage Collection**: Enabled with text and LCOV reporters
- **Coverage Directory**: `coverage/` with HTML reports
- **Coverage Thresholds**: Configured in Jest config
- **Codecov Integration**: Automated coverage reporting to Codecov

## Test Structure

### Frontend Tests (`src/__tests__/`)
The frontend test suite includes **54 test files** covering:

#### Component Tests
- **App.test.js**: Main application routing and layout (253 lines)
- **SearchBar.test.js**: Search functionality with comprehensive user interactions (1011 lines)
- **TrailUtils.test.js**: Utility functions for trail data processing (150 lines)

#### Page Tests
- **LandingPage.test.js**: Landing page components and interactions
- **Dashboard.test.js**: Dashboard functionality and user flows
- **Trails.test.js**: Trail listing and filtering
- **ProfilePage.test.js**: User profile management
- **Settings.test.js**: Application settings
- **HelpCenter.test.js**: Help center and FAQ functionality

#### Context & Hook Tests
- **SearchContext.test.js**: Search state management
- **LoaderContext.test.js**: Loading state management
- **ToastContext.test.js**: Notification system
- **ThemeProvider.test.js**: Theme management
- **useTrails.test.js**: Trail data fetching hook
- **useReverseGeocoding.test.js**: Geocoding functionality

#### Component-Specific Tests
- **Navbar.test.js**: Navigation component
- **Footer.test.js**: Footer component
- **FilterPanel.test.js**: Trail filtering interface
- **TrailMap.test.js**: Map integration
- **TrailSubmission.test.js**: Trail creation form
- **TrailEdit.test.js**: Trail editing functionality

### Backend Tests (`functions/test/`)
- **submitTrail.test.js**: Trail submission API endpoint (434 lines)
- **index.test.js**: Function exports and initialization

### API Tests (`tests/`)
The API test suite includes **8 comprehensive test files** covering:

#### Controller Tests
- **trail.test.js**: Trail CRUD operations and search functionality (23.962s execution time)
- **alert.test.js**: Alert management system (34.299s execution time)
- **report.test.js**: Report creation and management (50.7s execution time)
- **review.test.js**: Review system with ratings and comments (86.742s execution time)
- **user.test.js**: User profile and trail management (31.352s execution time)

#### Model Tests
- **trail-model.test.js**: Trail model validation and helper methods (67 tests)
- **user-model.test.js**: User model validation and helper methods (52 tests)

#### Middleware Tests
- **error-handler.test.js**: Error handling middleware (40 tests)

#### Test Setup
- **setup.js**: Global test configuration and Firebase mocking

## Test Coverage

### Current Coverage Status
Based on the latest test run:

#### Frontend Coverage
- **Test Suites**: 52 total (43 passed, 9 failed)
- **Tests**: 990 total (924 passed, 65 failed, 1 skipped)
- **Coverage Reports**: Available in `coverage/lcov-report/`

#### API Coverage (Orion-API)
- **Test Suites**: 8 total (8 passed)
- **Tests**: 326 total (326 passed)
- **Overall Coverage**: 85.03% statement coverage
- **Branch Coverage**: 86.7%
- **Function Coverage**: 87.87%
- **Line Coverage**: 85.03%
- **Lines Covered**: 784 of 922 lines

### Coverage Areas

#### Frontend Coverage
- **Components**: All major React components tested
- **Pages**: All application pages covered
- **Hooks**: Custom hooks with comprehensive testing
- **Utils**: Utility functions with edge case coverage
- **Context**: State management testing
- **API Functions**: Backend endpoint validation

#### API Coverage
- **Controllers**: 75-86% coverage across all controllers
  - `trailController.js`: 73.76% statement coverage
  - `alertController.js`: 86.53% statement coverage
  - `reportController.js`: 84.44% statement coverage
  - `reviewController.js`: 82.4% statement coverage
  - `userController.js`: 75.8% statement coverage
- **Models**: 100% coverage for Trail and User models
- **Middleware**: 100% coverage for error handling
- **Routes**: 100% coverage for all API routes
- **Validation**: 100% coverage for input validation schemas

## Testing Patterns

### Component Testing Patterns

#### 1. Basic Rendering Tests
```javascript
it('renders component with default props', () => {
  render(<Component />);
  expect(screen.getByText('Expected Text')).toBeInTheDocument();
});
```

#### 2. User Interaction Tests
```javascript
it('handles user input correctly', async () => {
  render(<SearchBar />);
  const input = screen.getByPlaceholderText(/search/i);
  await userEvent.type(input, 'test query');
  expect(input.value).toBe('test query');
});
```

#### 3. Context Integration Tests
```javascript
const renderWithProviders = (component) => {
  return render(
    <SearchProvider>
      {component}
    </SearchProvider>
  );
};
```

#### 4. Mock Implementation
```javascript
jest.mock('../components/SearchContext', () => ({
  useSearch: () => ({
    searchSuggestions: [],
    handleSearch: jest.fn()
  })
}));
```

### Backend Testing Patterns

#### 1. Function Validation Tests
```javascript
it('should return 400 when required fields are missing', async () => {
  const req = { method: 'POST', body: invalidData };
  const res = { status: jest.fn().mockReturnThis(), json: jest.fn() };
  
  await submitTrail(req, res);
  
  expect(res.status).toHaveBeenCalledWith(400);
});
```

#### 2. Authentication Testing
```javascript
it('should handle authentication when valid token is provided', async () => {
  const mockVerifyIdToken = admin.auth().verifyIdToken;
  mockVerifyIdToken.mockResolvedValue({ uid: 'test-user-123' });
  // ... test implementation
});
```

### API Testing Patterns

#### 1. Express App Testing Setup
```javascript
const request = require('supertest');
const express = require('express');
const trailRoutes = require('../src/routes/trailRoutes');

function createTestApp() {
  const app = express();
  app.use(express.json());
  app.use('/api/trails', trailRoutes);
  return app;
}

describe('Trail API', () => {
  let app;
  
  beforeAll(async () => {
    await connectDB(); // Connect to Firebase
    app = createTestApp();
  });
});
```

#### 2. HTTP Endpoint Testing
```javascript
it('should create a new trail', async () => {
  const trailData = {
    name: 'Test Trail',
    location: { latitude: 40.7128, longitude: -74.0060 },
    distance: 5.2,
    elevationGain: 800,
    difficulty: 'Moderate',
    description: 'A beautiful test trail',
    createdBy: global.generateFirebaseUserId()
  };

  const response = await request(app)
    .post('/api/trails')
    .send(trailData);

  expect(response.status).toBe(201);
  expect(response.body.success).toBe(true);
  expect(response.body.data.name).toBe('Test Trail');
});
```

#### 3. Database Integration Testing
```javascript
it('should retrieve trails from database', async () => {
  const response = await request(app)
    .get('/api/trails')
    .query({ page: 1, limit: 10 });

  expect(response.status).toBe(200);
  expect(response.body.success).toBe(true);
  expect(Array.isArray(response.body.data)).toBe(true);
  expect(response.body.pagination).toBeDefined();
});
```

#### 4. Validation Testing
```javascript
it('should return 400 for invalid trail data', async () => {
  const invalidTrail = {
    name: '', // Invalid: empty name
    location: { latitude: 200, longitude: -74.0060 }, // Invalid: latitude > 90
    // Missing required fields
  };

  const response = await request(app)
    .post('/api/trails')
    .send(invalidTrail);

  expect(response.status).toBe(400);
  expect(response.body.success).toBe(false);
  expect(response.body.errors).toBeDefined();
});
```

#### 5. Error Handling Testing
```javascript
it('should handle database errors gracefully', async () => {
  // Mock database error
  const mockError = new Error('Database connection failed');
  jest.spyOn(db, 'collection').mockImplementation(() => {
    throw mockError;
  });

  const response = await request(app)
    .get('/api/trails');

  expect(response.status).toBe(500);
  expect(response.body.success).toBe(false);
  expect(response.body.message).toBe('Server Error');
});
```

#### 6. Model Testing
```javascript
describe('Trail Model', () => {
  it('should validate trail data correctly', () => {
    const validTrail = new Trail({
      name: 'Test Trail',
      location: { latitude: 40.7128, longitude: -74.0060 },
      distance: 5.2,
      elevationGain: 800,
      difficulty: 'Moderate',
      description: 'A beautiful trail',
      createdBy: 'user123'
    });

    const errors = Trail.validate(validTrail);
    expect(errors).toHaveLength(0);
  });

  it('should return validation errors for invalid data', () => {
    const invalidTrail = {
      name: '', // Invalid: empty name
      location: { latitude: 200, longitude: -74.0060 }, // Invalid: latitude > 90
      distance: -5, // Invalid: negative distance
      difficulty: 'Invalid' // Invalid: not in enum
    };

    const errors = Trail.validate(invalidTrail);
    expect(errors.length).toBeGreaterThan(0);
  });
});
```

#### 7. Firebase Mocking
```javascript
// Global setup in tests/setup.js
jest.mock('firebase-admin', () => {
  const mockFirestore = {
    collection: jest.fn(() => mockFirestore),
    doc: jest.fn(() => mockFirestore),
    add: jest.fn(() => Promise.resolve({ id: global.generateFirebaseUserId() })),
    get: jest.fn(() => Promise.resolve({ exists: true, data: () => ({}) })),
    update: jest.fn(() => Promise.resolve()),
    delete: jest.fn(() => Promise.resolve()),
    limit: jest.fn(() => mockFirestore),
    orderBy: jest.fn(() => mockFirestore),
    where: jest.fn(() => mockFirestore)
  };

  return {
    initializeApp: jest.fn(),
    credential: { cert: jest.fn() },
    firestore: jest.fn(() => mockFirestore),
    apps: []
  };
});
```

## Running Tests

### Frontend Tests
```bash
# Run all tests
npm test

# Run tests with coverage
npm test -- --coverage --watchAll=false

# Run specific test file
npm test SearchBar.test.js

# Run tests in watch mode
npm test -- --watch
```

### Backend Tests
```bash
# Run Firebase function tests
cd functions
npm test

# Run with coverage
npm test -- --coverage
```

### API Tests (Orion-API)
```bash
# Run all API tests
npm test

# Run tests with coverage
npm run test:coverage

# Run tests in CI mode
npm run test:ci

# Run specific test file
npm test trail.test.js

# Run tests in watch mode
npm test -- --watch

# Run tests with verbose output
npm test -- --verbose
```

### Coverage Reports
```bash
# Generate coverage report
npm test -- --coverage --watchAll=false

# View HTML coverage report
open coverage/lcov-report/index.html
```

## Test Configuration

### Jest Configuration (`jest.config.js`)
```javascript
module.exports = {
  testEnvironment: 'jsdom',
  collectCoverage: true,
  coverageDirectory: 'coverage',
  coverageReporters: ['text', 'lcov'],
  testPathIgnorePatterns: ['/node_modules/'],
};
```

### Package.json Scripts

#### Frontend Scripts
```json
{
  "scripts": {
    "test": "react-scripts test",
    "test:coverage": "react-scripts test --coverage --watchAll=false"
  }
}
```

#### API Scripts (Orion-API)
```json
{
  "scripts": {
    "test": "jest",
    "test:coverage": "jest --coverage --watchAll=false",
    "test:ci": "jest --coverage --watchAll=false --ci",
    "lint": "eslint src/",
    "lint:fix": "eslint src/ --fix"
  },
  "jest": {
    "testEnvironment": "node",
    "setupFilesAfterEnv": ["<rootDir>/tests/setup.js"],
    "testTimeout": 30000,
    "collectCoverageFrom": [
      "src/**/*.js",
      "!src/app.js"
    ],
    "coverageDirectory": "coverage",
    "coverageReporters": ["text", "lcov", "html"]
  }
}
```

## Testing Best Practices

### 1. Test Organization
- Group related tests using `describe` blocks
- Use descriptive test names that explain the expected behavior
- Follow the Arrange-Act-Assert pattern

### 2. Mocking Strategy
- Mock external dependencies (APIs, Firebase, etc.)
- Use Jest mocks for functions and modules
- Mock user interactions with `@testing-library/user-event`

### 3. Accessibility Testing
- Test with screen readers in mind
- Use semantic queries (`getByRole`, `getByLabelText`)
- Ensure proper ARIA attributes

### 4. Edge Case Coverage
- Test error conditions and boundary values
- Test with invalid or missing data
- Test loading and error states

### 5. Performance Considerations
- Use `waitFor` for asynchronous operations
- Mock expensive operations
- Test with realistic data sizes

### 6. API Testing Best Practices
- **Database Setup**: Always connect to database in `beforeAll` hooks
- **Test Isolation**: Use unique test data to avoid conflicts
- **Mock External Services**: Mock Firebase operations for consistent testing
- **Error Scenarios**: Test both success and failure paths
- **Validation Testing**: Test input validation thoroughly
- **Response Format**: Verify response structure and status codes
- **Edge Cases**: Test boundary conditions and error states

## Common Test Utilities

### Custom Render Function
```javascript
const renderWithProviders = (component) => {
  return render(
    <BrowserRouter>
      <SearchProvider>
        <ToastProvider>
          {component}
        </ToastProvider>
      </SearchProvider>
    </BrowserRouter>
  );
};
```

### Mock Data Factories
```javascript
const createMockTrail = (overrides = {}) => ({
  id: 'test-trail-id',
  name: 'Test Trail',
  location: { lat: 37.2695, lng: -112.9470 },
  distance: 3.2,
  elevationGain: 500,
  difficulty: 'Moderate',
  status: 'open',
  ...overrides
});
```

### API Test Utilities

#### Test App Factory
```javascript
const createTestApp = (routes = []) => {
  const app = express();
  app.use(express.json());
  routes.forEach(route => app.use(route.path, route.handler));
  return app;
};
```

#### Firebase User ID Generator
```javascript
global.generateFirebaseUserId = () => {
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  let result = '';
  for (let i = 0; i < 28; i++) {
    result += chars[Math.floor(Math.random() * chars.length)];
  }
  return result;
};
```

#### API Response Assertions
```javascript
const expectSuccessResponse = (response, statusCode = 200) => {
  expect(response.status).toBe(statusCode);
  expect(response.body.success).toBe(true);
  expect(response.body.data).toBeDefined();
};

const expectErrorResponse = (response, statusCode = 400) => {
  expect(response.status).toBe(statusCode);
  expect(response.body.success).toBe(false);
  expect(response.body.message).toBeDefined();
};
```

## Troubleshooting

### Common Issues

#### 1. Test Timeouts
```javascript
// Increase timeout for specific tests
jest.setTimeout(10000);
```

#### 2. Async Operations
```javascript
// Use waitFor for async operations
await waitFor(() => {
  expect(screen.getByText('Loaded content')).toBeInTheDocument();
});
```

#### 3. Mock Cleanup
```javascript
afterEach(() => {
  jest.clearAllMocks();
});
```

#### 4. Environment Setup
```javascript
// Mock browser APIs
Object.defineProperty(window, 'IntersectionObserver', {
  writable: true,
  value: jest.fn()
});
```

#### 5. API Testing Issues

##### Database Connection Timeouts
```javascript
// Increase timeout for database operations
jest.setTimeout(30000);

// Ensure database connection in beforeAll
beforeAll(async () => {
  await connectDB();
}, 30000);
```

##### Port Conflicts
```javascript
// Use test-specific Express app instead of importing app.js
function createTestApp() {
  const app = express();
  app.use(express.json());
  app.use('/api/trails', trailRoutes);
  return app; // Don't call app.listen()
}
```

##### Firebase Mocking Issues
```javascript
// Clear mocks between tests
afterEach(() => {
  jest.clearAllMocks();
});

// Reset Firebase mocks
beforeEach(() => {
  jest.resetModules();
});
```

##### Test Data Cleanup
```javascript
afterAll(async () => {
  // Clean up test data
  await new Promise(resolve => setTimeout(resolve, 1000));
});
```

## Continuous Integration

### GitHub Actions Integration
Tests are automatically run on:
- Pull request creation
- Push to main branch
- Scheduled runs

#### Frontend CI
- Node.js 18.x environment
- npm install and test execution
- Coverage report generation

#### API CI (Orion-API)
- Node.js 18.x environment
- npm install and test execution
- Coverage report generation with Codecov integration
- Automatic coverage upload to Codecov platform

### Coverage Reporting
- Coverage reports are generated for each test run
- Coverage thresholds can be configured
- Reports are available in the `coverage/` directory
- **API Coverage**: Automatically uploaded to Codecov for tracking

## Future Improvements

### Planned Enhancements
1. **E2E Testing**: Add Cypress or Playwright for end-to-end testing
2. **Visual Regression Testing**: Implement screenshot testing
3. **Performance Testing**: Add performance benchmarks
4. **Accessibility Testing**: Automated accessibility checks
5. **API Testing**: Comprehensive API endpoint testing
6. **Load Testing**: API performance under load
7. **Security Testing**: Automated security vulnerability scanning
8. **Contract Testing**: API contract validation

### Testing Metrics

#### Frontend Metrics
- **Target Coverage**: 90%+ for critical components
- **Test Execution Time**: < 2 minutes for full suite
- **Test Reliability**: < 1% flaky test rate

#### API Metrics
- **Target Coverage**: 90%+ for all controllers and models
- **Test Execution Time**: < 2 minutes for full suite
- **Test Reliability**: < 1% flaky test rate
- **Current Coverage**: 85.03% statement coverage (326 tests, 784 of 922 lines)

## Resources

### Documentation Links
- [Jest Documentation](https://jestjs.io/docs/getting-started)
- [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
- [Firebase Functions Testing](https://firebase.google.com/docs/functions/unit-testing)
- [Supertest Documentation](https://github.com/visionmedia/supertest)
- [Express Testing Guide](https://expressjs.com/en/guide/testing.html)

### Internal Resources
- [Component Testing Guidelines](./development.md#testing-guidelines)
- [API Testing Standards](./api.md#testing)
- [Code Review Checklist](./git.md#testing-requirements)

---

*Last updated: 19 October 2025*
*Frontend coverage: 5275 of 5745 lines covered (91.81%) on `dev`*
*API coverage: 85.03% statement coverage (326 tests, 784 of 922 lines) on `main`*
