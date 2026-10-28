from books.availability import issued
def return_book(book_id):
    if book_id in issued: issued.discard(book_id); return f"Book {book_id} returned"
    return "Book was not issued"
