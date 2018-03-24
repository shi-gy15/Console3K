from exceptions import *


class Card:
    _types = ['basic', 'd-func', 'nd-func', 'equip']
    _colors = ['spade', 'heart', 'club', 'diamond']
    _points = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, type_, color, point):
        self.type = type_
        self.color = color
        self.point = point
        self._check()
        self.signals = {
            'show': []
        }
        self.hero = None

    def _check(self):
        if self.type not in Card._types:
            raise CardInfoError('type [%s]' % self.type)
        if self.color not in self._colors:
            raise CardInfoError('color [%s]' % self.color)
        if self.point not in self._points:
            raise CardInfoError('point [%s]' % self.point)

    # 使用牌
    # When being used, it emits all signals in use_signal, with all parameters known.
    def use(self):
        raise NotImplementedError('Not implemented [Card.use] yet.')

    # 打出牌
    def play(self):
        raise NotImplementedError('Not implemented [Card.play] yet.')        

class BasicCard(Card):
    def __init__(self, color, point):
        Card.__init__(self, 'basic', color, point)
        self.signals['use'] = []
        self.signals['play'] = []

class DelayFunctionCard(Card):
    def __init__(self, color, point):
        Card.__init__(self, 'd-func', color, point)
        self.signals['use'] = []

class NonDelayFunctionCard(Card):
    def __init__(self, color, point):
        Card.__init__(self, 'nd-func', color, point)
        self.signals['use'] = []

class EquipmentCard(Card):
    def __init__(self, color, point):
        Card.__init__(self, 'equip', color, point)
        self.signals['equip'] = []
        self.signals['unequip'] = []