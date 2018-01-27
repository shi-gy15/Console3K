# Console Game - Legends of Three Kingdom

### Update 2018-01-27

### signal_slots.py
提供信号槽机制。

**API**
- `Signal.form(msg, **kwargs)` 以`msg`字符串和附加数据`kwargs`作为输入，新建一个`Signal`类的信号对象，输入的附加数据存储在`params`字段中。
- 希望新建一个槽，定义一个继承自`Slot`的类，需要重写类的`handle(cls, signal)` 方法，其中`signal`是一个信号对象。
- `register(signal_str, slot_cls=None)` 将槽类`slot_cls`加入信号串`signal_str`的处理队列。如果`slot_cls`传入空，则为`signal_str`初始化一个空的队列。
- `emit(signal)` 处理信号`signal` 。

（注意为`Signal.form()`直接传入dictionary对象作为参数时，在其前加入\*\*）