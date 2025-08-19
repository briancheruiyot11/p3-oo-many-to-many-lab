class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise Exception("Name must be a non-empty string")
        self._name = value

    def contracts(self):
        """Return list of contracts for this author"""
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        """Return list of books through contracts"""
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Create a new contract and return it"""
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Sum up royalties from all contracts"""
        return sum(contract.royalties for contract in self.contracts())


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise Exception("Title must be a non-empty string")
        self._title = value

    def contracts(self):
        """Return list of contracts for this book"""
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        """Return list of authors for this book"""
        return [contract.author for contract in self.contracts()]



class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be an instance of Author")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("Book must be an instance of Book")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise Exception("Date must be a non-empty string")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int) or value < 0:
            raise Exception("Royalties must be a positive integer")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
