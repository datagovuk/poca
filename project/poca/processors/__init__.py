
from .base import Processor
from .carparks import CarparkProcessor

class DefaultProcessor(Processor):
    pass


def get_processors():
    return [CarparkProcessor, DefaultProcessor]

def get_processor_by_name(name):
    if name == 'carparks':
        return CarparkProcessor()

    return DefaultProcessor()