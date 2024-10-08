import os

os.environ['PYTEST_RUNNING'] = 'true'

from web.core.common.tests.fixtures import *  # noqa: F401, F403, E402
