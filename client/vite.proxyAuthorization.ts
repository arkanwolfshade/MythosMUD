/**
 * Dev-server proxy: forward the browser Authorization header to the backend.
 * Extracted from vite.config so proxy option callbacks stay small (complexity tooling).
 */
import type { ProxyOptions } from 'vite';

export const configureForwardAuthorization: NonNullable<ProxyOptions['configure']> = (proxy, _options) => {
  proxy.on('proxyReq', (proxyReq, req) => {
    const authHeader = req.headers.authorization || req.headers.Authorization;
    if (authHeader) {
      proxyReq.setHeader('Authorization', authHeader as string);
    }
  });
};
