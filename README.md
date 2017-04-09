# strava-friends-activities
Lists rides from your Strava friends, filtered by length / distance from home

Currently gets your friends' activities, filtered by the following criteria:
    - Activity length > 100km
    - Start or End of activity within 10km of your home (as defined in constants.HOME_LOC)

Returns 10 most recent matching results.

Ideas for improvement:
  - min / max activity length as command line arguments
  - max distance from home as command line argument
  - specify umber of results to be returned
  - return results newer than date / older than date
  - make it into a web app
