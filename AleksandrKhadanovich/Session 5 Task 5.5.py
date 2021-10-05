
def remember_result(func):
    a=None
    def wrapper_remember_result(*args):
        nonlocal a
        print (f"Last result= '{a}'")
        b=func(*args)
        a=b
    return wrapper_remember_result

@remember_result
def sum_list(*args):
    
    result = ''
    for item in args:
        result+=item
    print (f"Current result= '{result}'")
    return result

sum_list('df','fg')
sum_list('kl','nm')


