import logging
logging.basicConfig(filename="test.log",level=logging.INFO)
logging.info("this is my very first code for logging")
logging.warning("this will try to load a warning message")
logging.error("this is a error message form system")
l=[1,2,3,4,5,6,7,7]
for i in l:
    if i==2:
        logging.info(i)
        logging.warning("this is the warning for a user that they found out 2 in list")

    logging.shutdown()