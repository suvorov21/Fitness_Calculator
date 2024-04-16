from test_data import *


def aerobic_training(exercise_type: str, aerobic_dict: dict) -> int:
    """Function to calculate number of burned calories with aerobic type of exercise"""
    exercise_time = 30  # Ask user to input a number of minutes spent on exercise
    intensity = 2   # Ask user to indicate level of intensity during exercise
    if intensity == 1:
        factor = 1
    elif intensity == 2:
        factor = 1.2
    else:
        factor = 1.4
    burned_calories = round(aerobic_dict[exercise_type] * (exercise_time / 60) * factor, 2)
    return burned_calories


def anaerobic_training(exercise_type: str, anaerobic_dict: dict) -> int:
    """Function to calculate number of burned calories with anaerobic type of exercise"""
    # exercise_rate -- approximately what percentage of the maximum load this set was performed
    exercise_sets = 10 # Ask user to input a number of sets of this exercise performed
    exercise_repetition = 10 # Ask user to input a number repetition during one set
    exercise_rate = 80 # Ask user to input an approximate load percentage of maximum
    burned_calories = (anaerobic_dict[exercise_type] * exercise_sets * exercise_repetition * (exercise_rate / 100))
    return burned_calories

def workout_daily_goal(exercise_type: str, aerobic_dict: dict, anaerobic_dict: dict) -> int:
    """Function that takes exercise as input and returns quantity of burned calories as output """

    if exercise_type in aerobic_dict:
        burned_calories = aerobic_training(exercise_type, aerobic_dict)
    else:
        burned_calories = anaerobic_training(exercise_type, anaerobic_dict)


    print(f"You have burned {burned_calories} by doing this exercise!")

    return burned_calories

# print(workout_daily_goal("running", AEROBIC, ANAEROBIC))