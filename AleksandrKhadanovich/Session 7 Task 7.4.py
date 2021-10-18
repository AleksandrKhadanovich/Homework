import logging                                                                  
import sys
from contextlib import suppress

def er_supress(func):
    
    def wraper_er_supress(*args):
        log = logging.getLogger('no errors')
        log.setLevel (logging.INFO)
        handler = logging.StreamHandler(sys.stdout)                             
        handler.setLevel(logging.INFO)                                                     
        try:
            func(*args)                     
        except:
            suppress(Exception)                        
        else:                                   
            log.addHandler(handler) 
            log.info (f"{func} exception did not occur")                                               
    return wraper_er_supress


@er_supress
def sum_of_numbers(a,b):
    return a*b    

sum_of_numbers(134,567)

