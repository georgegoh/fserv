from pyramid.config import Configurator
from fserv.resources import Root

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=Root, settings=settings)
    config.include('pyramid_jinja2')
    config.add_view('fserv.views.home_view',
                    context='fserv:resources.Root',
                    renderer='fserv:templates/home.jinja2')
    config.add_static_view('static', 'fserv:static')
    config.add_route('idea', 'list/{dir}')
    config.add_view('fserv.views.site_view', route_name='idea')
    return config.make_wsgi_app()

