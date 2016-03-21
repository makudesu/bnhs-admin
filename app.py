from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from fields import excluded_fields, filtered_fields

app = Flask(__name__)
app.secret_key = 'super_secret_key=1a2511228276c7a743216e4543ce4652'
engine = create_engine("mysql://sql6111644:iGMQd39TBT@sql6.freesqldatabase.com/sql6111644", convert_unicode=True, echo=True)
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
    create_modal = True
    edit_modal = True
    page_size = 6
    can_view_details = True
    can_export = True
    export_types = ['html']
    column_export_exclude_list = ['password']
    column_filters = filtered_fields
    column_exclude_list = excluded_fields
    column_searchable_list = filtered_fields

class SubjectsView(ModelView):
    page_size = 10

admin = Admin(app, name='Bnhs', template_mode='bootstrap3', url='/', index_view=None)
admin.add_view(StudentsView(Students, loadSession()))
admin.add_view(SubjectsView(Subjects, loadSession()))

if __name__ == "__main__":
    session = loadSession()
    app.run(debug=True)


