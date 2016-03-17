from flask import Flask
from flask.ext.superadmin import Admin
import sqlsoup
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql://root:@localhost/codecalltut", echo=True)
Base = declarative_base(engine)
db = sqlsoup.SQLSoup("mysql://root:@localhost/codecalltut")

app = Flask(__name__)

class Prereg(Base):
    __tablename__ = 'tblprereg'
    __table_args__ = {'autoload':True}

    def __repr__(self):
        return self.username

def loadSession():
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

admin = Admin(app)
admin.register(Prereg, session=loadSession())

if __name__ == "__main__":
    session = loadSession()
    app.run(debug=True)


