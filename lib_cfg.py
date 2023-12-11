from inc.app_global import *
from configparser import ConfigParser
from lib.lib_log import *

global g_cfg
g_cfg = None

def cfg_init():
    try:
        global g_cfg
        g_cfg = ConfigParser()
        g_cfg.read(g_ini)
        return g_cfg
    except Exception as e:
        log_error(e)
        return None

#------------------------------------------------
# 운영단말 전문 수신 ip, port 정의 / Card 사 전문,파일 수신 ip, port
#------------------------------------------------
def cfg_web_socket_ip():
    return g_cfg.get('web_socket', 'ip')
def cfg_web_socket_port():
    return g_cfg.get('web_socket', 'port') 
def cfg_card_socket_ip():
    return g_cfg.get('card_socket', 'ip')
def cfg_card_socket_port():
    return g_cfg.get('card_socket', 'port') 
    
#----------------------------------------------------------
# DB 연결정보 
#----------------------------------------------------------
def cfg_get_db_ip():
    return g_cfg.get('database', 'ip')
def cfg_get_db_name():
    return g_cfg.get('database', 'dbname')
def cfg_get_db_user():
    return g_cfg.get('database', 'user')
def cfg_get_db_pwd():
    return g_cfg.get('database', 'pwd')

#----------------------------------------------------------
# 카드사 연결정보
#----------------------------------------------------------
def cfg_get_card_ip():
    return g_cfg.get('test_server', 'ip')
def cfg_get_card_port():
    return g_cfg.get('test_server', 'port')

#----------------------------------------------------------
# RabbitMQ 연결정보 
#----------------------------------------------------------
def cfg_get_rmq_ip():
    return g_cfg.get('rabbitmq', 'ip')

def cfg_get_rmq_data():
    qname = g_cfg.get('rabbitmq', 'rmq_data')
    return qname

    
__all__ = [
    'cfg_init',
    
    'cfg_web_socket_ip', 'cfg_web_socket_port','cfg_card_socket_ip','cfg_card_socket_port',
    
    'cfg_get_db_ip','cfg_get_db_name','cfg_get_db_user','cfg_get_db_pwd',
    
    'cfg_get_card_ip','cfg_get_card_port',
    
    'cfg_get_rmq_ip','cfg_get_rmq_data'
]