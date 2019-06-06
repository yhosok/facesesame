import logging.config


def getLogger():

    logging.config.fileConfig('logging.conf')

    return logging.getLogger()
