import pymysql.cursors

CREATE_DB = "CREATE DATABASE IF NOT EXISTS {0};" # counter
CREATE_TBL = "CREATE TABLE IF NOT EXISTS {0}; " #count ( num INT NOT NULL );" 
CREATE_ENTRY = "INSERT INTO {0} VALUES {1};" # count ( num ) , 0
# Generic
def execute_query(query, connection):
    with connection.cursor() as cursor:
        # Create a new record
        cursor.execute(query)
        connection.commit()

# Connect to the database
def create_db(db_name):
    connection = pymysql.connect(host='db',
                                 user='root',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        execute_query(CREATE_DB.format(db_name), connection)
    finally:
        connection.close()

# Create table
def create_tbl(db_name, tbl_specs):
    connection = pymysql.connect(host='db',
                                 user='root',
                                 db=db_name,
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        execute_query(CREATE_TBL.format(tbl_specs), connection)
    finally:
        connection.close()
    
# Create an entry
def create_entry(db_name, tbl_name, tbl_specs, entry_specs):
    connection = pymysql.connect(host='db',
                                 user='root',
                                 db=db_name,
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        execute_query(CREATE_ENTRY.format(tbl_specs, entry_specs), connection)
    finally:
        connection.close()

