class Work_with_file:
    def __init__(self, file_path,mode):
        self.file_path = file_path
        self.mode = mode

    def __enter__(self):
        self.opened_file = open(self.file_path, self.mode)
        return self.opened_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"Exception! {exc_type} {exc_val}")
        else:
            print(f"Done well!")
       
        self.opened_file.close()
        if file.closed == False:   
            print("Файл открыт для чтения.")       
        return True

with Work_with_file(r'data\unsorted_names4.txt', 'r') as file:
    print(file.readline())
    #file.write("Hi!")

