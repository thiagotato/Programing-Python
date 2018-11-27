class UppercaseAttributes:
    """
    A class that returns uppercase values on uppercase attributes access.
    """

    # Called (if it exists) if an attribute access fails:
    def __getattr__(self, name):
        if name.isupper():
            print name
            if name.islower() in self.__dict__:
                return self.__dict__[
                        name.lower()].upper()
        raise AttributeError(
                "'{}' object has no attribute {}."
                .format(self, name))
