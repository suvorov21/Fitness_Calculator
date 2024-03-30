def food():
    """
    Function that takes eaten food as input and returns quantity of calories as output
    """
    test_dict = {
        "dry rice" : 355, "wheat bread" : 260, "banana" : 90, "dark chocolate" : 550, "beef" : 250,
        "chicken breast" : 165
        }
    # Ask what food user ate
    eaten_food = input("Indicate the ingredient you ate please:\n")
    # Ask quantity of eaten food in grams
    food_mass = int(input("How much did you eat?(in grams)\n"))
    if eaten_food in test_dict:
        eaten_calories = round((test_dict[eaten_food] * food_mass / 100), 1)
    else:
        eaten_calories = "nuzhno dorabotat"
    return eaten_calories

# print(food())

