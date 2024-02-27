import logging
logging.basicConfig(filename="test1.log",level=logging.DEBUG,format="%(asctime)s %(name)s %(levelname)s %(message)s")
logging.info("this is my log with timestamp ")