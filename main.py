from management import BookManager, UserManager, CheckoutManager
from utils import book_menu, checkout_menu, main_menu, user_menu

# Menu Choices handlers
from handlers import handle_book_menu, handle_checkout_menu, handle_user_menu

def main():
    book_manager = BookManager("books.json")
    user_manager = UserManager("users.json")
    checkout_manager = CheckoutManager("checkouts.json", user_manager, book_manager)

    while True:
        choice = main_menu()

        # Handling choices based on the user's selection
        if choice == "1":
            while True:
                book_choice = book_menu()
                if not handle_book_menu(book_manager, book_choice):
                    break  # Breaking the loop if the user wants to go back to the main menu
        elif choice == "2":
            while True:
                user_choice = user_menu()
                if not handle_user_menu(user_manager, user_choice):
                    break  # Breaking the loop if the user wants to go back to the main menu
        elif choice == "3":
            while True:
                checkout_choice = checkout_menu()
                if not handle_checkout_menu(checkout_manager, checkout_choice):
                    break  # Breaking the loop if the user wants to go back to the main menu
        elif choice == "4":
            print("Exiting.")  
            break  # Exiting the main loop and ending the program
        else:
            print("Invalid choice, please try again.")  

if __name__ == "__main__":
    main()  
