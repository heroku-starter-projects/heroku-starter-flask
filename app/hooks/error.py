from werkzeug.exceptions import InternalServerError


def register_error_hook(app, api):

    def error_handler(_e):
        return api.handle_error(InternalServerError())

    app.register_error_handler(Exception, error_handler)
