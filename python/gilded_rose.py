# -*- coding: utf-8 -*-
from .Utilities import Item, AgedBrie, BackstagePass, NormalItem, Sulfuras, Conjured

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def create_item(self, item) -> None:
        """Cria e retorna a instância especializada correspondente ao item.

        Com base no atributo ``name`` do item recebido, instancia a classe
        apropriada para aplicar as regras de atualização de qualidade
        específicas daquele tipo de item.

        Args:
            item (Item): Item original que será convertido para uma das
                classes especializadas.

        Returns:
            Item: Instância de uma subclasse de Item (AgedBrie, Sulfuras,
            BackstagePass, Conjured ou NormalItem).
        """

        if item.name == "Aged Brie":
            return AgedBrie(item.name, item.sell_in, item.quality)

        if item.name == "Sulfuras, Hand of Ragnaros":
            return Sulfuras(item.name, item.sell_in, item.quality)

        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePass(item.name, item.sell_in, item.quality)

        if item.name.startswith("Conjured"):
            return Conjured(item.name, item.sell_in, item.quality)

        return NormalItem(item.name, item.sell_in, item.quality)

    def update_quality(self):
        """
        Atualiza a qualidade e a data de venda de todos os itens.

        Para cada item da coleção, cria uma instância especializada através
        de ``create_item()``, executa suas regras de atualização e copia os
        valores calculados de ``sell_in`` e ``quality`` de volta para o item
        original.

        Returns:
            None
        """

        for item in self.items:

            updater = self.create_item(item)

            updater.update_quality()

            item.sell_in = updater.sell_in
            item.quality = updater.quality

        