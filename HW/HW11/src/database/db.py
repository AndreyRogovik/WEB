from sqlalchemy import create_engine, func, Interval
from sqlalchemy.orm import sessionmaker
from datetime import timedelta

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:567234@localhost:5432/rest_app"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def has_date_next_days(sa_col, next_days: int = 0):
    return age_years_at(sa_col, next_days) > age_years_at(sa_col)


def age_years_at(sa_col, next_days: int = 0):
    stmt = func.age(
        (sa_col - func.cast(timedelta(next_days), Interval))
        if next_days != 0
        else sa_col
    )
    stmt = func.date_part("year", stmt)
    return stmt

