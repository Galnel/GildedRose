from .item import Item

class Conjured(Item):
    """Representa itens do tipo Conjured.

    Itens Conjured degradam sua qualidade duas vezes mais rápido que
    itens normais.

    - Antes da data de venda expirar, a qualidade diminui em 2 por dia.
    - Após a data de venda expirar, a qualidade diminui em 4 por dia.
    - A qualidade nunca pode ser negativa.
    """

    def __init__(self, name, sell_in, quality) -> None:
        """Inicializa uma instância de um item Conjured.

        Args:
            name (str): Nome do item.
            sell_in (int): Número de dias restantes para venda.
            quality (int): Qualidade atual do item.
        """
        super().__init__(name, sell_in, quality)

    def update_quality(self) -> None:
        """Atualiza a qualidade e a data de venda do item.

        Regras:
            - Se ``sell_in`` for maior que 0, a qualidade diminui em 2.
            - Se ``sell_in`` for menor ou igual a 0, a qualidade diminui
              em 4.
            - A qualidade nunca pode ser menor que 0.
            - Ao final da atualização, ``sell_in`` é decrementado em 1.
        """

        if self.sell_in > 0:
            self.quality = max(0, self.quality - 2)
        else:
            self.quality = max(0, self.quality - 4)

        self.sell_in -= 1