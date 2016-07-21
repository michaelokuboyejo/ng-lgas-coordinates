from app.config import mongoClient

__author__ = 'michaelokuboyejo'
# from pymongo import MongoClient
"""
Little Script to Update DB with LGA information
"""

#mongoClient = MongoClient('mongodb://ng_lga_coordinates:ng_lga_coordinates@ds011705.mlab.com:11705/ng_lga_coordinates')
db = mongoClient.ng_lga_coordinates

lga_list = [
  {
    "stateCode": "AB",
    "state": "Abia",
    "lga": "Ikwuano",
    "latitude": 5.4308921,
    "longitude": 7.5247243
  },
  {
    "stateCode": "AB",
    "state": "Abia",
    "lga": "Isiala Ngwa North",
    "latitude": 5.4308921,
    "longitude": 7.5247243
  },
  {
    "stateCode": "AB",
    "state": "Abia",
    "lga": "Isiala Ngwa South",
    "latitude": 5.4308921,
    "longitude": 7.5247243
  },
  {
    "stateCode": "AB",
    "state": "Abia",
    "lga": "Isuikwuato",
    "latitude": 5.4308921,
    "longitude": 7.5247243
  },
  {
    "stateCode": "AB",
    "state": "Abia",
    "lga": "Obingwa",
    "latitude": 5.4308921,
    "longitude": 7.5247243
  },
  {
    "stateCode": "AB",
    "state": "Abia",
    "lga": "Ohafia",
    "latitude": 5.4308921,
    "longitude": 7.5247243
  },
  {
    "stateCode": "AB",
    "state": "Abia",
    "lga": "Osisioma",
    "latitude": 5.4308921,
    "longitude": 7.5247243
  },
  {
    "stateCode": "AB",
    "state": "Abia",
    "lga": "Ugwunagbo",
    "latitude": 5.4308921,
    "longitude": 7.5247243
  },
  {
    "stateCode": "AB",
    "state": "Abia",
    "lga": "Ukwa East",
    "latitude": 5.4308921,
    "longitude": 7.5247243
  },
  {
    "stateCode": "AB",
    "state": "Abia",
    "lga": "Ukwa  West",
    "latitude": 5.4308921,
    "longitude": 7.5247243
  },
  {
    "stateCode": "AB",
    "state": "Abia",
    "lga": "Umuahia North",
    "latitude": 5.4308921,
    "longitude": 7.5247243
  },
  {
    "stateCode": "AB",
    "state": "Abia",
    "lga": "Umuahia  South",
    "latitude": 5.4308921,
    "longitude": 7.5247243
  },
  {
    "stateCode": "AB",
    "state": "Abia",
    "lga": "Umu - Nneochi",
    "latitude": 5.4308921,
    "longitude": 7.5247243
  },
  {
    "stateCode": "AD",
    "state": "Adamawa",
    "lga": "Demsa",
    "latitude": 9.3250497,
    "longitude": 12.4380581
  },
  {
    "stateCode": "AD",
    "state": "Adamawa",
    "lga": "Fufore",
    "latitude": 9.3250497,
    "longitude": 12.4380581
  },
  {
    "stateCode": "AD",
    "state": "Adamawa",
    "lga": "Ganye",
    "latitude": 9.3250497,
    "longitude": 12.4380581
  },
  {
    "stateCode": "AD",
    "state": "Adamawa",
    "lga": "Gire 1",
    "latitude": 9.3250497,
    "longitude": 12.4380581
  },
  {
    "stateCode": "AD",
    "state": "Adamawa",
    "lga": "Gombi",
    "latitude": 9.3250497,
    "longitude": 12.4380581
  },
  {
    "stateCode": "AD",
    "state": "Adamawa",
    "lga": "Guyuk",
    "latitude": 9.3250497,
    "longitude": 12.4380581
  },
  {
    "stateCode": "AD",
    "state": "Adamawa",
    "lga": "Hong",
    "latitude": 9.3250497,
    "longitude": 12.4380581
  },
  {
    "stateCode": "AD",
    "state": "Adamawa",
    "lga": "Jada",
    "latitude": 9.3250497,
    "longitude": 12.4380581
  },
  {
    "stateCode": "AD",
    "state": "Adamawa",
    "lga": "Lamurde",
    "latitude": 9.3250497,
    "longitude": 12.4380581
  },
  {
    "stateCode": "AD",
    "state": "Adamawa",
    "lga": "Madagali",
    "latitude": 9.3250497,
    "longitude": 12.4380581
  },
  {
    "stateCode": "AD",
    "state": "Adamawa",
    "lga": "Maiha",
    "latitude": 9.3250497,
    "longitude": 12.4380581
  },
  {
    "stateCode": "AD",
    "state": "Adamawa",
    "lga": "Mayo - Belwa",
    "latitude": 9.3250497,
    "longitude": 12.4380581
  },
  {
    "stateCode": "AD",
    "state": "Adamawa",
    "lga": "Michika",
    "latitude": 9.3250497,
    "longitude": 12.4380581
  },
  {
    "stateCode": "AD",
    "state": "Adamawa",
    "lga": "Mubi North",
    "latitude": 9.3250497,
    "longitude": 12.4380581
  },
  {
    "stateCode": "AD",
    "state": "Adamawa",
    "lga": "Mubi South",
    "latitude": 9.3250497,
    "longitude": 12.4380581
  },
  {
    "stateCode": "AD",
    "state": "Adamawa",
    "lga": "Numan",
    "latitude": 9.3250497,
    "longitude": 12.4380581
  },
  {
    "stateCode": "AD",
    "state": "Adamawa",
    "lga": "Shelleng",
    "latitude": 9.3250497,
    "longitude": 12.4380581
  },
  {
    "stateCode": "AD",
    "state": "Adamawa",
    "lga": "Song",
    "latitude": 9.3250497,
    "longitude": 12.4380581
  },
  {
    "stateCode": "AD",
    "state": "Adamawa",
    "lga": "Toungo",
    "latitude": 9.3250497,
    "longitude": 12.4380581
  },
  {
    "stateCode": "AD",
    "state": "Adamawa",
    "lga": "Yola North",
    "latitude": 9.3250497,
    "longitude": 12.4380581
  },
  {
    "stateCode": "AD",
    "state": "Adamawa",
    "lga": "Yola South",
    "latitude": 9.3250497,
    "longitude": 12.4380581
  },
  {
    "stateCode": "AK",
    "state": "Akwa Ibom",
    "lga": "Abak",
    "latitude": 4.9299869,
    "longitude": 7.87216
  },
  {
    "stateCode": "AK",
    "state": "Akwa Ibom",
    "lga": "Eastern Obolo",
    "latitude": 4.9299869,
    "longitude": 7.87216
  },
  {
    "stateCode": "AK",
    "state": "Akwa Ibom",
    "lga": "Eket",
    "latitude": 4.9299869,
    "longitude": 7.87216
  },
  {
    "stateCode": "AK",
    "state": "Akwa Ibom",
    "lga": "Esit Eket (uquo)",
    "latitude": 4.9299869,
    "longitude": 7.87216
  },
  {
    "stateCode": "AK",
    "state": "Akwa Ibom",
    "lga": "Essien Udim",
    "latitude": 4.9299869,
    "longitude": 7.87216
  },
  {
    "stateCode": "AK",
    "state": "Akwa Ibom",
    "lga": "Etim Ekpo",
    "latitude": 4.9299869,
    "longitude": 7.87216
  },
  {
    "stateCode": "AK",
    "state": "Akwa Ibom",
    "lga": "Etinan",
    "latitude": 4.9299869,
    "longitude": 7.87216
  },
  {
    "stateCode": "AK",
    "state": "Akwa Ibom",
    "lga": "Ibeno",
    "latitude": 4.9299869,
    "longitude": 7.87216
  },
  {
    "stateCode": "AK",
    "state": "Akwa Ibom",
    "lga": "Ibesikpo Asutan",
    "latitude": 4.9299869,
    "longitude": 7.87216
  },
  {
    "stateCode": "AK",
    "state": "Akwa Ibom",
    "lga": "Ibiono Ibom",
    "latitude": 4.9299869,
    "longitude": 7.87216
  },
  {
    "stateCode": "AK",
    "state": "Akwa Ibom",
    "lga": "Ika",
    "latitude": 4.9299869,
    "longitude": 7.87216
  },
  {
    "stateCode": "AK",
    "state": "Akwa Ibom",
    "lga": "Ikono",
    "latitude": 4.9299869,
    "longitude": 7.87216
  },
  {
    "stateCode": "AK",
    "state": "Akwa Ibom",
    "lga": "Ikot Abasi",
    "latitude": 4.9299869,
    "longitude": 7.87216
  },
  {
    "stateCode": "AK",
    "state": "Akwa Ibom",
    "lga": "Ikot Ekpene",
    "latitude": 4.9299869,
    "longitude": 7.87216
  },
  {
    "stateCode": "AK",
    "state": "Akwa Ibom",
    "lga": "Ini",
    "latitude": 4.9299869,
    "longitude": 7.87216
  },
  {
    "stateCode": "AK",
    "state": "Akwa Ibom",
    "lga": "Itu",
    "latitude": 4.9299869,
    "longitude": 7.87216
  },
  {
    "stateCode": "AK",
    "state": "Akwa Ibom",
    "lga": "Mbo",
    "latitude": 4.9299869,
    "longitude": 7.87216
  },
  {
    "stateCode": "AK",
    "state": "Akwa Ibom",
    "lga": "Mkpat Enin",
    "latitude": 4.9299869,
    "longitude": 7.87216
  },
  {
    "stateCode": "AK",
    "state": "Akwa Ibom",
    "lga": "Nsit Atai",
    "latitude": 4.9299869,
    "longitude": 7.87216
  },
  {
    "stateCode": "AK",
    "state": "Akwa Ibom",
    "lga": "Nsit Ibom",
    "latitude": 4.9299869,
    "longitude": 7.87216
  },
  {
    "stateCode": "AK",
    "state": "Akwa Ibom",
    "lga": "Nsit Ubium",
    "latitude": 4.9299869,
    "longitude": 7.87216
  },
  {
    "stateCode": "AK",
    "state": "Akwa Ibom",
    "lga": "Obot Akara",
    "latitude": 4.9299869,
    "longitude": 7.87216
  },
  {
    "stateCode": "AK",
    "state": "Akwa Ibom",
    "lga": "Okobo",
    "latitude": 4.9299869,
    "longitude": 7.87216
  },
  {
    "stateCode": "AK",
    "state": "Akwa Ibom",
    "lga": "Onna",
    "latitude": 4.9299869,
    "longitude": 7.87216
  },
  {
    "stateCode": "AK",
    "state": "Akwa Ibom",
    "lga": "Oron",
    "latitude": 4.9299869,
    "longitude": 7.87216
  },
  {
    "stateCode": "AK",
    "state": "Akwa Ibom",
    "lga": "Oruk Anam",
    "latitude": 4.9299869,
    "longitude": 7.87216
  },
  {
    "stateCode": "AK",
    "state": "Akwa Ibom",
    "lga": "Udung Uko",
    "latitude": 4.9299869,
    "longitude": 7.87216
  },
  {
    "stateCode": "AK",
    "state": "Akwa Ibom",
    "lga": "Ukanafun",
    "latitude": 4.9299869,
    "longitude": 7.87216
  },
  {
    "stateCode": "AK",
    "state": "Akwa Ibom",
    "lga": "Uruan",
    "latitude": 4.9299869,
    "longitude": 7.87216
  },
  {
    "stateCode": "AK",
    "state": "Akwa Ibom",
    "lga": "Urue Offong/oruko",
    "latitude": 4.9299869,
    "longitude": 7.87216
  },
  {
    "stateCode": "AK",
    "state": "Akwa Ibom",
    "lga": "Uyo",
    "latitude": 4.9299869,
    "longitude": 7.87216
  },
  {
    "stateCode": "AN",
    "state": "Anambra",
    "lga": "Aguata",
    "latitude": 6.2757656,
    "longitude": 7.0068393
  },
  {
    "stateCode": "AN",
    "state": "Anambra",
    "lga": "Ayamelum",
    "latitude": 6.2757656,
    "longitude": 7.0068393
  },
  {
    "stateCode": "AN",
    "state": "Anambra",
    "lga": "Anambra East",
    "latitude": 6.2757656,
    "longitude": 7.0068393
  },
  {
    "stateCode": "AN",
    "state": "Anambra",
    "lga": "Anambra West",
    "latitude": 6.2757656,
    "longitude": 7.0068393
  },
  {
    "stateCode": "AN",
    "state": "Anambra",
    "lga": "Anaocha",
    "latitude": 6.2757656,
    "longitude": 7.0068393
  },
  {
    "stateCode": "AN",
    "state": "Anambra",
    "lga": "Awka North",
    "latitude": 6.2757656,
    "longitude": 7.0068393
  },
  {
    "stateCode": "AN",
    "state": "Anambra",
    "lga": "Awka South",
    "latitude": 6.2757656,
    "longitude": 7.0068393
  },
  {
    "stateCode": "AN",
    "state": "Anambra",
    "lga": "Dunukofia",
    "latitude": 6.2757656,
    "longitude": 7.0068393
  },
  {
    "stateCode": "AN",
    "state": "Anambra",
    "lga": "Ekwusigo",
    "latitude": 6.2757656,
    "longitude": 7.0068393
  },
  {
    "stateCode": "AN",
    "state": "Anambra",
    "lga": "Idemili North",
    "latitude": 6.2757656,
    "longitude": 7.0068393
  },
  {
    "stateCode": "AN",
    "state": "Anambra",
    "lga": "Idemili-south",
    "latitude": 6.2757656,
    "longitude": 7.0068393
  },
  {
    "stateCode": "AN",
    "state": "Anambra",
    "lga": "Ihala",
    "latitude": 6.2757656,
    "longitude": 7.0068393
  },
  {
    "stateCode": "AN",
    "state": "Anambra",
    "lga": "Njikoka",
    "latitude": 6.2757656,
    "longitude": 7.0068393
  },
  {
    "stateCode": "AN",
    "state": "Anambra",
    "lga": "Nnewi North",
    "latitude": 6.2757656,
    "longitude": 7.0068393
  },
  {
    "stateCode": "AN",
    "state": "Anambra",
    "lga": "Nnewi South",
    "latitude": 6.2757656,
    "longitude": 7.0068393
  },
  {
    "stateCode": "AN",
    "state": "Anambra",
    "lga": "Ogbaru",
    "latitude": 6.2757656,
    "longitude": 7.0068393
  },
  {
    "stateCode": "AN",
    "state": "Anambra",
    "lga": "Onitsha-north",
    "latitude": 6.2757656,
    "longitude": 7.0068393
  },
  {
    "stateCode": "AN",
    "state": "Anambra",
    "lga": "Onitsha -south",
    "latitude": 6.2757656,
    "longitude": 7.0068393
  },
  {
    "stateCode": "AN",
    "state": "Anambra",
    "lga": "Orumba North",
    "latitude": 6.2757656,
    "longitude": 7.0068393
  },
  {
    "stateCode": "AN",
    "state": "Anambra",
    "lga": "Orumba  South",
    "latitude": 6.2757656,
    "longitude": 7.0068393
  },
  {
    "stateCode": "AN",
    "state": "Anambra",
    "lga": "Oyi",
    "latitude": 6.2757656,
    "longitude": 7.0068393
  },
  {
    "stateCode": "BA",
    "state": "Bauchi",
    "lga": "Alkaleri",
    "latitude": 10.30982,
    "longitude": 9.845172
  },
  {
    "stateCode": "BA",
    "state": "Bauchi",
    "lga": "Bauchi",
    "latitude": 10.30982,
    "longitude": 9.845172
  },
  {
    "stateCode": "BA",
    "state": "Bauchi",
    "lga": "Bogoro",
    "latitude": 10.30982,
    "longitude": 9.845172
  },
  {
    "stateCode": "BA",
    "state": "Bauchi",
    "lga": "Dambam",
    "latitude": 10.30982,
    "longitude": 9.845172
  },
  {
    "stateCode": "BA",
    "state": "Bauchi",
    "lga": "Darazo",
    "latitude": 10.30982,
    "longitude": 9.845172
  },
  {
    "stateCode": "BA",
    "state": "Bauchi",
    "lga": "Dass",
    "latitude": 10.30982,
    "longitude": 9.845172
  },
  {
    "stateCode": "BA",
    "state": "Bauchi",
    "lga": "Gamawa",
    "latitude": 10.30982,
    "longitude": 9.845172
  },
  {
    "stateCode": "BA",
    "state": "Bauchi",
    "lga": "Ganjuwa",
    "latitude": 10.30982,
    "longitude": 9.845172
  },
  {
    "stateCode": "BA",
    "state": "Bauchi",
    "lga": "Giade",
    "latitude": 10.30982,
    "longitude": 9.845172
  },
  {
    "stateCode": "BA",
    "state": "Bauchi",
    "lga": "Itas/gadau",
    "latitude": 10.30982,
    "longitude": 9.845172
  },
  {
    "stateCode": "BA",
    "state": "Bauchi",
    "lga": "JAMA'ARE",
    "latitude": 10.30982,
    "longitude": 9.845172
  },
  {
    "stateCode": "BA",
    "state": "Bauchi",
    "lga": "Katagum",
    "latitude": 10.30982,
    "longitude": 9.845172
  },
  {
    "stateCode": "BA",
    "state": "Bauchi",
    "lga": "Kirfi",
    "latitude": 10.30982,
    "longitude": 9.845172
  },
  {
    "stateCode": "BA",
    "state": "Bauchi",
    "lga": "Misau",
    "latitude": 10.30982,
    "longitude": 9.845172
  },
  {
    "stateCode": "BA",
    "state": "Bauchi",
    "lga": "Ningi",
    "latitude": 10.30982,
    "longitude": 9.845172
  },
  {
    "stateCode": "BA",
    "state": "Bauchi",
    "lga": "Shira",
    "latitude": 10.30982,
    "longitude": 9.845172
  },
  {
    "stateCode": "BA",
    "state": "Bauchi",
    "lga": "Tafawa Balewa",
    "latitude": 10.30982,
    "longitude": 9.845172
  },
  {
    "stateCode": "BA",
    "state": "Bauchi",
    "lga": "Toro",
    "latitude": 10.30982,
    "longitude": 9.845172
  },
  {
    "stateCode": "BA",
    "state": "Bauchi",
    "lga": "Warji",
    "latitude": 10.30982,
    "longitude": 9.845172
  },
  {
    "stateCode": "BA",
    "state": "Bauchi",
    "lga": "Zaki",
    "latitude": 10.30982,
    "longitude": 9.845172
  },
  {
    "stateCode": "BY",
    "state": "Bayelsa",
    "lga": "Brass",
    "latitude": 4.8677767,
    "longitude": 5.8987139
  },
  {
    "stateCode": "BY",
    "state": "Bayelsa",
    "lga": "Ekeremor",
    "latitude": 4.8677767,
    "longitude": 5.8987139
  },
  {
    "stateCode": "BY",
    "state": "Bayelsa",
    "lga": "Kolokuma/opokuma",
    "latitude": 4.8677767,
    "longitude": 5.8987139
  },
  {
    "stateCode": "BY",
    "state": "Bayelsa",
    "lga": "Nembe",
    "latitude": 4.8677767,
    "longitude": 5.8987139
  },
  {
    "stateCode": "BY",
    "state": "Bayelsa",
    "lga": "Ogbia",
    "latitude": 4.8677767,
    "longitude": 5.8987139
  },
  {
    "stateCode": "BY",
    "state": "Bayelsa",
    "lga": "Sagbama",
    "latitude": 4.8677767,
    "longitude": 5.8987139
  },
  {
    "stateCode": "BY",
    "state": "Bayelsa",
    "lga": "Southern Ijaw",
    "latitude": 4.8677767,
    "longitude": 5.8987139
  },
  {
    "stateCode": "BY",
    "state": "Bayelsa",
    "lga": "Yenagoa",
    "latitude": 4.8677767,
    "longitude": 5.8987139
  },
  {
    "stateCode": "BN",
    "state": "Benue",
    "lga": "Ado",
    "latitude": 7.3508259,
    "longitude": 8.8362755
  },
  {
    "stateCode": "BN",
    "state": "Benue",
    "lga": "Agatu",
    "latitude": 7.3508259,
    "longitude": 8.8362755
  },
  {
    "stateCode": "BN",
    "state": "Benue",
    "lga": "Apa",
    "latitude": 7.3508259,
    "longitude": 8.8362755
  },
  {
    "stateCode": "BN",
    "state": "Benue",
    "lga": "Buruku",
    "latitude": 7.3508259,
    "longitude": 8.8362755
  },
  {
    "stateCode": "BN",
    "state": "Benue",
    "lga": "Gboko",
    "latitude": 7.3508259,
    "longitude": 8.8362755
  },
  {
    "stateCode": "BN",
    "state": "Benue",
    "lga": "Guma",
    "latitude": 7.3508259,
    "longitude": 8.8362755
  },
  {
    "stateCode": "BN",
    "state": "Benue",
    "lga": "Gwer East",
    "latitude": 7.3508259,
    "longitude": 8.8362755
  },
  {
    "stateCode": "BN",
    "state": "Benue",
    "lga": "Gwer West",
    "latitude": 7.3508259,
    "longitude": 8.8362755
  },
  {
    "stateCode": "BN",
    "state": "Benue",
    "lga": "Katsina-ala",
    "latitude": 7.3508259,
    "longitude": 8.8362755
  },
  {
    "stateCode": "BN",
    "state": "Benue",
    "lga": "Konshisha",
    "latitude": 7.3508259,
    "longitude": 8.8362755
  },
  {
    "stateCode": "BN",
    "state": "Benue",
    "lga": "Kwande",
    "latitude": 7.3508259,
    "longitude": 8.8362755
  },
  {
    "stateCode": "BN",
    "state": "Benue",
    "lga": "Logo",
    "latitude": 7.3508259,
    "longitude": 8.8362755
  },
  {
    "stateCode": "BN",
    "state": "Benue",
    "lga": "Makurdi",
    "latitude": 7.3508259,
    "longitude": 8.8362755
  },
  {
    "stateCode": "BN",
    "state": "Benue",
    "lga": "Obi",
    "latitude": 7.3508259,
    "longitude": 8.8362755
  },
  {
    "stateCode": "BN",
    "state": "Benue",
    "lga": "Ogbadibo",
    "latitude": 7.3508259,
    "longitude": 8.8362755
  },
  {
    "stateCode": "BN",
    "state": "Benue",
    "lga": "Oju",
    "latitude": 7.3508259,
    "longitude": 8.8362755
  },
  {
    "stateCode": "BN",
    "state": "Benue",
    "lga": "Ohimini",
    "latitude": 7.3508259,
    "longitude": 8.8362755
  },
  {
    "stateCode": "BN",
    "state": "Benue",
    "lga": "Okpokwu",
    "latitude": 7.3508259,
    "longitude": 8.8362755
  },
  {
    "stateCode": "BN",
    "state": "Benue",
    "lga": "Otukpo",
    "latitude": 7.3508259,
    "longitude": 8.8362755
  },
  {
    "stateCode": "BN",
    "state": "Benue",
    "lga": "Tarka",
    "latitude": 7.3508259,
    "longitude": 8.8362755
  },
  {
    "stateCode": "BN",
    "state": "Benue",
    "lga": "Ukum",
    "latitude": 7.3508259,
    "longitude": 8.8362755
  },
  {
    "stateCode": "BN",
    "state": "Benue",
    "lga": "Ushongo",
    "latitude": 7.3508259,
    "longitude": 8.8362755
  },
  {
    "stateCode": "BN",
    "state": "Benue",
    "lga": "Vandeikya",
    "latitude": 7.3508259,
    "longitude": 8.8362755
  },
  {
    "stateCode": "BO",
    "state": "Borno",
    "lga": "Abadam",
    "latitude": 12.1205201,
    "longitude": 13.1740348
  },
  {
    "stateCode": "BO",
    "state": "Borno",
    "lga": "Askira / Uba",
    "latitude": 12.1205201,
    "longitude": 13.1740348
  },
  {
    "stateCode": "BO",
    "state": "Borno",
    "lga": "Bama",
    "latitude": 12.1205201,
    "longitude": 13.1740348
  },
  {
    "stateCode": "BO",
    "state": "Borno",
    "lga": "Bayo",
    "latitude": 12.1205201,
    "longitude": 13.1740348
  },
  {
    "stateCode": "BO",
    "state": "Borno",
    "lga": "Biu",
    "latitude": 12.1205201,
    "longitude": 13.1740348
  },
  {
    "stateCode": "BO",
    "state": "Borno",
    "lga": "Chibok",
    "latitude": 12.1205201,
    "longitude": 13.1740348
  },
  {
    "stateCode": "BO",
    "state": "Borno",
    "lga": "Damboa",
    "latitude": 12.1205201,
    "longitude": 13.1740348
  },
  {
    "stateCode": "BO",
    "state": "Borno",
    "lga": "Dikwa",
    "latitude": 12.1205201,
    "longitude": 13.1740348
  },
  {
    "stateCode": "BO",
    "state": "Borno",
    "lga": "Gubio",
    "latitude": 12.1205201,
    "longitude": 13.1740348
  },
  {
    "stateCode": "BO",
    "state": "Borno",
    "lga": "Guzamala",
    "latitude": 12.1205201,
    "longitude": 13.1740348
  },
  {
    "stateCode": "BO",
    "state": "Borno",
    "lga": "Gwoza",
    "latitude": 12.1205201,
    "longitude": 13.1740348
  },
  {
    "stateCode": "BO",
    "state": "Borno",
    "lga": "Hawul",
    "latitude": 12.1205201,
    "longitude": 13.1740348
  },
  {
    "stateCode": "BO",
    "state": "Borno",
    "lga": "Jere",
    "latitude": 12.1205201,
    "longitude": 13.1740348
  },
  {
    "stateCode": "BO",
    "state": "Borno",
    "lga": "Kaga",
    "latitude": 12.1205201,
    "longitude": 13.1740348
  },
  {
    "stateCode": "BO",
    "state": "Borno",
    "lga": "Kala Balge",
    "latitude": 12.1205201,
    "longitude": 13.1740348
  },
  {
    "stateCode": "BO",
    "state": "Borno",
    "lga": "Konduga",
    "latitude": 12.1205201,
    "longitude": 13.1740348
  },
  {
    "stateCode": "BO",
    "state": "Borno",
    "lga": "Kukawa",
    "latitude": 12.1205201,
    "longitude": 13.1740348
  },
  {
    "stateCode": "BO",
    "state": "Borno",
    "lga": "Kwaya / Kusar",
    "latitude": 12.1205201,
    "longitude": 13.1740348
  },
  {
    "stateCode": "BO",
    "state": "Borno",
    "lga": "Mafa",
    "latitude": 12.1205201,
    "longitude": 13.1740348
  },
  {
    "stateCode": "BO",
    "state": "Borno",
    "lga": "Magumeri",
    "latitude": 12.1205201,
    "longitude": 13.1740348
  },
  {
    "stateCode": "BO",
    "state": "Borno",
    "lga": "Maiduguri M. C.",
    "latitude": 12.1205201,
    "longitude": 13.1740348
  },
  {
    "stateCode": "BO",
    "state": "Borno",
    "lga": "Marte",
    "latitude": 12.1205201,
    "longitude": 13.1740348
  },
  {
    "stateCode": "BO",
    "state": "Borno",
    "lga": "Mobbar",
    "latitude": 12.1205201,
    "longitude": 13.1740348
  },
  {
    "stateCode": "BO",
    "state": "Borno",
    "lga": "Monguno",
    "latitude": 12.1205201,
    "longitude": 13.1740348
  },
  {
    "stateCode": "BO",
    "state": "Borno",
    "lga": "Ngala",
    "latitude": 12.1205201,
    "longitude": 13.1740348
  },
  {
    "stateCode": "BO",
    "state": "Borno",
    "lga": "Nganzai",
    "latitude": 12.1205201,
    "longitude": 13.1740348
  },
  {
    "stateCode": "BO",
    "state": "Borno",
    "lga": "Shani",
    "latitude": 12.1205201,
    "longitude": 13.1740348
  },
  {
    "stateCode": "CR",
    "state": "Cross River",
    "lga": "Abi",
    "latitude": 5.5805318,
    "longitude": 8.7481167
  },
  {
    "stateCode": "CR",
    "state": "Cross River",
    "lga": "Akamkpa",
    "latitude": 5.5805318,
    "longitude": 8.7481167
  },
  {
    "stateCode": "CR",
    "state": "Cross River",
    "lga": "Akpabuyo",
    "latitude": 5.5805318,
    "longitude": 8.7481167
  },
  {
    "stateCode": "CR",
    "state": "Cross River",
    "lga": "Bakassi",
    "latitude": 5.5805318,
    "longitude": 8.7481167
  },
  {
    "stateCode": "CR",
    "state": "Cross River",
    "lga": "Bekwarra",
    "latitude": 5.5805318,
    "longitude": 8.7481167
  },
  {
    "stateCode": "CR",
    "state": "Cross River",
    "lga": "Biase",
    "latitude": 5.5805318,
    "longitude": 8.7481167
  },
  {
    "stateCode": "CR",
    "state": "Cross River",
    "lga": "Boki",
    "latitude": 5.5805318,
    "longitude": 8.7481167
  },
  {
    "stateCode": "CR",
    "state": "Cross River",
    "lga": "Calabar Municipality",
    "latitude": 5.5805318,
    "longitude": 8.7481167
  },
  {
    "stateCode": "CR",
    "state": "Cross River",
    "lga": "Calabar South",
    "latitude": 5.5805318,
    "longitude": 8.7481167
  },
  {
    "stateCode": "CR",
    "state": "Cross River",
    "lga": "Etung",
    "latitude": 5.5805318,
    "longitude": 8.7481167
  },
  {
    "stateCode": "CR",
    "state": "Cross River",
    "lga": "Ikom",
    "latitude": 5.5805318,
    "longitude": 8.7481167
  },
  {
    "stateCode": "CR",
    "state": "Cross River",
    "lga": "Obanliku",
    "latitude": 5.5805318,
    "longitude": 8.7481167
  },
  {
    "stateCode": "CR",
    "state": "Cross River",
    "lga": "Obubra",
    "latitude": 5.5805318,
    "longitude": 8.7481167
  },
  {
    "stateCode": "CR",
    "state": "Cross River",
    "lga": "Obudu",
    "latitude": 5.5805318,
    "longitude": 8.7481167
  },
  {
    "stateCode": "CR",
    "state": "Cross River",
    "lga": "Odukpani",
    "latitude": 5.5805318,
    "longitude": 8.7481167
  },
  {
    "stateCode": "CR",
    "state": "Cross River",
    "lga": "Ogoja",
    "latitude": 5.5805318,
    "longitude": 8.7481167
  },
  {
    "stateCode": "CR",
    "state": "Cross River",
    "lga": "Yakurr",
    "latitude": 5.5805318,
    "longitude": 8.7481167
  },
  {
    "stateCode": "CR",
    "state": "Cross River",
    "lga": "Yala",
    "latitude": 5.5805318,
    "longitude": 8.7481167
  },
  {
    "stateCode": "DT",
    "state": "Delta",
    "lga": "Aniocha North",
    "latitude": 5.5324624,
    "longitude": 5.8987139
  },
  {
    "stateCode": "DT",
    "state": "Delta",
    "lga": "Aniocha - South",
    "latitude": 5.5324624,
    "longitude": 5.8987139
  },
  {
    "stateCode": "DT",
    "state": "Delta",
    "lga": "Bomadi",
    "latitude": 5.5324624,
    "longitude": 5.8987139
  },
  {
    "stateCode": "DT",
    "state": "Delta",
    "lga": "Burutu",
    "latitude": 5.5324624,
    "longitude": 5.8987139
  },
  {
    "stateCode": "DT",
    "state": "Delta",
    "lga": "Ethiope  East",
    "latitude": 5.5324624,
    "longitude": 5.8987139
  },
  {
    "stateCode": "DT",
    "state": "Delta",
    "lga": "Ethiope  West",
    "latitude": 5.5324624,
    "longitude": 5.8987139
  },
  {
    "stateCode": "DT",
    "state": "Delta",
    "lga": "Ika North- East",
    "latitude": 5.5324624,
    "longitude": 5.8987139
  },
  {
    "stateCode": "DT",
    "state": "Delta",
    "lga": "Ika - South",
    "latitude": 5.5324624,
    "longitude": 5.8987139
  },
  {
    "stateCode": "DT",
    "state": "Delta",
    "lga": "Isoko North",
    "latitude": 5.5324624,
    "longitude": 5.8987139
  },
  {
    "stateCode": "DT",
    "state": "Delta",
    "lga": "Isoko South",
    "latitude": 5.5324624,
    "longitude": 5.8987139
  },
  {
    "stateCode": "DT",
    "state": "Delta",
    "lga": "Ndokwa East",
    "latitude": 5.5324624,
    "longitude": 5.8987139
  },
  {
    "stateCode": "DT",
    "state": "Delta",
    "lga": "Ndokwa West",
    "latitude": 5.5324624,
    "longitude": 5.8987139
  },
  {
    "stateCode": "DT",
    "state": "Delta",
    "lga": "Okpe",
    "latitude": 5.5324624,
    "longitude": 5.8987139
  },
  {
    "stateCode": "DT",
    "state": "Delta",
    "lga": "Oshimili - North",
    "latitude": 5.5324624,
    "longitude": 5.8987139
  },
  {
    "stateCode": "DT",
    "state": "Delta",
    "lga": "Oshimili - South",
    "latitude": 5.5324624,
    "longitude": 5.8987139
  },
  {
    "stateCode": "DT",
    "state": "Delta",
    "lga": "Patani",
    "latitude": 5.5324624,
    "longitude": 5.8987139
  },
  {
    "stateCode": "DT",
    "state": "Delta",
    "lga": "Sapele",
    "latitude": 5.5324624,
    "longitude": 5.8987139
  },
  {
    "stateCode": "DT",
    "state": "Delta",
    "lga": "Udu",
    "latitude": 5.5324624,
    "longitude": 5.8987139
  },
  {
    "stateCode": "DT",
    "state": "Delta",
    "lga": "Ughelli North",
    "latitude": 5.5324624,
    "longitude": 5.8987139
  },
  {
    "stateCode": "DT",
    "state": "Delta",
    "lga": "Ughelli South",
    "latitude": 5.5324624,
    "longitude": 5.8987139
  },
  {
    "stateCode": "DT",
    "state": "Delta",
    "lga": "Ukwuani",
    "latitude": 5.5324624,
    "longitude": 5.8987139
  },
  {
    "stateCode": "DT",
    "state": "Delta",
    "lga": "Uvwie",
    "latitude": 5.5324624,
    "longitude": 5.8987139
  },
  {
    "stateCode": "DT",
    "state": "Delta",
    "lga": "Warri  North",
    "latitude": 5.5324624,
    "longitude": 5.8987139
  },
  {
    "stateCode": "DT",
    "state": "Delta",
    "lga": "Warri South",
    "latitude": 5.5324624,
    "longitude": 5.8987139
  },
  {
    "stateCode": "DT",
    "state": "Delta",
    "lga": "Warri South  West",
    "latitude": 5.5324624,
    "longitude": 5.8987139
  },
  {
    "stateCode": "EB",
    "state": "Ebonyi",
    "lga": "Abakaliki",
    "latitude": 6.177973,
    "longitude": 7.9592863
  },
  {
    "stateCode": "EB",
    "state": "Ebonyi",
    "lga": "Afikpo North",
    "latitude": 6.177973,
    "longitude": 7.9592863
  },
  {
    "stateCode": "EB",
    "state": "Ebonyi",
    "lga": "Afikpo  South",
    "latitude": 6.177973,
    "longitude": 7.9592863
  },
  {
    "stateCode": "EB",
    "state": "Ebonyi",
    "lga": "Ebonyi",
    "latitude": 6.177973,
    "longitude": 7.9592863
  },
  {
    "stateCode": "EB",
    "state": "Ebonyi",
    "lga": "Ezza North",
    "latitude": 6.177973,
    "longitude": 7.9592863
  },
  {
    "stateCode": "EB",
    "state": "Ebonyi",
    "lga": "Ezza South",
    "latitude": 6.177973,
    "longitude": 7.9592863
  },
  {
    "stateCode": "EB",
    "state": "Ebonyi",
    "lga": "Ikwo",
    "latitude": 6.177973,
    "longitude": 7.9592863
  },
  {
    "stateCode": "EB",
    "state": "Ebonyi",
    "lga": "Ishielu",
    "latitude": 6.177973,
    "longitude": 7.9592863
  },
  {
    "stateCode": "EB",
    "state": "Ebonyi",
    "lga": "Ivo",
    "latitude": 6.177973,
    "longitude": 7.9592863
  },
  {
    "stateCode": "EB",
    "state": "Ebonyi",
    "lga": "Izzi",
    "latitude": 6.177973,
    "longitude": 7.9592863
  },
  {
    "stateCode": "EB",
    "state": "Ebonyi",
    "lga": "Ohaozara",
    "latitude": 6.177973,
    "longitude": 7.9592863
  },
  {
    "stateCode": "EB",
    "state": "Ebonyi",
    "lga": "Ohaukwu",
    "latitude": 6.177973,
    "longitude": 7.9592863
  },
  {
    "stateCode": "EB",
    "state": "Ebonyi",
    "lga": "Onicha",
    "latitude": 6.177973,
    "longitude": 7.9592863
  },
  {
    "stateCode": "ED",
    "state": "Edo",
    "lga": "Akoko Edo",
    "latitude": 6.5438101,
    "longitude": 5.8987139
  },
  {
    "stateCode": "ED",
    "state": "Edo",
    "lga": "Egor",
    "latitude": 6.5438101,
    "longitude": 5.8987139
  },
  {
    "stateCode": "ED",
    "state": "Edo",
    "lga": "Esan Central",
    "latitude": 6.5438101,
    "longitude": 5.8987139
  },
  {
    "stateCode": "ED",
    "state": "Edo",
    "lga": "Esan North East",
    "latitude": 6.5438101,
    "longitude": 5.8987139
  },
  {
    "stateCode": "ED",
    "state": "Edo",
    "lga": "Esan South East",
    "latitude": 6.5438101,
    "longitude": 5.8987139
  },
  {
    "stateCode": "ED",
    "state": "Edo",
    "lga": "Esan West",
    "latitude": 6.5438101,
    "longitude": 5.8987139
  },
  {
    "stateCode": "ED",
    "state": "Edo",
    "lga": "Etsako Central",
    "latitude": 6.5438101,
    "longitude": 5.8987139
  },
  {
    "stateCode": "ED",
    "state": "Edo",
    "lga": "Etsako East",
    "latitude": 6.5438101,
    "longitude": 5.8987139
  },
  {
    "stateCode": "ED",
    "state": "Edo",
    "lga": "Etsako  West",
    "latitude": 6.5438101,
    "longitude": 5.8987139
  },
  {
    "stateCode": "ED",
    "state": "Edo",
    "lga": "Igueben",
    "latitude": 6.5438101,
    "longitude": 5.8987139
  },
  {
    "stateCode": "ED",
    "state": "Edo",
    "lga": "Ikpoba/okha",
    "latitude": 6.5438101,
    "longitude": 5.8987139
  },
  {
    "stateCode": "ED",
    "state": "Edo",
    "lga": "Oredo",
    "latitude": 6.5438101,
    "longitude": 5.8987139
  },
  {
    "stateCode": "ED",
    "state": "Edo",
    "lga": "Orhionmwon",
    "latitude": 6.5438101,
    "longitude": 5.8987139
  },
  {
    "stateCode": "ED",
    "state": "Edo",
    "lga": "Ovia North East",
    "latitude": 6.5438101,
    "longitude": 5.8987139
  },
  {
    "stateCode": "ED",
    "state": "Edo",
    "lga": "Ovia South West",
    "latitude": 6.5438101,
    "longitude": 5.8987139
  },
  {
    "stateCode": "ED",
    "state": "Edo",
    "lga": "Owan East",
    "latitude": 6.5438101,
    "longitude": 5.8987139
  },
  {
    "stateCode": "ED",
    "state": "Edo",
    "lga": "Owan West",
    "latitude": 6.5438101,
    "longitude": 5.8987139
  },
  {
    "stateCode": "ED",
    "state": "Edo",
    "lga": "Uhunmwode",
    "latitude": 6.5438101,
    "longitude": 5.8987139
  },
  {
    "stateCode": "EK",
    "state": "Ekiti",
    "lga": "Ado Ekiti",
    "latitude": 7.6655813,
    "longitude": 5.3102505
  },
  {
    "stateCode": "EK",
    "state": "Ekiti",
    "lga": "Efon",
    "latitude": 7.6655813,
    "longitude": 5.3102505
  },
  {
    "stateCode": "EK",
    "state": "Ekiti",
    "lga": "Ekiti East",
    "latitude": 7.6655813,
    "longitude": 5.3102505
  },
  {
    "stateCode": "EK",
    "state": "Ekiti",
    "lga": "Ekiti West",
    "latitude": 7.6655813,
    "longitude": 5.3102505
  },
  {
    "stateCode": "EK",
    "state": "Ekiti",
    "lga": "Ekiti South West",
    "latitude": 7.6655813,
    "longitude": 5.3102505
  },
  {
    "stateCode": "EK",
    "state": "Ekiti",
    "lga": "Emure",
    "latitude": 7.6655813,
    "longitude": 5.3102505
  },
  {
    "stateCode": "EK",
    "state": "Ekiti",
    "lga": "Gbonyin",
    "latitude": 7.6655813,
    "longitude": 5.3102505
  },
  {
    "stateCode": "EK",
    "state": "Ekiti",
    "lga": "Ido / Osi",
    "latitude": 7.6655813,
    "longitude": 5.3102505
  },
  {
    "stateCode": "EK",
    "state": "Ekiti",
    "lga": "Ijero",
    "latitude": 7.6655813,
    "longitude": 5.3102505
  },
  {
    "stateCode": "EK",
    "state": "Ekiti",
    "lga": "Ikere",
    "latitude": 7.6655813,
    "longitude": 5.3102505
  },
  {
    "stateCode": "EK",
    "state": "Ekiti",
    "lga": "Ikole",
    "latitude": 7.6655813,
    "longitude": 5.3102505
  },
  {
    "stateCode": "EK",
    "state": "Ekiti",
    "lga": "Ilejemeje",
    "latitude": 7.6655813,
    "longitude": 5.3102505
  },
  {
    "stateCode": "EK",
    "state": "Ekiti",
    "lga": "Irepodun / Ifelodun",
    "latitude": 7.6655813,
    "longitude": 5.3102505
  },
  {
    "stateCode": "EK",
    "state": "Ekiti",
    "lga": "Ise / Orun",
    "latitude": 7.6655813,
    "longitude": 5.3102505
  },
  {
    "stateCode": "EK",
    "state": "Ekiti",
    "lga": "Moba",
    "latitude": 7.6655813,
    "longitude": 5.3102505
  },
  {
    "stateCode": "EK",
    "state": "Ekiti",
    "lga": "Oye",
    "latitude": 7.6655813,
    "longitude": 5.3102505
  },
  {
    "stateCode": "EN",
    "state": "Enugu",
    "lga": "Aninri",
    "latitude": 6.4526667,
    "longitude": 7.5103333
  },
  {
    "stateCode": "EN",
    "state": "Enugu",
    "lga": "Awgu",
    "latitude": 6.4526667,
    "longitude": 7.5103333
  },
  {
    "stateCode": "EN",
    "state": "Enugu",
    "lga": "Enugu East",
    "latitude": 6.4526667,
    "longitude": 7.5103333
  },
  {
    "stateCode": "EN",
    "state": "Enugu",
    "lga": "Enugu North",
    "latitude": 6.4526667,
    "longitude": 7.5103333
  },
  {
    "stateCode": "EN",
    "state": "Enugu",
    "lga": "Enugu South",
    "latitude": 6.4526667,
    "longitude": 7.5103333
  },
  {
    "stateCode": "EN",
    "state": "Enugu",
    "lga": "Ezeagu",
    "latitude": 6.4526667,
    "longitude": 7.5103333
  },
  {
    "stateCode": "EN",
    "state": "Enugu",
    "lga": "Igbo Etiti",
    "latitude": 6.4526667,
    "longitude": 7.5103333
  },
  {
    "stateCode": "EN",
    "state": "Enugu",
    "lga": "Igbo Eze North",
    "latitude": 6.4526667,
    "longitude": 7.5103333
  },
  {
    "stateCode": "EN",
    "state": "Enugu",
    "lga": "Igbo Eze South",
    "latitude": 6.4526667,
    "longitude": 7.5103333
  },
  {
    "stateCode": "EN",
    "state": "Enugu",
    "lga": "Isi Uzo",
    "latitude": 6.4526667,
    "longitude": 7.5103333
  },
  {
    "stateCode": "EN",
    "state": "Enugu",
    "lga": "Nkanu East",
    "latitude": 6.4526667,
    "longitude": 7.5103333
  },
  {
    "stateCode": "EN",
    "state": "Enugu",
    "lga": "Nkanu West",
    "latitude": 6.4526667,
    "longitude": 7.5103333
  },
  {
    "stateCode": "EN",
    "state": "Enugu",
    "lga": "Nsukka",
    "latitude": 6.4526667,
    "longitude": 7.5103333
  },
  {
    "stateCode": "EN",
    "state": "Enugu",
    "lga": "Oji-river",
    "latitude": 6.4526667,
    "longitude": 7.5103333
  },
  {
    "stateCode": "EN",
    "state": "Enugu",
    "lga": "Udenu",
    "latitude": 6.4526667,
    "longitude": 7.5103333
  },
  {
    "stateCode": "EN",
    "state": "Enugu",
    "lga": "Udi",
    "latitude": 6.4526667,
    "longitude": 7.5103333
  },
  {
    "stateCode": "EN",
    "state": "Enugu",
    "lga": "Uzo-uwani",
    "latitude": 6.4526667,
    "longitude": 7.5103333
  },
  {
    "stateCode": "FC",
    "state": "Fct",
    "lga": "Abaji",
    "latitude": 8.8556838,
    "longitude": 7.179026
  },
  {
    "stateCode": "FC",
    "state": "Fct",
    "lga": "Bwari",
    "latitude": 8.8556838,
    "longitude": 7.179026
  },
  {
    "stateCode": "FC",
    "state": "Fct",
    "lga": "Gwagwalada",
    "latitude": 8.8556838,
    "longitude": 7.179026
  },
  {
    "stateCode": "FC",
    "state": "Fct",
    "lga": "Kuje",
    "latitude": 8.8556838,
    "longitude": 7.179026
  },
  {
    "stateCode": "FC",
    "state": "Fct",
    "lga": "Kwali",
    "latitude": 8.8556838,
    "longitude": 7.179026
  },
  {
    "stateCode": "FC",
    "state": "Fct",
    "lga": "Municipal",
    "latitude": 8.8556838,
    "longitude": 7.179026
  },
  {
    "stateCode": "GM",
    "state": "Gombe",
    "lga": "Akko",
    "latitude": 10.2824,
    "longitude": 11.17479
  },
  {
    "stateCode": "GM",
    "state": "Gombe",
    "lga": "Balanga",
    "latitude": 10.2824,
    "longitude": 11.17479
  },
  {
    "stateCode": "GM",
    "state": "Gombe",
    "lga": "Billiri",
    "latitude": 10.2824,
    "longitude": 11.17479
  },
  {
    "stateCode": "GM",
    "state": "Gombe",
    "lga": "Dukku",
    "latitude": 10.2824,
    "longitude": 11.17479
  },
  {
    "stateCode": "GM",
    "state": "Gombe",
    "lga": "Funakaye",
    "latitude": 10.2824,
    "longitude": 11.17479
  },
  {
    "stateCode": "GM",
    "state": "Gombe",
    "lga": "Gombe",
    "latitude": 10.2824,
    "longitude": 11.17479
  },
  {
    "stateCode": "GM",
    "state": "Gombe",
    "lga": "Kaltungo",
    "latitude": 10.2824,
    "longitude": 11.17479
  },
  {
    "stateCode": "GM",
    "state": "Gombe",
    "lga": "Kwami",
    "latitude": 10.2824,
    "longitude": 11.17479
  },
  {
    "stateCode": "GM",
    "state": "Gombe",
    "lga": "Nafada",
    "latitude": 10.2824,
    "longitude": 11.17479
  },
  {
    "stateCode": "GM",
    "state": "Gombe",
    "lga": "Shongom",
    "latitude": 10.2824,
    "longitude": 11.17479
  },
  {
    "stateCode": "GM",
    "state": "Gombe",
    "lga": "Yalmaltu/ Deba",
    "latitude": 10.2824,
    "longitude": 11.17479
  },
  {
    "stateCode": "IM",
    "state": "Imo",
    "lga": "Aboh Mbaise",
    "latitude": 5.5214533,
    "longitude": 6.9209135
  },
  {
    "stateCode": "IM",
    "state": "Imo",
    "lga": "Ahiazu Mbaise",
    "latitude": 5.5214533,
    "longitude": 6.9209135
  },
  {
    "stateCode": "IM",
    "state": "Imo",
    "lga": "Ehime Mbano",
    "latitude": 5.5214533,
    "longitude": 6.9209135
  },
  {
    "stateCode": "IM",
    "state": "Imo",
    "lga": "Ezinihitte Mbaise",
    "latitude": 5.5214533,
    "longitude": 6.9209135
  },
  {
    "stateCode": "IM",
    "state": "Imo",
    "lga": "Ideato North",
    "latitude": 5.5214533,
    "longitude": 6.9209135
  },
  {
    "stateCode": "IM",
    "state": "Imo",
    "lga": "Ideato South",
    "latitude": 5.5214533,
    "longitude": 6.9209135
  },
  {
    "stateCode": "IM",
    "state": "Imo",
    "lga": "Ihitte/uboma (isinweke)",
    "latitude": 5.5214533,
    "longitude": 6.9209135
  },
  {
    "stateCode": "IM",
    "state": "Imo",
    "lga": "Ikeduru (iho)",
    "latitude": 5.5214533,
    "longitude": 6.9209135
  },
  {
    "stateCode": "IM",
    "state": "Imo",
    "lga": "Isiala Mbano (umuelemai)",
    "latitude": 5.5214533,
    "longitude": 6.9209135
  },
  {
    "stateCode": "IM",
    "state": "Imo",
    "lga": "Isu (umundugba)",
    "latitude": 5.5214533,
    "longitude": 6.9209135
  },
  {
    "stateCode": "IM",
    "state": "Imo",
    "lga": "Mbaitoli (nwaorieubi)",
    "latitude": 5.5214533,
    "longitude": 6.9209135
  },
  {
    "stateCode": "IM",
    "state": "Imo",
    "lga": "Ngor Okpala (umuneke)",
    "latitude": 5.5214533,
    "longitude": 6.9209135
  },
  {
    "stateCode": "IM",
    "state": "Imo",
    "lga": "Njaba (nnenasa)",
    "latitude": 5.5214533,
    "longitude": 6.9209135
  },
  {
    "stateCode": "IM",
    "state": "Imo",
    "lga": "Nkwerre",
    "latitude": 5.5214533,
    "longitude": 6.9209135
  },
  {
    "stateCode": "IM",
    "state": "Imo",
    "lga": "Nwangele (onu-nwangele Amaigbo)",
    "latitude": 5.5214533,
    "longitude": 6.9209135
  },
  {
    "stateCode": "IM",
    "state": "Imo",
    "lga": "Obowo (otoko)",
    "latitude": 5.5214533,
    "longitude": 6.9209135
  },
  {
    "stateCode": "IM",
    "state": "Imo",
    "lga": "Oguta (oguta)",
    "latitude": 5.5214533,
    "longitude": 6.9209135
  },
  {
    "stateCode": "IM",
    "state": "Imo",
    "lga": "Ohaji/egbema (mmahu-egbema)",
    "latitude": 5.5214533,
    "longitude": 6.9209135
  },
  {
    "stateCode": "IM",
    "state": "Imo",
    "lga": "Okigwe  (okigwe)",
    "latitude": 5.5214533,
    "longitude": 6.9209135
  },
  {
    "stateCode": "IM",
    "state": "Imo",
    "lga": "Onuimo (okwe)",
    "latitude": 5.5214533,
    "longitude": 6.9209135
  },
  {
    "stateCode": "IM",
    "state": "Imo",
    "lga": "Orlu",
    "latitude": 5.5214533,
    "longitude": 6.9209135
  },
  {
    "stateCode": "IM",
    "state": "Imo",
    "lga": "Orsu (awo Idemili)",
    "latitude": 5.5214533,
    "longitude": 6.9209135
  },
  {
    "stateCode": "IM",
    "state": "Imo",
    "lga": "Oru-east",
    "latitude": 5.5214533,
    "longitude": 6.9209135
  },
  {
    "stateCode": "IM",
    "state": "Imo",
    "lga": "Oru West (mgbidi)",
    "latitude": 5.5214533,
    "longitude": 6.9209135
  },
  {
    "stateCode": "IM",
    "state": "Imo",
    "lga": "Owerri Municipal",
    "latitude": 5.5214533,
    "longitude": 6.9209135
  },
  {
    "stateCode": "IM",
    "state": "Imo",
    "lga": "Owerri North (orie Uratta)",
    "latitude": 5.5214533,
    "longitude": 6.9209135
  },
  {
    "stateCode": "IM",
    "state": "Imo",
    "lga": "Owerri West (umuguma)",
    "latitude": 5.5214533,
    "longitude": 6.9209135
  },
  {
    "stateCode": "JG",
    "state": "Jigawa",
    "lga": "Auyo",
    "latitude": 12.4460001,
    "longitude": 9.7232673
  },
  {
    "stateCode": "JG",
    "state": "Jigawa",
    "lga": "Babura",
    "latitude": 12.4460001,
    "longitude": 9.7232673
  },
  {
    "stateCode": "JG",
    "state": "Jigawa",
    "lga": "Birnin Kudu",
    "latitude": 12.4460001,
    "longitude": 9.7232673
  },
  {
    "stateCode": "JG",
    "state": "Jigawa",
    "lga": "Birniwa",
    "latitude": 12.4460001,
    "longitude": 9.7232673
  },
  {
    "stateCode": "JG",
    "state": "Jigawa",
    "lga": "Buji",
    "latitude": 12.4460001,
    "longitude": 9.7232673
  },
  {
    "stateCode": "JG",
    "state": "Jigawa",
    "lga": "Dutse",
    "latitude": 12.4460001,
    "longitude": 9.7232673
  },
  {
    "stateCode": "JG",
    "state": "Jigawa",
    "lga": "Garki",
    "latitude": 12.4460001,
    "longitude": 9.7232673
  },
  {
    "stateCode": "JG",
    "state": "Jigawa",
    "lga": "Gagarawa",
    "latitude": 12.4460001,
    "longitude": 9.7232673
  },
  {
    "stateCode": "JG",
    "state": "Jigawa",
    "lga": "Gumel",
    "latitude": 12.4460001,
    "longitude": 9.7232673
  },
  {
    "stateCode": "JG",
    "state": "Jigawa",
    "lga": "Guri",
    "latitude": 12.4460001,
    "longitude": 9.7232673
  },
  {
    "stateCode": "JG",
    "state": "Jigawa",
    "lga": "Gwaram",
    "latitude": 12.4460001,
    "longitude": 9.7232673
  },
  {
    "stateCode": "JG",
    "state": "Jigawa",
    "lga": "Gwiwa",
    "latitude": 12.4460001,
    "longitude": 9.7232673
  },
  {
    "stateCode": "JG",
    "state": "Jigawa",
    "lga": "Hadejia",
    "latitude": 12.4460001,
    "longitude": 9.7232673
  },
  {
    "stateCode": "JG",
    "state": "Jigawa",
    "lga": "Jahun",
    "latitude": 12.4460001,
    "longitude": 9.7232673
  },
  {
    "stateCode": "JG",
    "state": "Jigawa",
    "lga": "Kafin Hausa",
    "latitude": 12.4460001,
    "longitude": 9.7232673
  },
  {
    "stateCode": "JG",
    "state": "Jigawa",
    "lga": "Kaugama",
    "latitude": 12.4460001,
    "longitude": 9.7232673
  },
  {
    "stateCode": "JG",
    "state": "Jigawa",
    "lga": "Kazaure",
    "latitude": 12.4460001,
    "longitude": 9.7232673
  },
  {
    "stateCode": "JG",
    "state": "Jigawa",
    "lga": "Kirika Samma",
    "latitude": 12.4460001,
    "longitude": 9.7232673
  },
  {
    "stateCode": "JG",
    "state": "Jigawa",
    "lga": "Kiyawa",
    "latitude": 12.4460001,
    "longitude": 9.7232673
  },
  {
    "stateCode": "JG",
    "state": "Jigawa",
    "lga": "Maigatari",
    "latitude": 12.4460001,
    "longitude": 9.7232673
  },
  {
    "stateCode": "JG",
    "state": "Jigawa",
    "lga": "Malam Madori",
    "latitude": 12.4460001,
    "longitude": 9.7232673
  },
  {
    "stateCode": "JG",
    "state": "Jigawa",
    "lga": "Miga",
    "latitude": 12.4460001,
    "longitude": 9.7232673
  },
  {
    "stateCode": "JG",
    "state": "Jigawa",
    "lga": "Ringim",
    "latitude": 12.4460001,
    "longitude": 9.7232673
  },
  {
    "stateCode": "JG",
    "state": "Jigawa",
    "lga": "Roni",
    "latitude": 12.4460001,
    "longitude": 9.7232673
  },
  {
    "stateCode": "JG",
    "state": "Jigawa",
    "lga": "Sule-tankarkar",
    "latitude": 12.4460001,
    "longitude": 9.7232673
  },
  {
    "stateCode": "JG",
    "state": "Jigawa",
    "lga": "Taura",
    "latitude": 12.4460001,
    "longitude": 9.7232673
  },
  {
    "stateCode": "JG",
    "state": "Jigawa",
    "lga": "Yankwashi",
    "latitude": 12.4460001,
    "longitude": 9.7232673
  },
  {
    "stateCode": "KD",
    "state": "Kaduna",
    "lga": "Birnin Gwari",
    "latitude": 10.5166667,
    "longitude": 7.4333333
  },
  {
    "stateCode": "KD",
    "state": "Kaduna",
    "lga": "Chikun",
    "latitude": 10.5166667,
    "longitude": 7.4333333
  },
  {
    "stateCode": "KD",
    "state": "Kaduna",
    "lga": "Giwa",
    "latitude": 10.5166667,
    "longitude": 7.4333333
  },
  {
    "stateCode": "KD",
    "state": "Kaduna",
    "lga": "Igabi",
    "latitude": 10.5166667,
    "longitude": 7.4333333
  },
  {
    "stateCode": "KD",
    "state": "Kaduna",
    "lga": "Ikara",
    "latitude": 10.5166667,
    "longitude": 7.4333333
  },
  {
    "stateCode": "KD",
    "state": "Kaduna",
    "lga": "Jaba",
    "latitude": 10.5166667,
    "longitude": 7.4333333
  },
  {
    "stateCode": "KD",
    "state": "Kaduna",
    "lga": "JEMA'A",
    "latitude": 10.5166667,
    "longitude": 7.4333333
  },
  {
    "stateCode": "KD",
    "state": "Kaduna",
    "lga": "Kachia",
    "latitude": 10.5166667,
    "longitude": 7.4333333
  },
  {
    "stateCode": "KD",
    "state": "Kaduna",
    "lga": "Kaduna North",
    "latitude": 10.5166667,
    "longitude": 7.4333333
  },
  {
    "stateCode": "KD",
    "state": "Kaduna",
    "lga": "Kaduna South",
    "latitude": 10.5166667,
    "longitude": 7.4333333
  },
  {
    "stateCode": "KD",
    "state": "Kaduna",
    "lga": "Kagarko",
    "latitude": 10.5166667,
    "longitude": 7.4333333
  },
  {
    "stateCode": "KD",
    "state": "Kaduna",
    "lga": "Kajuru",
    "latitude": 10.5166667,
    "longitude": 7.4333333
  },
  {
    "stateCode": "KD",
    "state": "Kaduna",
    "lga": "Kaura",
    "latitude": 10.5166667,
    "longitude": 7.4333333
  },
  {
    "stateCode": "KD",
    "state": "Kaduna",
    "lga": "Kauru",
    "latitude": 10.5166667,
    "longitude": 7.4333333
  },
  {
    "stateCode": "KD",
    "state": "Kaduna",
    "lga": "Kubau",
    "latitude": 10.5166667,
    "longitude": 7.4333333
  },
  {
    "stateCode": "KD",
    "state": "Kaduna",
    "lga": "Kudan",
    "latitude": 10.5166667,
    "longitude": 7.4333333
  },
  {
    "stateCode": "KD",
    "state": "Kaduna",
    "lga": "Lere",
    "latitude": 10.5166667,
    "longitude": 7.4333333
  },
  {
    "stateCode": "KD",
    "state": "Kaduna",
    "lga": "Makarfi",
    "latitude": 10.5166667,
    "longitude": 7.4333333
  },
  {
    "stateCode": "KD",
    "state": "Kaduna",
    "lga": "Sabon Gari",
    "latitude": 10.5166667,
    "longitude": 7.4333333
  },
  {
    "stateCode": "KD",
    "state": "Kaduna",
    "lga": "Sanga",
    "latitude": 10.5166667,
    "longitude": 7.4333333
  },
  {
    "stateCode": "KD",
    "state": "Kaduna",
    "lga": "Soba",
    "latitude": 10.5166667,
    "longitude": 7.4333333
  },
  {
    "stateCode": "KD",
    "state": "Kaduna",
    "lga": "Zangon Kataf",
    "latitude": 10.5166667,
    "longitude": 7.4333333
  },
  {
    "stateCode": "KD",
    "state": "Kaduna",
    "lga": "Zaria",
    "latitude": 10.5166667,
    "longitude": 7.4333333
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Ajingi",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Albasu",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Bagwai",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Bebeji",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Bichi",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Bunkure",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Dala",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Danbata",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Dawaki Kudu",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Dawaki Tofa",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Doguwa",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Fagge",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Gabasawa",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Garko",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Garun Malam",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Gaya",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Gezawa",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Gwale",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Gwarzo",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Kabo",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Kano Municipal",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Karaye",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Kibiya",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Kiru",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Kumbotso",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Kunchi",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Kura",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Madobi",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Makoda",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Minjibir",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Nasarawa",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Rano",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Rimin Gado",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Rogo",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Shanono",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Sumaila",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Takai",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Tarauni",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Tofa",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Tsanyawa",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Tudun Wada",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Ungogo",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Warawa",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KN",
    "state": "Kano",
    "lga": "Wudil",
    "latitude": 12,
    "longitude": 8.516667
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Bakori",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Batagarawa",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Batsari",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Baure",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Bindawa",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Charanchi",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Dandume",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Danja",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Dan Musa",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Daura",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Dutsi",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Dutsin-ma",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Faskari",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Funtua",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Ingawa",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Jibia",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Kafur",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Kaita",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Kankara",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Kankia",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Katsina",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Kurfi",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Kusada",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "MAI'ADUA",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Malufashi",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Mani",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Mashi",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Matazu",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Musawa",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Rimi",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Sabuwa",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Safana",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Sandamu",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KT",
    "state": "Katsina",
    "lga": "Zango",
    "latitude": 12.99302,
    "longitude": 7.606163
  },
  {
    "stateCode": "KB",
    "state": "Kebbi",
    "lga": "Aliero",
    "latitude": 11.6781241,
    "longitude": 4.0695454
  },
  {
    "stateCode": "KB",
    "state": "Kebbi",
    "lga": "Arewa",
    "latitude": 11.6781241,
    "longitude": 4.0695454
  },
  {
    "stateCode": "KB",
    "state": "Kebbi",
    "lga": "Argungu",
    "latitude": 11.6781241,
    "longitude": 4.0695454
  },
  {
    "stateCode": "KB",
    "state": "Kebbi",
    "lga": "Augie",
    "latitude": 11.6781241,
    "longitude": 4.0695454
  },
  {
    "stateCode": "KB",
    "state": "Kebbi",
    "lga": "Bagudo",
    "latitude": 11.6781241,
    "longitude": 4.0695454
  },
  {
    "stateCode": "KB",
    "state": "Kebbi",
    "lga": "Birnin Kebbi",
    "latitude": 11.6781241,
    "longitude": 4.0695454
  },
  {
    "stateCode": "KB",
    "state": "Kebbi",
    "lga": "Bunza",
    "latitude": 11.6781241,
    "longitude": 4.0695454
  },
  {
    "stateCode": "KB",
    "state": "Kebbi",
    "lga": "Dandi",
    "latitude": 11.6781241,
    "longitude": 4.0695454
  },
  {
    "stateCode": "KB",
    "state": "Kebbi",
    "lga": "Fakai",
    "latitude": 11.6781241,
    "longitude": 4.0695454
  },
  {
    "stateCode": "KB",
    "state": "Kebbi",
    "lga": "Gwandu",
    "latitude": 11.6781241,
    "longitude": 4.0695454
  },
  {
    "stateCode": "KB",
    "state": "Kebbi",
    "lga": "Jega",
    "latitude": 11.6781241,
    "longitude": 4.0695454
  },
  {
    "stateCode": "KB",
    "state": "Kebbi",
    "lga": "Kalgo",
    "latitude": 11.6781241,
    "longitude": 4.0695454
  },
  {
    "stateCode": "KB",
    "state": "Kebbi",
    "lga": "Koko/besse",
    "latitude": 11.6781241,
    "longitude": 4.0695454
  },
  {
    "stateCode": "KB",
    "state": "Kebbi",
    "lga": "Maiyama",
    "latitude": 11.6781241,
    "longitude": 4.0695454
  },
  {
    "stateCode": "KB",
    "state": "Kebbi",
    "lga": "Ngaski",
    "latitude": 11.6781241,
    "longitude": 4.0695454
  },
  {
    "stateCode": "KB",
    "state": "Kebbi",
    "lga": "Sakaba",
    "latitude": 11.6781241,
    "longitude": 4.0695454
  },
  {
    "stateCode": "KB",
    "state": "Kebbi",
    "lga": "Shanga",
    "latitude": 11.6781241,
    "longitude": 4.0695454
  },
  {
    "stateCode": "KB",
    "state": "Kebbi",
    "lga": "Suru",
    "latitude": 11.6781241,
    "longitude": 4.0695454
  },
  {
    "stateCode": "KB",
    "state": "Kebbi",
    "lga": "Wasagu/danko",
    "latitude": 11.6781241,
    "longitude": 4.0695454
  },
  {
    "stateCode": "KB",
    "state": "Kebbi",
    "lga": "Yauri",
    "latitude": 11.6781241,
    "longitude": 4.0695454
  },
  {
    "stateCode": "KB",
    "state": "Kebbi",
    "lga": "Zuru",
    "latitude": 11.6781241,
    "longitude": 4.0695454
  },
  {
    "stateCode": "KG",
    "state": "Kogi",
    "lga": "Adavi",
    "latitude": 7.561891,
    "longitude": 6.5783387
  },
  {
    "stateCode": "KG",
    "state": "Kogi",
    "lga": "Ajaokuta",
    "latitude": 7.561891,
    "longitude": 6.5783387
  },
  {
    "stateCode": "KG",
    "state": "Kogi",
    "lga": "Ankpa",
    "latitude": 7.561891,
    "longitude": 6.5783387
  },
  {
    "stateCode": "KG",
    "state": "Kogi",
    "lga": "Bassa",
    "latitude": 7.561891,
    "longitude": 6.5783387
  },
  {
    "stateCode": "KG",
    "state": "Kogi",
    "lga": "Dekina",
    "latitude": 7.561891,
    "longitude": 6.5783387
  },
  {
    "stateCode": "KG",
    "state": "Kogi",
    "lga": "Ibaji",
    "latitude": 7.561891,
    "longitude": 6.5783387
  },
  {
    "stateCode": "KG",
    "state": "Kogi",
    "lga": "Idah",
    "latitude": 7.561891,
    "longitude": 6.5783387
  },
  {
    "stateCode": "KG",
    "state": "Kogi",
    "lga": "Igalamela/odolu",
    "latitude": 7.561891,
    "longitude": 6.5783387
  },
  {
    "stateCode": "KG",
    "state": "Kogi",
    "lga": "Ijumu",
    "latitude": 7.561891,
    "longitude": 6.5783387
  },
  {
    "stateCode": "KG",
    "state": "Kogi",
    "lga": "Kabba/bunu",
    "latitude": 7.561891,
    "longitude": 6.5783387
  },
  {
    "stateCode": "KG",
    "state": "Kogi",
    "lga": "Kogi . K. K.",
    "latitude": 7.561891,
    "longitude": 6.5783387
  },
  {
    "stateCode": "KG",
    "state": "Kogi",
    "lga": "Lokoja",
    "latitude": 7.561891,
    "longitude": 6.5783387
  },
  {
    "stateCode": "KG",
    "state": "Kogi",
    "lga": "Mopa Moro",
    "latitude": 7.561891,
    "longitude": 6.5783387
  },
  {
    "stateCode": "KG",
    "state": "Kogi",
    "lga": "Ofu",
    "latitude": 7.561891,
    "longitude": 6.5783387
  },
  {
    "stateCode": "KG",
    "state": "Kogi",
    "lga": "Ogori Mangogo",
    "latitude": 7.561891,
    "longitude": 6.5783387
  },
  {
    "stateCode": "KG",
    "state": "Kogi",
    "lga": "Okehi",
    "latitude": 7.561891,
    "longitude": 6.5783387
  },
  {
    "stateCode": "KG",
    "state": "Kogi",
    "lga": "Okene",
    "latitude": 7.561891,
    "longitude": 6.5783387
  },
  {
    "stateCode": "KG",
    "state": "Kogi",
    "lga": "Olamaboro",
    "latitude": 7.561891,
    "longitude": 6.5783387
  },
  {
    "stateCode": "KG",
    "state": "Kogi",
    "lga": "Omala",
    "latitude": 7.561891,
    "longitude": 6.5783387
  },
  {
    "stateCode": "KG",
    "state": "Kogi",
    "lga": "Yagba East",
    "latitude": 7.561891,
    "longitude": 6.5783387
  },
  {
    "stateCode": "KG",
    "state": "Kogi",
    "lga": "Yagba West",
    "latitude": 7.561891,
    "longitude": 6.5783387
  },
  {
    "stateCode": "KW",
    "state": "Kwara",
    "lga": "Asa",
    "latitude": 8.9847995,
    "longitude": 4.5624426
  },
  {
    "stateCode": "KW",
    "state": "Kwara",
    "lga": "Baruten",
    "latitude": 8.9847995,
    "longitude": 4.5624426
  },
  {
    "stateCode": "KW",
    "state": "Kwara",
    "lga": "Edu",
    "latitude": 8.9847995,
    "longitude": 4.5624426
  },
  {
    "stateCode": "KW",
    "state": "Kwara",
    "lga": "Ekiti",
    "latitude": 8.9847995,
    "longitude": 4.5624426
  },
  {
    "stateCode": "KW",
    "state": "Kwara",
    "lga": "Ifelodun",
    "latitude": 8.9847995,
    "longitude": 4.5624426
  },
  {
    "stateCode": "KW",
    "state": "Kwara",
    "lga": "Ilorin East",
    "latitude": 8.9847995,
    "longitude": 4.5624426
  },
  {
    "stateCode": "KW",
    "state": "Kwara",
    "lga": "Ilorin-south",
    "latitude": 8.9847995,
    "longitude": 4.5624426
  },
  {
    "stateCode": "KW",
    "state": "Kwara",
    "lga": "Ilorin-west",
    "latitude": 8.9847995,
    "longitude": 4.5624426
  },
  {
    "stateCode": "KW",
    "state": "Kwara",
    "lga": "Irepodun",
    "latitude": 8.9847995,
    "longitude": 4.5624426
  },
  {
    "stateCode": "KW",
    "state": "Kwara",
    "lga": "Isin",
    "latitude": 8.9847995,
    "longitude": 4.5624426
  },
  {
    "stateCode": "KW",
    "state": "Kwara",
    "lga": "Kaiama",
    "latitude": 8.9847995,
    "longitude": 4.5624426
  },
  {
    "stateCode": "KW",
    "state": "Kwara",
    "lga": "Moro",
    "latitude": 8.9847995,
    "longitude": 4.5624426
  },
  {
    "stateCode": "KW",
    "state": "Kwara",
    "lga": "Offa",
    "latitude": 8.9847995,
    "longitude": 4.5624426
  },
  {
    "stateCode": "KW",
    "state": "Kwara",
    "lga": "Oke - Ero",
    "latitude": 8.9847995,
    "longitude": 4.5624426
  },
  {
    "stateCode": "KW",
    "state": "Kwara",
    "lga": "Oyun",
    "latitude": 8.9847995,
    "longitude": 4.5624426
  },
  {
    "stateCode": "KW",
    "state": "Kwara",
    "lga": "Patigi",
    "latitude": 8.9847995,
    "longitude": 4.5624426
  },
  {
    "stateCode": "LA",
    "state": "Lagos",
    "lga": "Agege",
    "latitude": 6.4530556,
    "longitude": 3.3958333
  },
  {
    "stateCode": "LA",
    "state": "Lagos",
    "lga": "Ajeromi/ifelodun",
    "latitude": 6.4530556,
    "longitude": 3.3958333
  },
  {
    "stateCode": "LA",
    "state": "Lagos",
    "lga": "Alimosho",
    "latitude": 6.4530556,
    "longitude": 3.3958333
  },
  {
    "stateCode": "LA",
    "state": "Lagos",
    "lga": "Amuwo-odofin",
    "latitude": 6.4530556,
    "longitude": 3.3958333
  },
  {
    "stateCode": "LA",
    "state": "Lagos",
    "lga": "Apapa",
    "latitude": 6.4530556,
    "longitude": 3.3958333
  },
  {
    "stateCode": "LA",
    "state": "Lagos",
    "lga": "Badagry",
    "latitude": 6.4530556,
    "longitude": 3.3958333
  },
  {
    "stateCode": "LA",
    "state": "Lagos",
    "lga": "Epe",
    "latitude": 6.4530556,
    "longitude": 3.3958333
  },
  {
    "stateCode": "LA",
    "state": "Lagos",
    "lga": "Eti-osa",
    "latitude": 6.4530556,
    "longitude": 3.3958333
  },
  {
    "stateCode": "LA",
    "state": "Lagos",
    "lga": "Ibeju/lekki",
    "latitude": 6.4530556,
    "longitude": 3.3958333
  },
  {
    "stateCode": "LA",
    "state": "Lagos",
    "lga": "Ifako-ijaye",
    "latitude": 6.4530556,
    "longitude": 3.3958333
  },
  {
    "stateCode": "LA",
    "state": "Lagos",
    "lga": "Ikeja",
    "latitude": 6.4530556,
    "longitude": 3.3958333
  },
  {
    "stateCode": "LA",
    "state": "Lagos",
    "lga": "Ikorodu",
    "latitude": 6.4530556,
    "longitude": 3.3958333
  },
  {
    "stateCode": "LA",
    "state": "Lagos",
    "lga": "Kosofe",
    "latitude": 6.4530556,
    "longitude": 3.3958333
  },
  {
    "stateCode": "LA",
    "state": "Lagos",
    "lga": "Lagos Island",
    "latitude": 6.4530556,
    "longitude": 3.3958333
  },
  {
    "stateCode": "LA",
    "state": "Lagos",
    "lga": "Lagos Mainland",
    "latitude": 6.4530556,
    "longitude": 3.3958333
  },
  {
    "stateCode": "LA",
    "state": "Lagos",
    "lga": "Mushin",
    "latitude": 6.4530556,
    "longitude": 3.3958333
  },
  {
    "stateCode": "LA",
    "state": "Lagos",
    "lga": "Ojo",
    "latitude": 6.4530556,
    "longitude": 3.3958333
  },
  {
    "stateCode": "LA",
    "state": "Lagos",
    "lga": "Oshodi/isolo",
    "latitude": 6.4530556,
    "longitude": 3.3958333
  },
  {
    "stateCode": "LA",
    "state": "Lagos",
    "lga": "Somolu",
    "latitude": 6.4530556,
    "longitude": 3.3958333
  },
  {
    "stateCode": "LA",
    "state": "Lagos",
    "lga": "Surulere",
    "latitude": 6.4530556,
    "longitude": 3.3958333
  },
  {
    "stateCode": "NS",
    "state": "Nasarawa",
    "lga": "Akwanga",
    "latitude": 8.5474692,
    "longitude": 7.7118003
  },
  {
    "stateCode": "NS",
    "state": "Nasarawa",
    "lga": "Awe",
    "latitude": 8.5474692,
    "longitude": 7.7118003
  },
  {
    "stateCode": "NS",
    "state": "Nasarawa",
    "lga": "Doma",
    "latitude": 8.5474692,
    "longitude": 7.7118003
  },
  {
    "stateCode": "NS",
    "state": "Nasarawa",
    "lga": "Karu",
    "latitude": 8.5474692,
    "longitude": 7.7118003
  },
  {
    "stateCode": "NS",
    "state": "Nasarawa",
    "lga": "Keana",
    "latitude": 8.5474692,
    "longitude": 7.7118003
  },
  {
    "stateCode": "NS",
    "state": "Nasarawa",
    "lga": "Keffi",
    "latitude": 8.5474692,
    "longitude": 7.7118003
  },
  {
    "stateCode": "NS",
    "state": "Nasarawa",
    "lga": "Kokona",
    "latitude": 8.5474692,
    "longitude": 7.7118003
  },
  {
    "stateCode": "NS",
    "state": "Nasarawa",
    "lga": "Lafia",
    "latitude": 8.5474692,
    "longitude": 7.7118003
  },
  {
    "stateCode": "NS",
    "state": "Nasarawa",
    "lga": "Nasarawa",
    "latitude": 8.5474692,
    "longitude": 7.7118003
  },
  {
    "stateCode": "NS",
    "state": "Nasarawa",
    "lga": "Nasarawa Eggon",
    "latitude": 8.5474692,
    "longitude": 7.7118003
  },
  {
    "stateCode": "NS",
    "state": "Nasarawa",
    "lga": "Obi",
    "latitude": 8.5474692,
    "longitude": 7.7118003
  },
  {
    "stateCode": "NS",
    "state": "Nasarawa",
    "lga": "Toto",
    "latitude": 8.5474692,
    "longitude": 7.7118003
  },
  {
    "stateCode": "NS",
    "state": "Nasarawa",
    "lga": "Wamba",
    "latitude": 8.5474692,
    "longitude": 7.7118003
  },
  {
    "stateCode": "NG",
    "state": "Niger",
    "lga": "Agaie",
    "latitude": 9.607762,
    "longitude": 6.553394
  },
  {
    "stateCode": "NG",
    "state": "Niger",
    "lga": "Agwara",
    "latitude": 9.607762,
    "longitude": 6.553394
  },
  {
    "stateCode": "NG",
    "state": "Niger",
    "lga": "Bida",
    "latitude": 9.607762,
    "longitude": 6.553394
  },
  {
    "stateCode": "NG",
    "state": "Niger",
    "lga": "Borgu",
    "latitude": 9.607762,
    "longitude": 6.553394
  },
  {
    "stateCode": "NG",
    "state": "Niger",
    "lga": "Bosso",
    "latitude": 9.607762,
    "longitude": 6.553394
  },
  {
    "stateCode": "NG",
    "state": "Niger",
    "lga": "Chanchaga",
    "latitude": 9.607762,
    "longitude": 6.553394
  },
  {
    "stateCode": "NG",
    "state": "Niger",
    "lga": "Edatti",
    "latitude": 9.607762,
    "longitude": 6.553394
  },
  {
    "stateCode": "NG",
    "state": "Niger",
    "lga": "Gbako",
    "latitude": 9.607762,
    "longitude": 6.553394
  },
  {
    "stateCode": "NG",
    "state": "Niger",
    "lga": "Gurara",
    "latitude": 9.607762,
    "longitude": 6.553394
  },
  {
    "stateCode": "NG",
    "state": "Niger",
    "lga": "Katcha",
    "latitude": 9.607762,
    "longitude": 6.553394
  },
  {
    "stateCode": "NG",
    "state": "Niger",
    "lga": "Kontagora",
    "latitude": 9.607762,
    "longitude": 6.553394
  },
  {
    "stateCode": "NG",
    "state": "Niger",
    "lga": "Lapai",
    "latitude": 9.607762,
    "longitude": 6.553394
  },
  {
    "stateCode": "NG",
    "state": "Niger",
    "lga": "Lavun",
    "latitude": 9.607762,
    "longitude": 6.553394
  },
  {
    "stateCode": "NG",
    "state": "Niger",
    "lga": "Magama",
    "latitude": 9.607762,
    "longitude": 6.553394
  },
  {
    "stateCode": "NG",
    "state": "Niger",
    "lga": "Mariga",
    "latitude": 9.607762,
    "longitude": 6.553394
  },
  {
    "stateCode": "NG",
    "state": "Niger",
    "lga": "Mashegu",
    "latitude": 9.607762,
    "longitude": 6.553394
  },
  {
    "stateCode": "NG",
    "state": "Niger",
    "lga": "Mokwa",
    "latitude": 9.607762,
    "longitude": 6.553394
  },
  {
    "stateCode": "NG",
    "state": "Niger",
    "lga": "Munya",
    "latitude": 9.607762,
    "longitude": 6.553394
  },
  {
    "stateCode": "NG",
    "state": "Niger",
    "lga": "Paikoro",
    "latitude": 9.607762,
    "longitude": 6.553394
  },
  {
    "stateCode": "NG",
    "state": "Niger",
    "lga": "Rafi",
    "latitude": 9.607762,
    "longitude": 6.553394
  },
  {
    "stateCode": "NG",
    "state": "Niger",
    "lga": "Rijau",
    "latitude": 9.607762,
    "longitude": 6.553394
  },
  {
    "stateCode": "NG",
    "state": "Niger",
    "lga": "Shiroro",
    "latitude": 9.607762,
    "longitude": 6.553394
  },
  {
    "stateCode": "NG",
    "state": "Niger",
    "lga": "Suleja",
    "latitude": 9.607762,
    "longitude": 6.553394
  },
  {
    "stateCode": "NG",
    "state": "Niger",
    "lga": "Tafa",
    "latitude": 9.607762,
    "longitude": 6.553394
  },
  {
    "stateCode": "NG",
    "state": "Niger",
    "lga": "Wushishi",
    "latitude": 9.607762,
    "longitude": 6.553394
  },
  {
    "stateCode": "OG",
    "state": "Ogun",
    "lga": "Abeokuta North",
    "latitude": 6.9098333,
    "longitude": 3.2583626
  },
  {
    "stateCode": "OG",
    "state": "Ogun",
    "lga": "Abeokuta South",
    "latitude": 6.9098333,
    "longitude": 3.2583626
  },
  {
    "stateCode": "OG",
    "state": "Ogun",
    "lga": "Ado Odo-ota",
    "latitude": 6.9098333,
    "longitude": 3.2583626
  },
  {
    "stateCode": "OG",
    "state": "Ogun",
    "lga": "Egbado North",
    "latitude": 6.9098333,
    "longitude": 3.2583626
  },
  {
    "stateCode": "OG",
    "state": "Ogun",
    "lga": "Egbado South",
    "latitude": 6.9098333,
    "longitude": 3.2583626
  },
  {
    "stateCode": "OG",
    "state": "Ogun",
    "lga": "Ewekoro",
    "latitude": 6.9098333,
    "longitude": 3.2583626
  },
  {
    "stateCode": "OG",
    "state": "Ogun",
    "lga": "Ifo",
    "latitude": 6.9098333,
    "longitude": 3.2583626
  },
  {
    "stateCode": "OG",
    "state": "Ogun",
    "lga": "Ijebu East",
    "latitude": 6.9098333,
    "longitude": 3.2583626
  },
  {
    "stateCode": "OG",
    "state": "Ogun",
    "lga": "Ijebu North",
    "latitude": 6.9098333,
    "longitude": 3.2583626
  },
  {
    "stateCode": "OG",
    "state": "Ogun",
    "lga": "Ijebu North East",
    "latitude": 6.9098333,
    "longitude": 3.2583626
  },
  {
    "stateCode": "OG",
    "state": "Ogun",
    "lga": "Ijebu Ode",
    "latitude": 6.9098333,
    "longitude": 3.2583626
  },
  {
    "stateCode": "OG",
    "state": "Ogun",
    "lga": "Ikenne",
    "latitude": 6.9098333,
    "longitude": 3.2583626
  },
  {
    "stateCode": "OG",
    "state": "Ogun",
    "lga": "Imeko/afon",
    "latitude": 6.9098333,
    "longitude": 3.2583626
  },
  {
    "stateCode": "OG",
    "state": "Ogun",
    "lga": "Ipokia",
    "latitude": 6.9098333,
    "longitude": 3.2583626
  },
  {
    "stateCode": "OG",
    "state": "Ogun",
    "lga": "Obafemi/owode",
    "latitude": 6.9098333,
    "longitude": 3.2583626
  },
  {
    "stateCode": "OG",
    "state": "Ogun",
    "lga": "Odeda",
    "latitude": 6.9098333,
    "longitude": 3.2583626
  },
  {
    "stateCode": "OG",
    "state": "Ogun",
    "lga": "Odogbolu",
    "latitude": 6.9098333,
    "longitude": 3.2583626
  },
  {
    "stateCode": "OG",
    "state": "Ogun",
    "lga": "Ogun Water Side",
    "latitude": 6.9098333,
    "longitude": 3.2583626
  },
  {
    "stateCode": "OG",
    "state": "Ogun",
    "lga": "Remo North",
    "latitude": 6.9098333,
    "longitude": 3.2583626
  },
  {
    "stateCode": "OG",
    "state": "Ogun",
    "lga": "Sagamu",
    "latitude": 6.9098333,
    "longitude": 3.2583626
  },
  {
    "stateCode": "OD",
    "state": "Ondo",
    "lga": "Akoko North East",
    "latitude": 7.088721,
    "longitude": 4.838763
  },
  {
    "stateCode": "OD",
    "state": "Ondo",
    "lga": "Akoko North West",
    "latitude": 7.088721,
    "longitude": 4.838763
  },
  {
    "stateCode": "OD",
    "state": "Ondo",
    "lga": "Akoko South East",
    "latitude": 7.088721,
    "longitude": 4.838763
  },
  {
    "stateCode": "OD",
    "state": "Ondo",
    "lga": "Akoko South West",
    "latitude": 7.088721,
    "longitude": 4.838763
  },
  {
    "stateCode": "OD",
    "state": "Ondo",
    "lga": "Akure North",
    "latitude": 7.088721,
    "longitude": 4.838763
  },
  {
    "stateCode": "OD",
    "state": "Ondo",
    "lga": "Akure South",
    "latitude": 7.088721,
    "longitude": 4.838763
  },
  {
    "stateCode": "OD",
    "state": "Ondo",
    "lga": "Ese-odo",
    "latitude": 7.088721,
    "longitude": 4.838763
  },
  {
    "stateCode": "OD",
    "state": "Ondo",
    "lga": "Idanre",
    "latitude": 7.088721,
    "longitude": 4.838763
  },
  {
    "stateCode": "OD",
    "state": "Ondo",
    "lga": "Ifedore",
    "latitude": 7.088721,
    "longitude": 4.838763
  },
  {
    "stateCode": "OD",
    "state": "Ondo",
    "lga": "Ilaje",
    "latitude": 7.088721,
    "longitude": 4.838763
  },
  {
    "stateCode": "OD",
    "state": "Ondo",
    "lga": "Ileoluji/okeigbo",
    "latitude": 7.088721,
    "longitude": 4.838763
  },
  {
    "stateCode": "OD",
    "state": "Ondo",
    "lga": "Irele",
    "latitude": 7.088721,
    "longitude": 4.838763
  },
  {
    "stateCode": "OD",
    "state": "Ondo",
    "lga": "Odigbo",
    "latitude": 7.088721,
    "longitude": 4.838763
  },
  {
    "stateCode": "OD",
    "state": "Ondo",
    "lga": "Okitipupa",
    "latitude": 7.088721,
    "longitude": 4.838763
  },
  {
    "stateCode": "OD",
    "state": "Ondo",
    "lga": "Ondo East",
    "latitude": 7.088721,
    "longitude": 4.838763
  },
  {
    "stateCode": "OD",
    "state": "Ondo",
    "lga": "Ondo West",
    "latitude": 7.088721,
    "longitude": 4.838763
  },
  {
    "stateCode": "OD",
    "state": "Ondo",
    "lga": "Ose",
    "latitude": 7.088721,
    "longitude": 4.838763
  },
  {
    "stateCode": "OD",
    "state": "Ondo",
    "lga": "Owo",
    "latitude": 7.088721,
    "longitude": 4.838763
  },
  {
    "stateCode": "OS",
    "state": "Osun",
    "lga": "Atakumosa East",
    "latitude": 7.983333,
    "longitude": 5.083333
  },
  {
    "stateCode": "OS",
    "state": "Osun",
    "lga": "Atakumosa West",
    "latitude": 7.983333,
    "longitude": 5.083333
  },
  {
    "stateCode": "OS",
    "state": "Osun",
    "lga": "Ayedaade",
    "latitude": 7.983333,
    "longitude": 5.083333
  },
  {
    "stateCode": "OS",
    "state": "Osun",
    "lga": "Ayedire",
    "latitude": 7.983333,
    "longitude": 5.083333
  },
  {
    "stateCode": "OS",
    "state": "Osun",
    "lga": "Boluwaduro",
    "latitude": 7.983333,
    "longitude": 5.083333
  },
  {
    "stateCode": "OS",
    "state": "Osun",
    "lga": "Boripe",
    "latitude": 7.983333,
    "longitude": 5.083333
  },
  {
    "stateCode": "OS",
    "state": "Osun",
    "lga": "Ede North",
    "latitude": 7.983333,
    "longitude": 5.083333
  },
  {
    "stateCode": "OS",
    "state": "Osun",
    "lga": "Ede South",
    "latitude": 7.983333,
    "longitude": 5.083333
  },
  {
    "stateCode": "OS",
    "state": "Osun",
    "lga": "Egbedore",
    "latitude": 7.983333,
    "longitude": 5.083333
  },
  {
    "stateCode": "OS",
    "state": "Osun",
    "lga": "Ejigbo",
    "latitude": 7.983333,
    "longitude": 5.083333
  },
  {
    "stateCode": "OS",
    "state": "Osun",
    "lga": "Ife Central",
    "latitude": 7.983333,
    "longitude": 5.083333
  },
  {
    "stateCode": "OS",
    "state": "Osun",
    "lga": "Ifedayo",
    "latitude": 7.983333,
    "longitude": 5.083333
  },
  {
    "stateCode": "OS",
    "state": "Osun",
    "lga": "Ife East",
    "latitude": 7.983333,
    "longitude": 5.083333
  },
  {
    "stateCode": "OS",
    "state": "Osun",
    "lga": "Ifelodun",
    "latitude": 7.983333,
    "longitude": 5.083333
  },
  {
    "stateCode": "OS",
    "state": "Osun",
    "lga": "Ife North",
    "latitude": 7.983333,
    "longitude": 5.083333
  },
  {
    "stateCode": "OS",
    "state": "Osun",
    "lga": "Ife South",
    "latitude": 7.983333,
    "longitude": 5.083333
  },
  {
    "stateCode": "OS",
    "state": "Osun",
    "lga": "Ila",
    "latitude": 7.983333,
    "longitude": 5.083333
  },
  {
    "stateCode": "OS",
    "state": "Osun",
    "lga": "Ilesa East",
    "latitude": 7.983333,
    "longitude": 5.083333
  },
  {
    "stateCode": "OS",
    "state": "Osun",
    "lga": "Ilesa West",
    "latitude": 7.983333,
    "longitude": 5.083333
  },
  {
    "stateCode": "OS",
    "state": "Osun",
    "lga": "Irepodun",
    "latitude": 7.983333,
    "longitude": 5.083333
  },
  {
    "stateCode": "OS",
    "state": "Osun",
    "lga": "Irewole",
    "latitude": 7.983333,
    "longitude": 5.083333
  },
  {
    "stateCode": "OS",
    "state": "Osun",
    "lga": "Isokan",
    "latitude": 7.983333,
    "longitude": 5.083333
  },
  {
    "stateCode": "OS",
    "state": "Osun",
    "lga": "Iwo",
    "latitude": 7.983333,
    "longitude": 5.083333
  },
  {
    "stateCode": "OS",
    "state": "Osun",
    "lga": "Obokun",
    "latitude": 7.983333,
    "longitude": 5.083333
  },
  {
    "stateCode": "OS",
    "state": "Osun",
    "lga": "Odo-otin",
    "latitude": 7.983333,
    "longitude": 5.083333
  },
  {
    "stateCode": "OS",
    "state": "Osun",
    "lga": "Ola-oluwa",
    "latitude": 7.983333,
    "longitude": 5.083333
  },
  {
    "stateCode": "OS",
    "state": "Osun",
    "lga": "Olorunda",
    "latitude": 7.983333,
    "longitude": 5.083333
  },
  {
    "stateCode": "OS",
    "state": "Osun",
    "lga": "Oriade",
    "latitude": 7.983333,
    "longitude": 5.083333
  },
  {
    "stateCode": "OS",
    "state": "Osun",
    "lga": "Orolu",
    "latitude": 7.983333,
    "longitude": 5.083333
  },
  {
    "stateCode": "OS",
    "state": "Osun",
    "lga": "Osogbo",
    "latitude": 7.983333,
    "longitude": 5.083333
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Afijio",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Akinyele",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Atiba",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Atisbo",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Egbeda",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Ibadan North",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Ibadan North East",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Ibadan North West",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Ibadan South-east",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Ibadan South West",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Ibarapa Central",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Ibarapa East",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Ibarapa North",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Ido",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Irepo",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Iseyin",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Itesiwaju",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Iwajowa",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Kajola",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Lagelu",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Ogbomoso North",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Ogbomoso South",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Ogo-oluwa",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Olorunsogo",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Oluyole",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Ona-ara",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Oorelope",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Ori Ire",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Oyo East",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Oyo West",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Saki East",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Saki West",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "OY",
    "state": "Oyo",
    "lga": "Surulere",
    "latitude": 7.837154,
    "longitude": 3.934652
  },
  {
    "stateCode": "PL",
    "state": "Plateau",
    "lga": "Jos North",
    "latitude": 9.2350817,
    "longitude": 9.7232673
  },
  {
    "stateCode": "PL",
    "state": "Plateau",
    "lga": "Barikin Ladi",
    "latitude": 9.2350817,
    "longitude": 9.7232673
  },
  {
    "stateCode": "PL",
    "state": "Plateau",
    "lga": "Bassa",
    "latitude": 9.2350817,
    "longitude": 9.7232673
  },
  {
    "stateCode": "PL",
    "state": "Plateau",
    "lga": "Bokkos",
    "latitude": 9.2350817,
    "longitude": 9.7232673
  },
  {
    "stateCode": "PL",
    "state": "Plateau",
    "lga": "Jos East",
    "latitude": 9.2350817,
    "longitude": 9.7232673
  },
  {
    "stateCode": "PL",
    "state": "Plateau",
    "lga": "Jos South",
    "latitude": 9.2350817,
    "longitude": 9.7232673
  },
  {
    "stateCode": "PL",
    "state": "Plateau",
    "lga": "Kanam",
    "latitude": 9.2350817,
    "longitude": 9.7232673
  },
  {
    "stateCode": "PL",
    "state": "Plateau",
    "lga": "Kanke",
    "latitude": 9.2350817,
    "longitude": 9.7232673
  },
  {
    "stateCode": "PL",
    "state": "Plateau",
    "lga": "Langtang North",
    "latitude": 9.2350817,
    "longitude": 9.7232673
  },
  {
    "stateCode": "PL",
    "state": "Plateau",
    "lga": "Langtang South",
    "latitude": 9.2350817,
    "longitude": 9.7232673
  },
  {
    "stateCode": "PL",
    "state": "Plateau",
    "lga": "Mangu",
    "latitude": 9.2350817,
    "longitude": 9.7232673
  },
  {
    "stateCode": "PL",
    "state": "Plateau",
    "lga": "Mikang",
    "latitude": 9.2350817,
    "longitude": 9.7232673
  },
  {
    "stateCode": "PL",
    "state": "Plateau",
    "lga": "Pankshin",
    "latitude": 9.2350817,
    "longitude": 9.7232673
  },
  {
    "stateCode": "PL",
    "state": "Plateau",
    "lga": "QUA'AN PAN",
    "latitude": 9.2350817,
    "longitude": 9.7232673
  },
  {
    "stateCode": "PL",
    "state": "Plateau",
    "lga": "Riyom",
    "latitude": 9.2350817,
    "longitude": 9.7232673
  },
  {
    "stateCode": "PL",
    "state": "Plateau",
    "lga": "Shendam",
    "latitude": 9.2350817,
    "longitude": 9.7232673
  },
  {
    "stateCode": "PL",
    "state": "Plateau",
    "lga": "Wase",
    "latitude": 9.2350817,
    "longitude": 9.7232673
  },
  {
    "stateCode": "RV",
    "state": "Rivers",
    "lga": "Abua-odual",
    "latitude": 4.8580767,
    "longitude": 6.9209135
  },
  {
    "stateCode": "RV",
    "state": "Rivers",
    "lga": "Ahoada East",
    "latitude": 4.8580767,
    "longitude": 6.9209135
  },
  {
    "stateCode": "RV",
    "state": "Rivers",
    "lga": "Ahoada West",
    "latitude": 4.8580767,
    "longitude": 6.9209135
  },
  {
    "stateCode": "RV",
    "state": "Rivers",
    "lga": "Akuku Toru",
    "latitude": 4.8580767,
    "longitude": 6.9209135
  },
  {
    "stateCode": "RV",
    "state": "Rivers",
    "lga": "Andoni",
    "latitude": 4.8580767,
    "longitude": 6.9209135
  },
  {
    "stateCode": "RV",
    "state": "Rivers",
    "lga": "Asari-toru",
    "latitude": 4.8580767,
    "longitude": 6.9209135
  },
  {
    "stateCode": "RV",
    "state": "Rivers",
    "lga": "Bonny",
    "latitude": 4.8580767,
    "longitude": 6.9209135
  },
  {
    "stateCode": "RV",
    "state": "Rivers",
    "lga": "Degema",
    "latitude": 4.8580767,
    "longitude": 6.9209135
  },
  {
    "stateCode": "RV",
    "state": "Rivers",
    "lga": "Eleme",
    "latitude": 4.8580767,
    "longitude": 6.9209135
  },
  {
    "stateCode": "RV",
    "state": "Rivers",
    "lga": "Emohua",
    "latitude": 4.8580767,
    "longitude": 6.9209135
  },
  {
    "stateCode": "RV",
    "state": "Rivers",
    "lga": "Etche",
    "latitude": 4.8580767,
    "longitude": 6.9209135
  },
  {
    "stateCode": "RV",
    "state": "Rivers",
    "lga": "Gokana",
    "latitude": 4.8580767,
    "longitude": 6.9209135
  },
  {
    "stateCode": "RV",
    "state": "Rivers",
    "lga": "Ikwerre",
    "latitude": 4.8580767,
    "longitude": 6.9209135
  },
  {
    "stateCode": "RV",
    "state": "Rivers",
    "lga": "Khana",
    "latitude": 4.8580767,
    "longitude": 6.9209135
  },
  {
    "stateCode": "RV",
    "state": "Rivers",
    "lga": "Obio/akpor",
    "latitude": 4.8580767,
    "longitude": 6.9209135
  },
  {
    "stateCode": "RV",
    "state": "Rivers",
    "lga": "Ogba/egbema/ndoni",
    "latitude": 4.8580767,
    "longitude": 6.9209135
  },
  {
    "stateCode": "RV",
    "state": "Rivers",
    "lga": "Ogu/bolo",
    "latitude": 4.8580767,
    "longitude": 6.9209135
  },
  {
    "stateCode": "RV",
    "state": "Rivers",
    "lga": "Okrika",
    "latitude": 4.8580767,
    "longitude": 6.9209135
  },
  {
    "stateCode": "RV",
    "state": "Rivers",
    "lga": "Omuma",
    "latitude": 4.8580767,
    "longitude": 6.9209135
  },
  {
    "stateCode": "RV",
    "state": "Rivers",
    "lga": "Opobo/nekoro",
    "latitude": 4.8580767,
    "longitude": 6.9209135
  },
  {
    "stateCode": "RV",
    "state": "Rivers",
    "lga": "Oyigbo",
    "latitude": 4.8580767,
    "longitude": 6.9209135
  },
  {
    "stateCode": "RV",
    "state": "Rivers",
    "lga": "Port Harcourt",
    "latitude": 4.8580767,
    "longitude": 6.9209135
  },
  {
    "stateCode": "RV",
    "state": "Rivers",
    "lga": "Tai",
    "latitude": 4.8580767,
    "longitude": 6.9209135
  },
  {
    "stateCode": "SO",
    "state": "Sokoto",
    "lga": "Binji",
    "latitude": 13.0666667,
    "longitude": 5.2333333
  },
  {
    "stateCode": "SO",
    "state": "Sokoto",
    "lga": "Bodinga",
    "latitude": 13.0666667,
    "longitude": 5.2333333
  },
  {
    "stateCode": "SO",
    "state": "Sokoto",
    "lga": "Dange/shuni",
    "latitude": 13.0666667,
    "longitude": 5.2333333
  },
  {
    "stateCode": "SO",
    "state": "Sokoto",
    "lga": "Gada",
    "latitude": 13.0666667,
    "longitude": 5.2333333
  },
  {
    "stateCode": "SO",
    "state": "Sokoto",
    "lga": "Goronyo",
    "latitude": 13.0666667,
    "longitude": 5.2333333
  },
  {
    "stateCode": "SO",
    "state": "Sokoto",
    "lga": "Gudu",
    "latitude": 13.0666667,
    "longitude": 5.2333333
  },
  {
    "stateCode": "SO",
    "state": "Sokoto",
    "lga": "Gwadabawa",
    "latitude": 13.0666667,
    "longitude": 5.2333333
  },
  {
    "stateCode": "SO",
    "state": "Sokoto",
    "lga": "Illela",
    "latitude": 13.0666667,
    "longitude": 5.2333333
  },
  {
    "stateCode": "SO",
    "state": "Sokoto",
    "lga": "Isa",
    "latitude": 13.0666667,
    "longitude": 5.2333333
  },
  {
    "stateCode": "SO",
    "state": "Sokoto",
    "lga": "Kware",
    "latitude": 13.0666667,
    "longitude": 5.2333333
  },
  {
    "stateCode": "SO",
    "state": "Sokoto",
    "lga": "Kebbe",
    "latitude": 13.0666667,
    "longitude": 5.2333333
  },
  {
    "stateCode": "SO",
    "state": "Sokoto",
    "lga": "Rabah",
    "latitude": 13.0666667,
    "longitude": 5.2333333
  },
  {
    "stateCode": "SO",
    "state": "Sokoto",
    "lga": "S/birni",
    "latitude": 13.0666667,
    "longitude": 5.2333333
  },
  {
    "stateCode": "SO",
    "state": "Sokoto",
    "lga": "Shagari",
    "latitude": 13.0666667,
    "longitude": 5.2333333
  },
  {
    "stateCode": "SO",
    "state": "Sokoto",
    "lga": "Silame",
    "latitude": 13.0666667,
    "longitude": 5.2333333
  },
  {
    "stateCode": "SO",
    "state": "Sokoto",
    "lga": "Sokoto North",
    "latitude": 13.0666667,
    "longitude": 5.2333333
  },
  {
    "stateCode": "SO",
    "state": "Sokoto",
    "lga": "Sokoto South",
    "latitude": 13.0666667,
    "longitude": 5.2333333
  },
  {
    "stateCode": "SO",
    "state": "Sokoto",
    "lga": "Tambuwal",
    "latitude": 13.0666667,
    "longitude": 5.2333333
  },
  {
    "stateCode": "SO",
    "state": "Sokoto",
    "lga": "Tangaza",
    "latitude": 13.0666667,
    "longitude": 5.2333333
  },
  {
    "stateCode": "SO",
    "state": "Sokoto",
    "lga": "Tureta",
    "latitude": 13.0666667,
    "longitude": 5.2333333
  },
  {
    "stateCode": "SO",
    "state": "Sokoto",
    "lga": "Wamakko",
    "latitude": 13.0666667,
    "longitude": 5.2333333
  },
  {
    "stateCode": "SO",
    "state": "Sokoto",
    "lga": "Wurno",
    "latitude": 13.0666667,
    "longitude": 5.2333333
  },
  {
    "stateCode": "SO",
    "state": "Sokoto",
    "lga": "Yabo",
    "latitude": 13.0666667,
    "longitude": 5.2333333
  },
  {
    "stateCode": "TR",
    "state": "Taraba",
    "lga": "Ardo - Kola",
    "latitude": 7.9868755,
    "longitude": 10.9807003
  },
  {
    "stateCode": "TR",
    "state": "Taraba",
    "lga": "Bali",
    "latitude": 7.9868755,
    "longitude": 10.9807003
  },
  {
    "stateCode": "TR",
    "state": "Taraba",
    "lga": "Donga",
    "latitude": 7.9868755,
    "longitude": 10.9807003
  },
  {
    "stateCode": "TR",
    "state": "Taraba",
    "lga": "Gashaka",
    "latitude": 7.9868755,
    "longitude": 10.9807003
  },
  {
    "stateCode": "TR",
    "state": "Taraba",
    "lga": "Gassol",
    "latitude": 7.9868755,
    "longitude": 10.9807003
  },
  {
    "stateCode": "TR",
    "state": "Taraba",
    "lga": "Ibi",
    "latitude": 7.9868755,
    "longitude": 10.9807003
  },
  {
    "stateCode": "TR",
    "state": "Taraba",
    "lga": "Jalingo",
    "latitude": 7.9868755,
    "longitude": 10.9807003
  },
  {
    "stateCode": "TR",
    "state": "Taraba",
    "lga": "Karim-lamido",
    "latitude": 7.9868755,
    "longitude": 10.9807003
  },
  {
    "stateCode": "TR",
    "state": "Taraba",
    "lga": "Kurmi",
    "latitude": 7.9868755,
    "longitude": 10.9807003
  },
  {
    "stateCode": "TR",
    "state": "Taraba",
    "lga": "Lau",
    "latitude": 7.9868755,
    "longitude": 10.9807003
  },
  {
    "stateCode": "TR",
    "state": "Taraba",
    "lga": "Sardauna",
    "latitude": 7.9868755,
    "longitude": 10.9807003
  },
  {
    "stateCode": "TR",
    "state": "Taraba",
    "lga": "Takum",
    "latitude": 7.9868755,
    "longitude": 10.9807003
  },
  {
    "stateCode": "TR",
    "state": "Taraba",
    "lga": "Ussa",
    "latitude": 7.9868755,
    "longitude": 10.9807003
  },
  {
    "stateCode": "TR",
    "state": "Taraba",
    "lga": "Wukari",
    "latitude": 7.9868755,
    "longitude": 10.9807003
  },
  {
    "stateCode": "TR",
    "state": "Taraba",
    "lga": "Yorro",
    "latitude": 7.9868755,
    "longitude": 10.9807003
  },
  {
    "stateCode": "TR",
    "state": "Taraba",
    "lga": "Zing",
    "latitude": 7.9868755,
    "longitude": 10.9807003
  },
  {
    "stateCode": "YB",
    "state": "Yobe",
    "lga": "Bade",
    "latitude": 12.1871412,
    "longitude": 11.7068294
  },
  {
    "stateCode": "YB",
    "state": "Yobe",
    "lga": "Bursari",
    "latitude": 12.1871412,
    "longitude": 11.7068294
  },
  {
    "stateCode": "YB",
    "state": "Yobe",
    "lga": "Damaturu",
    "latitude": 12.1871412,
    "longitude": 11.7068294
  },
  {
    "stateCode": "YB",
    "state": "Yobe",
    "lga": "Fika",
    "latitude": 12.1871412,
    "longitude": 11.7068294
  },
  {
    "stateCode": "YB",
    "state": "Yobe",
    "lga": "Fune",
    "latitude": 12.1871412,
    "longitude": 11.7068294
  },
  {
    "stateCode": "YB",
    "state": "Yobe",
    "lga": "Geidam",
    "latitude": 12.1871412,
    "longitude": 11.7068294
  },
  {
    "stateCode": "YB",
    "state": "Yobe",
    "lga": "Gujba",
    "latitude": 12.1871412,
    "longitude": 11.7068294
  },
  {
    "stateCode": "YB",
    "state": "Yobe",
    "lga": "Gulani",
    "latitude": 12.1871412,
    "longitude": 11.7068294
  },
  {
    "stateCode": "YB",
    "state": "Yobe",
    "lga": "Jakusko",
    "latitude": 12.1871412,
    "longitude": 11.7068294
  },
  {
    "stateCode": "YB",
    "state": "Yobe",
    "lga": "Karasawa",
    "latitude": 12.1871412,
    "longitude": 11.7068294
  },
  {
    "stateCode": "YB",
    "state": "Yobe",
    "lga": "Machina",
    "latitude": 12.1871412,
    "longitude": 11.7068294
  },
  {
    "stateCode": "YB",
    "state": "Yobe",
    "lga": "Nangere",
    "latitude": 12.1871412,
    "longitude": 11.7068294
  },
  {
    "stateCode": "YB",
    "state": "Yobe",
    "lga": "Nguru",
    "latitude": 12.1871412,
    "longitude": 11.7068294
  },
  {
    "stateCode": "YB",
    "state": "Yobe",
    "lga": "Potiskum",
    "latitude": 12.1871412,
    "longitude": 11.7068294
  },
  {
    "stateCode": "YB",
    "state": "Yobe",
    "lga": "Tarmuwa",
    "latitude": 12.1871412,
    "longitude": 11.7068294
  },
  {
    "stateCode": "YB",
    "state": "Yobe",
    "lga": "Yunusari",
    "latitude": 12.1871412,
    "longitude": 11.7068294
  },
  {
    "stateCode": "YB",
    "state": "Yobe",
    "lga": "Yusufari",
    "latitude": 12.1871412,
    "longitude": 11.7068294
  },
  {
    "stateCode": "ZM",
    "state": "Zamfara",
    "lga": "Anka",
    "latitude": 12.1844159,
    "longitude": 6.2375947
  },
  {
    "stateCode": "ZM",
    "state": "Zamfara",
    "lga": "Bakura",
    "latitude": 12.1844159,
    "longitude": 6.2375947
  },
  {
    "stateCode": "ZM",
    "state": "Zamfara",
    "lga": "Birnin Magaji",
    "latitude": 12.1844159,
    "longitude": 6.2375947
  },
  {
    "stateCode": "ZM",
    "state": "Zamfara",
    "lga": "Bukkuyum",
    "latitude": 12.1844159,
    "longitude": 6.2375947
  },
  {
    "stateCode": "ZM",
    "state": "Zamfara",
    "lga": "Bungudu",
    "latitude": 12.1844159,
    "longitude": 6.2375947
  },
  {
    "stateCode": "ZM",
    "state": "Zamfara",
    "lga": "Gummi",
    "latitude": 12.1844159,
    "longitude": 6.2375947
  },
  {
    "stateCode": "ZM",
    "state": "Zamfara",
    "lga": "Gusau",
    "latitude": 12.1844159,
    "longitude": 6.2375947
  },
  {
    "stateCode": "ZM",
    "state": "Zamfara",
    "lga": "Kaura Namoda",
    "latitude": 12.1844159,
    "longitude": 6.2375947
  },
  {
    "stateCode": "ZM",
    "state": "Zamfara",
    "lga": "Maradun",
    "latitude": 12.1844159,
    "longitude": 6.2375947
  },
  {
    "stateCode": "ZM",
    "state": "Zamfara",
    "lga": "Maru",
    "latitude": 12.1844159,
    "longitude": 6.2375947
  },
  {
    "stateCode": "ZM",
    "state": "Zamfara",
    "lga": "Shinkafi",
    "latitude": 12.1844159,
    "longitude": 6.2375947
  },
  {
    "stateCode": "ZM",
    "state": "Zamfara",
    "lga": "Talata Mafara",
    "latitude": 12.1844159,
    "longitude": 6.2375947
  },
  {
    "stateCode": "ZM",
    "state": "Zamfara",
    "lga": "Tsafe",
    "latitude": 12.1844159,
    "longitude": 6.2375947
  },
  {
    "stateCode": "ZM",
    "state": "Zamfara",
    "lga": "Zurmi",
    "latitude": 12.1844159,
    "longitude": 6.2375947
  }
]

sum = 0
coordinates = db.lgas
for document in lga_list:
    post = coordinates.insert(document)
    print post
    sum += 1

print "Successfully bulk updated the Collection with ",sum," documents"