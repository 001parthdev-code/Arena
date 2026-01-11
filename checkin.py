import os
import json
from datetime import datetime

def run_check():
    checkin_file = "data/log.json"
    today = datetime.today().isoformat()

    if os.path.exists(checkin_file):
        try:
            with open(checkin_file, "r") as f:
                checkins = json.load(f)
        except json.JSONDecodeError:
            checkins = []
        
    else:
        checkins = []



    #Prevent multiple check-ins per day
    for entry in checkins:
        if entry["date"] == today:
            print("Already checked in")
            return
        
        
    # Ask the question
    while True:
        answer = input("Did you ship today? (y/n): ").strip().lower()

        if answer in {"y", "yes"}:
            status = "yes"
            break
        elif answer in {"n", "no"}:
            status = "no"
            break
        else:
            print("Invalid input. Enter y or n.")

    # Record check-in
    checkins.append({
        "date": today,
        "status": status
    })

    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)

    # Write back to disk
    with open(checkin_file, "w") as f:
        json.dump(checkins, f, indent=2)

    print("Check-in recorded.")