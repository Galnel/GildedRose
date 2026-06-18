import sys
from pathlib import Path

# item_abs_dir = Path("GildedRose/python/Utilities/item.py").resolve()
# normal_item_abs_path = Path("GildedRose/python/Utilities/normal_item.py").resolve()
# sulfuras_abs_path = Path("GildedRose/python/Utilities/sulfuras.py").resolve()
# aged_bride_abs_path = Path("GildedRose/python/Utilities/aged_brie.py").resolve()
# backstage_pass_abs_path = Path("GildedRose/python/Utilities/backstage_pass.py").resolve()
# conjured_abs_path = Path("GildedRose/python/Utilities/conjured").resolve()

# sys.path.append(item_abs_dir)
# sys.path.append(normal_item_abs_path)
# sys.path.append(sulfuras_abs_path)
# sys.path.append(aged_bride_abs_path)
# sys.path.append(backstage_pass_abs_path)
# sys.path.append(conjured_abs_path)

abs_utilites_dir = Path("GildedRose/python/Utilities")
sys.path.append(abs_utilites_dir)

from .item import Item
from .normal_item import NormalItem
from .sulfuras import Sulfuras
from .aged_brie import AgedBrie
from .backstage_pass import BackstagePass
from .conjured import Conjured


# from .item import Item
# from .normal_item import NormalItem
# from .sulfuras import Sulfuras
# from .aged_brie import AgedBrie
# from .backstage_pass import BackstagePass
# from .conjured import Conjured