from typing import List, Set, Dict, Tuple, Optional
from .constants import card_types


'''
Validates the card number with the rules added in constants
'''
def validate_rule(emission_rules: Dict, card_number: str) -> bool:
    for rule in emission_rules:
        length = rule[1]
        if len(card_number) != length:
            continue
        IIN_list = rule[0].split(",")
        for IIN in IIN_list:
            if "-" in IIN:
                min, max  = IIN.split("-")
                number = int(card_number[:len(min)])
                if int(min) <= number <= int(max):
                    return True
            else:
                number = int(card_number[:len(IIN)])
                if int(IIN) == number:
                    return True
    return False

#Calling the rules methods
def is_american_express(card_number: str) -> bool:
    emission_rules = card_types["american_express"]["IIN_length"]
    return validate_rule(emission_rules, card_number)


def is_diners_club(card_number: str) -> bool:
    emission_rules = card_types["diners_club"]["IIN_length"]
    return validate_rule(emission_rules, card_number)


def is_discover(card_number: str) -> bool:
    emission_rules = card_types["discover"]["IIN_length"]
    return validate_rule(emission_rules, card_number)


def is_jcb(card_number: str) -> bool:
    emission_rules = card_types["jbc"]["IIN_length"]
    return validate_rule(emission_rules, card_number)


def is_mastercard(card_number: str) -> bool:
    emission_rules = card_types["mastercard"]["IIN_length"]
    return validate_rule(emission_rules, card_number)


def is_visa(card_number: str) -> bool:
    emission_rules = card_types["visa"]["IIN_length"]
    return validate_rule(emission_rules, card_number)


#Luhn Algorithm
def luhn_checksum(card_number: str) -> int:
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10


def is_luhn_valid(card_number: str) -> bool:
    return luhn_checksum(card_number) == 0


def identify_card(card_number: str) -> str:
    if is_american_express(card_number):
        return "American Express"
    elif is_diners_club(card_number):
        return "Diners Club"
    elif is_discover(card_number):
        return "Discover"
    elif is_jcb(card_number):
        return "JCB"
    elif is_mastercard(card_number):
        return "MasterCard"
    elif is_visa(card_number):
        return "Visa"
    else:
        return "Unknown"
