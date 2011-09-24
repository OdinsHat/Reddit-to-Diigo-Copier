Reddit to Diigo Copier
======================
A simple Python script for transferring Reddit saved links from your account 
to a Diigo account.

Usage
-----
Use the `-h` flag to get a full listing of command line options

`python r_todiigo.py -u rusername -p rpassword -v dusername -q dpassword`

Possible Issues
---------------
The Diigo API has quite a low usage limit so you will hit errors if you
try to move over hundreds of links at a time.

Requirements
------------
* [PyDiigo 0.2](http://pypi.python.org/pypi/pydiigo/0.2)
* [Mellort Reddit API](https://github.com/mellort/reddit_api)
