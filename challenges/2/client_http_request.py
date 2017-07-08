"""RH 'monitoring'"""

# Dependencies
import random
from threading import Timer
import json
import requests

# The list of samples, and the sample rate are declared globally.
SAMPLE_LIST = []
RATE = 0.5

# I'm going to send requests based on this counter.
COUNT = 0

# []======================================================[]
# []      Define RH Sim, and Data Sampling Functions
# []======================================================[]

# Simulate the Relative Humidity Measurement.
def random_generator():
    """Return a random number between 56.00 and 78.00"""
    return random.uniform(56.00, 78.00)

# Take the simulated float number, and truncate it.
def sample():
    """sample rate for grabbing data from the simulated RH sensor."""
    truncated_sample = '%.2f' % random_generator()
    return truncated_sample

# Manage the 'buffer' where these measurements are kept.
def record_sample():
    """Insert a new data point into a list, shifting old items off the list."""
    global COUNT

    #Increment COUNT
    COUNT += 1

    # Run the sampler 30 times
    if COUNT < 31:
        if len(SAMPLE_LIST) < 10:
            SAMPLE_LIST.insert(0, sample())

            # function call to send POST request
            make_request()
        else:
            SAMPLE_LIST.insert(0, sample())
            SAMPLE_LIST.pop()

            # function call to send POST request
            make_request()

        #Recursively Call Timer function to self-invoke the record_sample function.
        Timer(RATE, record_sample).start()
    else:
        print('Demonstration Ended.')


# []======================================================[]
# []                    Server Comms
# []======================================================[]

# This time we are going to set up a nice set of post params.

def make_request():
    """Make request to the automation server"""

    # Define the type of content you intend to post.
    headers = {'content-type':'application/json'}

    # Our URL, same IP/Port as challenge #1, with the route '/rh_measurements'
    url = "http://localhost:8000/rh_measurements"

    # plug the list of samples into a data 'Dictionary'
    data = {'rh_measurements': SAMPLE_LIST}

    # Only send requests when the list has one item, or ten items.
    if len(SAMPLE_LIST) == 1:
        req1 = requests.post(url, data=json.dumps(data), headers=headers)
        print(req1.status_code)
    elif len(SAMPLE_LIST) == 10:
        req2 = requests.post(url, data=json.dumps(data), headers=headers)
        print(req2.status_code)

"""
00: The first parameter of Timer is looking for a value in seconds.
01: The second paramter of Timer is looking for a function to execute.
02: Timer is not an interval, it needs to be called recursively.
03: We call the start method for the Timer, immediately after defining it's params.
"""
Timer(RATE, record_sample).start()
