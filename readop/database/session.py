from sqlalchemy.orm import sessionmaker

from .engine import Engine


Session = sessionmaker(bind=Engine)
