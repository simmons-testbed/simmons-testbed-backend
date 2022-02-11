from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import session

Base = declarative_base()

class USER(Base):
    __tablename__='USER'

    id_num = Column(Integer, nullable=False, primary_key=True)
    howmany = Column(Integer, nullable=False)
    nowcheck = Column(Boolean, nullable=False)
    xboundary = Column(Integer, nullable=False)
    yboundaty = Column(Integer, nullable=False)

    def __init__(self, peop, check, xbound, ybound):
        self.howmany = peop
        self.nowcheck = check
        self.xboundary = xbound
        self.yboundaty = ybound

# 인원수 체크를 적용하는지 알아보는 함수 
def applyCheck(db_session):
    try:
        apply = db_session.query(USER).first()
    except:
        db_session.rollback()
        raise
    finally:
        db_session.close()

    # 인원수 적용 여부를 체크할지 확인 
    if apply is not None:
        if apply.nowcheck :
            return True
        else :
            return False
    return False

# 몇명이 있어야 하는지 알아보는 함수 
def getNumber(db_session):
    try:
        num = db_session.query(USER).first()
    except:
        db_session.rollback()
        raise
    finally:
        db_session.close()

    if num is not None:
        return num.howmany
    else :
        return '0'
    
# 사용자의 위치정보 반환 
def getPosition(db_session):
    try:
        pos = db_session.query(USER).first()
    except:
        db_session.rollback()
        raise
    finally:
        db_session.close()

    if pos is not None:
        return [pos.xboundary, pos.yboundaty]
    else :
        return [0,0]
