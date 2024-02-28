from sqlalchemy                 import create_engine
from sqlalchemy.orm             import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE    = "mysql+pymysql://mehmet.orhan:UkHMZyQD7Ru62*Z3@31.145.115.56:3306/fastapi_models"
engine          = create_engine(URL_DATABASE)
SessionLocal    = sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base            = declarative_base()