from .item import Item

class Sulfuras(Item):
    """Representa o item lendário Sulfuras.

    Sulfuras é um item lendário e, portanto, não sofre alterações com o
    passar do tempo.

    - O valor de ``sell_in`` permanece constante.
    - O valor de ``quality`` permanece constante.
    - No Kata original, sua qualidade é sempre 80.
    """

    def __init__(self, name, sell_in, quality) -> None:
        """Inicializa uma instância de Sulfuras.

        Args:
            name (str): Nome do item.
            sell_in (int): Número de dias restantes para venda.
            quality (int): Qualidade do item.
        """
        super().__init__(name, sell_in, quality)

    def update_quality(self) -> None:
        """Não realiza nenhuma atualização.

        Como Sulfuras é um item lendário, seus atributos não se alteram
        com o passar dos dias.
        """
        pass