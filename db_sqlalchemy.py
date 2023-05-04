from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sk_constants import INITIAL_LIST


Base = declarative_base()

class Access(Base):
    __tablename__ = 'access'
    id = Column(Integer(), primary_key=True)
    name = Column(String(350), nullable=False)
    pin = Column(String(4), nullable=False)
    is_active = Column(Integer(), nullable=False)


def db_init_sqlalchemy():

    db_engine = create_engine('sqlite:///smartkey.db')
    Base.metadata.create_all(db_engine)

    Session = sessionmaker()
    Session.configure(bind=db_engine)
    session = Session()

    lista = INITIAL_LIST
    
    for person in lista:
        entity = (
            session.query(Access)
            .filter(Access.name == person[0])
            .one_or_none()
        )
        if entity is None:
            entity = Access(
                name = person[0],
                pin = person[1],
                is_active = person[2]
            )
            session.add(entity)
            session.commit()



def get_data_sqlalchemy():
    db_engine = create_engine('sqlite:///smartkey.db')

    Session = sessionmaker()
    Session.configure(bind=db_engine)
    session = Session()

    return session.query(Access).all()


def db_add_data(new_entry):

    db_engine = create_engine('sqlite:///smartkey.db')
    Base.metadata.create_all(db_engine)

    Session = sessionmaker()
    Session.configure(bind=db_engine)
    session = Session()

    entity = (
        session.query(Access)
        .filter(Access.name == new_entry[0])
        .one_or_none()
        )
    if entity is None:
        entity = Access(
                name = new_entry[0],
                pin = new_entry[1],
                is_active = new_entry[2]
            )
        session.add(entity)
        session.commit()

    else:
        session.query(Access).filter(Access.name == new_entry[0]).update({Access.pin:new_entry[1], Access.is_active:new_entry[2]})

        session.commit()

def db_delete_data(new_entry):

    db_engine = create_engine('sqlite:///smartkey.db')
    Base.metadata.create_all(db_engine)

    Session = sessionmaker()
    Session.configure(bind=db_engine)
    session = Session()

    
    entity = (
        session.query(Access)
        .filter(Access.name == new_entry[0])
        .one_or_none()
        )
    if entity != None:
        session.delete(entity)
        session.commit()
