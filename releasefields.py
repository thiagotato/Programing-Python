class ReleaseFields:
    def __init__(self, data):
        self.data = data

    @property
    def name(self):
        return self.data[0:6]

    @property
    def version(self):
        return self.data[7:12]

    @property
    def date(self):
        return self.data[13:23]
