DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS university;
DROP TABLE IF EXISTS instructor;
DROP TABLE IF EXISTS instructor_rating;
DROP TABLE IF EXISTS instructor_comment;

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
    'physicist',
    'Berat',
    'Gonultas',
    'Berat bio',
    2,
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

INSERT INTO user (
    username,
    name,
    surname,
    bio,
    university_id,
    is_instructor,
    instructor_id
) VALUES (
    'ezerger',
    'Erkan',
    'ZERGEROĞLU',
    '-Doğrusal olmayan sistemlerde kontrol tasarımı
-Model tabanlı denetim sistemleri
-Çıkış geri beslemeli, uyarlamalı, dayanıklı denetleyici tasarımı
-Gerçek zamanlı sistemler ',
    1,
    1,
    2
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
    'hcelebi',
    'Hasari',
    'ÇELEBİ',
    'Kablosuz Haberleşme, sinyal işleme, konum belirleme, sezim ve kestirim kuramı.

Wireless Communications, Signal Processing, Localization and Positioning, Detection and Estimation Theory. ',
    1,
    1,
    3
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
    'favorite',
    'Uraz Cengiz',
    'TÜRKER',
    'Software engineering, Formal methods, Model checking, Finite state machine based testing, Automata theory, Computational complexity, Theory of computation, Algorithm analysis and optimization. ',
    1,
    1,
    4
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
    'alpaydin',
    'Ethem',
    'ALPAYDIN',
    'Machine Learning',
    2,
    1,
    5
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
    'alpaydin',
    'Fatih',
    'ALAGOZ',
    'CmpE 362 Intro.to Signal Proc. For Computer.Eng., CmpE 581 Sp.Tp. Com.Eng.For Mob./Wireless Network , CmpE 582 Sp.Tp. Satellite Networks, CmpE 49F Sp.Tp. Introduction to Satellite Space Network , SWE 523 Managing Software Development I, SWE 552 Telecommunications Software Engineering, SWE 520 Computer Networks',
    2,
    1,
    6
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
    'ersoy',
    'Cem',
    'ERSOY',
    'Wireless Networks and Mobile Applications, Pervasive Health, Internet of Things, 5G, SDN and Multi-tier Cloud Systems',
    2,
    1,
    7
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
    'gungort',
    'Tunga',
    'GUNGOR',
    'Artificial Intelligence, Natural Language Processing, Learning Systems, Theoretical Computer Science, Automated Theorem Proving',
    2,
    1,
    8
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
    'gurgen',
    'Fikret',
    'GURGEN',
    'Speech Processing, Biomedical applications, Intelligent Applications',
    2,
    1,
    9
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

INSERT INTO instructor (
    is_comments_active
) VALUES (
    0
);

INSERT INTO instructor (
    is_comments_active
) VALUES (
    0
);

INSERT INTO instructor (
    is_comments_active
) VALUES (
    0
);

INSERT INTO instructor (
    is_comments_active
) VALUES (
    0
);

INSERT INTO instructor (
    is_comments_active
) VALUES (
    0
);

INSERT INTO instructor (
    is_comments_active
) VALUES (
    0
);

INSERT INTO instructor (
    is_comments_active
) VALUES (
    0
);

SELECT * FROM user;
