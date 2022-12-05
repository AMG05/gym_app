DROP TABLE bookings;
DROP TABLE members;
DROP TABLE exercise_classes;


CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    membership_type VARCHAR(255),
    booked_classes VARCHAR(255)
);


CREATE TABLE exercise_classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255),
    duration VARCHAR(255),
    date VARCHAR(255),
    capacity INT,
    instructor VARCHAR (255)
);


CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    exercise_classes_id INT NOT NULL REFERENCES exercise_classes(id) ON DELETE CASCADE,
    members_id INT NOT NULL REFERENCES members(id) ON DELETE CASCADE
);