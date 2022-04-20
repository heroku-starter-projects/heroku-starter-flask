from app.hooks.cookie import register_cookies_hook
from app.hooks.cors import register_cors_hook
from app.hooks.database import register_database_hook
from app.hooks.error import register_error_hook
from app.hooks.log import register_log_hook


def register_hooks(app, api):
    register_error_hook(app, api)
    register_database_hook(app)
    register_log_hook(app)
    register_cookies_hook(app)
    register_cors_hook(app)
