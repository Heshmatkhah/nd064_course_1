DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS information;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);

-- Value is text, so we can store any kind of information, complex data can be stored in JSON.
CREATE TABLE information (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    key TEXT NOT NULL,
    value TEXT NOT NULL
);
