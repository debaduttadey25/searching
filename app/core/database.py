from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

# Retrieve the MySQL connection URL from the .env file.
# If not present, we provide a default local MySQL string.
# Ensure your MySQL server has a database named 'mydatabase' created.
SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "mysql+pymysql://root:12345@127.0.0.1:3306/playground"
)

# Production-ready Engine Configuration
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,  # Verify connections in the pool before usage
    pool_recycle=3600,   # Recycle connections after 1 hour (fixes MySQL timeout drops)
    pool_size=5,         # Number of connections to keep open
    max_overflow=10      # Max extra connections if pool is busy
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
