from flask import Flask
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from models import Base

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['TESTING'] = True

ENV = 'dev'
LOGIN = False
USER = ''

engine = create_engine('postgresql://postgres:0000@localhost/Diaries')

Base.prepare(engine, reflect=True)

session = Session(engine)