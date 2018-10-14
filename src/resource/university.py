import json

from repo import university

class UniversityListResource():
    def __init__(self, database_connection):
        self.repo = university.UniversityRepo(database_connection)

    def on_get(self, req, resp):
        data = self.repo.get_universities()

        resp.body = json.dumps(data, ensure_ascii=False)


class UniversityResource():
    def __init__(self, database_connection):
        self.repo = university.UniversityRepo(database_connection)

    def on_get(self, req, resp, uni_id):
        data = self.repo.get_university(uni_id)

        resp.body = json.dumps(data, ensure_ascii=False)
