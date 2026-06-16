from .item import Item

class Sulfuras(Item):
    """Classe para o item Sulfuras, que é um item lendário, e por isso não tem prazo de validade e nem qualidade.

    Args:
        Item (_type_): _description_
    """
    def __init__(self, name, sell_in, quality) -> None:
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        pass