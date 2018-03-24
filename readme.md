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

### Update 2018-3-24

### card.py
卡牌类。

**API**
- 卡牌分为四种类型
  - `BasicCard` ：基本牌
  - `DelayFunctionCard` : 延时锦囊牌
  - `NonDelayFunctionCard` ：非延时锦囊牌
  - `Equipment` ：装备牌

### card_factory.py
卡牌的构造。

**API**
- `CardFactory.produce(name, color, point)` 构造一个名为 `name` ，花色为 `color` ，点数为 `point` 的 `Card` 类对象。
- 希望添加一张新卡牌，在 `CardFactory.card_type` 中添加数据。
- 希望为某张牌加入新的响应，在 `CardFactory.signal_lib` 中添加数据。
- 卡牌产生的信号目前分为五种
  - `show` ：展示卡牌时发出， 适用于所有类型卡牌
  - `use` ：使用时发出，适用于基本、延时/非延时锦囊牌
  - `play` ：打出时发出，适用于基本牌
  - `equip` ：装备时发出，适用于装备牌
  - `unequip` ：卸下时发出，适用于装备牌