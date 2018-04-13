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

## Installation

To install:

```
git clone http://gitub.com/charlesreid1/scurvy-knave-theme

pelican-themes -i scurvy-knave-theme   # install theme

pelican-themes -U scurvy-knave-theme   # update theme

pelican-themes -r scurvy-knave-theme   # remove theme
```

## Usage

To use, set variables in `pelicanconf.py`.

