from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Video(Base):
   __tablename__ = 'Video'
   id = Column(Integer, primary_key=True)
   artist = Column(String)
   name = Column(String)
   # year  = Column(Integer)
   link = Column(String)
   genre = Column(String)
  #  is_in_cart = Column(Boolean)
# TODO: Add your models below this line!