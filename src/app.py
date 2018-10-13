import falcon
import sqlite3
import json
import user

conn = sqlite3.connect('../db/edurate.db')

application = falcon.API()

user_list = user.UserListResource(conn)
application.add_route('/user', user_list)

user = user.UserResource(conn)
application.add_route('/user/{uid}', user)
