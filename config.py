
import psycopg2

try:
    def connect():
        db_connection = psycopg2.connect(
            database="test_db",
            user="root",
            password="root",
            # get RDS endpoint
            host="localhost",
            port="5432")
        print("stablished connection")
        return db_connection

    db = connect()

    cursor = db.cursor()

# Handle the error throws by the command that is useful when using Python while working with PostgreSQL
except(Exception, psycopg2.Error) as error:
    print("Error connecting to PostgreSQL database", error)
    connection = None
