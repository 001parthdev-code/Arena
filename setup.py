import os 
import json
from datetime import datetime

def run_setup():

    user_file = "data/user.json"

    if os.path.exists(user_file):
        print("Setup already completed.")
        return



    vague = {"may", "maybe", "learn", "want"}
    name = input("Name: ")

    while True:
        goal = input("Goal: ")
        if any(word in goal.lower() for word in vague):
            print("Too vague. What will you ship in 7 days?")
        else: 
            break
        
       

    created_at = datetime.now().isoformat()
    start_date = datetime.now().date().isoformat()

    user_data = {
        "name": name,
        "goal": goal,
        "created_at": created_at,
        "start_date": start_date
    }

    os.makedirs("data", exist_ok=True)

    with open(user_file, "w") as f:
        json.dump(user_data, f, indent=2)

    print("\nSetup complete.")

