from holiday_factory import HolidayFactory
from enemies.enemy import Enemy
from enemies.santa import Santa
from enemies.present import Present
from enemies.reindeer import Reindeer

from hero import Hero
from christmas_hero import ChristmasHero

RED = (255, 0, 0)

class ChristmasFactory(HolidayFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def create_enemy_1(self, x, y) -> Enemy:
        return Santa(x, y)

    def create_enemy_2(self, x, y) -> Enemy:
        return Present(x, y)

    def create_enemy_3(self, x, y) -> Enemy:
        return Reindeer(x, y)
    def create_enemy(self, type, x, y) -> Enemy:
        #print("Creating Halloween Enemy:")
        if type == 0:
            return Reindeer(x, y)
        elif type == 1:
            return Present(x, y)
        else:
            return Santa(x, y)

    def create_hero(self, x, y, offset) -> Hero:
        return ChristmasHero(x, y, offset)

    def get_color(self):
        return RED

def print_info(self):
    print("I am the Christmas Factory")
