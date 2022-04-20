from flask import g, request
# from app import logger


def register_cookies_hook(app):
    @app.before_request
    def before_request():
        g.token = request.cookies.get('token')

    @app.after_request
    def after_request(response):
        if 'user' in g:
            token = g.user.generate_token()
            response.set_cookie('token', token, httponly=True)
        else:
            # response.delete_cookie('token')
            pass

        return response
