# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    """teste ja providenciado para verificar se o nome do item é mantido após a atualização da qualidade"""
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    """testes de funcionalidade das variaveis"""
    """decrescimo da qualidade"""
    def test_quality_degrades(self):
        items = [Item("foo", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(19, items[0].quality)

    """qualidade nunca negativa"""
    def test_quality_never_negative(self):
        items = [Item("foo", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    """decrescimo duas vezes mais rapido apos o sell_in chegar a zero"""
    def test_quality_degrades_twice_as_fast(self):
        items = [Item("foo", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(18, items[0].quality)

    """decrescimo do sell_in"""
    def test_sell_in_degrades(self):
        items = [Item("foo", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
    
    """testes de itens normais"""
    """qualidade de itens nunca maiores que 50 """
    def test_quality_never_greater_than_50(self):
        items = [Item("foo", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    """testes de aged brie"""
    """aumento da qualidade do aged brie com aumento do sell_in"""
    def test_aged_brie_quality_increases(self):
        items = [Item("Aged Brie", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)

    """qualidade do aged brie nunca maior que 50"""
    def test_aged_brie_quality_never_greater_than_50(self):
        items = [Item("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    """testes de sulfuras"""
    """sulfuras não possui sell_in"""
    def test_sulfuras_sell_in(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].sell_in)

    """qualidade do sulfuras é sempre 80"""
    def test_sulfuras_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

    """testes de backstage pass"""
    """aumento da qualidade do backstage pass com aumento do sell_in menor ou igual a 10"""
    def test_backstage_pass_quality_increases_by_2(self):
        items = [Item("Backstage Passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)

    """aumento da qualidade do backstage pass com aumento do sell_in menor ou igual a 5"""
    def test_backstage_pass_quality_increases_by_3(self):
        items = [Item("Backstage Passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)

    """qualidade do backstage pass é 0 quando sell_in tiver passado"""
    def test_backstage_pass_quality_is_zero_after_sell_in(self):
        items = [Item("Backstage Passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    """testes itens conjurados"""
    """teste degradação dos itens conjurados"""
    def test_conjured_item_quality_decrease(self):
        items = [Item("Conjured frog", 10, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(28, items[0].quality)

    """teste degradação dos itens conjurados após SellIn"""
    def test_conjured_item_quality_decrease_after_sellin(self):
        items = [Item("Conjured frog", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].quality)

if __name__ == '__main__':
    unittest.main()
