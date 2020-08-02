"""
The **logger** module manages the configuration of the logger.
It uses *colorlog* to get colored logging messages.
"""
import logging
import colorlog


def logger_config(level, name=None):
    """Setup the logging environment."""
    if not name:
        log = logging.getLogger()  # root logger
    else:
        log = logging.getLogger(name)
    log.setLevel(level)
    colors = {
        'DEBUG': 'green',
        'INFO': 'cyan',
        'WARNING': 'bold_yellow',
        'ERROR': 'bold_red',
        'CRITICAL': 'bold_purple'
    }
    formatter = colorlog.ColoredFormatter(
        fmt='%(log_color)s%(message)s',
        log_colors=colors
    )
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    log.addHandler(stream_handler)
    return log
