"""
Master configuration file for Evennia.

NOTE: NO MODIFICATIONS SHOULD BE MADE TO THIS FILE!

All settings changes should be done by copy-pasting the variable and
its value to game/settings.py. An empty game/settings.py can be
auto-generated by running game/manage.py without any arguments.

Hint: Don't copy&paste over more from this file than you actually want to
change.  Anything you don't copy&paste will thus retain its default
value - which may change as Evennia is developed. This way you can
always be sure of what you have changed and what is default behaviour.
"""

import os

###################################################
# Evennia base server config 
###################################################

# This is the name of your server and/or site. 
# Can be anything. 
SERVERNAME = "Evennia" 
# Activate telnet service
TELNET_ENABLED = True 
# A list of ports the Evennia telnet server listens on
# Can be one or many.
TELNET_PORTS = [4000]
# Start the evennia django+twisted webserver so you can 
# browse the evennia website and the admin interface
# (Obs - further web configuration can be found below
# in the section  'Config for Django web features')
WEBSERVER_ENABLED = True
# A list of ports the Evennia webserver listens on
WEBSERVER_PORTS = [8000]
# Start the evennia ajax client on /webclient
# (the webserver must also be running)
WEBCLIENT_ENABLED = True
# Activate full persistence if you want everything in-game to be
# stored to the database. With it set, you can do typeclass.attr=value
# and value will be saved to the database under the name 'attr'.
# This is easy but may be a performance hit for certain game types.
# Turning it off gives more control over what hits the database since
# typeclass.attr=value is then non-persistent (does not hit the
# database and won't survive a server reload) and you need to
# explicitly do typeclass.db.attr = value if you want to save your
# value to the database. Your choice, but DON'T change this 
# value once you have started using the server, it will not end well!
FULL_PERSISTENCE = True
# If multisessions are allowed, a user can log into the game
# from several different computers/clients at the same time.
# All feedback from the game will be echoed to all sessions. 
# If false, only one session is allowed, all other are logged off
# when a new connects. 
ALLOW_MULTISESSION = True
# Make this unique, and don't share it with anybody.
# NOTE: If you change this after creating any accounts, your users won't be
# able to login, as the SECRET_KEY is used to salt passwords.
SECRET_KEY = 'changeme!(*#&*($&*(#*(&SDFKJJKLS*(@#KJAS'
# The path that contains this settings.py file (no trailing slash).
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Path to the src directory containing the bulk of the codebase's code.
SRC_DIR = os.path.join(BASE_PATH, 'src')
# Path to the game directory (containing the database file if using sqlite).
GAME_DIR = os.path.join(BASE_PATH, 'game')
# Place to put log files
LOG_DIR = os.path.join(GAME_DIR, 'logs')
DEFAULT_LOG_FILE = os.path.join(LOG_DIR, 'evennia.log')
# Where to log server requests to the web server. This is VERY spammy, so this 
# file should be removed at regular intervals. 
HTTP_LOG_FILE = os.path.join(LOG_DIR, 'http_requests.log')
# Local time zone for this installation. All choices can be found here:
# http://www.postgresql.org/docs/8.0/interactive/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
TIME_ZONE = 'UTC'
# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
LANGUAGE_CODE = 'en-us'
# Should the default MUX help files be imported? This might be  
# interesting to developers for reference, but is frustrating to users 
# since it creates a lot of help entries that has nothing to do 
# with what is actually available in the game.
IMPORT_MUX_HELP = False 
# How long time (in seconds) a user may idle before being logged
# out. This can be set as big as desired. A user may avoid being
# thrown off by sending the empty system command 'idle' to the server
# at regular intervals. Set <=0 to deactivate idle timout completely.
IDLE_TIMEOUT = 3600
# The idle command can be sent to keep your session active without actually 
# having to spam normal commands regularly. It gives no feedback, only updates
# the idle timer.
IDLE_COMMAND = "idle"
# The set of encodings tried. A Player object may set an attribute "encoding" on 
# itself to match the client used. If not set, or wrong encoding is
# given, this list is tried, in order, aborting on the first match. 
# Add sets for languages/regions your players are likely to use.
# (see http://en.wikipedia.org/wiki/Character_encoding)
ENCODINGS = ["utf-8", "latin-1", "ISO-8859-1"] 
# The module holding text strings for the connection screen. 
# This module should contain one ore more variables 
# with strings defining the look of the screen.
CONNECTION_SCREEN_MODULE = "game.gamesrc.world.connection_screens"

