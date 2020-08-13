from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String,Integer
from sqlalchemy import DateTime

engine = create_engine('mysql://root:123456@localhost/shiyanlougithub')
Base = declarative_base()

class Repositories(Base):
    __tablename__ = 'repositories'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    update_time = Column(DateTime)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
