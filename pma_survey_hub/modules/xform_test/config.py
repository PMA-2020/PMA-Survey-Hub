"""Config"""
from glob import glob
import os
import platform

from pma_survey_hub.config import get_settings

# TODO: Dynamically get package name
PKG_NAME = 'xform-test'
module_name = 'XFormTest'
template = 'modules/xform_test/index.html'

IS_WINDOWS = platform.system() == 'Windows'
TEMP_DIR = 'temp'
PKG_DIR = os.path.dirname(os.path.realpath(__file__)) + '/'
XFORM_TEST_EXECUTABLE = glob(PKG_DIR + 'bin/xform-test/*.jar')[0]
LOGGING_ON = os.getenv('FLASK_ENV') in ('development', 'staging') or \
             os.getenv('APP_SETTINGS') in ('development', 'staging')
# Even if there is no error, Heroku always prints this message to the console
# under stderr. I file a bug report. - Joe 2018/11/10
HEROKU_ERR_EVERY_TIME = 'Picked up JAVA_TOOL_OPTIONS: -Xmx300m -Xss512k ' \
                        '-XX:CICompilerCount=2 -Dfile.encoding=UTF-8'

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
