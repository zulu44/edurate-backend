import json

from repo import user

class LoginResource():
    def __init__(self, database_connection):
        self.user_repo = user.UserRepo(database_connection)

    def on_post(self, req, resp):
        data = req.bounded_stream.read()
        username = json.loads(data)['username']
        user = self.user_repo.get_user_by_username(username)
        resp.set_cookie('edurate-user', str(user['id']))

