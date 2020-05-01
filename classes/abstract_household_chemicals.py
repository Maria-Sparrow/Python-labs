from abc import ABC


class AbstractHouseholdChemicals(ABC):
    def __init__(self, producer=None, price_in_uah=None, weight_in_grams=None, solubility_in_percent=None,
                 type_chemical=None, detergent_type=None):
        self.producer = producer
        self.price_in_uah = price_in_uah
        self.weight_in_grams = weight_in_grams
        self.solubility_in_percent = solubility_in_percent
        self.type_chemical = type_chemical
        self.detergent_type = detergent_type

    def __del__(self):
        return

    def __str__(self):
        producer = "Producer is: {0} \n".format(self.producer)
        price_in_uah = "Price is: {0} \n".format(self.price_in_uah)
        weight_in_grams = "Weight is: {0} \n".format(self.weight_in_grams)
        solubility_in_percent = "Solubility is: {0} \n".format(self.solubility_in_percent)
        type_chemical = "Type is: {0} \n".format(self.type_chemical)
        detergent_type = "Detergent type is: {0} \n".format(self.detergent_type)
        return producer + price_in_uah + weight_in_grams + solubility_in_percent + type_chemical + detergent_type

    def __repr__(self):
        return 'AbstractHouseholdChemicals(producer=' + self.producer + ', price_in_uah=' + str(self.price_in_uah) + \
               ', weight_in_grams=' + str(self.weight_in_grams) + ', solubility_in_percent=' + \
               str(self.solubility_in_percent) + ', type_chemical=' + self.type_chemical + ', detergent_type' + \
               str(self.detergent_type) + ')'
