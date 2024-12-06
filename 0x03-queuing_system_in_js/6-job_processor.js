import kue from 'kue';

const queue = kue.createQueue();
/**
 * Sends a notification to a specified phone number with a given message.
 *
 * @param {string} phoneNumber - The phone number to send the notification to.
 * @param {string} message - The message to be sent in the notification.
 */
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}
queue.process('push_notification_code', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});