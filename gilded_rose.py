# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    # refactored update_quality to deal with an array of special item names
    # and modified if statements to deal with each different item on its own
    # for example the previous code had quality of Backstage passes go up by 1 three times
    # in different nested if statements if the sell_in was 5 or lower at the time of update_quality
    # update_quality is NOT CURRENTLY degrading items faster after sell date

    def update_quality(self):
        exceptions = ["Backstage passes to a TAFKAL80ETC concert",
            "Aged Brie",
            "Sulfuras, Hand of Ragnaros",
            "Conjured Mana Cake"
        ]
        for item in self.items:
            if item.name not in exceptions:
                item.sell_in -= 1
                item.quality -= 1
            else:
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in > 10:
                        item.sell_in -= 1
                        item.quality += 1
                        if item.quality >= 50:
                            item.quality = 50
                    elif item.sell_in > 5:
                        item.sell_in -= 1
                        item.quality += 2
                        if item.quality >= 50:
                            item.quality = 50
                    elif item.sell_in > 0:
                        item.sell_in -= 1
                        item.quality += 3
                        if item.quality >= 50:
                            item.quality = 50
                    else:
                        item.sell_in -= 1
                        item.quality = 0
                if item.name == "Aged Brie":
                    item.sell_in -= 1
                    item.quality += 1
                    if item.quality >= 50:
                        item.quality = 50
                if item.name == "Conjured Mana Cake":
                    item.sell_in -= 1
                    item.quality -= 2


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
