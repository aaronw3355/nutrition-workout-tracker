import json

MEAL_FILE = "meals.json"
WORKOUT_FILE = "workouts.json"
CALORIE_GOAL_FILE = "calorie_goal.json"

def load_data(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def add_meal(meals):
    food = input("Food name: ")
    calories = int(input("Calories: "))
    protein = int(input("Protein (g): "))
    carbs = int(input("Carbs (g): "))
    fat = int(input("Fat (g): "))

    meals.append({
        "food": food,
        "calories": calories,
        "protein": protein,
        "carbs": carbs,
        "fat": fat
    })

def add_workout(workouts):
    exercise = input("Exercise name: ")
    duration = int(input("Duration (minutes): "))
    calories = int(input("Calories burned: "))

    workouts.append({
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    })


def main():
    pass

if __name__ == "__main__":
    main()
