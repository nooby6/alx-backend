import kue from 'kue';

const blacklist = ['4153518780', '4153518781'];

// eslint-disable-next-line consistent-return
/**
 * Sends a notification to a specified phone number.
 *
 * @param {string} phoneNumber - The phone number to send the notification to.
 * @param {string} message - The message to be sent in the notification.
 * @param {Object} job - The job object representing the notification task.
 * @param {Function} done - The callback function to be called when the notification process is complete.
 *
 * @throws {Error} If the phone number is blacklisted.
 */
function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (blacklist.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }
  job.progress(50, 100); // set progress to 50%
  console.log(`Sending notification to ${phoneNumber}, with message:`, message);
  done();
}

const queue = kue.createQueue();

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});