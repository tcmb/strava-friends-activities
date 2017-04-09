# Strava Friends' Activities Filter

A Python script to list rides from your Strava friends, filtered by length of the ride and distance from your home

## Current capabilities

Currently gets your friends' activities, filtered by the following criteria:
    - Activity length > 100km
    - Start or End of activity within 10km of your home

Returns 10 most recent matching results.

## How to use it

Prerequisites:
  - You need a Strava developer account (make it at https://www.strava.com/settings/api)
  - Insert your access token in a constant `ACCESS_TOKEN` in a local file `secrets.py`
  - Insert the latitude and longitude of your home location in `constants.HOME_LOC`
  - Python 2.7, use of virtualenv is recommended
  - The stravalib Strava API bindings from https://github.com/hozn/stravalib
  - Friends on Strava :) (i.e., people you follow)

When the prerequisites are fulfilled, just run `./friends_activities_filter.py`.

## Ideas for improvement:

  - min / max activity length as command line arguments
  - max distance from home as command line argument
  - specify umber of results to be returned
  - return results newer than date / older than date
  - make it into a web app
