#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'charlesreid1'

SITENAME = u'scurvy knave pelican theme'

SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# --------------8<---------------------

THEME = 'scurvy-knave-theme'

# Pelican is designed for files => pages.
# Use variables (below) to set pieces of pages.

TOPHEADCOLOR = "#c0deed"
ACOLOR = "#00aced"
AHOVERCOLOR = "#0084b4"
TEMPLATE_PAGES = {
    'custom.css' : 'custom.css'
}

# ---

# description appears between <p> tags, so don't include them

SITE_TITLE = "bots.charlesreid1.com"
SITE_DESCRIPTION = "a subdomain for charlesreid1 bots"

# ---

# include <p> tags in the description

ABOUT_TITLE = "about bots.charlesreid1.com"

ABOUT_DESCRIPTION = """

<p><b>What is a bot?</b></p>

<p>Broadly, a bot is an autonomous entity that executes a program.<br />
The bots on this site are principally Twitter bot flocks.<br />
Also see <a href="https://twitter.com/horse_ebooks">@horse_ebooks</a>.</p>

<p><b>What is a bot flock?</b></p>

<p>A bot flock is a group of Twitter bots that perform a related task,
access related data, or otherwise share some structure.<br />
See below for examples of Twitter bot flocks.</p>

<p><b>Where can I find the bots?</b></p>

<p>Each bot has a home page on bots.charlesreid1.com; see below for links.</p>
"""

# ---

# include <p> tags in the description

LINKS_TITLE = "links on bots.charlesreid1.com"

LINKS_DESCRIPTION = """
<p>Kadishtu n'ghft gof'nn fm'latgh Azathoth lloig chtenff hafh'drn shoggyar.</p>
<p>Ya nog Azathoth ah R'lyeh Chaugnar hupadgh kn'a hlirgh Nyarlathotep.</p>"""

FLOCK_URL = "https://twitter.com/charlesreid1/lists/miltonbotflock"

LINKS_BUTTONS = """<p><a href="%s" class="btn btn-default btn-lg"><i class="fa fa-twitter fa-fw"></i> Bot Flock</a></p>
<p>
<a href="https://twitter.com/milton_book1"  class="btn btn-default btn-lg">@milton_book1</a> &nbsp; &nbsp; &nbsp; 
<a href="https://twitter.com/milton_book2"  class="btn btn-default btn-lg">@milton_book2</a> &nbsp; &nbsp; &nbsp; 
<a href="https://twitter.com/milton_book3"  class="btn btn-default btn-lg">@milton_book3</a>
</p><p>
<a href="https://twitter.com/milton_book4"  class="btn btn-default btn-lg">@milton_book4</a> &nbsp; &nbsp; &nbsp; 
<a href="https://twitter.com/milton_book5"  class="btn btn-default btn-lg">@milton_book5</a> &nbsp; &nbsp; &nbsp; 
<a href="https://twitter.com/milton_book6"  class="btn btn-default btn-lg">@milton_book6</a>
</p><p>
<a href="https://twitter.com/milton_book7"  class="btn btn-default btn-lg">@milton_book7</a> &nbsp; &nbsp; &nbsp; 
<a href="https://twitter.com/milton_book8"  class="btn btn-default btn-lg">@milton_book8</a> &nbsp; &nbsp; &nbsp; 
<a href="https://twitter.com/milton_book9"  class="btn btn-default btn-lg">@milton_book9</a>
</p><p>
<a href="https://twitter.com/milton_book10" class="btn btn-default btn-lg">@milton_book10</a> &nbsp; &nbsp; &nbsp; 
<a href="https://twitter.com/milton_book11" class="btn btn-default btn-lg">@milton_book11</a> &nbsp; &nbsp; &nbsp; 
<a href="https://twitter.com/milton_book12" class="btn btn-default btn-lg">@milton_book12</a>
</p>
"""%(FLOCK_URL)


# ---


CONTACT_TITLE = "Contact @charlesreid1"

CONTACT_DESCRIPTION = """<p>Get in touch!</p>
<p><a href="mailto:charles@charlesreid1.com">charles__at__charlesreid1.com</a></p>
"""


# --------------8<---------------------

DISPLAY_PAGES_ON_MENU = False
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = False
