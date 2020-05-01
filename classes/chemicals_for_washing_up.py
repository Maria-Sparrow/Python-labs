from classes.abstract_household_chemicals import AbstractHouseholdChemicals


class ChemicalsForWashingUp(AbstractHouseholdChemicals):
    def __init__(self, producer, price_in_uah, weight_in_grams, solubility_in_percent, type_chemical, detergent_type,
                 additional_use=None):
        super().__init__(producer, price_in_uah, weight_in_grams, solubility_in_percent, type_chemical, detergent_type)
        self.additional_use = additional_use

    def __del__(self):
        return

    def __str__(self):
        additional_use = " Additional use is: {0} \n".format(self.additional_use)
        return super().__str__() + additional_use

    def __repr__(self):
        return 'ChemicalsForWashingUp(producer=' + self.producer + ', price_in_uah=' + str(self.price_in_uah) + \
               ', weight_in_grams=' + str(self.weight_in_grams) + ', solubility_in_percent=' + \
               str(self.solubility_in_percent) + ', type_chemical=' + self.type_chemical + ', detergent_type' + \
               str(self.detergent_type) + ', additional_use=' + self.additional_use + ')'
