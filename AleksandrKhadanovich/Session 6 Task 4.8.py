class Missed_pages(Exception):
    def __str__(self): return 'Exception: Invalid index. Page is missing.'

class Pagination:   
    def __init__ (self, text, num_on_page):
        self.text=text
        self.num_on_page=num_on_page
        self.item_count = len(text)
        if self.item_count%self.num_on_page !=0:
            self.pages_count = self.item_count//self.num_on_page +1
        else:
            self.pages_count = self.item_count//self.num_on_page
        
    def __str__(self):
        return f"'It is' {self} 'pages'"

  
    def count_items_on_page(self, page_number):
        if page_number < self.pages_count:
            return self.num_on_page
        elif page_number == self.pages_count and self.item_count%self.num_on_page ==0:
            return self.num_on_page
        elif page_number == self.pages_count and self.item_count%self.num_on_page !=0:
            return self.item_count%self.num_on_page
        else:
            raise Missed_pages()
        

pages = Pagination('Your beautiful text', 5)
print (pages.item_count)   
print (pages.pages_count)
print (pages.count_items_on_page(0))
print (pages.count_items_on_page(3))
print (pages.count_items_on_page(4))
print (pages.count_items_on_page(5))


