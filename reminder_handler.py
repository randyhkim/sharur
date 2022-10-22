from dotenv import load_dotenv
from google.cloud.sql.connector import Connector, IPTypes
import sqlalchemy
import pymysql
import os
from google.oauth2 import service_account


# initialize Connector object
connector = Connector()

# Google Application Credentials
load_dotenv()
credential_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
credentials = service_account.Credentials.from_service_account_file(credential_path)

# function to return the database connection
def getconn() -> pymysql.connections.Connection:
    conn: pymysql.connections.Connection = connector.connect(
        "sharur:us-central1:sharur-test",
        "pymysql",
        user="root",
        password=os.getenv('SQL_PASSWORD'),
        db="birthday_test",
        ip_type = IPTypes.PRIVATE if os.environ.get("PRIVATE_IP") else IPTypes.PUBLIC,
    )
    return conn

# create connection pool
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)


# insert entry to birthday
# TODO: birthday type to DateTime
def insert_birthday(pool, id: int, name: str, birthday: str, reminded_people: int, reminder_message: str):
    with pool.connect() as db_conn:
        insert_stmt = sqlalchemy.text(
            f'INSERT INTO reminder (ID, Name, Birthday, RemindedPeople, ReminderMessage) VALUES \
            ({id}, "{name}", "{birthday}", {reminded_people}, "{reminder_message}")'
        )
        db_conn.execute(insert_stmt)


# delete entry with user_id
def delete_birthday(pool, name: str):
    with pool.connect() as db_conn:
        delete_stmt = sqlalchemy.text(
            f'DELETE FROM reminder WHERE Name="{name}"'
        )
        db_conn.execute(delete_stmt)


# get all birthdays
def fetch_birthdays(pool):
    with pool.connect() as db_conn:
        stmt = sqlalchemy.text(
            f'SELECT * FROM birthday_test.reminder'
        )
        return str(db_conn.execute(stmt).all())


# TODO: remove
if __name__ == "__main__":
    # insert_birthday(pool, 1, "Randy Kim", "19971118", 1, "Happy Birthday!")
    # delete_birthday(pool, 1)
    print(fetch_birthdays(pool))
