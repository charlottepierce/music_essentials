class Interval(object):
    """Representation of an interval (i.e., gap) between notes."""

    def __init__(self, interval_type, distance):
        self.interval_type = interval_type
        self.distance = int(distance)
    
    @classmethod
    def from_interval_string(cls, interval_string):
        distance = interval_string[-1]
        interval_type = interval_string[:-1]

        return cls(interval_type, distance)

    def __str__(self):
        return self.interval_type + str(self.distance)


if __name__ == '__main__':
    i = Interval('m', 3)
    print(i)

    i = Interval.from_interval_string('dim5')
    print(i)