import falcon
import sqlite3
import json

import cors
from resource import user
from resource import university

conn = sqlite3.connect('../db/edurate.db')

application = falcon.API(middleware=[cors.CORSComponent()])

user_list = user.UserListResource(conn)
application.add_route('/user', user_list)

user = user.UserResource(conn)
application.add_route('/user/{uid}', user)

university_list = university.UniversityListResource(conn)
application.add_route('/university', university_list)

university = university.UniversityResource(conn)
application.add_route('/university/{uni_id}', university)
