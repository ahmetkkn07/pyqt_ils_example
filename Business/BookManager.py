from DataAccess.database import get, get_all, add


class UserManager:
    def get_books_by_name(self, name):
        books = get_all(f"SELECT * FROM books WHERE name='{name}'")
        return books

    def get_book_by_id(self, id):
        book = get(f"SELECT * FROM books WHERE id='{id}'")
        return book

    def add_book(self, name, author, number_of_pages, publisher):
        add(
            f"INSERT INTO books(name, author, number_of_pages, publisher) \
                VALUES('{name}','{author}',{number_of_pages},'{publisher}')")
