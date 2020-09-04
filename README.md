This is sample for FBK DevOps role
This is a script to recieve a POST request and write a value to Postgre DB

To test an app - run:
docker-compose up
pip install requests
python request-post.py
python request-get.py

Expected results for request-post.py:
OK! Received!
Expected results for request-get.py
<!-- <html>
<head><title>403 Forbidden</title></head>
<body>
<center><h1>403 Forbidden</h1></center>
<hr><center>nginx/1.19.2</center>
</body>
</html> -->


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
