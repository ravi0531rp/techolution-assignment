from models import Checkout
from storage import load_data, save_data

class CheckoutManager:
    """A class to manage checkouts of books."""
    
    def __init__(self, filename, user_manager, book_manager):
        """
        Initializes the CheckoutManager with the specified filename, user manager, and book manager.
        
        Args:
            filename (str): The name of the file to load and save checkout data.
            user_manager (UserManager): The user manager object.
            book_manager (BookManager): The book manager object.
        """
        self.filename = filename
        # Loading checkout data from the specified file and creating Checkout objects
        self.checkouts = [Checkout(**checkout_data) for checkout_data in load_data(filename)]
        self.user_manager = user_manager
        self.book_manager = book_manager

    def checkout_book(self, user_id, isbn):
        """
        Checks out a book to a user.
        
        Args:
            user_id (str): The ID of the user checking out the book.
            isbn (str): The ISBN of the book to be checked out.
            
        Returns:
            bool: True if the book is successfully checked out, False otherwise.
        """
        user = self.user_manager.search_users(user_id=user_id)
        book = self.book_manager.search_books(isbn=isbn)
        # Checking if the user and book exist, and if the book is not already checked out
        if user and book and not book[0].checked_out:
            checkout = Checkout(user_id, isbn)
            # Adding the checkout to the list of checkouts
            self.checkouts.append(checkout)
            # Updating the checked_out status of the book
            book[0].checked_out = True
            # Saving the updated data to the files
            save_data([checkout.to_dict() for checkout in self.checkouts], self.filename)
            save_data([book.to_dict() for book in self.book_manager.books], self.book_manager.filename)
            return True
        else:
            return False

    def checkin_book(self, user_id, isbn):
        """
        Checks in a book from a user.
        
        Args:
            user_id (str): The ID of the user checking in the book.
            isbn (str): The ISBN of the book to be checked in.
            
        Returns:
            bool: True if the book is successfully checked in, False otherwise.
        """
        for checkout in self.checkouts:
            if checkout.user_id == user_id and checkout.isbn == isbn:
                # Marking the checkout as checked out
                checkout.checked_out = False
                # Finding the corresponding book and updating its checked_out status
                book = self.book_manager.search_books(isbn=isbn)
                if book:
                    book[0].checked_out = False
                    save_data([book.to_dict() for book in self.book_manager.books], self.book_manager.filename)
                # Saving the updated data to the file
                save_data([checkout.to_dict() for checkout in self.checkouts], self.filename)
                return True
        return False

    def list_checkouts(self):
        """Lists all the checkouts."""
        for checkout in self.checkouts:
            print(checkout)

    def get_checked_out_books(self, user_id):
        """
        Retrieves the books checked out by a specific user.
        
        Args:
            user_id (str): The ID of the user.
            
        Returns:
            list: A list of checkouts for books checked out by the user.
        """
        return [checkout for checkout in self.checkouts if checkout.user_id == user_id and checkout.checked_out]
