import falcon
import sqlite3
import json

import cors
from resource import user
from resource import university
from resource import login
from resource import instructor

conn = sqlite3.connect('../db/edurate.db')

ro = falcon.response.ResponseOptions()
ro.secure_cookies_by_default = False

application = falcon.API(
    middleware=[cors.CORSComponent()]
)

application.resp_options = ro

user_list = user.UserListResource(conn)
application.add_route('/user', user_list)

instructor_list = user.InstructorListResource(conn)
application.add_route('/instructor', instructor_list)

instructor_list_by_university = user.InstructorListByUniversityResource(conn)
application.add_route('/instructor/{uni_domain}',
    instructor_list_by_university)

profile = user.ProfileResource(conn)
application.add_route('/profile', profile)

user_by_username = user.UserByUsernameResource(conn)
application.add_route('/user/{username}', user_by_username)

user = user.UserResource(conn)
application.add_route('/user/id/{uid}', user)

university_list = university.UniversityListResource(conn)
application.add_route('/university', university_list)

university = university.UniversityResource(conn)
application.add_route('/university/{uni_id}', university)

login = login.LoginResource(conn)
application.add_route('/login', login)

rate = instructor.RateResource(conn)
application.add_route('/rate', rate)

comment = instructor.CommentResource(conn)
application.add_route('/comment', comment)
