__author__ = "davood akbari <daak1365@yahoo.com>"
__status__ = "production"
__version__ = "0.0.0.1"
__date__ = "November 2017"

class Context:
    _name = None
    _service = 'service'
    _web = 'web'

    def __init__(self, name, service='service', web='web'):
        self._name = name
        self._service = service
        self._web = web


    @property
    def name(self):
        return self._name

    @property
    def service(self):
        return self._service

    @property
    def web(self):
        return self._web


class ContextManager(dict):
    @staticmethod
    def add(self, context):
        self.add(context.name, context)


