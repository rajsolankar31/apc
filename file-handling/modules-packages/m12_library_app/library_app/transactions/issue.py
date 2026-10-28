from books.availability import issued, is_available
def issue_book(book_id, member_id):
    if not is_available(book_id): return "Book already issued"
    issued.add(book_id); return f"Book {book_id} issued to member {member_id}"
