from app.routes.health import Health
from app.routes.user import User


def register_routes(api):
    api.add_resource(Health, '/health')
    api.add_resource(User, '/user')
