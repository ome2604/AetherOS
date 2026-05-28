from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from app.core.config import settings


# =========================================
# DATABASE CONFIG
# =========================================

DATABASE_URL = settings.DATABASE_URL

print(DATABASE_URL)

engine = create_engine(
    DATABASE_URL
)

# IMPORTANT:
# Prevent DetachedInstanceError
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    bind=engine,
)


# =========================================
# DATABASE DEPENDENCY
# =========================================

def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()