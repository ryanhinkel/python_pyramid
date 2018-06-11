from wsgiref.simple_server import make_server
from pyramid.config import Configurator

from pyramid.view import view_config


if __name__ == '__main__':
    with Configurator() as config:

        config.include('pyramid_jinja2')
        config.add_jinja2_renderer('.html')

        config.add_route('hello', '/')

        @view_config(
            route_name='hello',
            renderer='json',
        )
        def hello(request):
            return {'message': 'Hello'}

        config.scan()

        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
