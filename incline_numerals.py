# library for declension of nouns next to numerals
def incline(x) -> str:
    """Matches a noun to a numeral"""
    if x % 100 >= 11 and x % 100 <= 14:
        inclined = "лет"
    elif x % 10 == 1:
        inclined = "год"
    elif x % 10 == 2 or x % 10 == 3 or x % 10 == 4:
        inclined = "года"
    else:
        inclined = "лет"
    return inclined
