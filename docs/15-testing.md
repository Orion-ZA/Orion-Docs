# Testing Documentation

## Overview

The Orion project implements comprehensive testing across both frontend React components and backend Firebase functions. Our testing strategy ensures code quality, reliability, and maintainability through unit tests, integration tests, and coverage reporting.

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

### Coverage & Reporting
- **Coverage Collection**: Enabled with text and LCOV reporters
- **Coverage Directory**: `coverage/` with HTML reports
- **Coverage Thresholds**: Configured in Jest config

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

## Test Coverage

### Current Coverage Status
Based on the latest test run:
- **Test Suites**: 52 total (43 passed, 9 failed)
- **Tests**: 990 total (924 passed, 65 failed, 1 skipped)
- **Coverage Reports**: Available in `coverage/lcov-report/`

### Coverage Areas
- **Components**: All major React components tested
- **Pages**: All application pages covered
- **Hooks**: Custom hooks with comprehensive testing
- **Utils**: Utility functions with edge case coverage
- **Context**: State management testing
- **API Functions**: Backend endpoint validation

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
```json
{
  "scripts": {
    "test": "react-scripts test",
    "test:coverage": "react-scripts test --coverage --watchAll=false"
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

## Continuous Integration

### GitHub Actions Integration
Tests are automatically run on:
- Pull request creation
- Push to main branch
- Scheduled runs

### Coverage Reporting
- Coverage reports are generated for each test run
- Coverage thresholds can be configured
- Reports are available in the `coverage/` directory

## Future Improvements

### Planned Enhancements
1. **E2E Testing**: Add Cypress or Playwright for end-to-end testing
2. **Visual Regression Testing**: Implement screenshot testing
3. **Performance Testing**: Add performance benchmarks
4. **Accessibility Testing**: Automated accessibility checks
5. **API Testing**: Comprehensive API endpoint testing

### Testing Metrics
- **Target Coverage**: 90%+ for critical components
- **Test Execution Time**: < 2 minutes for full suite
- **Test Reliability**: < 1% flaky test rate

## Resources

### Documentation Links
- [Jest Documentation](https://jestjs.io/docs/getting-started)
- [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
- [Firebase Functions Testing](https://firebase.google.com/docs/functions/unit-testing)

### Internal Resources
- [Component Testing Guidelines](./2-development.md#testing-guidelines)
- [API Testing Standards](./12-api.md#testing)
- [Code Review Checklist](./7-git.md#testing-requirements)

---

*Last updated: 27 September 2025*
*Test coverage: 924/990 tests passing (88.27%)*
