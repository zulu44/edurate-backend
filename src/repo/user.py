from repo import university

class UserRepo():
    def __init__(self, database_connection):
        self.dbc = database_connection
        self.uni_repo = university.UniversityRepo(database_connection)

    def get_users(self):
        c = self.dbc.cursor()
        result = c.execute('SELECT * FROM user;')
        data = []
        for (user_id, name, surname, bio, university_id,
                is_instructor, instructor_id) in result:
            # get university info
            university = self.uni_repo.get_university(university_id)
            # create data object and append it to list
            user_info = {
                'id': user_id,
                'name': name,
                'surname': surname,
                'bio': bio,
                'university': university,
                'is_instructor': bool(is_instructor),
                'instructor_id': instructor_id
            }
            data.append(user_info)

        return data

    def get_user(self, uid):
        uid = int(uid)
        c = self.dbc.cursor()
        result = c.execute('SELECT * FROM user;')
        for (user_id, name, surname, bio, university_id,
                is_instructor, instructor_id) in result:
            # get university info
            university = self.uni_repo.get_university(university_id)
            # create data object
            if user_id == uid:
                data = {
                    'id': uid,
                    'name': name,
                    'surname': surname,
                    'bio': bio,
                    'university': university,
                    'is_instructor': bool(is_instructor),
                    'instructor_id': instructor_id
                }
                break;

        return data
