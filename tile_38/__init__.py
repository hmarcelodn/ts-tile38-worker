from tile_38.resources import DummyIngestionResource
import falcon

def handle_generic_errors(ex, req, resp, params):
    print('error')
    raise ex

def create_app():
    app = falcon.API(None)
    app.add_route('/ingestion', DummyIngestionResource())
    app.add_error_handler(Exception, handle_generic_errors)

    return app