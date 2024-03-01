from sqlalchemy                 import create_engine
from sqlalchemy.orm             import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_host         = "db_host"
db_port         = "db_port"
db_scheme       = "db_scheme"
db_username     = "db_username"
db_password     = "db_password"
URL_DATABASE    = f"mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_scheme}"
engine          = create_engine(URL_DATABASE)
SessionLocal    = sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base            = declarative_base()