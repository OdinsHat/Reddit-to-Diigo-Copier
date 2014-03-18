Reddit to Diigo Copier
======================
A simple Python script for transferring saved links from your Reddit account
to a Diigo account.

Usage
-----
Use the `-h` flag to get a full listing of command line options

`python red2dig.py --ru rusername --rp rpassword --du dusername --dp dpassword`

Recent Changes
--------------
And API key has now become necessary for ths to work.
This script has its own API key applied to it but please don't abuse this and consider obtaining your own.

Possible Issues
---------------
The Diigo API has quite a low usage limit so you will hit errors if you
try to move over hundreds of links at a time.

Requirements
------------
* [PyDiigo 0.5](http://pypi.python.org/pypi/pydiigo/0.2)
* [PRAW Library](https://github.com/mellort/reddit_api)
