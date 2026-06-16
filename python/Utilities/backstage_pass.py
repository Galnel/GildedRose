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

        self.sell_in -= 1

        if self.sell_in <= 0:
            self.quality += 10
        ...