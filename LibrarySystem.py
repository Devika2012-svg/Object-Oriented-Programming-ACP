class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            print(f'⚠️ "{self.title}" is already borrowed!')
        else:
            self.is_borrowed = True
            print(f'✅ You borrowed "{self.title}". Enjoy reading! 📖')

    def return_book(self):
        if not self.is_borrowed:
            print(f'⚠️ "{self.title}" was not borrowed!')
        else:
            self.is_borrowed = False
            print(f'✅ You returned "{self.title}". Thank you! 😊')

    def __str__(self):
        status = "🔴 Borrowed" if self.is_borrowed else "🟢 Available"
        return f"📘 {self.title} by {self.author} [{status}]"

book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Hobbit", "J.R.R. Tolkien")
book3 = Book("The Lord of The Rings", "J.R.R. Tolkien")
book4 = Book("The Alchemist", "Paulo Coelho")

print("=" * 50)
print("          📚 WELCOME TO THE LIBRARY 📚")
print("=" * 50)

print("\n📋 --- INITIAL BOOK LIST ---")
print(book1)
print(book2)
print(book3)
print(book4)

print("\n📤 --- BORROW BOOKS ---")
book1.borrow()
book4.borrow()

print("\n🔁 --- TRYING DOUBLE BORROWING ---")
book1.borrow()

print("\n📥 --- RETURNING A BOOK ---")
book1.return_book()

print("\n🔁 --- TESTING AN INVALID RETURN ---")
book3.return_book()

print("\n📋 --- FINAL BOOK LIST ---")
print(book1)
print(book2)
print(book3)
print(book4)

print("\n" + "=" * 50)
print("       🎉 THANK YOU FOR VISITING! 🎉")
print("            📚 Happy Reading! 📚")
print("=" * 50)
