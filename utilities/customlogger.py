import logging

class LogGen:

    @staticmethod
    def logging():
        logging.basicConfig(filename='.\\Logs\\automation.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
