THEME = 'theme'

AUTHOR = 'Clara Matos'
SITENAME = 'Clara Matos'
SITEURL = ""
COPYRIGHT_YEAR = 2025

PATH = "content"

TIMEZONE = 'Europe/Lisbon'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social links (optional)
SOCIAL = (
    ('GitHub', 'https://github.com/claramatos'),
    ('LinkedIn', 'https://www.linkedin.com/in/claramatos/'),
    ('X', 'https://x.com/clarafrmatos'),
    ('Email', 'mailto:anaclaraferreiramats@gmail.com'),
)

# URL structure (creates clean URLs)
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'

# Feeds (disabled for development, enabled in publishconf.py)
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Pagination
DEFAULT_PAGINATION = 10

# Static files
STATIC_PATHS = [
    "pdfs",
    "pdfs/cv.pdf",
]

EXTRA_PATH_METADATA = {
    "pdfs/cv.pdf": {"path": "cv.pdf"},
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
