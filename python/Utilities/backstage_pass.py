from .item import Item

class BackstagePass(Item):
    """Classe para itens do tipo Backstage Pass, que tem a qualidade aumentada em 1 a cada dia, 
    e depois do prazo de validade, a qualidade se torna 0.

    Args:
        Item (_type_): _description_
    """
    def __init__(self, name, sell_in, quality) -> None:
        super().__init__(name, sell_in, quality)

    
    def update_quality(self):

        if self.sell_in <= 0:
            self.quality = 0
        elif self.sell_in <= 5:
            self.quality += 3
        elif self.sell_in <= 10:
            self.quality += 2
        else:
            self.quality += 1

        self.quality = min(50, self.quality)
        self.sell_in -= 1
            