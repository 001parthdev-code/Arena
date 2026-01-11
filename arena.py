from setup import run_setup
import os


USER_PATH = "data/user.json"



if os.path.exists(USER_PATH):
    print("Check in")
else:
    run_setup()

