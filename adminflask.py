from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.secret_key = 'super_secret_key=1a2511228276c7a743216e4543ce4652'

engine = create_engine("mysql://bnhs:123456@db4free.net/codecalltut", convert_unicode=True, echo=True)
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

class StudentsView(ModelView):
    page_size = 5
    can_view_details = True
#    create_modal = True
#    edit_modal = True
    can_export = True

    column_filters =['username','YearLevel','Status','SchoolYear','Student_ID','Lastname','Middlename','Gender','BirthDate','Age','BirthPlace','Religion','Email','Address','CPnumber',]
    column_exclude_list = ['password','CPnumber','Religion','BirthPlace','BirthDate','Guardian','Relationship','Emergency','ERelationship','Address  EAddress','username','SchoolYear','Email']
    column_searchable_list = ['username','YearLevel','Status','SchoolYear','Student_ID','Lastname','Middlename','Gender','BirthDate','Age','BirthPlace','Religion','Email','Address','CPnumber',]

class SubjectsView(ModelView):
    page_size = 10

admin = Admin(app, name='Bnhs', template_mode='bootstrap3')
admin.add_view(StudentsView(Students, loadSession()))
admin.add_view(SubjectsView(Subjects, loadSession()))

if __name__ == "__main__":
    session = loadSession()
    app.run(debug=True)


