from pyramid.view import view_config


@view_config(
    route_name='hello',
    renderer='json',
)
def hello(request):
    return {'message': 'Hello'}
