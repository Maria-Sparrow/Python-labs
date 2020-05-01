from classes.chemicals_for_clothes import ChemicalsForClothes
from classes.chemicals_for_floor import ChemicalsForFloor
from classes.chemicals_for_washing_up import ChemicalsForWashingUp
from classes.chemicals_for_windows import ChemicalsForWindows
from classes.detergent_type import DetergentType


class HouseholdChemicalsManager:
    def __init__(self, household_chemicals_list=[]):
        self.household_chemicals_list = household_chemicals_list

    def find_by_weight(self, weight_in_grams: int):
        """
        Find by weight in grams
        >>> clothes = ChemicalsForClothes("USA", 230, 890, 23, "powder", DetergentType.GALA, 43)
        >>> floor = ChemicalsForFloor("UK", 346, 900, 12, "liquid", DetergentType.MRPROPPER, "oak")
        >>> windows = ChemicalsForWindows("Canada", 345, 700, 34, "liquid", DetergentType.CLIN, "ammonia")
        >>> washing = ChemicalsForWashingUp("Ukraine", 56, 560, 10, "liquid", DetergentType.FAIRY,"dishwasher")
        >>> print(str(HouseholdChemicalsManager([clothes, floor, washing, windows]).find_by_weight(700))) #doctest: +ELLIPSIS
        [ChemicalsForWindows(...weight_in_grams=700...)]
        """
        return list(filter(lambda chemical: chemical.weight_in_grams == weight_in_grams, self.household_chemicals_list))


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
