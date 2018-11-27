class PropertyEg:
    """@property example"""
    def __init__(self):
        self._x = 'Uninitialized'

    @property
    def x(self):
        """The 'x' property"""
        print('called x getter()')
        return self._x

    @x.setter
    def x(self, value):
        print('called x.setter()')
        self._x = value

    @x.deleter
    def x(self):
        print('called x.deleter')
        self.__init__()
