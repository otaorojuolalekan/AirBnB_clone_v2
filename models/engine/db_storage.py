#!/usr/bin/python3
"""database storage engine"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.place import place_amenity

classes = {
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class DBStorage:
    '''database storage engine for mysql storage'''

    def __init__(self):
        '''instantiate new DBStorage instance'''
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.engine = create_engine(
            f'mysql+mysqldb://{HBNB_MYSQL_USER}:{HBNB_MYSQL_PWD}@{HBNB_MYSQL_HOST}/{HBNB_MYSQL_DB}',
            pool_pre_ping=True
        )

        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.engine)

        session_factory = sessionmaker(bind=self.engine, expire_on_commit=False)
        self.session = scoped_session(session_factory)()

    def all(self, cls=None):
        '''query on the current db session all cls objects'''
        dct = {}
        if cls is None:
            for c in classes.values():
                objs = self.session.query(c).all()
                for obj in objs:
                    key = f'{obj.__class__.__name__}.{obj.id}'
                    dct[key] = obj
        else:
            objs = self.session.query(cls).all()
            for obj in objs:
                key = f'{obj.__class__.__name__}.{obj.id}'
                dct[key] = obj
        return dct

    def new(self, obj):
        '''adds the obj to the current db session'''
        if obj is not None:
            try:
                self.session.add(obj)
                self.session.flush()
                self.session.refresh(obj)
            except Exception as ex:
                self.session.rollback()
                raise ex

    def save(self):
        '''commit all changes of the current db session'''
        self.session.commit()

    def delete(self, obj=None):
        '''deletes from the current database session the obj if it's not None'''
        if obj is not None:
            self.session.query(type(obj)).filter(type(obj).id == obj.id).delete()

    def reload(self):
        '''reloads the database'''
        Base.metadata.create_all(self.engine)

    def close(self):
        """closes the working SQLAlchemy session"""
        self.session.close()
