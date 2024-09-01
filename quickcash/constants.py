# imports
import dj_database_url

# Directory Constants
TEMPLATES_BASE_DIR = "templates/"
STATIC_URL_NAME = "static/"
STATIC_URL_PATH = "templates/static"
STATIC_ROOT_PATH = "assets/"
MEDIA_URL_NAME = "media/"
MEDIA_ROOT_PATH = "media/"
LOCALHOST = "127.0.0.1"
TZ_ASIA_KOLKATA = "Asia/Kolkata"
LANGUAGE_CODE_EN_US = "en-us"

# Database
POSTGRE_SQL_URL = dj_database_url.parse(
    "postgres://postgres:7877@localhost:5432/QuickCash"
)
SQLITE_URL = dj_database_url.parse("sqlite://{PATH}/db.sqlite3")

# Cache Constants
CACHE_TABLE = "quickcash_cache"
