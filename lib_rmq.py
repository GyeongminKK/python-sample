import pika
import time

from lib.lib_log import *
from lib.lib_cfg import *

def rmq_init():
    rmq_ip = cfg_get_rmq_ip()
    rmq_qu_process = cfg_get_rmq_data()
    try : 
        while mq_make_queue(rmq_ip, rmq_qu_process) == False:
            time.sleep(3)
            log_info("FILE_MSG 메시지큐 접속 오류 .... 재시도")
        mq_connect(rmq_ip)
        log_info('Rabbit MQ : Connect success')
        return True
    except Exception as e:
        log_error('메시지큐 연결에 실패했습니다. 점검 후 재기동하세요')
        return False

def mq_make_queue(host_ip, queue_name):
    try:
        parameters = pika.ConnectionParameters(host=host_ip, heartbeat=0)
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        res = channel.queue_declare(queue=queue_name, durable=True)
        connection.close()
        if res:
            return True
        else:
            return False
    except Exception as e:
        return False    

def mq_connect(host_ip):
    try:
        parameters = pika.ConnectionParameters(host=host_ip, port=5672, heartbeat=0)
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        return connection, channel
    except Exception as e:
        log_debug('[mq_connect] ' + str(e))
        return None, None
    
def rmq_publish(msg):
    mq_ip = cfg_get_rmq_ip()
    mq_nm = cfg_get_rmq_data()
    try:
        parameters = pika.ConnectionParameters(host=mq_ip, port=5672, heartbeat=0)
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_declare(queue=mq_nm, durable=True)
        channel.basic_publish(exchange='', routing_key=mq_nm, body=msg)
        log_debug('FILE_MSG 큐에 메시지('+msg+') 저장 완료')
        connection.close()
        return True
    except Exception as e:
        log_debug('[mq_connect] ' + str(e))


__all__ = [
    'rmq_init',
    'rmq_publish'
    
]