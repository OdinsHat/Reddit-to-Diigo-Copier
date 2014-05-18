#!/usr/bin/env python
# -*- coding: utf8 -*-
from reddittodiigo import RedditSaves
from reddittodiigo import DiigoSaver
import argparse
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        usage='Copy your saved Reddit links to a Diigo account',
        description='Your Reddit and Diigo credentials'
    )
    parser.add_argument("-u", "--ru", dest="ruser", help="Reddit username")
    parser.add_argument("-p", "--rp", dest="rpass", help="Reddit password")
    parser.add_argument("-v", "--du", dest="duser", help="Diigo username")
    parser.add_argument("-q", "--dp", dest="dpass", help="Diigo password")
    parser.add_argument("-l", "--limit", dest="limit", default=25,
        help="How many saved links to process at once")
    parser.add_argument("-m", "--move", dest="unsave", default=True,
        help="Move and delete from Reddit saves")

    args = parser.parse_args()

    if not args.ruser or not args.rpass or not args.duser or not args.dpass:
        parser.print_help()
        sys.exit(-1)

    r = RedditSaves(args.ruser, args.rpass)
    d = DiigoSaver(args.duser, args.dpass)

    d.save_to_diigo(r.get_saved())