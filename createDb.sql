CREATE TABLE users (
    userId INT AUTO_INCREMENT PRIMARY KEY
);

CREATE TABLE birthday_reminder(
    id INT PRIMARY KEY,
    date DATE NOT NULL,
    name TEXT NOT NULL,
    flag INT NOT NULL,
    userId INT REFERENCES users(userId)
);

