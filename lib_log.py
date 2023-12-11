import logging
import logging.config
import logging.handlers
import json
import pprint

global _logger
_logger = logging.getLogger()
class MyPrettyPrinter(pprint.PrettyPrinter):
    def format(self, _object, context, maxlevels, level):
        return pprint.PrettyPrinter.format(self, _object, context, maxlevels, level)
    
def log_init(app, config_file, log_file):
    global _logger
    try:
        with open(config_file, 'rt') as f:
            config = json.load(f)
            config['handlers']['file_handler']['filename'] = log_file
        logging.config.dictConfig(config)
        log_app_start(app)
        return True
    except Exception as e:
        print("*"*100)
        print("Error : Log Configuration Check")
        print(e)
        print("*"*100)
        return False

def log_app_start(msg):
    global _logger
    _logger.info("=" * 100)
    _logger.info('[' + msg + '] Process START')
    _logger.info("=" * 100)

def log_info(content):
    global _logger
    try:
        content_type = type(content)
        if content_type == str:
            _logger.info(content)
        elif content_type == dict:
            _logger.info(MyPrettyPrinter().pformat(content))
        else:
            ppresult = MyPrettyPrinter().pformat(content)
            ppresult = ppresult.replace("\n","")
            ppresult = ppresult.replace("  ","")
            _logger.info(ppresult)
    except Exception as e:
        _logger.error('log_info Method Error')
        _logger.error(str(e))

def log_debug(content):
    global _logger
    try:
        content_type = type(content)
        if content_type == str:
            _logger.debug(content)
        elif content_type == dict:
            _logger.debug(MyPrettyPrinter().pformat(content))
        else:
            ppresult = MyPrettyPrinter().pformat(content)
            ppresult = ppresult.replace("\n", "")
            ppresult = ppresult.replace("  ", "")
            _logger.debug(ppresult)
    except Exception as e:
        _logger.error('log_debug Method Error')
        _logger.error(str(e))

def log_error(content):
    global _logger
    try:
        content_type = type(content)
        if content_type == str:
            _logger.error(content)
        elif content_type == dict:
            _logger.error(MyPrettyPrinter().pformat(content))
        else:
            ppresult = MyPrettyPrinter().pformat(content)
            ppresult = ppresult.replace("\n", "")
            ppresult = ppresult.replace("  ", "")
            _logger.error(ppresult)
    except Exception as e:
        _logger.error('log_error Method Error')
        _logger.error(str(e))

__all__ = [
    'log_init',
    'log_info',
    'log_debug',
    'log_error'
]