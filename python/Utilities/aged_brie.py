
from .item import Item

class AgedBrie(Item):
    """Classe para o item Aged Brie, que tem a qualidade aumentada em 1 a cada dia, 
    e depois do prazo de validade, a qualidade aumenta em 2 a cada dia.

    Args:
        Item (_type_): _description_
    """
    def __init__(self, name, sell_in, quality) -> None:
        super().__init__(name, sell_in, quality)
        
    def update_quality(self):
        
        if self.sell_in >= 0:
            self.quality = self.quality + 1
        else:
            self.quality = min(50, self.quality + 2)
            
        self.sell_in = self.sell_in - 1
        