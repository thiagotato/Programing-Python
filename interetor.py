class MyList:
    """Demonstrate the interator protocol"""
    def __init__(self, sequence):
        self.items = sequence

    def __getitem__(self, key):
        print('called __getitem({})'.format(key))
        return self.items[key]
