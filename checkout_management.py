from models import Checkout
from storage import load_data, save_data


class CheckoutManager:
    def __init__(self, filename):
        self.filename = filename
        self.checkouts = [
            Checkout(**checkout_data) for checkout_data in load_data(filename)
        ]

    def checkout_book(self, user_id, isbn):
        checkout = Checkout(user_id, isbn)
        self.checkouts.append(checkout)
        save_data([checkout.to_dict() for checkout in self.checkouts], self.filename)

    def checkin_book(self, user_id, isbn):
        for checkout in self.checkouts:
            if checkout.user_id == user_id and checkout.isbn == isbn:
                checkout.checked_out = False
                save_data(
                    [checkout.to_dict() for checkout in self.checkouts], self.filename
                )
                return True
        return False

    def list_checkouts(self):
        for checkout in self.checkouts:
            print(checkout)

    def get_checked_out_books(self, user_id):
        return [
            checkout
            for checkout in self.checkouts
            if checkout.user_id == user_id and checkout.checked_out
        ]
