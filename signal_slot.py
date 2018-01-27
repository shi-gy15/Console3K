
'''
Signal: {
    msg: play / summon / ...
    params: {}
}

Slot: {
    def handle(cls, signal)
}

'''

class Signal:

    def __init__(self, msg):
        self.msg = msg

    @classmethod
    def form(cls, msg, **kwargs):
        signal = Signal(msg)
        signal.params = kwargs
        return signal

class Slot:
    @classmethod
    def handle(cls, signal):
        raise NotImplementedError

class Dispatcher():
    slots = {}

    @classmethod
    def dispatch(cls, signal):
        if signal.msg in cls.slots.keys():
            for slot in cls.slots[signal.msg]:
                slot.handle(signal)

    @classmethod
    def register(cls, signal_str, slot_cls=None):
        if slot_cls is None:
            if signal_str not in cls.slots.keys():
                cls.slots[signal_str] = []
            return

        if slot_cls.handle:
            if signal_str in cls.slots.keys():
                cls.slots[signal_str].append(slot_cls)
            else:
                cls.slots[signal_str] = [slot_cls]

def register(signal_str, slot_cls=None):
    Dispatcher.register(signal_str, slot_cls)

def emit(signal):
    Dispatcher.dispatch(signal)
