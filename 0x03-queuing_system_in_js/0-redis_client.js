import { createClient } from 'redis';

createClient()
  .on('error', (err) => console.log('Redis client not connected to the server:', err.stack))
.on('ready', () => console.log('Redis client connected to the server'));
