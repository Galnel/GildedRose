# -*- coding: utf-8 -*-
from .Utilities import Item, AgedBrie, BackstagePass, NormalItem, Sulfuras, Conjured

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def create_item(self, item):

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

        for item in self.items:

            updater = self.create_item(item)

            updater.update_quality()

            item.sell_in = updater.sell_in
            item.quality = updater.quality

        