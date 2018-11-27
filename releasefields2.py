class ReleaseFields:
    slices = {
            'name': slice(0, 6),
            'version': slice(7,12),
            'date': slice(13, 23)
            }
    
    def __init__(self, data):
        self.data = data

    def __getattr__(self, attribute):
        if attribute in self.slices:
            return self.data[self.slices[attribute]]
        raise AttributeError(
                "{!r} has no attribute {!r}"
                .format(self, attribute))

