class Book:
    def __init__(self, title, author, pages, price):
        self.title = title;
        self.author = author;
        self.pages = pages;
        self.price = price;
        self.__secret = "This is a secret Attibute.";
        self._notsosecret = "This is not so secret attibute."

    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount);
        else:
            return self.price;

    def setdiscount(self, amount):
        self._discount = amount;


class Newspaper:
    def __init__(self, name):
        self.name = name;


b1 = Book("War and Peace.", "Leo Tolstoy", 1225, 39.95);
b2 = Book("The catcher in the Rye.", "JD Salinger", 234, 29.95);
n1 = Newspaper("The Washington Post");

print(isinstance(b1, Book));
print(isinstance(n1, Newspaper));
print(isinstance(n1, Book));
print(isinstance(n1, object));
# print(b1.getprice());
# print(b2.getprice());
# b2.setdiscount(0.25);
# print(b2.getprice())
# print(b2._Book__secret);
