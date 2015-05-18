from logging import Formatter
from logging.handlers import TimedRotatingFileHandler


def get_file_logger(file_path, log_level):
    handler = TimedRotatingFileHandler(file_path, when='D', interval=1, backupCount=7)
    handler.setLevel(log_level)
    handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )

    return handler
