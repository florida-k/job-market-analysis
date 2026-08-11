# Job Market Analysis
A project exploring job market trends.

## Project Structure
A common way to do any project is to first get input the processing followed by output .

input - web scraping using APIs.(An API (Application Programming Interface) is a way for one program to ask another
program for information. Another program here stands for webstites that collect data. you can ask for what u need and 
they will provide it.  )
    

## Goals
Make a website where people can look up a job and see the common jobs available currently and see the job market 
expectations and predictions for the future.

## Tech Stack
- **Python 3.10+**
- **pandas** — data manipulation
- **NumPy** — numerical operations
- **Matplotlib** — visualization?
- **Jupyter** — exploratory notebooks?


## Steps

1. Made a Git repository and cloned it.

2. Learned about the common structure used for software projects.

    - input -> processing -> output

3. Decided to use an API as the input source.

4. Chose Adzuna as the API source.(Mostly provides career information,jobs etc)
   - Created an account.
   - Received an API ID and API key.

5. Created an `.env` file to store the API ID and API key.

6. Created a `.gitignore` file and added `.env` so the credentials will not be shared when committed to Git.

   - `.env` and `.gitignore` are files that were created in the project root.
   - `.venv/` is the existing virtual environment folder and is not the file to use.

7. Made a file `.env_testing` to see if the .env file can be used properly

    - I had to install package and (pip freeze > requirements.txt)in git to see the package in req.txt

8. Made a file `adzuna_testing` to see if i can retrieve data from adzuna properly for the project

    - We usee the same approach from .envtesting to read api id and key
    - Learned to request from Adzuna
    - received data in json format(like a dictionary)
    - stored it in a list

9. Made file `api` that has a function to get data from adzuna and use it for the project
10. 