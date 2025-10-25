import json

def max_age():
    try:
        data = {
            'Ali': 23,
            'Saad': 24,
            'Salman': 15,
            'Shams': 25,
            'Sadiq': 46,
            'Hammad': 23
        }

        with open("data.json", "w") as f:
            json.dump(data, f)
        print("Dictionary saved to data.json")

        with open("data.json", "r") as f:
            loaded_data = json.load(f)

        max_age = max(loaded_data.values())
        oldest = [name for name, age in loaded_data.items() if age == max_age]

        print(f"\nMaximum Age: {max_age}")
        print("Person(s) with maximum age:", ", ".join(oldest))

        age_groups = {}
        for name, age in loaded_data.items():
            if age not in age_groups:
                age_groups[age] = []
            age_groups[age].append(name)

        print()
        for age, people in age_groups.items():
            if len(people) > 1:
                print(f"People with same age ({age}): {', '.join(people)}")

    except FileNotFoundError:
        print("Error: data.json file not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON data.")
    except Exception as e:
        print("Unexpected Error:", e)

max_age()
