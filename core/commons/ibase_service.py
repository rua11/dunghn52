from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configs.dev_config import DATABASE


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123456@localhost/dun"
                        


# DB_URL = SQLALCHEMY_DATABASE_URL % (DATABASE['default']['user'], DATABASE['default']['password'],
#                                     DATABASE['default']['host'], DATABASE['default']['db_name'])
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


