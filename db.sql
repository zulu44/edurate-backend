DROP TABLE IF EXISTS user;

CREATE TABLE user (
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    bio TEXT,
    university_id INTEGER,
    is_instructor INTEGER,
    instructor_id INTEGER
);

INSERT INTO user (
    name,
    surname,
    bio,
    university_id,
    is_instructor,
    instructor_id
    ) VALUES (
    'Enes',
    'Gonultas',
    'Enes böo',
    null,
    0,
    null
);

INSERT INTO user (
    name,
    surname,
    bio,
    university_id,
    is_instructor,
    instructor_id
    ) VALUES (
    'Osman',
    'Akkus',
    'Osman bio',
    null,
    0,
    null
);

SELECT * FROM user;

