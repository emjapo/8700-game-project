class ThanksgivingnFactory(HolidayFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def create_enemy_1(self) -> Enemy:
        return Turkey()

    def create_enemy_2(self) -> Enemy:
        return Corn()

    def create_enemy_3(self) -> Enemy:
        return Macaroni()
