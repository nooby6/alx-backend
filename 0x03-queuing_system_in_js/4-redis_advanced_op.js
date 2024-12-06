import redis from 'redis';

/**
 * Creates a Redis client instance and sets up event listeners for connection and error events.
 * 
 * @constant {object} client - The Redis client instance.
 * @event client#error - Emitted when there is an error connecting to the Redis server.
 * @param {Error} err - The error object containing details of the connection error.
 * @event client#connect - Emitted when the client successfully connects to the Redis server.
 */
const client = redis.createClient()
  .on('error', (err) => console.log('Redis client not connected to the server:', err.stack))
  .on('connect', () => console.log('Redis client connected to the server'));

const key = 'HolbertonSchools';

client.hset(key, 'Portland', 50, redis.print);
client.hset(key, 'Seattle', 80, redis.print);
client.hset(key, 'New York', 20, redis.print);
client.hset(key, 'Bogota', 20, redis.print);
client.hset(key, 'Cali', 40, redis.print);
client.hset(key, 'Paris', 2, redis.print);
client.hgetall(key, (err, resp) => {
  console.log(resp);
});