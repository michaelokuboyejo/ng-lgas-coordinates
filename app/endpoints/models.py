from app.config import mongo_client

__author__ = 'michaelokuboyejo'


class LGA:

    @staticmethod
    def get_lgas():
        """
        Static method to get all LGA's
        :return: List of Dicts of LGA's
        """
        lgas = mongo_client.db.lgas.find()
        lga_list = [{'stateName': lga['state'], 'stateCode': lga['stateCode'], 'lga': lga['lga'], 'latitude': lga['latitude'], 'longitude': lga['longitude']} for lga in lgas]
        return lga_list

    @staticmethod
    def get_lga_with_state_name_or_code(state_name_or_code):
        """
        Method to get
        :param state_name_or_code:
        :return: list of dicts of local governments
        """
        lgas = mongo_client.db.lgas.find({'$or': [{'stateCode': state_name_or_code}, {'state': state_name_or_code}]})
        if lgas.count() == 0:
            return None
        lga_list = [{'stateName': lga['state'], 'stateCode': lga['stateCode'], 'lga': lga['lga'], 'latitude': lga['latitude'], 'longitude': lga['longitude']} for lga in lgas]
        return lga_list
