from contextlib import contextmanager

@contextmanager
def write_to_file(file_path):
    
    try:
        file = open(file_path, mode="w")
        yield file

    except Exception as e:
        print (f"Error because of {e}")
    finally:
        file.close()
        

with write_to_file(r'data\unsorted_names3.txt') as file:
    file.write("Hi!")





