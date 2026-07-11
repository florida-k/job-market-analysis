# this file is to test that if the id and key in .env can be used properly

## think of this file like the if statement ot check if a file is opened properly

from dotenv import load_dotenv
import os

# dotenv is a package that allows Python to read values stored in a .env file
# os allows Python to interact with the computer's environment variables

# load_dotenv() loads the information from the .env file into the Python environment

load_dotenv()

API_ID = os.getenv("API_ID")
API_KEY = os.getenv("API_KEY")

print(f"API_ID = {API_ID}")
print(f"API_KEY = {API_KEY}")

# works properly