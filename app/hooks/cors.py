def register_cors_hook(app):

    @app.after_request
    def after_request(response):
        # https://stackoverflow.com/a/52875875/1217998
        response.headers.add("Access-Control-Allow-Origin", "http://localhost:3000")
        response.headers.add("Access-Control-Allow-Headers", "content-type, set-cookie")
        response.headers.add("Access-Control-Allow-Methods", "*")
        response.headers.add("Access-Control-Allow-Credentials", "true")

        return response
