import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    
# class CustomException(Exception):: Defines a custom exception class named CustomException, which inherits from the built-in Exception class.
# def __init__(self, error_message, error_detail: sys):: Defines the constructor for the CustomException class. It takes two arguments: error_message, which is the error message to be associated with the exception, and error_detail, which is expected to be a sys module object.
# super().__init__(error_message): Calls the constructor of the parent class (Exception) and passes the error_message to it.
# self.error_message = error_message_detail(error_message, error_detail=error_detail): Calls the error_message_detail function to generate a detailed error message based on the provided error_message and error_detail, and assigns it to the error_message attribute of the instance.
# def __str__(self):: Defines the __str__ method for the CustomException class, which returns a string representation of the exception.
        