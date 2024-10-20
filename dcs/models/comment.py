from sqlalchemy import Column, Integer, String, DateTime, Identity
from sqlalchemy.sql import func

from dcs import db


class Comment(db.Model):
    id = Column(Integer, Identity(), primary_key=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    name = Column(String(30), nullable=False)
    content = Column(String(200), nullable=False)
