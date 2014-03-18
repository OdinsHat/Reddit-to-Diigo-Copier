# -*- coding: utf8 -*-
from reddittodiigo import RedditSaves
from reddittodiigo import DiigoSaver
import optparse

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

    r = RedditSaves(options.ruser, options.rpass)
    d = DiigoSaver(options.duser, options.dpass)

    d.save_to_diigo(r.get_saved())
