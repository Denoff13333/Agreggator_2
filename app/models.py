from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.settings import config

Base = declarative_base()
engine = create_engine(config.DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

class AccessLog(Base):
    __tablename__ = 'access_logs'
    id = Column(Integer, primary_key=True)
    ip_address = Column(String)
    timestamp = Column(DateTime)
    request_method = Column(String)
    request_path = Column(String)
    response_code = Column(Integer)
    user_agent = Column(String)

Base.metadata.create_all(engine)
