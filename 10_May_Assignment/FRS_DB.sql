create database frs_db;
use frs_db;

CREATE TABLE `frs_log` (
  `log_id` int,
  `user_name` varchar(255) NOT NULL,
  `email_id` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
);

CREATE TABLE `frs_registation` (
  `reg_id` int PRIMARY KEY,
  `aadhar_number` int NOT NULL,
  `phone_number` int NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `middle_name` varchar(255),
  `date_of_birth` date,
  `reg_time` timestamp
);

CREATE TABLE `frs_city` (
  `city_id` int PRIMARY KEY,
  `city_name` varchar(255),
  `state` varchar(255)
);

CREATE TABLE `frs_station` (
  `station_id` int PRIMARY KEY,
  `station_name` varchar(255),
  `station_address` varchar(255),
  `city_id` int,
  `pincode` int
);

CREATE TABLE `frs_train` (
  `train_id` int PRIMARY KEY,
  `train_name` varchar(255),
  `boarding_city` int,
  `destination_city` int,
  `train_spec_id` int
);

CREATE TABLE `frs_train_specifications` (
  `train_spec_id` int PRIMARY KEY,
  `number_of_carts` int,
  `speed` float8
);

CREATE TABLE `frs_carts` (
  `cart_id` int PRIMARY KEY,
  `type_of_cart` varchar(255),
  `steating_capacity` int
);

CREATE TABLE `frs_train_cart_map` (
  `train_cart_map_id` int PRIMARY KEY,
  `train_id` int,
  `cart_id` int
);

CREATE TABLE `frs_seating` (
  `seat_id` int PRIMARY KEY,
  `train_cart_map_id` int,
  `seat_spec_id` int
);

CREATE TABLE `frs_seat_spec` (
  `seat_spec_id` int PRIMARY KEY,
  `seat_type` varchar(255),
  `seat_position` varchar(255),
  `seat_price` decimal,
  `cart_id` int
);

CREATE TABLE `frs_booking` (
  `booking_id` int PRIMARY KEY,
  `user_id` int,
  `seat_id` int,
  `status` varchar(255),
  `transaction_id` int,
  `booking_time` timestamp
);

CREATE TABLE `frs_transaction` (
  `transaction_id` int PRIMARY KEY,
  `transaction_amount` decimal,
  `payment_mode` varchar(255),
  `transaction_status` varchar(255),
  `transaction_time` timestamp
);

CREATE TABLE `frs_train_schedule` (
  `schedule_id` int PRIMARY KEY,
  `train_id` int,
  `arraival_time` datetime,
  `departure_time` datetime
);

CREATE TABLE `frs_cancellation` (
  `cancellation_id` int PRIMARY KEY,
  `booking_id` int,
  `refund_id` int
);

CREATE TABLE `frs_refund` (
  `refund_id` int PRIMARY KEY,
  `refund_amount` decimal,
  `refund_status` varchar(255)
);

ALTER TABLE `frs_log` ADD FOREIGN KEY (`log_id`) REFERENCES `frs_registation` (`reg_id`);

ALTER TABLE `frs_station` ADD FOREIGN KEY (`city_id`) REFERENCES `frs_city` (`city_id`);

ALTER TABLE `frs_train` ADD FOREIGN KEY (`boarding_city`) REFERENCES `frs_city` (`city_id`);

ALTER TABLE `frs_train` ADD FOREIGN KEY (`destination_city`) REFERENCES `frs_city` (`city_id`);

ALTER TABLE `frs_train` ADD FOREIGN KEY (`train_spec_id`) REFERENCES `frs_train_specifications` (`train_spec_id`);

ALTER TABLE `frs_train_cart_map` ADD FOREIGN KEY (`train_id`) REFERENCES `frs_train` (`train_id`);

ALTER TABLE `frs_train_cart_map` ADD FOREIGN KEY (`cart_id`) REFERENCES `frs_carts` (`cart_id`);

ALTER TABLE `frs_seating` ADD FOREIGN KEY (`train_cart_map_id`) REFERENCES `frs_train_cart_map` (`train_cart_map_id`);

ALTER TABLE `frs_seating` ADD FOREIGN KEY (`seat_spec_id`) REFERENCES `frs_seat_spec` (`seat_spec_id`);

ALTER TABLE `frs_seat_spec` ADD FOREIGN KEY (`cart_id`) REFERENCES `frs_carts` (`cart_id`);

ALTER TABLE `frs_booking` ADD FOREIGN KEY (`user_id`) REFERENCES `frs_registation` (`reg_id`);

ALTER TABLE `frs_booking` ADD FOREIGN KEY (`seat_id`) REFERENCES `frs_seating` (`seat_id`);

ALTER TABLE `frs_booking` ADD FOREIGN KEY (`transaction_id`) REFERENCES `frs_transaction` (`transaction_id`);

ALTER TABLE `frs_train_schedule` ADD FOREIGN KEY (`train_id`) REFERENCES `frs_train` (`train_id`);

ALTER TABLE `frs_cancellation` ADD FOREIGN KEY (`booking_id`) REFERENCES `frs_booking` (`booking_id`);

ALTER TABLE `frs_cancellation` ADD FOREIGN KEY (`refund_id`) REFERENCES `frs_refund` (`refund_id`);
