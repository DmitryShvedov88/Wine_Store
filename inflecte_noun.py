# library for declension of nouns next to numerals
def inflecte_noun(age) -> str:
    """Function for noun declension"""
    if age % 100 >= 11 and age % 100 <= 14:
        inflecte = "лет"
    elif age % 10 == 1:
        inflecte = "год"
    elif age % 10 == 2 or age % 10 == 3 or age % 10 == 4:
        inflecte = "года"
    else:
        inflecte = "лет"
    return inflecte
