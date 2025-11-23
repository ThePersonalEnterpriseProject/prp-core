import { render, fireEvent } from '@testing-library/svelte';
import { describe, it, expect } from 'vitest';
import Counter from './Counter.svelte';

describe('Counter.svelte', () => {
  it('should render with initial count of 0', () => {
    const { getByText } = render(Counter);
    expect(getByText('Clicks: 0')).toBeInTheDocument();
  });

  it('should increment count on button click', async () => {
    const { getByText } = render(Counter);
    const button = getByText('Clicks: 0');
    await fireEvent.click(button);
    expect(getByText('Clicks: 1')).toBeInTheDocument();
  });
});
