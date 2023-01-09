CREATE TABLE users (
    userId INT AUTO_INCREMENT PRIMARY KEY
);

CREATE TABLE birthday_reminder(
    id INT PRIMARY KEY,
    date TEXT CHECK(date_column GLOB '[0-1][0-9]-[0-3][0-9]'),
    name TEXT NOT NULL,
    flag INT NOT NULL,
    userId INT REFERENCES users(userId)
);