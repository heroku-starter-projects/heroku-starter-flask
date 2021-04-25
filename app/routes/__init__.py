from app.routes.health import Health
from app.routes.user import User
from app.routes.login import Login
from app.routes.signup import Signup


def register_routes(api):
    api.add_resource(Health, '/health')
    api.add_resource(User, '/user/<int:user_id>')
    api.add_resource(Signup, '/signup')
    api.add_resource(Login, '/login')
