CREATE TABLE users (
    userId INT PRIMARY KEY
);

CREATE TABLE birthday_reminder(
    id INT AUTO_INCREMENT PRIMARY KEY,
    date TEXT CHECK(date GLOB '[0-1][0-9]-[0-3][0-9]'),
    name TEXT NOT NULL,
    flag INT NOT NULL,
    userId INT REFERENCES users(userId)
);