###################################################
# Evennia Database config 
###################################################

# Database config syntax for Django 1.2+. You can add several 
# database engines in the dictionary (untested). 
# ENGINE - path to the the database backend (replace
#          sqlite3 in the example with the one you want.
#          Supported database engines are 
#            'postgresql_psycopg2', 'postgresql', 'mysql',
#             'sqlite3' and 'oracle').
# NAME - database name, or path the db file for sqlite3
# USER - db admin (unused in sqlite3)
# PASSWORD - db admin password (unused in sqlite3)
# HOST - empty string is localhost (unused in sqlite3)
# PORT - empty string defaults to localhost (unused in sqlite3) 
DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.sqlite3', 
        'NAME':os.path.join(GAME_DIR, 'evennia.db3'), 
        'USER':'',
        'PASSWORD':'',
        'HOST':'',
        'PORT':''    
        }}
# Engine Config style for Django versions < 1.2. See above.
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(GAME_DIR, 'evennia.db3')
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''


###################################################
# Evennia in-game parsers
###################################################

# An alternate command parser module to use 
# (if not set, uses 'src.commands.cmdparser')
ALTERNATE_PARSER = ""
# How many space-separated words a command name may have
# and still be identified as one single command 
# (e.g. 'push button' instead of 'pushbutton')
COMMAND_MAXLEN = 3
# The handler that outputs errors when searching
# objects using object.search(). (If not set, uses
# src.objects.object_search_funcs.handle_search_errors)
ALTERNATE_OBJECT_SEARCH_ERROR_HANDLER = ""
# The parser used in order to separate multiple
# object matches (so you can separate between same-named
# objects without using dbrefs). (If not set, uses
# src.objects.object_search_funcs.object_multimatch_parser).
ALTERNATE_OBJECT_SEARCH_MULTIMATCH_PARSER = ""

###################################################
# Default command sets 
###################################################

# Command set used before player has logged in
CMDSET_UNLOGGEDIN = "game.gamesrc.commands.basecmdset.UnloggedinCmdSet"
# Default set for logged in players (fallback)
CMDSET_DEFAULT = "game.gamesrc.commands.basecmdset.DefaultCmdSet"

###################################################
# Default Object typeclasses 
###################################################

# Note that all typeclasses must originally
# inherit from src.objects.objects.Object somewhere in
# their path. 

# This sets the default base dir to search when importing 
# things, so one doesn't have to write the entire 
# path in-game.
BASE_TYPECLASS_PATH = "game.gamesrc.objects"
# Typeclass for player objects (linked to a character) (fallback)
BASE_PLAYER_TYPECLASS = "game.gamesrc.objects.baseobjects.Player"
# Typeclass and base for all following objects (fallback)
BASE_OBJECT_TYPECLASS = "game.gamesrc.objects.baseobjects.Object"
# Typeclass for character objects linked to a player (fallback)
BASE_CHARACTER_TYPECLASS = "game.gamesrc.objects.baseobjects.Character"
# Typeclass for rooms (fallback)
BASE_ROOM_TYPECLASS = "game.gamesrc.objects.baseobjects.Room"
# Typeclass for Exit objects (fallback)
BASE_EXIT_TYPECLASS = "game.gamesrc.objects.baseobjects.Exit"

###################################################
# Scripts
###################################################

# Python path to a directory to start searching 
# for scripts. 
BASE_SCRIPT_PATH = "game.gamesrc.scripts"

###################################################
# Batch processors 
###################################################

# Python path to a directory to be searched for batch scripts 
# for the batch processors (.ev and/or .py files).
BASE_BATCHPROCESS_PATH = 'game.gamesrc.world'

###################################################
# Game Time setup
###################################################

# You don't actually have to use this, but it affects the routines in
# src.utils.gametime.py and allows for a convenient measure to determine the
# current in-game time. You can of course read "week", "month" etc
# as your own in-game time units as desired. 

