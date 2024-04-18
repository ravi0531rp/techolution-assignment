from utils import check_non_empty, check_valid_options


def handle_book_menu(book_manager, choice):
    if choice == "1":
        title = input("Enter title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        if check_non_empty(isbn) and check_non_empty(title):
            save_status = book_manager.add_book(title, author, isbn)
            if save_status == "saved":
                print("Book added.")
        else:
            print("Book Title or ISBN cannot be empty.")
        return True
    elif choice == "2":
        isbn = input("Enter ISBN of the book to update: ")
        new_title = input("Enter new title (leave blank to keep current): ")
        new_author = input("Enter new author (leave blank to keep current): ")
        if book_manager.update_book(isbn, new_title, new_author):
            print("Book updated.")
        else:
            print("Book not found.")
        return True
    elif choice == "3":
        isbn = input("Enter ISBN of the book to delete: ")
        if book_manager.delete_book(isbn):
            print("Book deleted.")
        else:
            print("Book not found.")
        return True
    elif choice == "4":
        print("\nList of Books:")
        book_manager.list_books()
        return True
    elif choice == "5":
        search_by = input("Enter attribute to search by (title/author/isbn): ")
        if not check_valid_options(search_by, ["title", "author", "isbn"]):
            print("Invalid choice, please try again.")
            return True
        value = input("Enter value to search for: ")
        results = book_manager.search_books(**{search_by: value})
        if results:
            print("\nSearch Results:")
            for book in results:
                print(book)
        else:
            print("No books found.")
        return True
    elif choice == "6":
        return False
    else:
        print("Invalid choice, please try again.")
        return True


def handle_user_menu(user_manager, choice):
    if choice == "1":
        name = input("Enter name: ")
        saved_user = user_manager.add_user(name)
        if saved_user == "saved":
            print("User added.")
        return True
    elif choice == "2":
        user_id = input("Enter user ID of the user to update: ")
        new_name = input("Enter new name (leave blank to keep current): ")
        if user_manager.update_user(user_id, new_name):
            print("User updated.")
        else:
            print("User not found.")
        return True
    elif choice == "3":
        user_id = input("Enter user ID of the user to delete: ")
        if user_manager.delete_user(user_id):
            print("User deleted.")
        else:
            print("User not found.")
        return True
    elif choice == "4":
        print("\nList of Users:")
        user_manager.list_users()
        return True
    elif choice == "5":
        search_by = input("Enter attribute to search by (name/user_id): ")
        if not check_valid_options(search_by, ["name", "user_id"]):
            print("Invalid choice, please try again.")
            return True
        value = input("Enter value to search for: ")
        results = user_manager.search_users(**{search_by: value})
        if results:
            print("\nSearch Results:")
            for user in results:
                print(user)
        else:
            print("No users found.")
        return True
    elif choice == "6":
        return False
    else:
        print("Invalid choice, please try again.")
        return True


def handle_checkout_menu(checkout_manager, choice):
    if choice == "1":
        user_id = input("Enter user ID: ")
        isbn = input("Enter ISBN of the book to checkout: ")
        checked_out = checkout_manager.checkout_book(user_id, isbn)
        if checked_out:
            print("Book checked out.")
        else:
            print("Error. Please Check the details..")
        return True
    elif choice == "2":
        user_id = input("Enter user ID: ")
        isbn = input("Enter ISBN of the book to checkin: ")
        if checkout_manager.checkin_book(user_id, isbn):
            print("Book checked in.")
        else:
            print("Book not checked out by this user.")
        return True
    elif choice == "3":
        print("\nList of Checkouts:")
        checkout_manager.list_checkouts()
        return True
    elif choice == "4":
        return False
    else:
        print("Invalid choice, please try again.")
        return True
