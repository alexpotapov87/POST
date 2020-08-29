from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
POSTGRES = {
    'user': 'postgres',
    'pw': 'pgpassword',
    'db': 'postgres',
    'host': 'postgres',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db = SQLAlchemy(app)


class request_table(db.Model):
    ''' Define table '''
    __tablename__ = 'requests'
    id = db.Column(db.Integer, primary_key=True)
    response = db.Column(db.String(200), unique=False)


db.create_all()


@app.route('/post', methods=['POST'])
def result():
    ''' Recieve request & write it to db request and value '''
    response_re = request.form['POST_REQUEST']
    received = request_table(response=str({response_re}))
    db.session.add(received)
    db.session.commit()
    return 'OK! Received!'  # response to the request.


if __name__ == '__main__':
    postgres = db.init_app(app)
    app.run(debug=True, host='0.0.0.0')
