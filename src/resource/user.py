import json

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
        data = self.repo.get_user(int(uid))

        resp.body = json.dumps(data, ensure_ascii=False)
