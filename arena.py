from setup import run_setup
from checkin import run_check
import os


USER_PATH = "data/user.json"



if os.path.exists(USER_PATH):
    run_check()
else:
    run_setup()

