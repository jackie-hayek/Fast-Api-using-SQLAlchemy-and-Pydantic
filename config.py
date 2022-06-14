# This code creates:
# a SQLAlchemy Engine that will interact with our dockerized PostgreSQL database,
# a SQLAlchemy ORM session factory bound to this engine,
# and a base class for our classes definitions.

import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

Database_URL = "postgresql://postgres:password@localhost:5432"
engine = _sql.create_engine(url=Database_URL)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = _declarative.declarative_base()
