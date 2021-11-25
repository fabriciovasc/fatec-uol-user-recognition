from .distance_abstract import DistanceAbstract


class ManhattanDistance(DistanceAbstract):
    def __init__(self):
        pass

    def measure(cls, list1, list2):
        distance = 0
        min_len = min(len(list1), len(list2))

        for i in range(0, min_len):
            distance += abs(list1[i] - list2[i])

        return distance
