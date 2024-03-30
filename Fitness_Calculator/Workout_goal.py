def workout_daily_goal() -> int:
    """
    Function that takes exercise as input and returns quantity of burned calories as output
    """
    aerobic = {"running" : 650, "swimming" : 350, "rope jumping" : 400, "bicycling" : 300}
    anaerobic = {"arms" : 2.25, "legs" : 4.75, "abs" : 1.75}
    exercise_type = input("What exercise did you do today?():\n")
    if exercise_type in aerobic:
        exercise_time = int(input("For how long have you been doing this exercise?(in minutes):\n"))
        burned_calories = round(aerobic[exercise_type] * (exercise_time / 60), 2)
    else:
        exercise_sets = int(input("How many sets have you completed?\n"))
        exercise_repetition = int(input("How many repetition did you do in this set?:\n"))
        exercise_rate = int(input("Indicate approximately what percentage of the maximum load this set was performed with\n"))
        burned_calories = (anaerobic[exercise_type] * exercise_sets * exercise_repetition * (exercise_rate / 100))

    if burned_calories >= 500:
        return f"You have completed your daily training norm. Congratulations!\nP.S You have burned {burned_calories} calories"
    else:
        return f"You have burned {burned_calories} calories. {500 - burned_calories} calories until the end of the norm"

print(workout_daily_goal())