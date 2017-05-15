import connexion
from connexion.resolver import RestyResolver


def connexion_app():
    app = connexion.App(__name__)
    app.add_api(
        'swagger.yaml',
        strict_validation=False,
        validate_responses=False,
        resolver=RestyResolver('py.controllers'),
    )
    return app


def connexion_validation_app():
    app = connexion.App(__name__)
    app.add_api(
        'swagger.yaml',
        strict_validation=True,
        validate_responses=True,
        resolver=RestyResolver('py.controllers'),
    )
    return app


def simple_app():
    def app(environ, start_response):
        """Simplest possible application object"""
        data = 'Hello, World!\n'
        status = '200 OK'
        response_headers = [
            ('Content-type','text/plain'),
            ('Content-Length', str(len(data)))
        ]
        start_response(status, response_headers)
        return iter([data])
    return app
