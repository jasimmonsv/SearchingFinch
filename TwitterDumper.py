#! /usr/bin/python
"""
GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007
See LICENSE file from git repository

https://github.com/jasimmonsv/??????????????????

Just a quick app that will return the Twitter timeline of a given user

Args:
XML_FILE: file of the xml document

Requirements:
git clone git://github.com/kennethreitz/requests.git
python ./requests/setup.py install

"""

import json
import requests

config = {}
execfile("config.py", config)
auth = OAuth1(config["access_key"], config["access_secret"],
            config["consumer_key"], config["consumer_secret"])



def main():
    """
    Args:
        N/A
    Returns:
        N/A
    Raises:
        N/A
    """
    #TODO Read in variables
    #TODO Read in request
    r = requests.get('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=twitterapi&count=200',
                    auth=auth)
    r.status_code
    r.headers['content-type']
    r.encoding
    r.text
    r.json()
    #TODO submit request
    #TODO process output
    quit();

if __name__ == '__main__':
    main()
