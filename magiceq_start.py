class Book:
    def __init__(self, title, author, price):
        self.title = title;
        self.author = author;
        self.price = price;

    def __str__(self):
        return f"{self.title}, author: {self.author}, and is priced at: {self.price}";

    # TODO: __eq__ method for checking equality of two objects

    # ToDO: __ge__ method

    # TODO: __le__ method


b1 = Book("War and Peace", "Leo Tolstoy", 39.90);
b2 = Book("The Da Vinci COde", "Dan Brwon", 29.90);
print(b1);
print(b2);
