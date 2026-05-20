from app.database import Base
from app.database import engine
from app.models import GameSnapshot
import os
from dotenv import load_dotenv


#load_dotenv()
#print(os.environ.get("CONN_STRING"))


Base.metadata.create_all(engine)