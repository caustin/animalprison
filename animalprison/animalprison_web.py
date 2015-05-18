import logging

from animalprison.web.app import create_app

class Config(object):
    JSONIFY_PRETTYPRINT_REGULAR = False
    REDIS_URL = 'redis://localhost'
    LOG_FILE = 'ap.log'
    LOG_LEVEL = logging.DEBUG


if __name__ == '__main__':
    app = create_app(Config())
    app.run(port=8881, debug=True)
