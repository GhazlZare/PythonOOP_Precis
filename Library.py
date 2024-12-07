import uuid
from datetime import datetime

class Book:
    def __init__(self, title, author) -> None:
        self.id_ = str(uuid.uuid4())
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book ID: {self.id_}, Title: {self.title}, Author: {self.author}"

class Library:
    def __init__(self, start_time: str, end_time: str) -> None:
        self.books = {} 
        self.start_time = datetime.strptime(start_time, "%H:%M")
        self.end_time = datetime.strptime(end_time, "%H:%M")

    def add_book(self, new_book):
        if new_book.id_ not in self.books:
            self.books[new_book.id_] = new_book
            return print(f"Book '{new_book.title}' added successfully.")
        return print("Book already exists in the library.")

    def remove_book(self, book_id: str):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            return print(f"Book '{removed_book.title}' with ID '{book_id}' removed.")
        return print("Book not found.")

    def display_books(self):
        if not self.books:
            return "No books available in the library."
        return '\n'.join(str(book) for book in self.books.values())

    def is_open(self):
        current_time = datetime.now().time()  
        if self.start_time.time() <= current_time <= self.end_time.time():
            return print("The library is open.")
        else:
            return print("The library is closed.")

def main():
    library = Library("09:00", "22:00")

    while True:
        print('''What do you wanna do?(Enter the number)
    1. Add a new book
    2. Remove a book
    3. Show books
    4. Is this shop open now?
    5. Exit''')
        choice = str(input())
        if choice == "1":
            title = str(input("Enter the title of the book: "))
            author = str(input("Enter the author: "))
            new_book = Book(title, author)
            library.add_book(new_book)
        elif choice == "2":
            book_id = str(input("Enter the id of the book you want to remove: "))
            library.remove_book(book_id)
        
        elif choice == "3":
            list_books = library.display_books()
            print(list_books)

        elif choice == "4":
            library.is_open()

        elif choice == "5":
            break

        else:
            print("Out of range")

if __name__ == "__main__":
    main()