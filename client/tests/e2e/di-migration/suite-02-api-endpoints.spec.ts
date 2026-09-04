/**
 * Suite 2: API Endpoint Validation Tests (DI migration validation).
 */

import { expect, test } from '@playwright/test';

import { testAPIEndpoint } from './fixtures/api';

test.describe('Suite 2: API Endpoint Validation Tests', () => {
  test('Metrics API Test - GET /metrics', async ({ page }) => {
    const response = await testAPIEndpoint(page, 'GET', '/metrics');
    expect(response.status()).toBeLessThan(500);
  });

  test('Metrics API Test - GET /metrics/summary', async ({ page }) => {
    const response = await testAPIEndpoint(page, 'GET', '/metrics/summary');
    expect(response.status()).toBeLessThan(500);
  });

  test('Metrics API Test - GET /metrics/dlq', async ({ page }) => {
    const response = await testAPIEndpoint(page, 'GET', '/metrics/dlq');
    expect(response.status()).toBeLessThan(500);
  });

  test('Metrics API Test - POST /metrics/reset', async ({ page }) => {
    const response = await testAPIEndpoint(page, 'POST', '/metrics/reset');
    expect(response.status()).toBeLessThan(500);
  });

  test('Metrics API Test - POST /metrics/circuit-breaker/reset', async ({ page }) => {
    const response = await testAPIEndpoint(page, 'POST', '/metrics/circuit-breaker/reset');
    expect(response.status()).toBeLessThan(500);
  });

  test('API Endpoint Dependency Injection Test', async ({ page }) => {
    const endpoints = ['/metrics', '/metrics/summary', '/metrics/dlq'];

    for (const endpoint of endpoints) {
      const response = await testAPIEndpoint(page, 'GET', endpoint);
      expect(response.status()).toBeLessThan(500);
    }
  });
});
