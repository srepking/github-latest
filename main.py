import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    #username = sys.argv[1]

    # TODO:
    #
    # 1. Retrieve a list of "events" associated with the given user name
    # 2. Print out the time stamp associated with the first event in that list.
    username = 'JASchilz'
    user_events = requests.get('https://api.github.com/users/{}/events/public'.format(username))
    first_event_time = user_events.json()[0]['created_at']

    print("The first public event listed for username {} was created at {}.".format(username, first_event_time))
    


