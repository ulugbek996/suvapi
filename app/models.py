from  sqlalchemy   import Column, Integer, String, Boolean, ForeignKey, Float
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
        "users.id", ondelete="CASCADE"))
    user_add = Column(Boolean, server_default = 'FALSE' , nullable = False)
    station_add = Column(Boolean, server_default = 'FALSE' , nullable = False)


class Region(Base):
    __tablename__ = "regions"
    id = Column(Integer,primary_key=True, nullable=False)
    name = Column(String,nullable=False)


class Balans(Base):
    __tablename__ = "tashkilot"
    id = Column(Integer,primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    region_id = Column(Integer, ForeignKey(
        "regions.id", ondelete="CASCADE"))



class District(Base):
    __tablename__ = "districts"
    id = Column(Integer,primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    region_id = Column(Integer, ForeignKey(
        "regions.id", ondelete="CASCADE"))

class Sensor(Base):
    __tablename__ = "sensors"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)


class Station(Base):
    __tablename__ = "stations"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String , nullable=False)
    owner_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"))
    edit_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"))
    region_id = Column(Integer, ForeignKey(
        "regions.id", ondelete="CASCADE"))
    tashkilot_id = Column(Integer, ForeignKey(
        "tashkilot.id", ondelete="CASCADE"))
    district_id = Column(Integer, ForeignKey(
        "districts.id", ondelete="CASCADE"))
    sensor_id = Column(Integer, ForeignKey(
        "sensors.id", ondelete="CASCADE"))
    simcard = Column(String, nullable=False)
    code = Column(String,unique=True , nullable=False)
    update_at = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))



class DataLastWater(Base):
    __tablename__ = "datalastwaters"
    id = Column(Integer, primary_key=True, nullable=False)
    station_id = Column(Integer, ForeignKey(
        "stations.id", ondelete="CASCADE"))
    level = Column(Float, nullable = False)
    flow = Column(Float, nullable = False)
    corec = Column(Integer, nullable = False)
    timedata = Column(Integer , nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))