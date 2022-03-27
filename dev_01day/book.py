class Book(object):
    def __init__(self, book_id, book_name, book_pos):
        self.book_id = book_id
        self.book_name = book_name
        self.book_pos = book_pos

    def __del__(self):
        pass

    def __str__(self):
        return
