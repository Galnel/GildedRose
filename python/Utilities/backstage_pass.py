from .item import Item

class BackstagePass(Item):
    """Representa ingressos para um show (Backstage Pass).

    A qualidade aumenta à medida que a data do evento se aproxima:

    - Mais de 10 dias restantes: qualidade aumenta em 1 por dia.
    - Entre 6 e 10 dias restantes: qualidade aumenta em 2 por dia.
    - Entre 0 e 5 dias restantes: qualidade aumenta em 3 por dia.
    - Após o evento (sell_in <= 0): qualidade passa a ser 0.

    A qualidade nunca pode ultrapassar o valor máximo de 50.
    """
    
    def __init__(self, name, sell_in, quality) -> None:
        
        """Inicializa uma instância de Backstage Pass.

        Args:
            name (str): Nome do item.
            sell_in (int): Número de dias restantes até o evento.
            quality (int): Qualidade atual do item.
        """

        super().__init__(name, sell_in, quality)

    
    def update_quality(self):
        """Atualiza a qualidade e os dias restantes para o evento.

        Regras:
            - Se o evento já ocorreu (sell_in <= 0), a qualidade se
              torna 0.
            - Se faltam 5 dias ou menos, a qualidade aumenta em 3.
            - Se faltam entre 6 e 10 dias, a qualidade aumenta em 2.
            - Se faltam mais de 10 dias, a qualidade aumenta em 1.
            - A qualidade não pode ultrapassar 50.
            - Ao final da atualização, sell_in é decrementado em 1.
        """

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
            