import sys
import traceback
import logging
logging.basicConfig(filename = "log.log", 
        level = logging.DEBUG, 
        format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
import init_db
from flask import Flask
from flaskext.mysql import MySQL

def log_uncaught_exceptions(ex_cls, ex, tb):
    logging.critical(''.join(traceback.format_tb(tb)))
    logging.critical('{0}: {1}'.format(ex_cls, ex))
    
sys.excepthook = log_uncaught_exceptions

init_db.create_db("counter")
init_db.create_tbl("counter", "count ( num INT NOT NULL )")
init_db.create_entry("counter", "count", "count ( num )", "( 0 )")

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_DB'] = 'counter'

SELECT_NUM = "SELECT num FROM count;"
UPDATE_NUM = "UPDATE count SET num = {0};"
mysql = MySQL()
mysql.init_app(app)

def execute_sql(mysql, statement, fetch_type='one'):
    con = mysql.connect()
    with con.cursor() as cursor:
        logging.info("Executing statement : " + statement)
        res = cursor.execute(statement)
        logging.info("Results : " + str(res))
    ret = cursor.fetchone() if (res > 0 and fetch_type == 'one') else None
    con.commit()
    return ret

@app.route('/')
def hello():
    count = execute_sql(mysql, SELECT_NUM)[0]
    execute_sql(mysql, UPDATE_NUM.format(count+1)) 
    return 'Hello World! I have been seen {} times.\n'.format(count+1)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
