from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy import Date, Boolean

engine = create_engine('mysql://root:123456@localhost/shiyanlou')
Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), index=True)
    description = Column(String(1024))
    type = Column(String(64), index=True)
    students = Column(Integer)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), index=True)
    is_vip = Column(Boolean, default=False)
    school_job = Column(String(64))
    level = Column(Integer,index=True)
    join_date = Column(Date)
    learn_courses_num = Column(Integer)
    status = Column(String(64), index=True)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
