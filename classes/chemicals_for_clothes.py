from chemicals.classes.household_chemicals import HouseholdChemicals


class ChemicalsForClothes(HouseholdChemicals):
    def __init__(self, producer, price_in_uah, weight_in_grams, solubility_in_percent, type_chemical, detergent_type,
                 temperature_modes_in_percent=None):
        super().__init__(producer, price_in_uah, weight_in_grams, solubility_in_percent, type_chemical, detergent_type)
        self.temperature_modes_in_percent = temperature_modes_in_percent

    def __del__(self):
        return

    def __str__(self):
        temperature_modes_in_percent = "Temperature is: {0} \n".format(self.temperature_modes_in_percent)
        return super().__str__() + temperature_modes_in_percent

    def __repr__(self):
        return 'ChemicalsForClothes(producer=' + self.producer + ', price_in_uah=' + str(self.price_in_uah) + \
               ', weight_in_grams=' + str(self.weight_in_grams) + ', solubility_in_percent=' + \
               str(self.solubility_in_percent) + ', type_chemical=' + self.type_chemical + ', detergent_type' + \
               str(self.detergent_type) + ', temperature_modes_in_percent=' + str(self.temperature_modes_in_percent) + ')'
