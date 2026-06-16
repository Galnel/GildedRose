
from .item import Item

class NormalItem(Item):
    """Classe para itens normais, que tem a qualidade decrescida em 1 a cada dia, 
    e depois do prazo de validade, a qualidade decresce em 2 a cada dia.

    Args:
        Item (_type_): _description_
    """
    def __init__(self, name, sell_in, quality) -> None:
        super().__init__(name, sell_in, quality)

    def update_quality(self):

        self.sell_in -= 1

        if self.sell_in > 0:
            self.quality = max(0, self.quality - 1)
        else:
            self.quality = max(0, self.quality - 2)