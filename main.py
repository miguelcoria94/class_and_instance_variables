from datetime import date

class Book:
    loan_duration = 14

    def __init__(self, title, series, author):
        self._title = title
        self._series = series
        self._author = author
        self._checked_out_on = None

    def __repr__(self):
        return f"{self._title} by {self._author}"

    def checkout(self, checked_out_on=date.today()):
        """
        method to checkout a book
        """
        self._checked_out_on = checked_out_on

    def is_overdue(self):
        """
        method to check if book is overdue.
        """
        overdue = False

        if self._checked_out_on is not None:
            elapsed_days = (date.today() - self._checked_out_on).days
            overdue = elapsed_days > self.loan_duration

        return overdue

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

print(fellowship_of_the_ring.is_overdue())

fellowship_of_the_ring.checkout(
    checked_out_on=date.fromisoformat("2020-04-01")
)

print(fellowship_of_the_ring.loan_duration)