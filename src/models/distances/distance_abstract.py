from abc import ABCMeta, abstractmethod


class DistanceAbstract(metaclass=ABCMeta):
    def __init__(self):
        pass

    @classmethod
    @abstractmethod
    def measure(cls, list1, list2):
        pass
