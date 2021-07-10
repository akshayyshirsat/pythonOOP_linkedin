class Publication:
    def __init__(self, title, price):
        self.title = title;
        self.price = price;


class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price);
        self.period = period;
        self.publisher = publisher;


class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price);
        self.author = author;
        self.pages = pages;


class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher);


class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher);


b1 = Book("Brace New World", "Aldous Huxley", 311, 20.01);
m1 = Magazine("NY Times", "New York Times Company", 6.0, "Daily");
n1 = Newspaper("Scientic American", "Springer Nature", 5.99, "Monthly");

print(b1.author);
print(m1.publisher);
print(n1.price);
