from DataAccess.database import get, get_all, add, update


class BookManager:
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

    def get_all(self):
        books = get_all("SELECT * FROM books ORDER BY id ASC")
        return books

    def update_book(self, selected_id, name, author, number_of_pages, publisher):
        update(
            f"UPDATE books SET name='{name}', author='{author}', \
                number_of_pages={number_of_pages}, publisher='{publisher}' \
                    WHERE id={selected_id}")
