"""Module for copying Reddit saved links to Diigo"""

__author__ = "Doug Bromley"
__copyright__ = "Doug Bromley"
__licese__ = "BSD"
__email__ = "Doug@tintophat.com"

import praw
import pydiigo
import sys

class RedditSaves:
    def __init__(self, username, password):
        self.red = praw.Reddit(user_agent="Reddit to Diigo Copier")
        self.username = username
        self.password = password
        self.limit = 10
        self.unsave = False

        try:
            self.red.login(username, password)
        except praw.errors.InvalidUserPass:
            print('Incorrect Reddit credentials')
            sys.exit(-1)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise


    def get_saved(self):
        reddit_saved_links = []
        reddit_saves = self.red.user.get_saved(self.limit)
        for reddit_save in reddit_saves:
            reddit_saved_links.append(reddit_save)
            if self.unsave:
                reddit_save.unsave()
        return reddit_saved_links

class DiigoSaver:
    def __init__(self, username, password, apikey="f299650f020c5a7a"):
        self.username = username
        self.password = password
        self.apikey = apikey
        self.diigo = pydiigo.DiigoApi(user=self.username, password=self.password, apikey=self.apikey)

    def save_to_diigo(self, reddit_saves):
        for reddit_save in reddit_saves:
            res = self.diigo.bookmark_add(
                title=reddit_save.title.encode('utf-8'),
                description=reddit_save.selftext[:10].encode('utf-8'),
                url=reddit_save.url,
                shared="no",
                tags="reddit"
            )
            print(res)