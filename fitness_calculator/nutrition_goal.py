import math
"""
Glossary :

BMR -- Basal metabolic rate
TDEE -- Total Daily Energy Expenditure
DPD -- Deficit of calories per day
NDC -- Number of daily calories


"""
def nutrition_goal(sex, age, weight, height, weight_goal, days_to_goal, level_of_activity) -> int:
    """
    Function to calculate the number of calories for daily consumption
    """

    # Using Mifflin-St Jeor Equation calculate a basal metabolic rate
    if sex == "men":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    # print(bmr)

    # Calculate total daily energy expenditure
    if level_of_activity == 1:
        tdee = bmr * 1.25
    elif level_of_activity == 2:
        tdee = bmr * 1.5
    else:
        tdee = bmr * 1.75
    # print(tdee)

    # Calculate the required calorie deficit
    dpd = math.ceil(((weight - weight_goal) * 8000) / days_to_goal) # 8000 approximate number of calories needed to burn 1 kg
    # print(DPD)

    # Calculate the number of calories for daily consumption
    ndc = tdee - dpd

    return ndc


# nutrition_goal("men", 28,85, 180, 80, 60, 2)