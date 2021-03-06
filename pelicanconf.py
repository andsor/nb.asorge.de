#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Andreas Sorge'
SITENAME = 'Notebooks'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS = ()

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DEFAULT_DATE = 'fs'

MARKUP = ('md', )

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['liquid_tags.notebook', 'interlinks']

THEME = 'pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'

IGNORE_FILES = ['README.md']

STATIC_PATHS = ['extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }

INTERLINKS = {
    'nbviewer': 'http://nbviewer.ipython.org/github/andsor/notebooks/blob/master/notebooks/',
    'pdf':      'https://github.com/andsor/notebooks/raw/master/notebooks/'
}

CC_LICENSE = "CC-BY"
