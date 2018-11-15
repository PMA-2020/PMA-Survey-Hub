"""Config"""
import os
import platform

from pma_survey_hub.config import get_settings

# TODO: Dynamically get package name
PKG_NAME = 'ppp'
module_name = 'PPP'
template = 'modules/ppp/index.html'

version = '1.3.1'
PROJECT_ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '..'))
APP_DIR = os.path.join(PROJECT_ROOT_DIR, 'ppp_web')
BIN_DIR = os.path.join(APP_DIR, 'bin')
IS_WINDOWS = platform.system() == 'Windows'
TEMP_DIR = 'temp'
PKG_DIR = os.path.dirname(os.path.realpath(__file__)) + '/'
LOGGING_ON = os.getenv('FLASK_ENV') in ('development', 'staging') or \
             os.getenv('APP_SETTINGS') in ('development', 'staging')
# Even if there is no error, Heroku always prints this message to the console
# under stderr. I file a bug report. - Joe 2018/11/10
basedir = os.path.abspath(os.path.dirname(__file__))
path_char = '\\' if IS_WINDOWS else '/'

settings = {
    'module_name': module_name,
    'page_name': "Welcome",
    # 'icon': "fa fa-star-o",
    'module_abbreviation': "Home",
    'app_config_settings': get_settings(),
    'messages': [],
    'notifications': [],
    'current_user': '',
    'logged_in': True
}


class Config:
    """Base configuration."""
    WKHTMLTOPDF_PATH_LOCAL = os.path.join(BIN_DIR, 'wkhtmltopdf')
    WKHTMLTOPDF_PATH_SYSTEM = \
        os.getenv('WKHTMLTOPDF_PATH_SYSTEM', 'wkhtmltopdf')

    THREADS_PER_PAGE = 2
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = "?x1234567890x!"  # TODO: To env.
    SECRET_KEY = "!x1234567890x?"  # TODO: To env.
    DEBUG = False
    TESTING = False


class StagingConfig(Config):
    """Production configuration."""
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'staging': StagingConfig,
    'default': DevelopmentConfig
}
