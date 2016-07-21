#from app.config import dbServerHandShake
from app.config import mongoClient

__author__ = 'michaelokuboyejo'


class LGA:

    @staticmethod
    def get_lgas():
        """
        Static method to get all LGA's
        :return: List of Dicts of LGA's
        """
        lgas = mongoClient.db.lgas.find()
        lga_list = []
        for lga in lgas:
            lga_list.append({
                "stateName": lga['state'],
                "stateCode": lga['stateCode'],
                "lga": lga['lga'],
                "latitude": lga['latitude'],
                "longitude": lga['longitude'],
            })
        return lga_list

    @staticmethod
    def get_lgas_with_state_name_or_code(state_name_or_code):
        """
        Method to get
        :param state_name_or_code:
        :return: list of dicts of local governments
        """
        lgas = mongoClient.db.lgas.find({"$or": [{'stateCode': state_name_or_code}, {'state': state_name_or_code}]})
        lga_list = []
        for lga in lgas:
            lga_list.append({
                "stateName": lga['state'],
                "stateCode": lga['stateCode'],
                "lga": lga['lga'],
                "latitude": lga['latitude'],
                "longitude": lga['longitude'],
            })
        return lga_list
