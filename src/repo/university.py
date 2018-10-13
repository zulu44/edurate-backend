class UniversityRepo():
    def __init__(self, database_connection):
        self.dbc = database_connection

    def get_universities(self):
        c = self.dbc.cursor()
        result = c.execute('SELECT * FROM university;')
        data = []
        for (uni_id, domain, name) in result:
            user_info = {
                'id': uni_id,
                'domain': domain,
                'name': name
            }
            data.append(user_info)

        return data

    def get_university(self, uni_id):
        uni_id = int(uni_id)
        c = self.dbc.cursor()
        result = c.execute('SELECT * FROM university;')
        for (university_id, domain, name) in result:
            if university_id == uni_id:
                data = {
                    'id': uni_id,
                    'domain': domain,
                    'name': name
                }
                break;

        return data
