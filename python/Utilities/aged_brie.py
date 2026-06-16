
from .item import Item

class AgedBrie(Item):
    """Classe para o item Aged Brie, que tem a qualidade aumentada em 1 a cada dia, 
    e depois do prazo de validade, a qualidade aumenta em 2 a cada dia.

    Args:
        Item (_type_): _description_
    """
    def __init__(self, name, sell_in, quality) -> None:
        super().__init__(name, sell_in, quality)