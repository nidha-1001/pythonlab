class Publisher:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Publisher:", self.name)


class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)  # invoking base class constructor
        self.title = title
        self.author = author

    def display(self):
        super().display()
        print("Title:", self.title)
        print("Author:", self.author)


class Python(Book):
    def __init__(self, name, title, author, price, no_of_pages):
        super().__init__(name, title, author)  # invoking base class constructor
        self.price = price
        self.no_of_pages = no_of_pages

    # Method overriding
    def display(self):
        super().display()
        print("Price:", self.price)
        print("No. of Pages:", self.no_of_pages)


# -------- Main Program -------- #
# Creating a Python book object
python_book = Python(
    name="O'Reilly Media",
    title="Learning Python",
    author="Mark Lutz",
    price=650,
    no_of_pages=1648
)

# Displaying book information
python_book.display()

