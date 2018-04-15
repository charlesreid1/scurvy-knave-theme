# scurvy-knave-theme

The scurvy knave is a pelican theme for a one-off one-page site.

Pelican is designed for 1 file -> 1 page, 
so assembling a single-page site from 
different files is difficult.

Instead, we define a fixed layout for the site,
and everything is configured by the user using
variables in `pelicanconf.py`.

Unlike most pelican sites, the `content/` folder 
will remain completely empty, and all site
content will be defined in the theme 
and configured in the `pelicanconf.py`.

# Branches

This repo has three disparate branches:

* `master` - the branch you are looking at now. This contains the files for the actual theme.
* `source` - a branch containing a working pelican site that uses this theme. used to generate `gh-pages` branch.
* `gh-pages` - a branch containing static HTML content to be served up via Github Pages

The `gh-pages` branch can be viewed live at 
[https://charlesreid1.github.io/scurvy-knave-theme](https://charlesreid1.github.io/scurvy-knave-theme).

# Installation

To install:

```
git clone http://gitub.com/charlesreid1/scurvy-knave-theme

pelican-themes -i scurvy-knave-theme   # install theme

pelican-themes -U scurvy-knave-theme   # update theme

pelican-themes -r scurvy-knave-theme   # remove theme
```

# Usage

First, set the theme in `pelican.conf`.

## Section 1: title/subtitle

Set the site title and subtitle (description):

```
SITE_TITLE = "bots.charlesreid1.com"

SITE_DESCRIPTION = "a subdomain for charlesreid1 bots"
```

## Section 2: about

Set the title and contents of the about section:

```
ABOUT_TITLE = "about bots.charlesreid1.com"

ABOUT_DESCRIPTION = """
<p>Your html goes <a href="https://example.com/">here</a>.</p>
"""
```

Because these variables are being defined in Python,
this allows you to hook in any number of methods for 
generating HTML for your pages.

## Section 3: links

The links section has three parts: 
the title, the description, and the buttons.

Set the following variables:

```
LINKS_TITLE = "links on bots.charlesreid1.com"

LINKS_DESCRIPTION = """
<p>HTML goes here</p>
<a href="https://example.com" class="btn btn-circle btn-lg">
    <i class="fa fa-key animated"></i>     
</a>
"""

LINKS_BUTTONS = """
<p>
<a href="https://example.com/" class="btn btn-default">example 1</a>
&nbsp;
<a href="https://example.com/" class="btn btn-default">example 2</a>
</p>
"""
```

# Styles

This one-pager is basically all black and white,
except for color provided by buttons, links, and
background photographs.

The file `custom.css` in the scurvy-knave-theme templates
provides a templated CSS file that can be used to 
customize the colors/styles in the theme.

First, set style-related variables.

You can define as many style variables as you want, 
and as long as there is a corresponding variable 
in `custom.css`, these will give you full control
over the CSS on the page:

```
H1_COLOR = "#F00"
H2_COLOR = "#00F"
BUTTON_COLOR = "#077"

...

```

Next, we have to tell pelican to actually copy
the templated CSS file to the final HTML folder
(we don't have to do this with HTML because 
HTML files are copied over by default):

```
TEMPLATE_PAGES = {
    'custom.css' : 'custom.css'
}
```

Now, when you run `pelican content`, it will 
pick up the theme, set the CSS theme variables,
apply them to the CSS template file, and copy
the final CSS file along with the rest of the 
HTML files into `output/`.



## Custom Colors

This theme currrently defines three custom colors:

* `H1COLOR` - color of title text
* `ACOLOR` - color of links and buttons
* `AHOVERCOLOR` - color of links and buttons when hovering over them

## Useful Color Schema

Twitter blue:

```
ACOLOR      = "#00aced"
AHOVERCOLOR = "#0084b4"
BRIGHTCOLOR = "#1dcaff"
```

Nginx green:

```
ACOLOR      = "#aced00"
AHOVERCOLOR = "#84b400"
BRIGHTCOLOR = "#caf1d"
```

Perky magenta:

```
ACOLOR      = "#ed00ac"
AHOVERCOLOR = "#b40084"
BRIGHTCOLOR = "#ff1dca"
```

Seafoam green:

```
ACOLOR      = "#00edac"
AHOVERCOLOR = "#00b484"
BRIGHTCOLOR = "#1df1ca"
```

Sunflower yellow:

```
ACOLOR      = "#edac00"
AHOVERCOLOR = "#b48400"
BRIGHTCOLOR = "#f1ca1d"
```

Purple mountains' majesty:

```
ACOLOR      = "#ac00ed"
AHOVERCOLOR = "#8400b4"
BRIGHTCOLOR = "#ca1df1"
```


