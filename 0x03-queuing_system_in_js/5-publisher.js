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

function delay(time) {
  return new Promise((resolve) => setTimeout(resolve, time));
}

async function publishMessage(message, time) {
  await delay(time);
  console.log(`About to send ${message}`);
  client.publish(channel, message);
}

publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);