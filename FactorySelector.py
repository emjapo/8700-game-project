from HalloweenFactory import HalloweenFactory
from ThanksgivingFactory import ThanksgivingFactory
from ChristmasFactory import ChristmasFactory
from HolidayType import HolidayType

class FactorySelector:
    # Step 5: Abstract Factory Selector
    @staticmethod
    def get_factory(factory_type):
        if factory_type == HolidayType.HALLOWEEN:
            return HalloweenFactory()
        elif factory_type == HolidayType.THANKSGIVING:
            return ThanksgivingFactory()
        elif factory_type == HolidayType.CHRISTMAS:
            return ChristmasFactory()
        else:
            raise ValueError("Unknown factory type")
