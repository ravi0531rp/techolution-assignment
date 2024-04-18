from book_management import BookManager
from checkout_management import CheckoutManager
from user_management import UserManager
from utils import book_menu, checkout_menu, main_menu, user_menu

from handlers import handle_book_menu, handle_checkout_menu, handle_user_menu


def main():
    book_manager = BookManager("books.json")
    user_manager = UserManager("users.json")
    checkout_manager = CheckoutManager("checkouts.json", user_manager, book_manager)

    while True:
        choice = main_menu()

        if choice == "1":
            while True:
                book_choice = book_menu()
                if not handle_book_menu(book_manager, book_choice):
                    break
        elif choice == "2":
            while True:
                user_choice = user_menu()
                if not handle_user_menu(user_manager, user_choice):
                    break
        elif choice == "3":
            while True:
                checkout_choice = checkout_menu()
                if not handle_checkout_menu(checkout_manager, checkout_choice):
                    break
        elif choice == "4":
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
