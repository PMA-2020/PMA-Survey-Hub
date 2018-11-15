"""Config"""
import os
import platform

from pma_survey_hub.config import get_settings

# TODO: Dynamically get package name
PKG_NAME = 'borrow'
module_name = 'Borrow'
template = 'modules/borrow/index.html'

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
