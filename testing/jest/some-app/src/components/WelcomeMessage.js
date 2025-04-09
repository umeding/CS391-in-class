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
