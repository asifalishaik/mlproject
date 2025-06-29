import sys
import logging
import logger


def error_message_details(error, error_detail:sys):
    _,_,exc_tab=error_detail.exc_info()
    file_name=exc_tab.tb_frame.f_code.co_filename
    error_message="Error occured in python script name[{0}] line number [{1}] and error message [{2}]".format(
        file_name,exc_tab.tb_lineno,str(error))

    return error_message
    

class CustomException(Exception): ## Creating customException class by inheriting Exception class
    # we can customize the behavior by overriding the __init__ or __str__ methods:

    def __init__(self,error_message,error_detail:sys): # constructor, its called when an instance(object) is created for CustomException
        
        self.error_message=error_message_details(error_message,error_detail=error_detail) # This stores the error_message argument into an instance variable so it can be accessed later.

        super().__init__(error_message) # calls the constructor of the base Exception class. It passes a formatted string like "Error occured in python script name...." to the base class.

    
    def __str__(self):
        return self.error_message

'''
for testing the file...
if __name__=="__main__":

    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by zeror exception")
        raise CustomException(e, sys)
    
'''
