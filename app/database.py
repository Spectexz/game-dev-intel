import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

CONN_STRING = os.environ.get("CONN_STRING")
engine = create_engine(CONN_STRING, echo=True)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
