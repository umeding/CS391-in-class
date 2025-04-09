# JEST In-Class Exercise / Tutorial


## Prerequisites (in general):

* `vscode` installed and runnning
* A working React or Next.js project environment (e.g., created with
  `create-react-app` or `create-next-app`).
* `Node.js` and `npm` or `yarn` installed.
* Jest and `@testing-library/react` installed and configured (usually included
  by default in newer versions of the above tools). If not, a quick install
  might be needed, along with potential Jest configuration:

```
npm install --save-dev jest @testing-library/react @testing-library/jest-dom @testing-library/user-event
```

> #
> # NOTE: The test project is ALREADY set up with all the libraries
> # Check the `package.json` file
> #


## Setup and the component to test 

* Navigate to the project directory (`some-app`) and bring up `vscode`
* Create a new component file named src/components/WelcomeMessage.js (adjust
  path if your structure differs).
* Paste the following code into `WelcomeMessage.js`:

```javascript
// src/components/WelcomeMessage.js
import React from 'react';

function WelcomeMessage({ userName }) {
  return (
    <div>
      <h2>Welcome, {userName || 'Guest'}!</h2>
      <p>We're glad you're here.</p>
    </div>
  );
}

export default WelcomeMessage;
```

* Create a corresponding test file named `src/components/WelcomeMessage.test.js`
* Paste the basic test structure into `WelcomeMessage.test.js`:

```javascript
// src/components/WelcomeMessage.test.js
import React from 'react';
import { render, screen } from '@testing-library/react';

// Provides helpful matchers like .toBeInTheDocument():
import '@testing-library/jest-dom'; 
import WelcomeMessage from './WelcomeMessage';

describe('WelcomeMessage Component', () => {
  // Tests will go here
});
```

## Task 1: Testing Basic Rendering

Inside the describe block in `WelcomeMessage.test.js`, add the following test
case:

```javascript
// Inside describe('WelcomeMessage Component', () => { ... });

it('renders the default welcome message when no userName is provided', () => {
  // 1. Render the component without any props
  render(<WelcomeMessage />);

  // 2. Find elements by their text content (case-sensitive)
  const headingElement = screen.getByText('Welcome, Guest!');
  const paragraphElement = screen.getByText("We're glad you're here.");

  // 3. Assert that these elements are actually in the rendered output
  expect(headingElement).toBeInTheDocument();
  expect(paragraphElement).toBeInTheDocument();

  // Optional: Find by role (good practice for accessibility)
  const headingByRole = screen.getByRole('heading', { level: 2 });
  expect(headingByRole).toBeInTheDocument();
});
```

* Run the tests using the command provided by your setup (usually `npm test` or
  `yarn test`).
* Verify that the test passes. If it fails, debug common issues (typos in text,
  component not importing correctly).

## Task 2: Testing Props

Add a second test case inside the describe block:

```javascript
// Inside describe('WelcomeMessage Component', () => { ... });

it('renders the correct welcome message when a userName is provided', () => {
  const testUser = 'Alice';

  // 1. Render the component, passing the userName prop
  render(<WelcomeMessage userName={testUser} />);

  // 2. Find the element with the user-specific message
  // Using a regular expression (i flag for case-insensitive) can be more robust
  const userHeadingElement = screen.getByText(`Welcome, ${testUser}!`);
  // Or: const userHeadingElement = screen.getByText(/welcome, alice!/i);

  // 3. Assert the user-specific heading is present
  expect(userHeadingElement).toBeInTheDocument();

  // 4. Assert the default "Guest" message is NOT present
  const guestHeadingElement = screen.queryByText('Welcome, Guest!');
  expect(guestHeadingElement).not.toBeInTheDocument(); // or expect(guestHeadingElement).toBeNull();

  // 5. The paragraph should still be there
  const paragraphElement = screen.getByText("We're glad you're here.");
  expect(paragraphElement).toBeInTheDocument();
});
```

* Run the tests again (npm test or yarn test).
* Verify that both tests now pass. Debug if necessary.

