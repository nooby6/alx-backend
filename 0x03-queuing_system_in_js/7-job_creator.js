import kue from 'kue';

/**
 * An array of job objects, each containing a phone number and a message.
 * This array is used to store information about different jobs that need to be processed.
 *
 * Each job object has the following properties:
 * @typedef {Object} Job
 * @property {string} phoneNumber - The phone number associated with the job.
 * @property {string} message - The message to be sent to the phone number.
 *
 * @type {Job[]}
 * @example
 * const jobs = [
 *   {
 *     phoneNumber: '4153518780',
 *     message: 'This is the code 1234 to verify your account',
 *   },
 *   {
 *     phoneNumber: '4153518781',
 *     message: 'This is the code 4562 to verify your account',
 *   },
 *   // more job objects...
 * ];
 */
const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account',
  },
];

const queue = kue.createQueue();

for (const data of jobs) {
  const job = queue.create('push_notification_code_2', data)
    .save((err) => {
      if (!err) console.log('Notification job created:', job.id);
    });

  job.on('complete', () => {
    console.log(`Notification job #${job.id} completed`);
  }).on('failed', (errorMessage) => {
    console.log(`Notification job #${job.id} failed: `, errorMessage);
  }).on('progress', (progress) => {
    console.log(`Notification job #${job.id} ${progress}% complete`);
  });
}