#The time factor dictates if the game world runs faster (timefactor>1)
# or slower (timefactor<1) than the real world.
TIME_FACTOR = 2.0 
# The tick is the smallest unit of time in the game. Smallest value is 1s. 
TIME_TICK = 1.0
# These measures might or might not make sense to your game world.
TIME_MIN_PER_HOUR = 60
TIME_HOUR_PER_DAY = 24
TIME_DAY_PER_WEEK = 7
TIME_WEEK_PER_MONTH = 4
TIME_MONTH_PER_YEAR = 12


###################################################
# In-Game access 
###################################################
# The access hiearchy, in climbing order. A higher
# permission in the hierarchy includes access of all
# levels below it. 
PERMISSION_HIERARCHY = ("Players","PlayerHelpers","Builders", "Wizards", "Immortals")
# The default permission given to all new players
PERMISSION_PLAYER_DEFAULT = "Players"
# Tuple of modules implementing lock functions. All callable functions
# inside these modules will be available as lock functions.
LOCK_FUNC_MODULES = ("src.locks.lockfuncs",)

###################################################
# In-game Channels created from server start
###################################################
# Defines a dict with one key for each from-start
# channel. Each key points to a tuple containing
# (name, aliases, description, locks)
# where aliases may be a tuple too, and locks is 
# a valid lockstring definition.
# Default user channel for communication
CHANNEL_PUBLIC = ("Public", 'ooc', 'Public discussion',
                  "admin:perm(Wizards);listen:all();send:all()")
# General info about the server
CHANNEL_MUDINFO = ("MUDinfo", '', 'Informative messages',
                   "admin:perm(Immortals);listen:perm(Immortals);send:false()")
# Channel showing when new people connecting
CHANNEL_CONNECTINFO = ("MUDconnections", ('connections, mud_conns'),
                       'Connection log',
                       "admin:perm(Immortals);listen:perm(Wizards);send:false()")

###################################################
# External Channel connections 
###################################################

# Evennia can connect to external IRC channels and 
# echo what is said on the channel to IRC and vice 
# versa. Obs - make sure the IRC network allows bots.
# If disabled, the default @irc2chan command won't be 
# available in-game. 
IRC_ENABLED = True

# OBS: IMC is not implemented at this point! 

# IMC (Inter-MUD communication) allows for an evennia chat channel
# that connects to people on other MUDs also using the IMC. Your
# evennia server do *not* have to be open to the public to use IMC; it
# works as a stand-alone chat client.  Evennia's IMC2 client was
# developed against MudByte's network. You must register your MUD on
# the network before you can use it, go to
# http://www.mudbytes.net/imc2-intermud-join-network.  Choose 'Other
# unsupported IMC2 version' from the choices and and enter your
# information there. You have to enter the same 'short mud name',
# 'client password' and 'server password' as you define in this file.
# The Evennia discussion channel is on server02.mudbytes.net:9000.

# Change to True if you want IMC active at all.
IMC2_ENABLED = False
# Which channel to tie to the imc2 connection
COMMCHAN_IMC2_INFO = 'MUDInfo'
# The hostname/ip address of your IMC2 server of choice.
IMC2_SERVER_ADDRESS = 'server02.mudbytes.net' 
#IMC2_SERVER_ADDRESS = None
# The port to connect to on your IMC2 server.
IMC2_SERVER_PORT = 9000
#IMC2_SERVER_PORT = None
# This is your game's IMC2 name on the network (e.g. "MyMUD").
IMC2_MUDNAME = None 
# Your IMC2 client-side password. Used to authenticate with your network. 
IMC2_CLIENT_PW = None 
# Your IMC2 server-side password. Used to verify your network's identity.
IMC2_SERVER_PW = None 
# Emit additional debugging info to log.
IMC2_DEBUG = False
# This isn't something you should generally change.
IMC2_PROTOCOL_VERSION = '2'


###################################################
# Config for Django web features
###################################################

