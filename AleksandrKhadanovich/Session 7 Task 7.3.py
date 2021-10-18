from time import perf_counter


def exec_time (func):    
    def wrapper_exec_time (*args):
        start = perf_counter()        
        try:
            func(*args)                                           
            end = perf_counter()
            tm = (end - start)      
        except BaseException as e:
            print('Failed: {}: {}'.format(func, e))       
        else:
            tm = '{:.50f}'.format(tm)
            with open (r'unsorted_names.txt6','w') as writer:
                writer.write (f"Execution time of {func}: {str (tm)}\n")
                print (f"Written to {writer.name}")
    return wrapper_exec_time

        
@exec_time
def mult_of_numb(z,x):
    return z*x


mult_of_numb (134,55456)
            
     
            
    

