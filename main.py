from book_management import BookManager
from user_management import UserManager
from checkout_management import CheckoutManager

def main_menu():
    print("\nLibrary Management System")
    print("1. Book Management")
    print("2. User Management")
    print("3. Checkout Management")
    print("4. Exit")
    choice = input("Enter choice: ")
    return choice

def book_menu():
    print("\nBook Management")
    print("1. Add Book")
    print("2. Update Book")
    print("3. Delete Book")
    print("4. List Books")
    print("5. Search Books")
    print("6. Back to Main Menu")
    choice = input("Enter choice: ")
    return choice

def user_menu():
    print("\nUser Management")
    print("1. Add User")
    print("2. Update User")
    print("3. Delete User")
    print("4. List Users")
    print("5. Search Users")
    print("6. Back to Main Menu")
    choice = input("Enter choice: ")
    return choice

def checkout_menu():
    print("\nCheckout Management")
    print("1. Checkout Book")
    print("2. Checkin Book")
    print("3. List Checkouts")
    print("4. Back to Main Menu")
    choice = input("Enter choice: ")
    return choice

def main():
    book_manager = BookManager("books.json")
    user_manager = UserManager("users.json")
    checkout_manager = CheckoutManager("checkouts.json")

    while True:
        choice = main_menu()

        if choice == '1':
            while True:
                book_choice = book_menu()
                if book_choice == '1':
                    title = input("Enter title: ")
                    author = input("Enter author: ")
                    isbn = input("Enter ISBN: ")
                    save_status = book_manager.add_book(title, author, isbn)
                    if save_status == "saved":
                        print("Book added.")
                elif book_choice == '2':
                    isbn = input("Enter ISBN of the book to update: ")
                    new_title = input("Enter new title (leave blank to keep current): ")
                    new_author = input("Enter new author (leave blank to keep current): ")
                    if book_manager.update_book(isbn, new_title, new_author):
                        print("Book updated.")
                    else:
                        print("Book not found.")
                elif book_choice == '3':
                    isbn = input("Enter ISBN of the book to delete: ")
                    if book_manager.delete_book(isbn):
                        print("Book deleted.")
                    else:
                        print("Book not found.")
                elif book_choice == '4':
                    print("\nList of Books:")
                    book_manager.list_books()
                elif book_choice == '5':
                    search_by = input("Enter attribute to search by (title/author/isbn): ")
                    value = input("Enter value to search for: ")
                    results = book_manager.search_books(**{search_by: value})
                    if results:
                        print("\nSearch Results:")
                        for book in results:
                            print(book)
                    else:
                        print("No books found.")
                elif book_choice == '6':
                    break
                else:
                    print("Invalid choice, please try again.")

        elif choice == '2':
            while True:
                user_choice = user_menu()
                if user_choice == '1':
                    name = input("Enter name: ")
                    user_id = input("Enter user ID: ")
                    saved_user = user_manager.add_user(name, user_id)
                    if saved_user == "saved":
                        print("User added.")
                elif user_choice == '2':
                    user_id = input("Enter user ID of the user to update: ")
                    new_name = input("Enter new name (leave blank to keep current): ")
                    if user_manager.update_user(user_id, new_name):
                        print("User updated.")
                    else:
                        print("User not found.")
                elif user_choice == '3':
                    user_id = input("Enter user ID of the user to delete: ")
                    if user_manager.delete_user(user_id):
                        print("User deleted.")
                    else:
                        print("User not found.")
                elif user_choice == '4':
                    print("\nList of Users:")
                    user_manager.list_users()
                elif user_choice == '5':
                    search_by = input("Enter attribute to search by (name/user_id): ")
                    value = input("Enter value to search for: ")
                    results = user_manager.search_users(**{search_by: value})
                    if results:
                        print("\nSearch Results:")
                        for user in results:
                            print(user)
                    else:
                        print("No users found.")
                elif user_choice == '6':
                    break
                else:
                    print("Invalid choice, please try again.")

        elif choice == '3':
            while True:
                checkout_choice = checkout_menu()
                if checkout_choice == '1':
                    user_id = input("Enter user ID: ")
                    isbn = input("Enter ISBN of the book to checkout: ")
                    checkout_manager.checkout_book(user_id, isbn)
                    print("Book checked out.")
                elif checkout_choice == '2':
                    user_id = input("Enter user ID: ")
                    isbn = input("Enter ISBN of the book to checkin: ")
                    if checkout_manager.checkin_book(user_id, isbn):
                        print("Book checked in.")
                    else:
                        print("Book not checked out by this user.")
                elif checkout_choice == '3':
                    print("\nList of Checkouts:")
                    checkout_manager.list_checkouts()
                elif checkout_choice == '4':
                    break
                else:
                    print("Invalid choice, please try again.")

        elif choice == '4':
            print("Exiting.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
