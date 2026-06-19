from .item import Item

class NormalItem(Item):
    """Representa um item comum.

    Itens normais perdem qualidade com o passar do tempo.

    - Antes da data de venda expirar, a qualidade diminui em 1 por dia.
    - Após a data de venda expirar, a qualidade diminui em 2 por dia.
    - A qualidade nunca pode ser negativa.
    """

    def __init__(self, name, sell_in, quality) -> None:
        """Inicializa uma instância de um item normal.

        Args:
            name (str): Nome do item.
            sell_in (int): Número de dias restantes para venda.
            quality (int): Qualidade atual do item.
        """
        super().__init__(name, sell_in, quality)

    def update_quality(self) -> None:
        """Atualiza a qualidade e a data de venda do item.

        Regras:
            - Se ``sell_in`` for maior que 0, a qualidade diminui em 1.
            - Se ``sell_in`` for menor ou igual a 0, a qualidade diminui em 2.
            - A qualidade nunca pode ser menor que 0.
            - Após a atualização da qualidade, ``sell_in`` é decrementado em 1.
        """

        if self.sell_in > 0:
            self.quality = max(0, self.quality - 1)
        else:
            self.quality = max(0, self.quality - 2)

        self.sell_in -= 1
