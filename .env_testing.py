# this file is to test that if the id and key in .env can be used properly

## think of this file like the if statement ot check if a file is opened properly

from dotenv import load_dotenv
import os

load_dotenv()

API_ID = os.getenv("API_ID")
API_KEY = os.getenv("API_KEY")

print(f"API_ID = {API_ID}")
print(f"API_KEY = {API_KEY}")

# works properly