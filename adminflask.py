from flask import Flask
from flask.ext.superadmin import Admin

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

engine = create_engine("mysql://root:@localhost/codecalltut", echo=True)
Base = declarative_base(engine)

class Students(Base):
    __tablename__ = 'tblprereg'
    __table_args__ = {'autoload':True}

    def __repr__(self):
        return self.username

class Subjects(Base):
    __tablename__ = 'tblsubjects'
    __table_args__ = {'autoload':True}

    def __repr__(self):
        return '%r' % self.RecNo

def loadSession():
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

admin = Admin(app)
admin.register(Students, session=loadSession())
admin.register(Subjects, session=loadSession())

if __name__ == "__main__":
    session = loadSession()
    app.run(debug=True)


