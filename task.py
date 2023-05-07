from sqlalchemy import Column,Integer,String
from base import base

class task(base):
    __tablename__ = "tasks"
    sr_no = Column(Integer, primary_key=True,autoincrement=True)
    title = Column(String(50), nullable=False)
    description= Column(String(50))

    def __init__(self,title,desc):
        self.title = title
        self.description = desc

