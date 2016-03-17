from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql://bnhs:123456@db4free.net", echo=True)
Base = declarative_base(engine)

class Prereg(Base):
    __tablename__ = 'tblprereg'
    __table_args__ = {'autoload':True}

    def loadSession():
        metadata = Base.metadata
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

    if __name__ == "__main__":
        session = loadSession()
        res = session.query(Prereg).all()
        print res[1].title
