from models import Book  
from storage import load_data, save_data  

class BookManager:
    """A class to manage books."""
    
    def __init__(self, filename):
        """
        Initializes the BookManager with the specified filename.
        
        Args:
            filename (str): The name of the file to load and save book data.
        """
        self.filename = filename
        # Loading book data from the specified file and creating Book objects
        self.books = [Book(**book_data) for book_data in load_data(filename)]

    def add_book(self, title, author, isbn):
        """
        Adds a new book to the collection.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
            
        Returns:
            str: A message indicating the status of the operation.
        """
        if not title:
            print("Error: Title cannot be empty")
            return "not saved"
        # Creating a new Book object with the provided details
        book = Book(title, author, isbn)
        # Appending the new book to the list of books
        self.books.append(book)
        # Saving the updated list of books to the file
        save_data([book.to_dict() for book in self.books], self.filename)
        return "saved"  

    def update_book(self, isbn, new_title=None, new_author=None):
        """
        Updates the details of a book.
        
        Args:
            isbn (str): The ISBN of the book to update.
            new_title (str): The new title for the book.
            new_author (str): The new author for the book.
            
        Returns:
            bool: True if the book is updated successfully, False otherwise.
        """
        for book in self.books:
            if book.isbn == isbn:
                # Updating the title if a new title is provided
                if new_title:
                    book.title = new_title
                # Updating the author if a new author is provided
                if new_author:
                    book.author = new_author
                # Saving the updated list of books to the file
                save_data([book.to_dict() for book in self.books], self.filename)
                return True  
        return False  

    def delete_book(self, isbn):
        """
        Deletes a book from the collection.
        
        Args:
            isbn (str): The ISBN of the book to delete.
        """
        # Filtering out the book with the provided ISBN and updating the list
        self.books = [book for book in self.books if book.isbn != isbn]
        # Saving the updated list of books to the file
        save_data([book.to_dict() for book in self.books], self.filename)
        
    def list_books(self):
        """Lists all the books in the collection."""
        for book in self.books:
            print(book)

    def search_books(self, **kwargs):
        """
        Searches for books based on the provided criteria.
        
        Args:
            **kwargs: Keyword arguments representing the search criteria.
            
        Returns:
            list: A list of books matching the search criteria.
        """
        results = []
        for book in self.books:
            match = all(
                getattr(book, attr, None) == value for attr, value in kwargs.items()
            )
            if match:
                results.append(book)
        return results
