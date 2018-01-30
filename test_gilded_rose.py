# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    def test_normal_item(self):
        items = [Item("normal item", 1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].sell_in)
        self.assertEquals(0, items[0].quality)

    def test_backstage_pass(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert",15,20),
            Item("Backstage passes to a TAFKAL80ETC concert",10,49),
            Item("Backstage passes to a TAFKAL80ETC concert",5,49),
            Item("Backstage passes to a TAFKAL80ETC concert",0,49)
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(14, items[0].sell_in)
        self.assertEquals(21, items[0].quality)
        self.assertEquals(9, items[1].sell_in)
        self.assertEquals(50, items[1].quality)
        self.assertEquals(4, items[2].sell_in)
        self.assertEquals(50, items[2].quality)
        self.assertEquals(-1, items[3].sell_in)
        self.assertEquals(0, items[3].quality)

    def test_aged_brie(self):
        items = [Item("Aged Brie", 1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].sell_in)
        self.assertEquals(2, items[0].quality)

    def test_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(1, items[0].sell_in)
        self.assertEquals(1, items[0].quality)

    def test_conjured(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(2, items[0].sell_in)
        self.assertEquals(4, items[0].quality)



if __name__ == '__main__':
    unittest.main()
