import logging
logging.basicConfig(filename="test.log",level=logging.INFO)
logging.info("this is my very first code for logging")

class list:

    def list1(self,l):
        l = [3, 4, 5, 6, 7, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (234, 6657, 6),
             {"key1": "sudh", 234: [23, 45, 656]}]
        self.x = l
        for i in self.x:
            if type(i) == list:
                logging.info(i)
                logging.warning("this is the warning for a user that they found out 2 in list")
                # print(i)

m = list()
print(m.list1())

logging.shutdown()
