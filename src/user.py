import json

class UserListResource():
    def __init__(self, database_connection):
        self.dbc = database_connection

    def on_get(self, req, resp):
        c = self.dbc.cursor()
        result = c.execute('SELECT * FROM user;')
        data = []
        for (user_id, name, surname, bio, university_id,
                is_instructor, instructor_id) in result:
            user_info = {
                'id': user_id,
                'name': name,
                'surname': surname,
                'bio': bio,
                'university_id': university_id,
                'is_instructor': bool(is_instructor),
                'instructor_id': instructor_id
            }
            data.append(user_info)


        resp.body = json.dumps(data, ensure_ascii=False)


class UserResource():
    def __init__(self, database_connection):
        self.dbc = database_connection

    def on_get(self, req, resp, uid):
        uid = int(uid)
        c = self.dbc.cursor()
        result = c.execute('SELECT * FROM user;')
        for (user_id, name, surname, bio, university_id,
                is_instructor, instructor_id) in result:
            if user_id == uid:
                data = {
                    'id': uid,
                    'name': name,
                    'surname': surname,
                    'bio': bio,
                    'university_id': university_id,
                    'is_instructor': bool(is_instructor),
                    'instructor_id': instructor_id
                }
                break;

        resp.body = json.dumps(data, ensure_ascii=False)
