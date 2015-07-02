#! /usr/bin/python
"""
GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007
See LICENSE file from git repository

https://github.com/jasimmonsv/SearchingFinch

Just a quick app that will return at most 200 of the most recent tweets from the
timeline of a given user. Software will pull auth variables from the config.py
file.

Args:
    screen_name: Default screen name to grab timeline from (default: twitterapi)
    count: Number of tweets to grab (default:200)
    max_id: the max tweet id that will be returned (grab older then...)
    trim_user: When set to either true, t or 1, each tweet returned in a
               timeline will include a user object including only the status
               authors numerical ID. Omit this parameter to receive the complete
               user object.
               (default: true)
    exclude_replies: This parameter will prevent replies from appearing in the
                     returned timeline. Using exclude_replies with the count
                     parameter will mean you will receive up-to count tweets -
                     this is because the count parameter retrieves that many
                     tweets before filtering out retweets and replies. This
                     parameter is only supported for JSON and XML responses.
                     (default: true)
    include_rts: When set to false, the timeline will strip any native retweets
                 (though they will still count toward both the maximal length of
                 the timeline and the slice selected by the count parameter).
                 Note: If you're using the trim_user parameter in conjunction
                 with include_rts, the retweets will still contain a full user
                 object.
                 (default: false)

Returns:
    Returns json data

Requirements:
    Requests:
        git clone git://github.com/kennethreitz/requests.git
        python ./requests/setup.py install

    Requests-oauthlib:
        git clone https://github.com/requests/requests-oauthlib
        python ./requests/setup.py install
"""

import json
import requests
from requests_oauthlib import OAuth1

config = {}
execfile("config.py", config)
auth = OAuth1(config["consumer_key"],
              config["consumer_secret"],
              config["access_key"],
              config["access_secret"])


def SearchingFinch(screen_name='twitterapi',
                   count='200',
                   max_id='',
                   trim_user='true',
                   exclude_replies='true',
                   include_rts='false'):
    """
    Args:
        N/A
    Returns:
        N/A
    Raises:
        N/A
    """
    request_url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=%s&count=%s&trim_user=%s&exclude_replies=%s&include_rts=%s&max_id=%s' % \
                  (screen_name,
                   count,
                   trim_user,
                   exclude_replies,
                   include_rts,
                   max_id)
    # GO GO GO
    r = requests.get(request_url, auth=auth)
    return r.json

if __name__ == '__main__':
    import sys
    # SearchingFinch(int(sys.argv[0]))
    SearchingFinch()
