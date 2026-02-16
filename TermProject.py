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

def load_calorie_goal():
    try:
        with open(CALORIE_GOAL_FILE, "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return None


def save_calorie_goal(goal):
    with open(CALORIE_GOAL_FILE, "w") as file:
        file.write(str(goal))


def set_calorie_goal():
    goal = int(input("Enter your daily calorie goal: "))
    save_calorie_goal(goal)
    print(f"Daily calorie goal set to {goal} calories.")

def show_nutrition_summary(meals):
    total_cal = sum(m["calories"] for m in meals)
    total_protein = sum(m["protein"] for m in meals)
    total_carbs = sum(m["carbs"] for m in meals)
    total_fat = sum(m["fat"] for m in meals)

    goal = load_calorie_goal()

    print("\nNutrition Summary")
    print(f"Calories consumed: {total_cal}")
    print(f"Protein: {total_protein} g")
    print(f"Carbs: {total_carbs} g")
    print(f"Fat: {total_fat} g")

    if goal:
        remaining = goal - total_cal
        if remaining >= 0:
            print(f"Calories remaining: {remaining}")
        else:
            print(f"Calories over goal: {-remaining}")


def show_workout_summary(workouts):
    total_time = sum(w["duration"] for w in workouts)
    total_burned = sum(w["calories"] for w in workouts)

    print("\nWorkout Summary")
    print(f"Total workout time: {total_time} minutes")
    print(f"Calories burned: {total_burned}")
def main():
    pass

if __name__ == "__main__":
    main()
