from datetime import date

class Book:
    def __init__(self, title, series, author):
        self._title = title
        self._series = series
        self._author = author
        self._checked_out_on = None

    def __repr__(self):
        return f"{self._title} by {self._author}"

    def checkout(self, checked_out_on=data.today()):
        """
        method to checkout a book
        """
        self._checked_out_on = checked_out_on

fellowship_of_the_ring = Book(
    "The Fellowship of the Ring",
    "The Lord of the Rings",
    "J.R.R Tolkien"
)

grapes_of_wrath = Book(
    "The Grapes of Wrath",
    None,
    "John Steinbeck"
)

print(fellowship_of_the_ring)