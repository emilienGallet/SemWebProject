class Query:
    """Manage the Spark Query Language"""

    def __init__(self, **kwargs):
        super().__init__()
        for el in kwargs:
            self.__dict__.update(kwargs)

    def build():
        pass
