## IMPORTS

from messages import SayText2
from paths import PLUGIN_PATH

## LOG CONFIGURATION

LOG_PRIORITY = 0
LOG_LOCATION = PLUGIN_PATH / 'warcraft' / 'debug.log'

## DATABASE CONFIGURATION

DATABASE_TYPE = 1 # Types = 1 (SQLite), 2 (MySQL), 3 (UNKOWN)
SQLITE_LOCATION = PLUGIN_PATH / 'warcraft' / 'database' / 'players.sqlite'
MYSQL_ADDRESS = '127.0.0.1'
MYSQL_PORT = ''
MYSQL_LOGIN = 'username'
MYSQL_PASSWORD = 'password'
MYSQL_DATABASE_NAME = 'warcraft'

## NOTIFICATION CONFIGURATION

MESSAGE_TYPE = SayText2

## WARCRAFT HERO CONFIGURATION

WARCRAFT_DEFAULT_HERO = 'Undead'

# All required experience will be calculated by <BASE> + (<LEVEL BONUS> * <CURRENT LEVEL>)
WARCRAFT_BASE_EXPERIENCE = 100
WARCRAFT_LEVEL_BONUS_EXPERIENCE = 40

WARCRAFT_KILL_EXPERIENCE = 50
WARCRAFT_ASSIST_EXPERIENCE = 20