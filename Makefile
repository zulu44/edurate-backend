me:
	cd src && gunicorn app -b ${EDURATE_ENDPOINT}

dev: reset_db
	cd src && gunicorn app -b ${EDURATE_ENDPOINT} --reload --reload-extra-file .

reset_db:
	rm -rf db
	mkdir db
	sqlite3 db/edurate.db < db.sql
