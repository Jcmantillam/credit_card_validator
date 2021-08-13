
API_SERVICE = 'api/v1/verify_card'


'''
Based on https://es.wikipedia.org/wiki/N%C3%BAmero_de_tarjeta_bancaria
IIN table updated at 27 may 2021
'''
card_types = {
    "american_express": {
        "IIN_length": [("34,37", 15)],
        "Brand": "American Express"
    },
    "diners_club": {
        "IIN_length": [
            ("300-305,309,36,38-39", 14),
            ("54,55", 16),
        ],
        "Brand": "Diners Club"
    },
    "discover": {
        "IIN_length": [
            ("6011,622126-622925,644-649,65", 16)
        ],
        "Brand": "Discover"
    },
    "jbc": {
        "IIN_length": [
            ("3528-3589", 16),
            ("3", 16)
        ],
        "Brand": "JBC"
    },
    "mastercard": {
        "IIN_length": [
            ("222100-272099,51-55", 16)
        ],
        "Brand": "MasterCard"
    },
    "visa": {
        "IIN_length": [
            ("4", 13),
            ("4", 16),
        ],
        "Brand": "Visa"
    },
}