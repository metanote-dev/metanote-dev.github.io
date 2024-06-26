AUTHOR = 'Metanote Team'
SITENAME = 'Metanote-notes,docs,tasks'
SITEURL = ""
APP_NAME = "Metanote"
APP_DESCRIPTION = "A text editor designed for writing, maintaining TODO lists, and project planning."

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
# that' strange, only folder can be add
STATIC_PATHS = ['images','data','copy2root',]
# '.' is the articles path, so, need excludes from articles
ARTICLE_EXCLUDES = ['images','data','copy2root',]
# settings for some static file's copy dest
EXTRA_PATH_METADATA = {
    'copy2root/README.md': {'path': 'README.md'},
    'copy2root/privacy.html': {'path': 'privacy.html'},
    'copy2root/update_info.json': {'path': 'update_info.json'},
    'copy2root/update_info_ios.json': {'path': 'update_info_ios.json'},
    'copy2root/.nojekyll': {'path': '.nojekyll'},
    'copy2root/microsoft-identity-association.json': {'path': '.well-known/microsoft-identity-association.json'},
    }


DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".git",]

INDEX_SAVE_AS = 'blog/index.html'
ARTICLE_URL = '{slug}.html'
ARTICLE_SAVE_AS = '{slug}.html'
ARTICLE_LANG_URL = '{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = '{slug}-{lang}.html'

THEME = './themes/clean-blog'
#:plugins
PLUGIN_PATHS = ["plugins", "./plugins"]
PLUGINS = ["org_reader","i18n_subsites","neighbors",]
ORG_READER_EMACS_LOCATION = 'emacs'

MENUITEMS = (
    ("Blog", "/blog/index.html"),
    ("FAQ", "/pages/faq.html"),
    ("ChangeLog", "/pages/changelog.html"),
    ("Archive", "/archives.html"),
)

languages_lookup = {
             'en': 'English',
             'zh': '中文',
             }

def lookup_lang_name(lang_code):
    return languages_lookup[lang_code]

JINJA_FILTERS = {
             'lookup_lang_name': lookup_lang_name,
             }

I18N_UNTRANSLATED_ARTICLES = 'remove'
I18N_UNTRANSLATED_PAGES = 'remove'
# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
    'zh': {
        'SITENAME': 'Metanote-文档,日程,待办',
        'APP_DESCRIPTION': '一款支持知识管理，写作，TODO-list 和项目管理的纯文本编辑器',
        'MENUITEMS': (
    ("Blog", "/zh/blog/index.html"),
    ("FAQ", "/zh/pages/faq.html"),
    ("更新日志", "/zh/pages/changelog.html"),
    ("归档", "/zh/archives.html"),
        ),
        'STATIC_PATHS': ['images','data']
    }
    }
TWITTER_URL = 'https://twitter.com/MetanoteTeam'
EMAIL_URL = 'mailto:metanote.team@gmail.com'
GITHUB_URL = 'https://www.github.com/metanote-dev'
APP_STORE_URL = 'https://apps.apple.com/app/metanote-notes-docs-tasks/id6452550221'
GOOGLE_PLAY_STORE_URL = 'https://play.google.com/store/apps/details?id=com.iknockdoor.metanote'
