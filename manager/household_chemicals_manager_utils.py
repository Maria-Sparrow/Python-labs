from classes.chemicals_for_clothes import ChemicalsForClothes
from classes.chemicals_for_floor import ChemicalsForFloor
from classes.chemicals_for_washing_up import ChemicalsForWashingUp
from classes.chemicals_for_windows import ChemicalsForWindows
from classes.detergent_type import DetergentType
import doctest


class HouseholdChemicalsManagerUtils:

    def __init__(self):
        pass

    @staticmethod
    def sort_by_price(household_chemicals_list, reverse=False):
        """
        >>> clothes = ChemicalsForClothes("USA", 230, 890, 23, "powder", DetergentType.GALA, 43)
        >>> floor = ChemicalsForFloor("UK", 345, 900, 12, "liquid", DetergentType.MRPROPPER, "oak")
        >>> windows = ChemicalsForWindows("Canada", 346, 700, 34, "liquid", DetergentType.CLIN, "ammonia")
        >>> washing = ChemicalsForWashingUp("Ukraine", 560, 560, 10, "liquid", DetergentType.FAIRY,"dishwasher")
        >>> print(str(HouseholdChemicalsManagerUtils.sort_by_price(([clothes, floor, washing, windows])))) #doctest: +ELLIPSIS
        [ChemicalsForClothes(...price_in_uah=230...), ChemicalsForFloor(...price_in_uah=345...), ChemicalsForWindows(...price_in_uah=346...), ChemicalsForWashingUp(...price_in_uah=560...)]
        """
        return sorted(household_chemicals_list, key=lambda chemical: chemical.price_in_uah, reverse=reverse)

    @staticmethod
    def sort_by_price_dsc(household_chemicals_list, reverse=True):
        """
        >>> clothes = ChemicalsForClothes("USA", 230, 890, 23, "powder", DetergentType.GALA, 43)
        >>> floor = ChemicalsForFloor("UK", 345, 900, 12, "liquid", DetergentType.MRPROPPER, "oak")
        >>> windows = ChemicalsForWindows("Canada", 346, 700, 34, "liquid", DetergentType.CLIN, "ammonia")
        >>> washing = ChemicalsForWashingUp("Ukraine", 560, 560, 10, "liquid", DetergentType.FAIRY,"dishwasher")
        >>> print(str(HouseholdChemicalsManagerUtils.sort_by_price_dsc(([clothes, floor, washing, windows])))) #doctest: +ELLIPSIS
        [ChemicalsForWashingUp(...price_in_uah=560...), ChemicalsForWindows(...price_in_uah=346...), ChemicalsForFloor(...price_in_uah=345...), ChemicalsForClothes(...price_in_uah=230...)]
        """
        return sorted(household_chemicals_list, key=lambda chemical: chemical.price_in_uah, reverse=reverse)

    @staticmethod
    def sort_by_weight(household_chemicals_list, reverse=True):
        """
        >>> clothes = ChemicalsForClothes("USA", 230, 900, 23, "powder", DetergentType.GALA, 43)
        >>> floor = ChemicalsForFloor("UK", 345, 890, 12, "liquid", DetergentType.MRPROPPER, "oak")
        >>> windows = ChemicalsForWindows("Canada", 346, 700, 34, "liquid", DetergentType.CLIN, "ammonia")
        >>> washing = ChemicalsForWashingUp("Ukraine", 560, 560, 10, "liquid", DetergentType.FAIRY,"dishwasher")
        >>> print(str(HouseholdChemicalsManagerUtils.sort_by_weight(([clothes, floor, washing, windows])))) #doctest: +ELLIPSIS
        [ChemicalsForClothes(...weight_in_grams=900...), ChemicalsForFloor(...weight_in_grams=890...), ChemicalsForWindows(...weight_in_grams=700...), ChemicalsForWashingUp(...weight_in_grams=560...)]
        """
        return sorted(household_chemicals_list, key=lambda chemical: chemical.weight_in_grams, reverse=reverse)

    @staticmethod
    def sort_by_weight(household_chemicals_list, reverse=False):
        """
        >>> clothes = ChemicalsForClothes("USA", 230, 900, 23, "powder", DetergentType.GALA, 43)
        >>> floor = ChemicalsForFloor("UK", 345, 890, 12, "liquid", DetergentType.MRPROPPER, "oak")
        >>> windows = ChemicalsForWindows("Canada", 346, 700, 34, "liquid", DetergentType.CLIN, "ammonia")
        >>> washing = ChemicalsForWashingUp("Ukraine", 560, 560, 10, "liquid", DetergentType.FAIRY,"dishwasher")
        >>> print(str(HouseholdChemicalsManagerUtils.sort_by_weight(([clothes, floor, washing, windows])))) #doctest: +ELLIPSIS
        [ChemicalsForWashingUp(...weight_in_grams=560...), ChemicalsForWindows(...weight_in_grams=700...), ChemicalsForFloor(...weight_in_grams=890...), ChemicalsForClothes(...weight_in_grams=900...)]
        """
        return sorted(household_chemicals_list, key=lambda chemical: chemical.weight_in_grams, reverse=reverse)


if __name__ == "__main__":

    doctest.testmod(verbose=True)
