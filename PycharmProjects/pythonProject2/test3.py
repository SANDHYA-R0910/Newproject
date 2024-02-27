import logging
logging.basicConfig(filename="test3.log",level=logging.ERROR,format='%(levelname)s %(asctime)s %(name)s  %(message)s')

try:
    logging.info("i am trying to read a file")
    with open("sudh.txt",'r'):
        logging.info("succsfully it has read the file")
except Exception as e:
    logging.critical("this is a sitution for us")
    logging.error(e)
    logging.exception(e)
