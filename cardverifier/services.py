from typing import List, Set, Dict, Tuple, Optional
from .utils import is_luhn_valid, identify_card


def validate_card_number(card_number: str) -> Dict:
    card_number = card_number.replace(" ", "")
    if not is_luhn_valid(card_number):
        return {"valid": False}

    emisor = identify_card(card_number)

    data = {
        "valid": True,
        "emisor": emisor
    }

    return data
