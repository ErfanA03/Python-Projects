
#Import Modules
import datetime
"""
We'll use this library for time zone calculations.
Keep in mind that if you get an error for "pytz", it
is most likely because you don't have it installed
in your python environment. In that case, open up
your command prompt or terminal and run the following:
'pip install pytz' (Assuming you already have pip installed, Python 2.7.9 and Python 3.4 and later versions include pip by default.)
"""
import pytz  

# Define the time zones for Portland, NYC, and London
portland_timezone = pytz.timezone('America/Los_Angeles')  # Pacific Time Zone (Portland)
nyc_timezone = pytz.timezone('America/New_York')  # Eastern Time Zone (NYC)
london_timezone = pytz.timezone('Europe/London')  # Greenwich Mean Time (London)

# Get the current time in each branch's time zone
portland_time = datetime.datetime.now(portland_timezone)
nyc_time = datetime.datetime.now(nyc_timezone)
london_time = datetime.datetime.now(london_timezone)

# Define the opening and closing hours for the branches
branch_hours = {
    'Portland': (datetime.time(9, 0), datetime.time(17, 0)),
    'NYC': (datetime.time(9, 0), datetime.time(17, 0)),
    'London': (datetime.time(9, 0), datetime.time(17, 0))
}

# Function to check if a branch is open or closed
def is_branch_open(branch_name, current_time):
    open_time, close_time = branch_hours[branch_name]
    return open_time <= current_time.time() <= close_time

# Check if each branch is open or closed
portland_open = is_branch_open('Portland', portland_time)
nyc_open = is_branch_open('NYC', nyc_time)
london_open = is_branch_open('London', london_time)

# Print the status of each branch
"""
The "f" before every string denotes that we want to format it,
This is known as an f-string in Python. F-strings are a way to
format strings by allowing you to embed expressions inside string
literals, using curly braces {}. It's another way to format string
without having to use the .format() method.
"""
print(f'Portland branch is {"open" if portland_open else "closed"}')
print(f'NYC branch is {"open" if nyc_open else "closed"}')
print(f'London branch is {"open" if london_open else "closed"}')
