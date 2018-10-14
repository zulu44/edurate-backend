import json
import falcon

from repo import user


class UserListResource():
    def __init__(self, database_connection):
        self.repo = user.UserRepo(database_connection)

    def on_get(self, req, resp):
        data = self.repo.get_users()

        resp.body = json.dumps(data, ensure_ascii=False)


class UserResource():
    def __init__(self, database_connection):
        self.repo = user.UserRepo(database_connection)

    def on_get(self, req, resp, uid):
        data = self.repo.get_user(uid)

        resp.body = json.dumps(data, ensure_ascii=False)


class UserByUsernameResource():
    def __init__(self, database_connection):
        self.repo = user.UserRepo(database_connection)

    def on_get(self, req, resp, username):
        data = self.repo.get_user_by_username(username)

        resp.body = json.dumps(data, ensure_ascii=False)


class InstructorListResource():
    def __init__(self, database_connection):
        self.repo = user.UserRepo(database_connection)

    def on_get(self, req, resp):
        data = self.repo.get_instructors()

        resp.body = json.dumps(data, ensure_ascii=False)


class ProfileResource:
    def __init__(self, database_connection):
        self.repo = user.UserRepo(database_connection)

    def on_post(self, req, resp):
        data = req.bounded_stream.read()
        username = json.loads(data)['username']
        data = self.repo.get_user_by_username(username)
        resp.body = json.dumps(data, ensure_ascii=False)


class InstructorListByUniversityResource():
    def __init__(self, database_connection):
        self.repo = user.UserRepo(database_connection)

    def on_get(self, req, resp, uni_domain):
        data = self.repo.get_instructors_by_university(uni_domain)

        resp.body = json.dumps(data, ensure_ascii=False)
