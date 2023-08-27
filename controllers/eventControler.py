from db import conect
from model import Ekitaldiak, EkitaldiPartehartzaileak, Erabiltzaileak
from datetime import datetime, date, time


def getEvent(event_id):
    try:
        session = conect()
        event = session.query(Ekitaldiak).where(Ekitaldiak.col_eventID == event_id).all()[0]
    except Exception as e:
        print(e)
    finally:
        session.close()
    return event

def getAllEvents():
    try:
        session = conect()
        events = session.query(Ekitaldiak).all()
    except Exception as e:
        print(e)
        return False
    finally:
        session.close()
    return events

def addEvent(name, location, date, time):
    try:
        internal_date = datetime.strptime(date, '%Y/%m/%d').date()
        internal_time = datetime.strptime(time, '%H:%M').time()
        session = conect()
        event = Ekitaldiak(col_ekitaldi_izena=name,
                           col_ekitaldi_kokalekua=location,
                           col_ekitaldi_data=internal_date,
                           col_ekitaldi_ordua=internal_time)
        session.add(event)
        session.commit()

    except Exception as e:
        print(e)
        return False
    finally:
        session.close()
    return True     




def getEventParticipants(event_id):
    try:
        result = []
        session = conect()
        participants = session.query(EkitaldiPartehartzaileak).where(EkitaldiPartehartzaileak.col_eventID == event_id).order_by(EkitaldiPartehartzaileak.col_partehartzeMota).all()
        for participant in participants:
            participant_info = session.query(Erabiltzaileak).filter(Erabiltzaileak.col_userID == participant.col_userID).all()[0]
            result.append({"col_userID" : participant_info.col_userID, "col_erabiltzaile_izena" :participant_info.col_erabiltzaile_izena, "col_erabiltzaile_abizena" : participant_info.col_erabiltzaile_abizena, "col_partehartzeMota":participant.col_partehartzeMota})
    except Exception as e:
        print(e)
    finally:
        session.close()
    return result

def putEventParticipant(event_id, user_id, participation_type):
    try:
        session = conect()
        ekitaldiPartehartzailea = EkitaldiPartehartzaileak(col_eventID=event_id,
                                                           col_userID=user_id,
                                                           col_partehartzeMota=participation_type)
        session.add(ekitaldiPartehartzailea)
        session.commit()

    except Exception as e:
        print(e)
        return False
    finally:
        session.close()
    return True