class BaseDataTransformer:
    def __init__(self, data):
        self.data = data

    def transform_data(self, **kwargs):
        raise NotImplementedError()
