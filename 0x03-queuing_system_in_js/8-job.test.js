import createPushNotificationsJobs from './8-job';
import kue from 'kue';
import { expect } from 'chai';

const queue = kue.createQueue();

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account',
  },
];

