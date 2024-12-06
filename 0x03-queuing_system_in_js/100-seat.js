import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';
import kue from 'kue';

const client = createClient();
const key = 'available_seats';
const initialSeats = 50;
let reservationEnabled = true;
const queue = kue.createQueue();
const queueName = 'reserve_seat';
const app = express();
const port = 1245;

const getAsync = promisify(client.get).bind(client);
async function getCurrentAvailableSeats() {
  const availableSeats = await getAsync(key);
  return availableSeats;
}
function reserveSeat(number) {
  client.set(key, number);
}
/**
 * Creates a job for seat reservation in the queue.
 *
 * @function
 * @returns {Object} The created job object.
 * @throws {Error} If the reservation fails.
 *
 * @example
 * const job = createJob();
 * job.on('complete', () => {
 *   console.log(`Seat reservation job ${job.id} completed`);
 * }).on('failed', (error) => {
 *   console.log(`Seat reservation job ${job.id} failed:`, error);
 * });
 */
function createJob() {
  const job = queue.create(queueName, {
    title: 'Seat Reservation',
  }).save((error) => {
    if (error) {
      throw new Error('Reservation failed');
    }
  });
  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  }).on('failed', (error) => {
    console.log(`Seat reservation job ${job.id} failed:`, error);
  });
  return job;
}

async function makeReservation(job, done) {
  const availableSeats = await getCurrentAvailableSeats();
  if (availableSeats < 1) {
    return done(new Error('Not enough seats available'));
  }
  const newSeats = availableSeats - 1;
  reserveSeat(newSeats);
  if (newSeats === 0) {
    reservationEnabled = false;
  }
  done();
}

reserveSeat(initialSeats);

app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});

app.get('/available_seats', async (req, res) => {
  const seats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: seats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservations are blocked' });
  }
  try {
    const job = createJob();
    res.json({ status: 'Reservation in process' });
  } catch (error) {
    res.json({ status: 'Reservation failed' });
  }
});

app.get('/process', (req, res) => {
  queue.process(queueName, (job, done) => {
    makeReservation(job, done);
  });
  res.json({ status: 'Queue processing' });
});