CREATE DATABASE IF NOT EXISTS GYM;
USE GYM;

CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(50)
);

INSERT INTO users (username, password) VALUES
-- ('name ', 'pass12'),
-- ('name', 'pass34'),
-- ('name', 'pass56'),
-- ('batool', 'pass78');

select * from users;

CREATE TABLE IF NOT EXISTS customers (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  cell_number VARCHAR(15),
  id_number VARCHAR(50),
  join_date DATE,
  fee DECIMAL(10, 2)
);

INSERT INTO customers (id, name, cell_number, id_number, join_date, fee) VALUES
(1, 'Ali Raza', '03001234567', 'C-01', '2023-01-01', 1500),
(2, 'Zaina', '03012345678', 'C-02', '2023-02-01', 1500),
(3, 'Ahmed Khan', '03101234567', 'C-03', '2023-03-01', 1500),
(4, 'Sana', '03211234567', 'C-04', '2023-04-01', 1500),
(5, 'Hassan', '03301234567', 'C-05', '2023-05-01', 1500),
(6, 'Maria', '03451234567', 'C-06', '2023-06-01', 1500),
(7, 'Faizan', '03561234567', 'C-07', '2023-07-01', 1500),
(8, 'Sara', '03671234567', 'C-08', '2023-08-01', 1500),
(9, 'Usman', '03781234567', 'C-09', '2023-09-01', 1500),
(10, 'Ayesha', '03891234567', 'C-10', '2023-10-01', 1500);

select * from customers;

CREATE TABLE IF NOT EXISTS trainers (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  cell_number VARCHAR(15),
  id_number VARCHAR(50),
  join_date DATE,
  salary DECIMAL(10, 2)
);

INSERT INTO trainers (id, name, cell_number, id_number, join_date, salary) VALUES
(1, 'Kamran', '03009876543', 'T-01', '2020-01-01', 20000),
(2, 'Rehan', '03119876543', 'T-02', '2020-02-01', 20000),
(3, 'Nida', '03219876543', 'T-03', '2020-03-01', 20000),
(4, 'Aliya', '03319876543', 'T-04', '2020-04-01', 20000),
(5, 'Hammad', '03419876543', 'T-05', '2020-05-01', 20000),
(6, 'Fahad', '03519876543', 'T-06', '2020-06-01', 20000),
(7, 'Kiran', '03619876543', 'T-07', '2020-07-01', 20000),
(8, 'Usama', '03719876543', 'T-08', '2020-08-01', 20000),
(9, 'Saba', '03819876543', 'T-09', '2020-09-01', 20000),
(10, 'shiza', '03919876543', 'T-10', '2020-10-01', 20000);

select * from trainers;

CREATE TABLE IF NOT EXISTS equipment (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  damaged BOOLEAN
);

INSERT INTO equipment (id, name, damaged) VALUES
(1, 'Treadmill', FALSE),
(2, 'Dumbbells', FALSE),
(3, 'Exercise Bike', TRUE),
(4, 'Squat Rack', FALSE),
(5, 'Pull-up Bar', FALSE),
(6, 'Bench Press', FALSE),
(7, 'Rowing Machine', FALSE),
(8, 'Leg Press', FALSE),
(9, 'Elliptical', FALSE),
(10, 'Kettlebells', FALSE);

select * from equipment;


CREATE TABLE IF NOT EXISTS membership (
  id INT PRIMARY KEY,
  type VARCHAR(50),
  perks VARCHAR(100),
  time_limit VARCHAR(20),
  cost DECIMAL(10, 2)
);

INSERT INTO membership (id, type, perks, time_limit, cost) VALUES
(1, 'Basic', 'Access to general training sessions', '1 Month', 100.00),
(2, 'Premium', 'Personalized coaching, priority access', '3 Months', 300.00),
(3, 'Elite', 'Exclusive training sessions, personalized coaching', '6 Months', 600.00),
(4, 'Student', 'Discounted rates, access to general training sessions', '1 Semester', 150.00),
(5, 'Family', 'Access for 4 family members', '1 Year', 1200.00),
(6, 'Corporate', 'Access for company employees', '1 Year', 10000.00),
(7, 'Senior', 'Discounted rates for seniors', '1 Year', 500.00),
(8, 'Couples', 'Access for couples', '1 Year', 800.00),
(9, 'Day Pass', 'One-day access', '1 Day', 20.00),
(10, 'Weekly Pass', 'One-week access', '1 Week', 65.00);

select * from membership;

CREATE TABLE IF NOT EXISTS payments (
  id INT PRIMARY KEY,
  customer_id INT,
  payment_id VARCHAR(55),
  amount DECIMAL(10, 2),
  due_date DATE,
  FOREIGN KEY (customer_id) REFERENCES customers(id)
);

INSERT INTO payments (id, customer_id, payment_id, amount, due_date) VALUES
(1, 1, 'PAY001', 1500.00, '2023-01-15'),
(2, 2, 'PAY002', 1500.00, '2023-02-15'),
(3, 3, 'PAY003', 1500.00, '2023-03-15'),
(4, 4, 'PAY004', 1500.00, '2023-04-15'),
(5, 5, 'PAY005', 1500.00, '2023-05-15'),
(6, 6, 'PAY006', 1500.00, '2023-06-15'),
(7, 7, 'PAY007', 1500.00, '2023-07-15'),
(8, 8, 'PAY008', 1500.00, '2023-08-15'),
(9, 9, 'PAY009', 1500.00, '2023-09-15'),
(10, 10, 'PAY010', 1500.00, '2023-10-15');

select * from payments;
