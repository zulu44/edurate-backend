DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS university;
DROP TABLE IF EXISTS instructor;

-- create tables

CREATE TABLE user (
    id INTEGER PRIMARY KEY,
    username TEXT,
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
    is_comments_active INTEGER
);

CREATE TABLE instructor_rating (
    user_id INTEGER,
    instructor_id INTEGER,
    rating INTEGER
);

CREATE TABLE instructor_comment (
    user_id INTEGER,
    instructor_id INTEGER,
    comment TEXT
);

-- insert users

INSERT INTO user (
    username,
    name,
    surname,
    bio,
    university_id,
    is_instructor,
    instructor_id
) VALUES (
    'admin',
    'Enes',
    'Gonultas',
    'Enes böo',
    1,
    0,
    null
);

INSERT INTO user (
    username,
    name,
    surname,
    bio,
    university_id,
    is_instructor,
    instructor_id
) VALUES (
    'king',
    'Osman',
    'Akkus',
    'Osman bio',
    1,
    0,
    null
);

INSERT INTO user (
    username,
    name,
    surname,
    bio,
    university_id,
    is_instructor,
    instructor_id
) VALUES (
    'godfather',
    'Yusuf Sinan',
    'AKGÜL',
    'Bilgisayarla Görme ve Bilgisayar Grafikleri, Tıbbı görüntüleme ve görüntü işlemleme, doğal dil işleme ve üretme, makina öğrenmesi, örüntü tanıma, endüstriyel muayene',
    1,
    1,
    1
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

-- insert instructor related info

INSERT INTO instructor (
    is_comments_active
) VALUES (
    1
);

INSERT INTO instructor (
    is_comments_active
) VALUES (
    0
);

SELECT * FROM user;
