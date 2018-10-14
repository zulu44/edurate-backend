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


class InstructorListResource():
    def __init__(self, database_connection):
        self.repo = user.UserRepo(database_connection)

    def on_get(self, req, resp):
        data = self.repo.get_instructors()

        resp.body = json.dumps(data, ensure_ascii=False)

class ProfileResource:
    def __init__(self, database_connection):
        self.repo = user.UserRepo(database_connection)

    def on_get(self, req, resp):
        if 'edurate-user' in req.cookies:
            uid = req.cookies['edurate-user']
            data = self.repo.get_user(uid)
            resp.body = json.dumps(data, ensure_ascii=False)
        else:
            resp.status = falcon.HTTP_401
