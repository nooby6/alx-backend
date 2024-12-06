import { createClient } from 'redis';

createClient()
  .on('error', (err) => console.log('Redis client not connected to the server:', err.stack))
<<<<<<< HEAD
  .on('ready', () => console.log('Redis client connected to the server'));
=======
  .on('ready', () => console.log('Redis client connected to the server'));
>>>>>>> a091f12e16d84bbdf6d2d9d2a11005351b870746
