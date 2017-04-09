#!/usr/bin/env python

from client import client
from helpers import matches_criteria, get_min_dist, km
from pprint import pprint


def get_match_candidates():

    matches = list()

    print "Getting friend activities"
    friend_activities_iterator = client.get_friend_activities()

    while len(matches) < 10:
        activity = friend_activities_iterator.next()
        print "Considering activity %s" % activity.id
        if matches_criteria(activity):
            matches.append(activity)
            print "Added %s" % activity.id
        else:
            print "Disregarding %s" % activity.id

    for match in matches:
        print "\n"
        print u"Name: %s, Length: %s, Dist from home: %.2f" % (match.name, km(match.distance), get_min_dist(match))
        print u"URL: https://www.strava.com/activities/%s" % match.id


if __name__ == "__main__":
    get_match_candidates()
