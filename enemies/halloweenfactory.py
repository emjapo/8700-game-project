from enemies.holidayfactory import HolidayFactory
from enemies.enemy import Enemy
from enemies.pumpkin import Pumpkin
from enemies.ghost import Ghost
from enemies.witch import Witch

class HalloweenFactory(HolidayFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def create_enemy_1(x, y) -> Enemy:
        return Pumpkin(x, y)

    def create_enemy_2(x, y) -> Enemy:
        return Ghost(x, y)

    def create_enemy_3(x, y) -> Enemy:
        return Witch(x, y)
