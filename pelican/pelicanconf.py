#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'charlesreid1'

SITENAME = u'scurvy knave pelican theme'

SITEURL = '/scurvy-knave-theme'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# --------------8<---------------------

THEME = 'scurvy-knave-theme'

# Pelican is designed for files => pages.
# Use variables (below) to set pieces of pages.

INTROCOLOR  = "#fff"
ACOLOR      = "#edac00"
AHOVERCOLOR = "#b48400"
BRIGHTCOLOR = "#f1ca1d"
TEMPLATE_PAGES = {
    'custom.css' : 'custom.css'
}

# ---

# description appears between <p> tags, so don't include them

SITE_TITLE = "scurvy knave pelican theme"
SITE_DESCRIPTION = "a simple single-color single-page theme for pelican"

# ---

# include <p> tags in the description

ABOUT_TITLE = "about this theme"

ABOUT_DESCRIPTION = """
<p><a href="https://github.com/charlesreid1/scurvy-knave-theme">scurvy knave on github</a></p>

<p>&nbsp;</p>

<p><b>What is the scurvy knave?</b></p>

<p>Being a get-off-my-lawn technology user, I got tired of fussing around
setting up the latest hipster javascript library invented by a fixie-riding
developer with nerd glasses at their favorite muffin shop.</p>

<p>I wanted a dead-simple, single-page, single-color theme where the user can expend
as little effort as possible (with the bare minimum being, defining a name and a sentence
for each of the four sections on the page).

<p>This theme is so simple, you barely even have to write HTML.
You just populate a few variables that are shimmed into a 
nice pretty page.</p>

<p>&nbsp;</p>

<p><b>What about colors? Are there pretty pastel colors like my favorite hipster javascript library?</b></p>

<p>Colors? You want colors? What is this, a flower shop??</p>

<p>This theme has one color. One. You get to 
pick one color, and you live with it for the rest of the 
short, four-section page.</p>

<p>&nbsp;</p>

<p><b>::starts crying:: I want my colors!!!</b></p>

<p>Okay, fine, you can have a custom CSS file to define
everything you could possibly ever want. I'll call it...
I don't know... <code>custom.css</code>
</p>

<p>&nbsp;</p>

<p><b>::sniffles:: Custom javascript too?</b></p>

<p>Don't push it.</p>
"""

# ---

# include <p> tags in the description

LINKS_TITLE = "links section"

LINKS_DESCRIPTION = """
<p>Kadishtu n'ghft gof'nn fm'latgh Azathoth lloig chtenff hafh'drn shoggyar.</p>
<p>Find the <a href="https://github.com/charlesreid1/scurvy-knave-theme">scurvy knave on github</a>.
</p>
"""


# ---


CONTACT_TITLE = "Author"

CONTACT_DESCRIPTION = """
<p><b>who is responsible for this abomination?</b>
<br />
This theme is authored by @charlesreid1. Find charles on <a href="https://github.com/charlesreid1">github</a>
or on <a href="https://charlesereid1.com">charlesreid1.com</a>.
You can also find the <a href="https://github.com/charlesreid1/scurvy-knave-theme">scurvy knave pelican theme on github</a></p>.

<p><b>are you confused by this very simple theme and desperate for unpaid intensive one-on-one tech support?
</b><br /> 
<a href="https://github.com/charlesreid1/scurvy-knave-theme/issues">open an issue on github</a></p>

<p><b>do you love this theme like Michael Cohen loves Donald Trump?
</b><br />
<a href="https://charlesreid1.com/contact">hire me</a> to build on it.</p>

<p><b>are you benevolent and rich?
</b><br />
<a href="https://charlesreid1.com/money">give me moneydollars</a> to keep building
<a href="https://charlesreid1.com/bots">weird stuff</a>.
</p>

<p>&nbsp;</p>
"""


# --------------8<---------------------


DISPLAY_PAGES_ON_MENU = False
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = False

