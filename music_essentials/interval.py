class Interval(object):
    """Representation of an interval (i.e., gap) between notes."""

    NAMED_INTERVALS = ('M', 'm', 'dim', 'aug')
    """Explicit interval types supported - major, minor, diminished, augmented."""

    def __init__(self, interval_type, distance):
        if interval_type not in Interval.NAMED_INTERVALS:
            raise ValueError('Unsupported interval type specified: ' + str(interval_type))

        try:
            int(distance) # test if distance value is a number
        except:
            raise ValueError('Expected integer for interval distance (provided ' + str(distance) + ')')
        if '.' in str(distance): # check that the distance number doesn't have a decimal place
            raise ValueError('Expected integer for interval distance (provided ' + str(distance) + ')')
        if int(distance) < 0:
            raise ValueError('Expected interval distance to be positive (provided ' + str(distance) + ')')

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