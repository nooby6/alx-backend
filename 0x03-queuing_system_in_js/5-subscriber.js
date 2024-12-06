import redis from 'redis';

/**
 * Redis client instance.
 * 
 * This client is used to connect to a Redis server and handle events such as errors and successful connections.
 * 
 * @constant {object} client - The Redis client instance.
 * @event error - Emitted when there is an error connecting to the Redis server.
 * @param {Error} err - The error object containing details of the connection error.
 * @event connect - Emitted when the client successfully connects to the Redis server.
 */
const client = redis.createClient()
  .on('error', (err) => console.log('Redis client not connected to the server:', err.stack))
  .on('connect', () => console.log('Redis client connected to the server'));

const channel = 'holberton school channel';

client.subscribe(channel);

client.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
});