This is sample for FBK DevOps role
This is a script to recieve a POST request and write a value to Postgre DB

app_srv folder:
app.py - Script to catch&write a POST request )
Dockerfile - dockerfile for flask app
requirements.txt - requirements for pip

to run docker postgres for test:
docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=pgpassword postgres:13-alpine
to check the table :
docker exec -u postgres -it container_ID psql
\dt
\c postgres

TABLE requests;

SELECT *
  FROM information_schema.columns
 WHERE table_schema = 'postgres'
   AND table_name   = 'requests'
     ;

SQLAlchemy resource:
https://flask-sqlalchemy.palletsprojects.com/en/2.x/
