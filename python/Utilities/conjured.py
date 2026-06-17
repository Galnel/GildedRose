from .item import Item

class Conjured(Item):
    """Itens Conjured 
    degradam duas vezes mais rápido que itens normais.

    Args:
        Item (_type_): _description_
    """

    def __init__(self, name, sell_in, quality) -> None:
        super().__init__(name, sell_in, quality)

    def update_quality(self):

        if self.sell_in > 0:
            self.quality = max(0, self.quality - 2)
        else:
            self.quality = max(0, self.quality - 4)

        self.sell_in -= 1