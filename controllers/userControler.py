from db import conect
from model import Erabiltzaileak, EkitaldiPartehartzaileak


def addUser(name,surname):
    try:
        session = conect()
        user = Erabiltzaileak(col_erabiltzaile_izena = name, col_erabiltzaile_abizena = surname)
        session.add(user)
        session.commit()

    except Exception as e:
        print(e)
        return False
    finally:
        session.close()
    return True

def getUser(userID):
    try:
        session = conect()
        user = session.query(Erabiltzaileak).filter(Erabiltzaileak.col_userID == userID).all()[0]
    
    except Exception as e:
        print(e)
    finally:
        session.close()
    return user