# While DEBUG is False, show a regular server error page on the web
# stuff, email the traceback to the people in the ADMINS tuple
# below. If True, show a detailed traceback for the web
# browser to display. Note however that this will leak memory when
# active, so make sure to turn it off for a production server!
DEBUG = False
# While true, show "pretty" error messages for template syntax errors.
TEMPLATE_DEBUG = DEBUG
# Emails are sent to these people if the above DEBUG value is False. If you'd
# rather nobody recieve emails, leave this commented out or empty.
ADMINS = () #'Your Name', 'your_email@domain.com'),)
# These guys get broken link notifications when SEND_BROKEN_LINK_EMAILS is True.
MANAGERS = ADMINS
# Absolute path to the directory that holds media (no trailing slash).
# Example: "/home/media/media.lawrence.com"
MEDIA_ROOT = os.path.join(SRC_DIR, 'web', 'media')
# Absolute path to the directory that holds (usually links to) the
# django admin media files. If the target directory does not exist, it
# is created and linked by Evennia upon first start. Otherwise link it
# manually to django/contrib/admin/media.
ADMIN_MEDIA_ROOT = os.path.join(MEDIA_ROOT, 'admin')
# It's safe to dis-regard this, as it's a Django feature we only half use as a
# dependency, not actually what it's primarily meant for.
SITE_ID = 1
# The age for sessions.
# Default: 1209600 (2 weeks, in seconds)
SESSION_COOKIE_AGE = 1209600
# Session cookie domain
# Default: None
SESSION_COOKIE_DOMAIN = None
# The name of the cookie to use for sessions.
# Default: 'sessionid'
SESSION_COOKIE_NAME = 'sessionid'
# Should the session expire when the browser closes?
# Default: False
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False
# This should be turned off unless you want to do tests with Django's 
# development webserver (normally Evennia runs its own server)
SERVE_MEDIA = False
# The master urlconf file that contains all of the sub-branches to the
# applications.
ROOT_URLCONF = 'src.web.urls'
# Where users are redirected after logging in via contrib.auth.login.
LOGIN_REDIRECT_URL = '/'
# Where to redirect users when using the @login_required decorator.
LOGIN_URL = '/accounts/login'
# Where to redirect users who wish to logout.
LOGOUT_URL = '/accounts/login'
# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = '/media/'
# URL prefix for admin media -- CSS, JavaScript and images. Make sure
# to use a trailing slash. This should match the position defined 
# by ADMIN_MEDIA_ROOT. 
ADMIN_MEDIA_PREFIX = '/media/admin/'
# The name of the currently selected web template. This corresponds to the
# directory names shown in the webtemplates directory.
ACTIVE_TEMPLATE = 'prosimii'
# We setup the location of the website template as well as the admin site.
TEMPLATE_DIRS = (
    os.path.join(SRC_DIR, "web", "templates", ACTIVE_TEMPLATE),
    os.path.join(SRC_DIR, "web", "templates"),)
# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',)
# MiddleWare are semi-transparent extensions to Django's functionality.
# see http://www.djangoproject.com/documentation/middleware/ for a more detailed
# explanation.
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',)
# Context processors define context variables, generally for the template
# system to use.
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.auth',
    'django.core.context_processors.media',
    'django.core.context_processors.debug',
    'src.web.utils.general_context.general_context',)

###################################################
# Evennia components
###################################################

# Global and Evennia-specific apps. This ties everything together so we can
# refer to app models and perform DB syncs.
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.flatpages',
    'src.server',    
    'src.players',
    'src.objects',
    'src.comms',    
    'src.help',
    'src.scripts',
    'src.web.news',
    'src.web.website',)
# The user profile extends the User object with more functionality;
# This should usually not be changed. 
AUTH_PROFILE_MODULE = "players.PlayerDB"
# Use a custom test runner that just tests Evennia-specific apps.
TEST_RUNNER = 'src.utils.test_utils.EvenniaTestSuiteRunner'

###################################################
# Django extensions 
###################################################

# Django extesions are useful third-party tools that are not
# always included in the default django distro. 
try:
    import django_extensions
    INSTALLED_APPS = INSTALLED_APPS + ('django_extensions',)
except ImportError:
    pass
# South handles automatic database scheme migrations when evennia updates
try:
    import south
    INSTALLED_APPS = INSTALLED_APPS + ('south',)
except ImportError:
    pass
