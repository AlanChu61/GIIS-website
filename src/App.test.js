import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import { HelmetProvider } from 'react-helmet-async';
import Header from './components/Header/Header';

test('header shows language toggle and Moodle link', () => {
  render(
    <HelmetProvider>
      <MemoryRouter>
        <Header language="en" toggleLanguage={() => {}} />
      </MemoryRouter>
    </HelmetProvider>
  );
  expect(screen.getByRole('button', { name: /switch to chinese/i })).toBeInTheDocument();
  expect(screen.getByRole('link', { name: /^login$/i })).toBeInTheDocument();
  expect(screen.getByRole('link', { name: /^moodle$/i })).toBeInTheDocument();
});
