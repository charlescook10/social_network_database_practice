-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email text,
    username text
);

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text,
    views int,
    user_id int,
    constraint fk_user foreign key(user_id)
        references users(id)
        on delete cascade
);


INSERT INTO users (email, username) VALUES ('charles@email.com', 'charles123');
INSERT INTO users (email, username) VALUES ('hotdog@yahoo.co.uk', 'hotdogman');

INSERT INTO posts (title, content, views, user_id) VALUES ('Reflection Day 1', 'Today I made a database', 192, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('Reflection Day 2', 'Today I made a table', 32, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('Hot Dog Stand Review 1', 'Very nice', 1283, 2);
INSERT INTO posts (title, content, views, user_id) VALUES ('Confession', 'I no longer enjoy hot dogs', 9992, 2);
INSERT INTO posts (title, content, views, user_id) VALUES ('Leaving', 'I am leaving the internet', 1232, 2);