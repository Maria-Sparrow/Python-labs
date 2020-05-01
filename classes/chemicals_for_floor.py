from classes.abstract_household_chemicals import AbstractHouseholdChemicals


class ChemicalsForFloor(AbstractHouseholdChemicals):
    def __init__(self, producer, price_in_uah, weight_in_grams, solubility_in_percent, type_chemical, detergent_type,
                 type_of_floor=None):
        super().__init__(producer, price_in_uah, weight_in_grams, solubility_in_percent, type_chemical, detergent_type)
        self.type_of_floor = type_of_floor

    def __del__(self):
        return

    def __str__(self):
        type_of_floor = " Type of floor is: {0} \n".format(self.type_of_floor)
        return super().__str__() + type_of_floor

    def __repr__(self):
        return 'ChemicalsForFloor(producer=' + self.producer + ', price_in_uah=' + str(self.price_in_uah) + \
               ', weight_in_grams=' + str(self.weight_in_grams) + ', solubility_in_percent=' + \
               str(self.solubility_in_percent) + ', type_chemical=' + self.type_chemical + ', detergent_type' + \
               str(self.detergent_type) + ', type_of_floor=' + self.type_of_floor + ')'
