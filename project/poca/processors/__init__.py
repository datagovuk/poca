
from .base import Processor
from .carparks import CarparkProcessor
from .spend import SpendProcessor

class DefaultProcessor(Processor):
    pass


def get_processors():
    return [SpendProcessor, CarparkProcessor, DefaultProcessor]

def get_processor_by_name(name):
    if name == 'carparks':
        return CarparkProcessor()
    elif name == 'spend':
        return SpendProcessor()

    return DefaultProcessor()