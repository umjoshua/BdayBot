CREATE TABLE users (
    userId INT PRIMARY KEY
);

CREATE TABLE birthday_reminder(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT CHECK(date GLOB '[0-3][0-9]-[0-1][0-9]'),
    name TEXT NOT NULL,
    userId INT REFERENCES users(userId)
);