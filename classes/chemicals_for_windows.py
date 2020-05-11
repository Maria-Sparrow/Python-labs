from chemicals.classes.household_chemicals import HouseholdChemicals


class ChemicalsForWindows(HouseholdChemicals):
    def __init__(self, producer, price_in_uah, weight_in_grams, solubility_in_percent, type_chemical, detergent_type,
                 excipients=None):
        super().__init__(producer, price_in_uah, weight_in_grams, solubility_in_percent, type_chemical, detergent_type)
        self.excipients = excipients

    def __del__(self):
        return

    def __str__(self):
        excipients = " Excipients is: {0} \n".format(self.excipients)
        return super().__str__() + excipients

    def __repr__(self):
        return 'ChemicalsForWindows(producer=' + self.producer + ', price_in_uah=' + str(self.price_in_uah) + \
               ', weight_in_grams=' + str(self.weight_in_grams) + ', solubility_in_percent=' + \
               str(self.solubility_in_percent) + ', type_chemical=' + self.type_chemical + ', detergent_type' + \
               str(self.detergent_type) + ', excipients=' + self.excipients + ')'
