import pytest
from management.book_management import BookManager


@pytest.fixture
def book_manager(tmp_path):
    tmp_dir = tmp_path / "data"
    tmp_dir.mkdir()

    # Create a BookManager instance with the temporary JSON file
    filename = tmp_dir / "test_books.json"
    manager = BookManager(str(filename))

    yield manager

    filename.unlink()


def test_add_book(book_manager):
    """Test adding a new book."""
    title = "Test Book"
    author = "Test Author"
    isbn = "1234567890"

    save_status = book_manager.add_book(title, author, isbn)

    assert save_status == "saved"
    assert len(book_manager.books) == 1
    assert book_manager.books[0].title == title
    assert book_manager.books[0].author == author
    assert book_manager.books[0].isbn == isbn


def test_update_book(book_manager):
    """Test updating an existing book."""

    initial_title = "Initial Title"
    new_title = "Updated Title"
    author = "Test Author"
    isbn = "1234567890"
    book_manager.add_book(initial_title, author, isbn)

    update_status = book_manager.update_book(isbn, new_title)

    assert update_status is True
    assert len(book_manager.books) == 1
    assert book_manager.books[0].title == new_title


def test_delete_book(book_manager):
    """Test deleting an existing book."""

    title = "Test Book"
    author = "Test Author"
    isbn = "1234567890"
    book_manager.add_book(title, author, isbn)

    delete_status = book_manager.delete_book(isbn)

    assert delete_status is True
    assert len(book_manager.books) == 0


def test_list_books(book_manager, capsys):
    """Test listing all books."""

    book_manager.add_book("Book 1", "Author 1", "1234567890")
    book_manager.add_book("Book 2", "Author 2", "0987654321")

    book_manager.list_books()
    captured = capsys.readouterr()

    assert "Book(title='Book 1', author='Author 1'" in captured.out
    assert "Book(title='Book 2', author='Author 2'" in captured.out


def test_search_books(book_manager):
    """Test searching for books."""

    book_manager.add_book("Python Programming", "John Doe", "1234567890")
    book_manager.add_book("Machine Learning", "Jane Smith", "0987654321")

    results = book_manager.search_books(title="Python Programming")

    assert len(results) == 1
    assert results[0].title == "Python Programming"
    assert results[0].author == "John Doe"
    assert results[0].isbn == "1234567890"
