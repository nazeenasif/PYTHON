class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()


    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1    
    

    @classmethod
    def get_total_books(cls):
        return cls.total_books
    

book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Lord of the Rings", "J.R.R. Tolkien")
print(Book.get_total_books())  # Output: 2
