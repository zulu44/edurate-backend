from repo import user

class InstructorRepo():
    def __init__(self, database_connection):
        self.dbc = database_connection

    def get_instructor(self, ins_id):
        c = self.dbc.cursor()
        result = c.execute('SELECT * FROM instructor WHERE id=?;', (ins_id,))
        (instructor_id, is_comments_active) = result.fetchone()
        data = {
            'id': instructor_id,
            'is_comments_active': is_comments_active
        }

        return data

    def set_rating(self, uid, ins_id, rating):
        c = self.dbc.cursor()
        c.execute('SELECT * FROM instructor_rating'
            ' WHERE user_id=? and instructor_id=?;', (uid, ins_id))
        if c.fetchone() is None:
            c.execute('INSERT INTO instructor_rating '
                '(user_id, instructor_id, rating) values (?, ?, ?);',
                (uid, ins_id, rating))
            self.dbc.commit()
        else:
            c.execute('UPDATE instructor_rating SET rating=? WHERE '
                'user_id=? and instructor_id=?;', (rating, uid, ins_id))
            self.dbc.commit()

    def add_comment(self, uid, ins_id, comment):
        c = self.dbc.cursor()
        c.execute('INSERT INTO instructor_comment'
            ' (user_id, instructor_id, comment) values (?, ?, ?);',
            (uid, ins_id, comment))
        self.dbc.commit()

    def get_id(self, username):
        c = self.dbc.cursor()
        c.execute('SELECT id FROM user WHERE username=?;', (username,))
        user_id = c.fetchone()[0]
        return user_id


