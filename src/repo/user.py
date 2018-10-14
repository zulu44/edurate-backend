import math

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
                instructor = (
                    self.get_instructor_details(instructor_id, user_id)
                )
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
            instructor = self.get_instructor_details(instructor_id, user_id)
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
        result = result.fetchone()
        if result == None:
            return None
        (user_id, username, name, surname, bio, university_id,
                is_instructor, instructor_id) = result
        # get university info
        university = self.uni_repo.get_university(university_id)
        # get instructor related info
        if (is_instructor):
            instructor = self.get_instructor_details(instructor_id, user_id)
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
            instructor = self.get_instructor_details(instructor_id, user_id)
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

    def get_instructors_by_university(self, uni_domain):
        c = self.dbc.cursor()
        uni_id = c.execute('SELECT id FROM university WHERE domain=?',
            (uni_domain,)).fetchone()[0]
        result = c.execute('SELECT * FROM user WHERE is_instructor=1 and'
            ' university_id=?', (uni_id,))
        data = []
        for (user_id, username, name, surname, bio, university_id,
                is_instructor, instructor_id) in result:
            # get university info
            university = self.uni_repo.get_university(university_id)
            # get instructor related info
            instructor = self.get_instructor_details(instructor_id, user_id)
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

    def get_student(self, uid):
        c = self.dbc.cursor()
        result = c.execute('SELECT * FROM user WHERE id=?;', (uid,))
        (user_id, username, name, surname, bio, university_id,
                is_instructor, instructor_id) = result.fetchone()
        # get university info
        university = self.uni_repo.get_university(university_id)
        # create data object
        data = {
            'id': user_id,
            'username': username,
            'name': name,
            'surname': surname,
            'bio': bio,
            'university': university
        }

        return data

    def calculate_rating(self, ins_id):
        c = self.dbc.cursor()
        c.execute('SELECT university_id FROM user WHERE id=?;', (ins_id,))
        uni_id = c.fetchone()[0]
        students = c.execute('SELECT * FROM user WHERE is_instructor=? and '
            'university_id=?;', ("0", uni_id))
        student_count = 0
        for student in students:
            student_count += 1
        # calculate a rating unit by using student count
        unit_rating = 50 / (student_count*2)
        ratings = c.execute('SELECT rating FROM instructor_rating'
            ' WHERE instructor_id=?;', (ins_id,))
        # calculate final rating
        gpa = 50
        for (rating,) in ratings:
            gpa += rating * unit_rating
        return gpa

    def get_comments(self, ins_id):
        c = self.dbc.cursor()
        comments = c.execute('SELECT comment FROM instructor_comment'
            ' WHERE instructor_id=?;', (ins_id,))
        comment_list = []
        for (comment,) in comments:
            comment_list.append(comment)
        return comment_list

    def calculate_letter_note(self, gpa):
        num = math.ceil((98.0-gpa) / 4.0)
        msl = chr(ord('A') + num)
        if gpa - (98.0 - num * 4.0) > 2.0:
            return msl + chr(ord(msl) - 1)
        else:
            return msl + msl

    def get_instructor_details(self, instructor_id, user_id):
        instructor = self.ins_repo.get_instructor(instructor_id)
        gpa = instructor["gpa"] = self.calculate_rating(user_id)
        instructor["comments"] = self.get_comments(user_id)
        instructor["letter_note"] = self.calculate_letter_note(gpa)

        return instructor
