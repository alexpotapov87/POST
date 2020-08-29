This is sample for FBK DevOps role
This is a script to recieve POST request, write a value to PostgreSQL 

to run docker postgres for test:
docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=pgpassword postgres:13-alpine
to check the table :
docker exec -u postgres -it  ID psql
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
