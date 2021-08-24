from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

Base = automap_base()

class User(Base):
    __tablename__ = 'user'

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String)
    password = Column('password', String)
    age = Column('age', String)
    sex = Column('sex', String)
    country = Column('country', String)
    city = Column('city', String)
  
    def __init__(self, id, username, password, age, sex, country, city):
        self.id = id
        self.username = username
        self.password = password
        self.age = age
        self.sex = sex,
        self.country = country
        self.city = city

class Friendship(Base):
    __tablename__ = 'friendship'

    id = Column('id', Integer, primary_key=True)
    requester_id = Column('requester_id', Integer, ForeignKey('user.id'))
    addresse_id = Column('addresse_id', Integer, ForeignKey('user.id'))
    status = Column('status', Integer)
   
    requester = relationship("User", foreign_keys=[requester_id])
    addresse = relationship("User", foreign_keys=[addresse_id])

    def __init__(self, requester_id, addresse_id, status):
        self.requester_id = requester_id
        self.addresse_id = addresse_id
        self.status = status
    
class DiaryLog(Base):
    __tablename__ = 'diary_log'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    date = Column('date', String)
    log = Column('log', String)
    visible = Column('visible', Integer)
    user_id = Column('user_id', Integer, ForeignKey('user.id'))

    def __init__(self, name, date, log, visible, user_id):
        self.name = name
        self.date = date
        self.log = log
        self.visible = visible
        self.user_id = user_id

