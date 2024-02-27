import logging
logging.basicConfig(filename='task.log',level=logging.INFO,format='%(levelname)s %(ascitime)s %(name)s %(message)s')
try:
    logging.info("i am writting calss")
    class string:
        s = "this is my first python programming"
        def __int__(self,s):
            self.s = s
        def reverse_data(self):
            return self.s.upper()
    print("success")
    str = string()
    print(str.reverse_data())
except Exception as e:
    logging.exception(e)
finally:
    print("completed task")