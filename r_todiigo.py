# -*- coding: utf8 -*-
import praw
import pydiigo
import optparse

def transfer_links(ruser, rpass, duser, dpass, limit, unsave, apikey="f299650f020c5a7a", verbose=True):
    d = pydiigo.DiigoApi(user=duser, password=dpass, apikey=apikey)
    r = praw.Reddit(user_agent="Reddit to Diigo Copier")
    r.login(ruser, rpass)
    r_saves = r.user.get_saved(limit)

    for r_save in r_saves:
        res = d.bookmark_add(
            title=r_save.title.encode('utf-8'), 
            description=r_save.selftext[:249].encode('utf-8'), 
            url=r_save.url, 
            shared="no", 
            tags=r_save.subreddit.display_name
        )
        
        if unsave:
            r_save.unsave()

        if verbose:
            print res

if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option("-u", "--ru", dest="ruser", help="Reddit username")
    parser.add_option("-p", "--rp", dest="rpass", help="Reddit password")
    parser.add_option("-v", "--du", dest="duser", help="Diigo username")
    parser.add_option("-q", "--dp", dest="dpass", help="Diigo password")
    parser.add_option("-l", "--limit", dest="limit", default=25,
        help="How many saved links to process at once")
    parser.add_option("-m", "--move", dest="unsave", default=True,
        help="Move and delete from Reddit saves")

    (options, args) = parser.parse_args()
    transfer_links(options.ruser, options.rpass, options.duser, options.dpass, options.limit, options.unsave)
