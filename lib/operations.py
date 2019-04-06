

class OperationsPluginsInterface(type):

    def __init__(cls, name, parents, dct):
        if not hasattr(cls, 'plugins'):
            cls.plugins = []
        else:
            cls.plugins.append(cls)

        super(OperationsPluginsInterface, cls).__init__(name, parents, dct)


class ImperativeOperations(object):
    __metaclass__ = OperationsPluginsInterface

    def __init__(self):
        self.plugins = []
