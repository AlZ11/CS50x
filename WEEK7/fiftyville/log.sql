-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT * FROM crime_scene_reports WHERE day = 28 AND month = 7 AND year = 2021 AND street = 'Humphrey Street';
-- Obtain initial information/description on theft
SELECT * FROM interviews WHERE day = 28 AND month = 7 AND year = 2021 AND transcript LIKE '%bakery%';
-- Filter out interview transcripts from the day that mentions bakery
SELECT destination_airport_id FROM flights WHERE origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville') AND year = 2021 AND month = 7 AND day = 29 ORDER BY hour ASC, minute ASC LIMIT 1;
-- Find the city the thief escaped to
SELECT city FROM airports WHERE id = (SELECT destination_airport_id FROM flights WHERE origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville') AND year = 2021 AND month = 7 AND day = 29 ORDER BY hour ASC, minute ASC LIMIT 1);
-- New York City

SELECT * FROM passengers WHERE flight_id = (SELECT id FROM flights WHERE origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville') AND year = 2021 AND month = 7 AND day = 29 ORDER BY hour ASC, minute ASC LIMIT 1);
-- Filter out passport_number of possible suspects

SELECT * FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND activity = 'exit';
SELECT * FROM phone_calls WHERE day = 28 AND month = 7 AND year = 2021 AND duration < 60;

SELECT bakery_security_logs.license_plate, bakery_security_logs.id, phone_calls.caller, phone_calls.receiver, people.name, people.passport_number,people.id FROM bakery_security_logs JOIN phone_calls ON bakery_security_logs.id = phone_calls.id JOIN people ON phone_calls.caller = people.phone_number WHERE phone_calls.day = 28 AND phone_calls.month = 7 AND phone_calls.year = 2021 AND phone_calls.duration < 60 AND bakery_security_logs.activity = 'exit' AND people.id IN (SELECT person_id FROM atm_transactions JOIN bank_accounts ON bank_accounts.account_number = atm_transactions.account_number WHERE day = 28 AND month = 7 AND year = 2021 AND transaction_type = 'withdraw' AND atm_location = 'Leggett Street');
-- Found thief

SELECT name FROM people WHERE phone_number = (SELECT phone_calls.receiver FROM bakery_security_logs JOIN phone_calls ON bakery_security_logs.id = phone_calls.id JOIN people ON phone_calls.caller = people.phone_number WHERE phone_calls.day = 28 AND phone_calls.month = 7 AND phone_calls.year = 2021 AND phone_calls.duration < 60 AND bakery_security_logs.activity = 'exit' AND people.id IN (SELECT person_id FROM atm_transactions JOIN bank_accounts ON bank_accounts.account_number = atm_transactions.account_number WHERE day = 28 AND month = 7 AND year = 2021 AND transaction_type = 'withdraw' AND atm_location = 'Leggett Street'));
-- Found accomplice
