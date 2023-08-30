#!/usr/bin/env node

/* redis basics */

import { createClient } from 'redis';

const client = createClient();

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
})
  .on('connect', () => {
    console.log('Redis client connected to the server');
  });
