import kue from 'kue';

const queue = kue.createQueue();

const data = {
  phoneNumber: '0712345678',
  message: 'This is it',
};

/**
 * Creates a job for push notification code and saves it to the queue.
 *
 * @param {Object} data - The data to be used in the job.
 * @returns {Job} The created job instance.
 * @throws Will throw an error if the job creation fails.
 */
const job = queue.create('push_notification_code', data)
  .save((err) => {
    if (!err) console.log('Notification job created:', job.id);
  });

job.on('complete', () => {
  console.log('Notification job completed');
}).on('failed', () => {
  console.log('Notification job failed');
});