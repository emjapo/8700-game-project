from HolidayFactory import HolidayFactory
from enemies.enemy import Enemy
from enemies.santa import Santa
from enemies.present import Present
from enemies.reindeer import Reindeer

class ChristmasFactory(HolidayFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def create_enemy_1(x, y) -> Enemy:
        return Santa(x, y)

    def create_enemy_2(x, y) -> Enemy:
        return Present(x, y)

    def create_enemy_3(x, y) -> Enemy:
        return Reindeer(x, y)
