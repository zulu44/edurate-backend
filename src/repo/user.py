from repo import university
from repo import instructor

class UserRepo():
    def __init__(self, database_connection):
        self.dbc = database_connection
        self.uni_repo = university.UniversityRepo(database_connection)
        self.ins_repo = instructor.InstructorRepo(database_connection)

    def get_users(self):
        c = self.dbc.cursor()
        result = c.execute('SELECT * FROM user;')
        data = []
        for (user_id, username, name, surname, bio, university_id,
                is_instructor, instructor_id) in result:
            # get university info
            university = self.uni_repo.get_university(university_id)
            # get instructor related info
            if (is_instructor):
                instructor = self.ins_repo.get_instructor(instructor_id)
            else:
                instructor = None
            # create data object and append it to list
            user_info = {
                'id': user_id,
                'username': username,
                'name': name,
                'surname': surname,
                'bio': bio,
                'university': university,
                'is_instructor': bool(is_instructor),
                'instructor': instructor
            }
            data.append(user_info)

        return data

    def get_user(self, uid):
        c = self.dbc.cursor()
        result = c.execute('SELECT * FROM user WHERE id=?;', (uid,))
        (user_id, username, name, surname, bio, university_id,
                is_instructor, instructor_id) = result.fetchone()
        # get university info
        university = self.uni_repo.get_university(university_id)
        # get instructor related info
        if (is_instructor):
            instructor = self.ins_repo.get_instructor(instructor_id)
        else:
            instructor = None
        # create data object
        data = {
            'id': user_id,
            'username': username,
            'name': name,
            'surname': surname,
            'bio': bio,
            'university': university,
            'is_instructor': bool(is_instructor),
            'instructor': instructor
        }

        return data

    def get_user_by_username(self, username):
        c = self.dbc.cursor()
        result = c.execute('SELECT * FROM user WHERE username=?;', (username,))
        (user_id, username, name, surname, bio, university_id,
                is_instructor, instructor_id) = result.fetchone()
        # get university info
        university = self.uni_repo.get_university(university_id)
        # get instructor related info
        if (is_instructor):
            instructor = self.ins_repo.get_instructor(instructor_id)
        else:
            instructor = None
        # create data object
        data = {
            'id': user_id,
            'username': username,
            'name': name,
            'surname': surname,
            'bio': bio,
            'university': university,
            'is_instructor': bool(is_instructor),
            'instructor': instructor
        }

        return data


    def get_instructors(self):
        c = self.dbc.cursor()
        result = c.execute('SELECT * FROM user WHERE is_instructor=?;', ("1",))
        data = []
        for (user_id, username, name, surname, bio, university_id,
                is_instructor, instructor_id) in result:
            # get university info
            university = self.uni_repo.get_university(university_id)
            # get instructor related info
            instructor = self.ins_repo.get_instructor(instructor_id)
            # create data object and append it to list
            user_info = {
                'id': user_id,
                'username': username,
                'name': name,
                'surname': surname,
                'bio': bio,
                'university': university,
                'is_instructor': bool(is_instructor),
                'instructor': instructor
            }
            data.append(user_info)

        return data
