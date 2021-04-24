from flask import request
# from app import logger


def register_log_hook(app):

    @app.after_request
    def after_request(response):
        if request.path != "/health":
            print("Request completed", dict(req=request, res=response))
        return response
