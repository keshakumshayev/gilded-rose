# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        exceptions = ["Backstage passes to a TAFKAL80ETC concert",
            "Aged Brie",
            "Sulfuras, Hand of Ragnaros",
            "Conjured Mana Cake"
        ]
        for item in self.items:
            if item.name not in exceptions:
                self.normal_update_quality(item)
            else:
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    self.backstage_pass_update_quality(item)
                if item.name == "Aged Brie":
                    self.aged_update_quality(item)
                if item.name == "Conjured Mana Cake":
                    self.conjured_update_quality(item)

    # THIS METHOD CONTROLS MIN/MAX VALUE OF ITEM QUALITY

    def stop_at_limit(self, item):
        if item.quality >= 50:
            item.quality = 50
        if item.quality < 0:
            item.quality = 0

    # METHODS FOR DIFFERENT ITEM TYPES BELOW

    def normal_update_quality(self, item):
        item.sell_in -= 1
        item.quality -= 1 if item.sell_in > 0 else 2
        self.stop_at_limit(item)

    def backstage_pass_update_quality(self, item):
        item.sell_in -= 1
        if item.sell_in >= 10:
            item.quality += 1
        elif item.sell_in >= 5:
            item.quality += 2
        elif item.sell_in >= 0:
            item.quality += 3
        else:
            item.quality = 0
        self.stop_at_limit(item)

    def aged_update_quality(self, item):
        item.sell_in -= 1
        item.quality += 1
        self.stop_at_limit(item)

    def conjured_update_quality(self, item):
        item.sell_in -= 1
        item.quality -= 2 if item.sell_in > 0 else 4
        self.stop_at_limit(item)

# IT WOULD BE NICE TO ADD A TYPE FOR ITEM
# TO MAKE IT EASIER TO JUST PLUG IN A TYPE FOR update_quality

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
