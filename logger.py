import logging
import time


def startLogging():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='log_at_' + time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) + '.log',
                        filemode='w')
def info(info):
    logging.info(info)


def warning(warning):
    logging.warning(warning)


def exception(exception):
    logging.exception(exception)


def stopLogging():
    logging.getLogger().handlers = []

def report(info):
    logging.info("#####----Report----#####")
    logging.info(info)
    logging.info("#####----Report----#####")
