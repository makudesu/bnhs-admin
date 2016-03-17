from flask import Flask
from flask.ext.superadmin import Admin
import sqlsoup

#db = sqlsoup.SQLSoup("mysql://bnhs:123456@db4free.net/codecalltut")
db = sqlsoup.SQLSoup("mysql://root:@localhost/codecalltut")
users = db.tblprereg.all()

app = Flask(__name__)
admin = Admin(app)


if __name__ == "__main__":
    app.run(debug=True)

