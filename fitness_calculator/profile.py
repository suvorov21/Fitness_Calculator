"""
Class to represent a user
"""
class User:
    def __init__(self, first, last, sex, age, weight, height):
        self.first = first
        self.last = last
        self.age = age
        self.sex = sex
        self.weight = weight
        self.height = height

    def __repr__(self):
        return f"It is {self.first}"

    def set_goal(self,  weight_goal):
        self.weight_goal = weight_goal
        return weight_goal
    def days_to_goal(self, days):
        self.days = days
        return days
    def level(self, level_of_activity):
        self.level_of_activity = level_of_activity
        return level_of_activity


# alex = User('Alex', 'Bes', 'men', 28, 85, 180)
