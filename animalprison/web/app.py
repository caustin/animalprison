from flask import Flask
from animalprison.extensions import redis_store
from animalprison.web.views import service_blueprint
from animalprison.log import get_file_logger


def create_app(config_object: object) -> Flask:
    """
    :param config_object:
    :return:
    """

    app = Flask(__name__)
    app.config.from_object(config_object)
    app.logger.addHandler(
        get_file_logger(app.config.get('LOG_FILE'), log_level=app.config.get('LOG_LEVEL')))

    redis_store.init_app(app=app)
    app.register_blueprint(service_blueprint)

    return app
