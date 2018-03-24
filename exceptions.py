
class MyException(Exception):
    def __init__(self, arg):
        self.args = arg;

class CardInfoError(TypeError):
    def __init__(self, arg):
        self.args = 'Wrong card info: ' + arg;
        TypeError.__init__(self, arg);

class ProducingError(TypeError):
    def __init__(self, arg):
        self.args = 'Wrong in producing: ' + arg;
        TypeError.__init__(self, arg);