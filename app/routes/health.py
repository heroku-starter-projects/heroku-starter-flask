from flask_restful import Resource


class Health(Resource):

    @staticmethod
    def get():
        return dict(status='I am alive')
