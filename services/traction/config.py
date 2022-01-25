import os


class Config:
    DEBUG = True

    PSQL_HOST = os.environ.get("POSTGRESQL_HOST")
    PSQL_PORT = os.environ.get("POSTGRESQL_PORT")
    PSQL_USER = os.environ.get("TRACTION_DB_USER")
    PSQL_PASS = os.environ.get("TRACTION_DB_USER_PWD")
    PSQL_DB = os.environ.get("POSTGRESQL_DB")
    PSQL_SCHEMA = os.environ.get("POSTGRESQL_SCHEMA")

    SQLALCHEMY_DATABASE_URI = f"postgresql+asyncpg://{PSQL_USER}:{PSQL_PASS}@{PSQL_HOST}:{PSQL_PORT}/{PSQL_DB}"

    PSQL_ADMIN_USER = os.environ.get("TRACTION_DB_ADMIN")
    PSQL_ADMIN_PASS = os.environ.get("TRACTION_DB_ADMIN_PWD")
    SQLALCHEMY_DATABASE_ADMIN_URI = f"postgresql+asyncpg://{PSQL_ADMIN_USER}:{PSQL_ADMIN_PASS}@{PSQL_HOST}:{PSQL_PORT}/{PSQL_DB}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    INNKEEPER_ADMIN_KEY = os.environ.get("INNKEEPER_ADMIN_KEY")

    ACAPY_ADMIN_URL = os.environ.get("ACAPY_ADMIN_URL")
    ACAPY_ADMIN_URL_API_KEY = os.environ.get("ACAPY_ADMIN_URL_API_KEY")
