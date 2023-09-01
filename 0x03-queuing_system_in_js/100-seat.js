import express from 'express';
import kue from 'kue';
import redis from 'redis';
import { promisify } from 'util';

// utils =================================================

// redis =================================================

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
let reservationEnabled;

const seatsKey = 'available_seats';

function reserveSeat(number) {
  client.set(seatsKey, number);
}

async function getCurrentAvailableSeats() {
  const availableSeats = await getAsync(seatsKey);
  return availableSeats;
}

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');

  reserveSeat(50);
  reservationEnabled = true;
