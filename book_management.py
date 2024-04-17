from storage import save_data, load_data
from models import Book

class BookManager:
    def __init__(self, filename):
        self.filename = filename
        self.books = [Book(**book_data) for book_data in load_data(filename)]
    
    def add_book(self, title, author, isbn):
        if not title:
            print("Error: Title cannot be empty")
            return "not saved"
        book = Book(title, author, isbn)
        self.books.append(book)
        save_data([book.to_dict() for book in self.books], self.filename)
        return "saved"
    
    def update_book(self, isbn, new_title=None, new_author=None):
        for book in self.books:
            if book.isbn == isbn:
                if new_title:
                    book.title = new_title
                if new_author:
                    book.author = new_author
                save_data([book.to_dict() for book in self.books], self.filename)
                return True
        return False
    
    def delete_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]
        save_data([book.to_dict() for book in self.books], self.filename)
    
    def list_books(self):
        for book in self.books:
            print(book)
    
    def search_books(self, **kwargs):
        results = []
        for book in self.books:
            match = all(getattr(book, attr, None) == value for attr, value in kwargs.items())
            if match:
                results.append(book)
        return results
