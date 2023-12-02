AUTHOR = 'Metanote Team'
SITENAME = 'Metanote-notes,docs,tasks'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

#:==================
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".git",]

INDEX_SAVE_AS = 'blog/index.html'
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
ARTICLE_LANG_URL = 'blog/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = 'blog/{slug}-{lang}.html'

THEME = './themes/clean-blog'
#:plugins
PLUGIN_PATHS = ["plugins", "./plugins"]
PLUGINS = ["org_reader","i18n_subsites",]
ORG_READER_EMACS_LOCATION = '/usr/local/bin/emacs'

# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
    'zh': {}
    }
TWITTER_URL = 'https://twitter.com/MetanoteTeam'
EMAIL_URL = 'mailto:metanote.team@gmail.com'
GITHUB_URL = 'https://www.github.com/metanote-dev'
APP_STORE_URL = 'https://apps.apple.com/app/metanote-notes-docs-tasks/id6452550221'
GOOGLE_PLAY_STORE_URL = 'https://play.google.com/store/apps/details?id=com.iknockdoor.metanote'
