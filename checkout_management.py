from models import Checkout
from storage import load_data, save_data


class CheckoutManager:
    def __init__(self, filename, user_manager, book_manager):
        self.filename = filename
        self.checkouts = [Checkout(**checkout_data) for checkout_data in load_data(filename)]
        self.user_manager = user_manager
        self.book_manager = book_manager

    def checkout_book(self, user_id, isbn):
        user = self.user_manager.search_users(user_id=user_id)
        book = self.book_manager.search_books(isbn=isbn)
        if user!= [] and book!= [] and not book[0].checked_out:
            checkout = Checkout(user_id, isbn)
            self.checkouts.append(checkout)
            book[0].checked_out = True
            save_data([checkout.to_dict() for checkout in self.checkouts], self.filename)
            save_data([book.to_dict() for book in self.book_manager.books], self.book_manager.filename)
            return True
        else:
            return False

    def checkin_book(self, user_id, isbn):
        for checkout in self.checkouts:
            if checkout.user_id == user_id and checkout.isbn == isbn:
                checkout.checked_out = False
                book = self.book_manager.search_books(isbn=isbn)
                if book:
                    book[0].checked_out = False
                    save_data([book.to_dict() for book in self.book_manager.books], self.book_manager.filename)
                save_data([checkout.to_dict() for checkout in self.checkouts], self.filename)
                return True
        return False

    def list_checkouts(self):
        for checkout in self.checkouts:
            print(checkout)

    def get_checked_out_books(self, user_id):
        return [checkout for checkout in self.checkouts if checkout.user_id == user_id and checkout.checked_out]
