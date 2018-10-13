DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS university;
DROP TABLE IF EXISTS instructor;

-- create tables

CREATE TABLE user (
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    bio TEXT,
    university_id INTEGER,
    is_instructor INTEGER,
    instructor_id INTEGER
);

CREATE TABLE university (
    id INTEGER PRIMARY KEY,
    domain TEXT,
    name TEXT
);

CREATE TABLE instructor (
    id INTEGER PRIMARY KEY,
    gpa REAL,
    comments_active INTEGER
);

-- insert users

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
    1,
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
    1,
    0,
    null
);

-- insert universities

INSERT INTO university (
    domain,
    name
    ) VALUES (
    'gtu',
    'Gebze Teknik Üniversitesi'
);

INSERT INTO university (
    domain,
    name
    ) VALUES (
    'boun',
    'Boğaziçi Üniversitesi'
);

INSERT INTO university (
    domain,
    name
    ) VALUES (
    'hacettepe',
    'Hacettepe Üniversitesi'
);

INSERT INTO university (
    domain,
    name
    ) VALUES (
    'itu',
    'İstanbul Teknik Üniversitesi'
);

INSERT INTO university (
    domain,
    name
    ) VALUES (
    'metu',
    'Orta Doğu Teknik Üniversitesi'
);
