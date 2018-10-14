import json
import falcon

from repo import instructor

class RateResource():
    def __init__(self, database_connection):
        self.repo = instructor.InstructorRepo(database_connection)

    def on_post(self, req, resp):
        if 'edurate-user' in req.cookies:
            uid = req.cookies['edurate-user']
            data = req.bounded_stream.read()
            rating_data = json.loads(data)
            instructor_id = rating_data['instructor_id']
            rating = rating_data['rating']
            self.repo.set_rating(uid, instructor_id, rating)
        else:
            resp.status = falcon.HTTP_401


class CommentResource():
    def __init__(self, database_connection):
        self.repo = instructor.InstructorRepo(database_connection)

    def on_post(self, req, resp):
        if 'edurate-user' in req.cookies:
            uid = req.cookies['edurate-user']
            data = req.bounded_stream.read()
            comment_data = json.loads(data)
            instructor_id = comment_data['instructor_id']
            comment = comment_data['comment']
            self.repo.add_comment(uid, instructor_id, comment)
        else:
            resp.status = falcon.HTTP_401


