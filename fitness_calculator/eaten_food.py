from test_data import *


def food(eaten_food: str, food_mass: int, ingredients_dict: dict) -> int:
    """
    Function that takes eaten food as input and returns quantity of calories as output
    """
    if eaten_food in ingredients_dict:
        eaten_calories = round((ingredients_dict[eaten_food] * food_mass / 100), 1)
    else:
        raise NotImplementedError("Some error")
    return eaten_calories


# print(food("dry rice", 100, TEST_FOOD))
