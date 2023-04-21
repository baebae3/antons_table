import urllib
from urllib.parse import urlparse

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


sandbox_params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};SERVER=srv-sqldev02;DATABASE=Sandbox;trusted_connection=yes")
sandbox_engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % sandbox_params, fast_executemany=True)

# logistics_reports_params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};SERVER=srv-sqldev02;DATABASE=Logistics_reports;trusted_connection=yes")
# logistics_reports_engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % logistics_reports_params, fast_executemany=True)

sand_con = sandbox_engine.connect()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=sandbox_engine)

Base = declarative_base()