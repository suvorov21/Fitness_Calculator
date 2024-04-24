import test_data


def aerobic_training(exercise_type: str, aerobic_dict: dict, exercise_time: int, intensity: int) -> int:
    """Function to calculate number of burned calories with aerobic type of exercise"""
    if intensity == 1:
        factor = 1
    elif intensity == 2:
        factor = 1.2
    else:
        factor = 1.4
    burned_calories = round(aerobic_dict[exercise_type] * (exercise_time / 60) * factor, 2)
    return burned_calories


def anaerobic_training(exercise_type: str, anaerobic_dict: dict, exercise_sets: int,
                       exercise_repetition: int, exercise_rate: int) -> int:
    """Function to calculate number of burned calories with anaerobic type of exercise"""
    # exercise_rate -- approximately what percentage of the maximum load this set was performed
    burned_calories = (anaerobic_dict[exercise_type] * exercise_sets * exercise_repetition * (exercise_rate / 100))
    return burned_calories

def workout_daily_goal(exercise_type: str, aerobic_dict: dict, anaerobic_dict: dict) -> int:
    """Function that takes exercise as input and returns quantity of burned calories as output """

    if exercise_type in aerobic_dict:
        # ASK USER FOR INPUT OF exercise_time, intensity?
        burned_calories = aerobic_training(exercise_type, aerobic_dict, exercise_time=30, intensity=2)
    else:
        # ASK USER FOR INPUT OF exercise_sets, exercise_repetition, exercise_rate?
        burned_calories = anaerobic_training(exercise_type, anaerobic_dict, exercise_sets=10, exercise_repetition=10,
                                             exercise_rate= 80)


    print(f"You have burned {burned_calories} by doing this exercise!")

    return burned_calories

# print(workout_daily_goal("running", test_data.AEROBIC, test_data.ANAEROBIC))