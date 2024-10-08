import os.path
from pathlib import Path

from split_settings.tools import include, optional

from web.core.common.utils.pytest import is_pytest_running

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

ENVVAR_SETTINGS_PREFIX = 'CORESETTING_'
LOCAL_SETTINGS_PATH = os.getenv(f'{ENVVAR_SETTINGS_PREFIX}LOCAL_SETTINGS_PATH')

if not LOCAL_SETTINGS_PATH:
    LOCAL_SETTINGS_PATH = os.path.join('local', f'settings.{"unittests" if is_pytest_running else "dev"}.py')

if not os.path.isabs(LOCAL_SETTINGS_PATH):
    LOCAL_SETTINGS_PATH = os.path.join(BASE_DIR, LOCAL_SETTINGS_PATH)

assert (os.path.isfile(LOCAL_SETTINGS_PATH))

# yapf: disable
include(
    'base.py',
    'logging.py',
    'custom.py',
    optional(LOCAL_SETTINGS_PATH),
    'envvars.py',
    'docker.py',
)
# yapf: enable
