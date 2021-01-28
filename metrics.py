
from datetime import datetime


def benc_time(func):
    """
    function for measuring function time
    :param func:
    :return: time complete, function result
    """
    def inner(*args, **kwargs):
        time_start = datetime.now()
        try:
            return func(*args, **kwargs)
        finally:
            print(f'Time: {datetime.now() - time_start}')

    return inner