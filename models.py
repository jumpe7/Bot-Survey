from datetime import datetime

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import (Column, BigInteger, Text, DATETIME, Integer, ForeignKey)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    telegram_id = Column(BigInteger, primary_key=True)
    username = Column(Text, nullable=False)

    created_at = Column(DATETIME, nullable=False)

class AnonymousMessage(Base):
    __tablename__ = 'anonymous_messages'

    id = Column(BigInteger, primary_key=True)

    sender_id = Column(BigInteger, nullable=False, index=True)

    receiver_id = Column(BigInteger, nullable=False, index=True)

    text = Column(Text, nullable=False)
    created_at = Column(DATETIME, nullable=False, index=True)

