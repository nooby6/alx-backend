/**
 * Creates push notification jobs and adds them to the queue.
 *
 * @param {Array} jobs - An array of job data objects.
 * @param {Object} queue - The queue to which the jobs will be added.
 * @throws {Error} If jobs is not an array.
 */
export default function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
      throw new Error('Jobs is not an array');
    }
  
    for (const data of jobs) {
      const job = queue.create('push_notification_code_3', data)
        .save((err) => {
          if (!err) console.log('Notification job created:', job.id);
        });
      job.on('complete', () => {
        console.log(`Notification job #${job.id} completed`);
      }).on('failed', (errorMessage) => {
        console.log(`Notification job #${job.id} failed:`, errorMessage);
      }).on('progress', (progress) => {
        console.log(`Notification job #${job.id} ${progress}% complete`);
      });
    }
  }