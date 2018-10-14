import json
import falcon

from repo import instructor

class RateResource():
    def __init__(self, database_connection):
        self.repo = instructor.InstructorRepo(database_connection)

    def on_post(self, req, resp):
        data = req.bounded_stream.read()
        username = json.loads(data)['username']
        uid = self.repo.get_id(username)
        rating_data = json.loads(data)
        instructor_id = rating_data['instructor_id']
        rating = rating_data['rating']
        self.repo.set_rating(uid, instructor_id, rating)


class CommentResource():
    def __init__(self, database_connection):
        self.repo = instructor.InstructorRepo(database_connection)

    def on_post(self, req, resp):

        data = req.bounded_stream.read()
        username = json.loads(data)['username']
        uid = self.repo.get_id(username)
        comment_data = json.loads(data)
        instructor_id = comment_data['instructor_id']
        comment = comment_data['comment']
        self.repo.add_comment(uid, instructor_id, comment)

