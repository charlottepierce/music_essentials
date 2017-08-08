class Interval(object):
    """Representation of an interval (i.e., gap) between notes."""

    NAMED_INTERVALS = ('M', 'm', 'dim', 'aug')
    """Explicit interval types supported - major, minor, diminished, augmented."""

    def __init__(self, interval_type, size):
        """Create a new Interval.

        Args:
            interval_type : str
                The type of interval. Should be one of:attr:`~music_essentials.interval.Interval.NAMED_INTERVALS`.
            distance : int
                The size of the interval. Should be positive.

        Returns:
            Interval
                A new interval of the given type and size.

        Raises:
            ValueError
                If an invalid interval type or size is provided.
        
        Examples:
            >>> i = Interval('M', 4)
            >>> print(i)
            M4
            >>> i = Interval('dim', 13)
            >>> print(i)
            dim13
            >>> i = Interval('i', 6)
            ValueError: Unsupported interval type specified: i
            >>> i = Interval('m', -1)
            ValueError: Expected interval distance to be positive (provided -1)
        """
        if interval_type not in Interval.NAMED_INTERVALS:
            raise ValueError('Unsupported interval type specified: ' + str(interval_type))

        try:
            int(size) # test if distance value is a number
        except:
            raise ValueError('Expected integer for interval distance (provided ' + str(size) + ')')
        if '.' in str(size): # check that the distance number doesn't have a decimal place
            raise ValueError('Expected integer for interval distance (provided ' + str(size) + ')')
        if int(size) < 0:
            raise ValueError('Expected interval distance to be positive (provided ' + str(size) + ')')

        self.interval_type = interval_type
        self.size = int(size)
    
    @classmethod
    def from_interval_string(cls, interval_string):
        """Create a new Interval.

        Processes the interval string then uses the constructor :attr:`~music_essentials.interval.Interval.__init__()`

        Args:
            interval_string : str
                A string representing the interval to create. Should be in the form:
                    ``<interval type><size>``
                
                The interval type should be one of:attr:`~music_essentials.interval.Interval.NAMED_INTERVALS`.

                The size of the interval should be positive.

        Returns:
            Interval
                A new interval of the given type and size.

        Raises:
            ValueError
                If an invalid interval type or size is provided.
        
        Examples:
            >>> i = Interval.from_interval_string('M4')
            >>> print(i)
            M4
            >>> i = Interval.from_interval_string('dim13')
            >>> print(i)
            dim13
            >>> i = Interval.from_interval_string('i6')
            ValueError: Unsupported interval type specified: i
            >>> i = Interval.from_interval_string('m-1')
            ValueError: Expected interval distance to be positive (provided -1)
        """
        size = interval_string[-1]
        interval_type = interval_string[:-1]

        return cls(interval_type, size)

    def __str__(self):
        return self.interval_type + str(self.distance)


if __name__ == '__main__':
    i = Interval('m', 3)
    print(i)

    i = Interval.from_interval_string('dim5')
    print(i)