
from .item import Item

class AgedBrie(Item):
    """Representa o item Aged Brie.

    Diferentemente dos itens comuns, a qualidade do Aged Brie aumenta
    com o passar do tempo. Antes da data de venda expirar, a qualidade
    aumenta em 1 por dia. Após a expiração, a qualidade aumenta em 2
    por dia.

    A qualidade nunca deve ultrapassar o valor máximo de 50.
    """
    def __init__(self, name, sell_in, quality) -> None:
        """Inicializa uma instância de Aged Brie.

        Args:
            name (str): Nome do item.
            sell_in (int): Número de dias restantes para venda.
            quality (int): Qualidade atual do item.
        """
        
        super().__init__(name, sell_in, quality)
        
    def update_quality(self) -> None:

        """Atualiza a qualidade e o prazo de venda do item.

        Regras:
            - Se ``sell_in`` for maior ou igual a zero, a qualidade
              aumenta em 1.
            - Se ``sell_in`` for menor que zero, a qualidade aumenta
              em 2.
            - A qualidade não pode ultrapassar 50.
            - Ao final da atualização, ``sell_in`` é decrementado em 1.
        """
        
        if self.sell_in >= 0:
            self.quality = min(50, self.quality + 1)
        else:
            self.quality = min(50, self.quality + 2)
            
        self.sell_in = self.sell_in - 1
        