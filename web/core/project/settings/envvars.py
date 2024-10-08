from web.core.common.utils.collections import deep_update
from web.core.common.utils.settings import get_env_settings

deep_update(globals(), get_env_settings(ENVVAR_SETTINGS_PREFIX))  # type: ignore # noqa: F821
