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

def main():
    pass

if __name__ == "__main__":
    main()
