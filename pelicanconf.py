AUTHOR = 'Pinar Batat Buke'
SITENAME = "Pinar's DataLog"
SITEURL = ''

PATH = 'content'

STATIC_PATHS = ['static']

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'EN'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'themes/pelican-clean-blog'

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

HEADER_COVER = 'static/blog_cover1.png'

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/pinar-batat-buke-b7025a2a/'),
          ('Email App', 'mailto:pinarbbuke@gmail.com'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['pelican-plugins']

PLUGINS = ['pelican-ipynb.pelican_jupyter.markup']
MARKUP = ('md', 'ipynb')

from pelican_jupyter import markup as nb_markup
PLUGINS = [nb_markup]

IGNORE_FILES = [".ipynb_checkpoints"]  

AUTHORS_BIO = {
	"Pinar Buke": {
		"name" : "Pinar Batat Buke",
		"location" : "Edinburgh, UK",
		"bio" : "Brewing Data Scientist"}
}

