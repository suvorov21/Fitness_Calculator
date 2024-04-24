from profile import User
from nutrition_goal import nutrition_goal
import test_data
from workout_goal import workout_daily_goal
from eaten_food import food

def users_data():
    user = User("Alex", "Besouro", "man", 28, 85, 180)
    weight_goal = user.set_goal(80)  # Ask user to input desired weight
    level_of_activity = user.level(2)  # Ask user to input activity level in range 1-3
    days = user.days_to_goal(60)  # Ask user to input number of days to achieve desired weight
    return user

user_1 = users_data()


def main(user):
    ndc = nutrition_goal(user.sex, user.age, user.weight, user.height, user.weight_goal, user.days, user.level_of_activity)
    print(f"Your recommended amount of calories per day to reach your goal is {ndc}")
    daily_workout = 0
    add_exercise = True
    while add_exercise:
        print("Please enter what exercise did you done: \n")    # Ask user to input an exercise.
                                                                # Put it into daily_workout function as exercise type
        daily_workout += workout_daily_goal("running", test_data.AEROBIC, test_data.ANAEROBIC)
        add_exercise = False    # Ask user if he wants to add another exercises

    if test_data.CALORIES_PER_TRAINING - daily_workout > 0:
        print(f"Today you have burned {daily_workout}, you have {test_data.CALORIES_PER_TRAINING - daily_workout} "
              f"to accomplish your daily norm ")
    else:
        print(f"You did great job, you have burned {daily_workout} calories")

    eaten_calories = 0
    add_food = True
    while add_food:
        print("Please enter what food and how much of it did you eat: \n")  # Ask user to input an eaten food.
                                                                            # Put it into food function as eaten food
        eaten_calories += food("dry rice", 100, test_data.TEST_FOOD)
        add_food = False    # Ask user if he wants to add another exercises

    if ndc - eaten_calories < 0:
        print(f"Today you have eat {eaten_calories}, it is more than your daily goal on {eaten_calories - ndc} calories")
    else:
        print(f"Today you have eat {eaten_calories}, you can eat {ndc - eaten_calories} more")

    return None

print(main(user_1))