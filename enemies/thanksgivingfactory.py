from enemies.holidayfactory import HolidayFactory
from enemies.enemy import Enemy
from enemies.turkey import Turkey
from enemies.corn import Corn
from enemies.macaroni import Macaroni

class ThanksgivingnFactory(HolidayFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def create_enemy_1(x, y) -> Enemy:
        return Turkey(x, y)

    def create_enemy_2(x, y) -> Enemy:
        return Corn(x, y)

    def create_enemy_3(x, y) -> Enemy:
        return Macaroni(x, y)
