""" App utilities """
import logging

def setup_logger(name: str = __name__, level: int = logging.INFO) -> logging.Logger:
    """
    Set a logger to log messages in console
    """
    logging.basicConfig(
        level=level,
        format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[logging.StreamHandler()]
    )
    return logging.getLogger(name)
