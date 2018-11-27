class Number():
    """A number class."""
    __version__ = '1.0'

    def __init__(self, amount):
        self.amount = amount

    def add(self, value):
        """Add a value to the number."""
        print('Call: add({!r}, {})'.format(self, value))
        return self.amount + value
