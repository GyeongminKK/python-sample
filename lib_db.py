import time
import pyodbc

from lib.lib_log import *
from lib.lib_cfg import *
from inc.define_val import *

global g_db_conn

def db_connect():
    global g_ini
    global g_db_conn
    g_db_conn = None
    dbname = cfg_get_db_name()
    user = cfg_get_db_user()
    pwd = cfg_get_db_pwd()
    db_disconnect()
    while True:
        try:
            g_db_conn = pyodbc.connect(DSN=dbname, uid=user, pwd=pwd)            
            if g_db_conn is not None:                
                g_db_conn.setdecoding(pyodbc.SQL_CHAR, encoding='euc-kr')
                g_db_conn.setdecoding(pyodbc.SQL_WCHAR, encoding='euc-kr')
                g_db_conn.setdecoding(pyodbc.SQL_WMETADATA, encoding='euc-kr')
                g_db_conn.setencoding(encoding='euc-kr')                
                log_debug("데이터베이스 연결 성공")
                return g_db_conn
        except Exception as e:
            log_error("데이터베이스 접속 오류 ... 재시도(Exception) = " + str(e))
            time.sleep(2)

def db_disconnect():
    if tib_is_connected(g_db_conn):
        g_db_conn.cursor().close()
        g_db_conn.close()
        
def tib_is_connected(tib_conn):
    try:
        tib_cursor = tib_conn.cursor()
        tib_cursor.execute('SELECT * FROM DUAL')
        tib_cursor.close()
        return True
    except Exception as e:
        return False

def dbSelect(conn, sql):
    try:
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        return True, result
    except Exception as e:
        log_error("DB select log.error")
        return False, None

def dbSqlrun(conn, sql):
    try:
        cur = conn.cursor()
        cur.execute(sql)
        return True
    except Exception as e:
        log_error("DB insert log.error")
        return False

__all__ = [
    'db_connect','db_disconnect','tib_is_connected','dbSelect','dbSqlrun'
]