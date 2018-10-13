me:
	rm -rf db
	mkdir db
	sqlite3 db/edurate.db < db.sql
	cd src && gunicorn app
