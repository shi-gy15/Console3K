from card import *
from signal_slot import *

class CardFactory:
    card_type = {
        BasicCard: ['sha', 'shan', 'tao', 'jiu'],
        DelayFunctionCard: ['lebusishu', 'bingliangcunduan', 'shandian'],
        NonDelayFunctionCard: ['taoyuanjieyi', 'wanjianqifa', 'huogong', 'wuxiekeji'],
        EquipmentCard: ['hanbingjian', 'baguazhen', 'dilu', 'chitu']
    }
    # Generally,
    # basic cards have use/play signals,
    # delay and non-delay function cards have use signals only,
    # equipment cards have equip/unequip signals.
    signal_lib = {
        'use': {
            'sha': []
        }, 
        'play': {
            'sha': []
        }, 
        'equip': {
            'chitu': []
        }, 
        'unequip': {
            'chitu': []
        }
    }
    
    def __init__(self):
        pass

    @classmethod
    def produce(cls, name, color, point):
        card = None

        # create a card object
        for type_cls in cls.card_type.keys():
            if name in cls.card_type[type_cls]:
                card = type_cls(color, point)
        if card is None:
            raise ProducingError(name)

        # add use signals
        for type_ in cls.signal_lib:
            if name in cls.signal_lib[type_]:
                card.signals[type_] = cls.signal_lib[type_][name]

        # assign to a hero
        pass

        return card
