from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://ojaialim_ti:@localhost:3306/ojaialim_visita_granjas"
#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql://dxuxmkvgbkorbr:9ab1a1ef687526acb51ca5ec8af36e8a0fe6b913380dedc45faa58deace9aa1a@ec2-54-145-224-156.compute-1.amazonaws.com/ddqgm0v6j8voj4"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
