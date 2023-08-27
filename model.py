import sqlalchemy
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase,Mapped, Session, mapped_column
from sqlalchemy.types import DateTime, Integer, String, Date, Time
from dataclasses import dataclass
from datetime import date, time

_UserTableName = "erabiltzaileak"
_EventTableName = "ekitaldiak"
_UsersInEventTableName = "ekitaldipartaideak"
class Base(DeclarativeBase):
    pass

@dataclass
class Erabiltzaileak(Base):
    __tablename__ = _UserTableName


    col_userID: Mapped[int]                 = Column(Integer, name="userid", primary_key=True, autoincrement=True)
    col_erabiltzaile_izena: Mapped[str]     = Column(String(128), name="user_name", nullable=False)
    col_erabiltzaile_abizena: Mapped[str]   = Column(String(128), name="user_surname", nullable=False)

    def __repr__(self):
        return f"{self.col_erabiltzaile_izena} {self.col_erabiltzaile_abizena}"

@dataclass
class Ekitaldiak(Base):

    __tablename__ = _EventTableName
    col_eventID: Mapped[int]            = Column(Integer, name="eventid",  primary_key=True, autoincrement=True)
    col_ekitaldi_izena: Mapped[str]     = Column(String(128), name="event_name", nullable=False)
    col_ekitaldi_kokalekua: Mapped[str] = Column(String(128),name="event_location", nullable=False)
    col_ekitaldi_data: Mapped[date]     = Column(Date, name="event_date", nullable=False)
    col_ekitaldi_ordua: Mapped[time]    = Column(Time,name="event_time", nullable=False)

    def __repr__(self):
        return f"{self.col_ekitaldi_izena} {self.col_ekitaldi_kokalekua} {self.col_ekitaldi_data} {self.col_ekitaldi_ordua}"
    

@dataclass
class EkitaldiPartehartzaileak(Base):

    __tablename__ = _UsersInEventTableName

    col_entryID: Mapped[int]        = Column(Integer, name="entryid",  primary_key=True, autoincrement=True)
    col_eventID: Mapped[int]        = Column(Integer, ForeignKey(_EventTableName + '.eventid'), name="eventid", nullable=False)
    col_userID:  Mapped[int]        = Column(Integer, ForeignKey(_UserTableName + '.userid'),  name="userid",nullable=False)
    col_partehartzeMota: Mapped[int]= Column(Integer,  name="participation_type", nullable= False)


