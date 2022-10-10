from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer ,primary_key=True ,nullable=False)
    first_name = Column(String,nullable=False)
    last_name = Column(String,nullable=False)
    email = Column(String,nullable=False,unique=True)
    login = Column(String,nullable=False , unique=True)
    password = Column(String,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))


class UserPrivate(Base):
    __tablename__ = "userprivate"
    id = Column(Integer, primary_key=True , nullable=False)
    user_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), primary_key=True)
    user_add = Column(Boolean, server_default = 'FALSE' , nullable = False)
    station_add = Column(Boolean, server_default = 'FALSE' , nullable = False)


class Region(Base):
    __tablename__ = "regions"
    id = Column(Integer,primary_key=True, nullable=False)
    name = Column(String,nullable=False)


class Balans(Base):
    __tablename__ = "balans"
    id = Column(Integer,primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    region_id = Column(Integer, ForeignKey(
        "regions.id", ondelete="CASCADE"), primary_key=True)


class District(Base):
    __tablename__ = "districts"
    id = Column(Integer,primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    region_id = Column(Integer, ForeignKey(
        "regions.id", ondelete="CASCADE"), primary_key=True)



class Station(Base):
    __tablename__ = "stations"
    id = Column(Integer, primary_key=True, nullable=False)
    owner_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), primary_key=True)
    edit_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), primary_key=True)
    region_id = Column(Integer, ForeignKey(
        "regions.id", ondelete="CASCADE"), primary_key=True)
    balans_id = Column(Integer, ForeignKey(
        "balans.id", ondelete="CASCADE"), primary_key=True)
    district_id = Column(Integer, ForeignKey(
        "districts.id", ondelete="CASCADE"), primary_key=True)
    code = Column(String,unique=True , nullable=False)


