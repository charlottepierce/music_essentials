# TODO: add shorthands for tone/semitone intervals

class Interval(object):
    """Representation of an interval (i.e., gap) between notes."""

    NAMED_INTERVAL_TYPES = ('M', 'm', 'P', 'dim', 'aug')
    """Explicit interval types supported - major, minor, diminished, augmented."""

    VALID_INTERVAL_TYPES = ('dim1', 'P1', 'aug1', 'dim2', 'm2', 'aug2', 'M2', 'dim3',
    'm3', 'M3', 'aug3', 'dim4', 'P4', 'aug4', 'dim5', 'P5', 'aug5', 'dim6',
    'm6', 'M6', 'aug6', 'dim7', 'm7', 'M7', 'aug7')
    """List of valid intervals up to (but not including) a perfect octave.

    Compound intervals are formed/processed internally by adding perfect 
    octaves to these valid interval types.
    
    Inclues:

    * ``'dim1'``/``'P1'``/``'aug1'``: diminished/perfect/augmented unison
    * ``'dim2'``/``'m2'``/``'M2'``/``'aug2'``: diminished/minor/major/augmented second
    * ``'dim3'``/``'m3'``/``'M3'``/``'aug3'``: diminished/minor/major/augmented third
    * ``'dim4'``/``'P4'``/``'aug4'``: diminished/perfect/augmented fourth
    * ``'dim5'``/``'P5'``/``'aug5'``: diminished/perfect/augmented fifth
    * ``'dim6'``/``'m6'``/``'M6'``/``'aug6'``: diminished/minor/major/augmented sixth
    * ``'dim7'``/``'m7'``/``'M7'``/``'aug7'``: diminished/minor/major/augmented seventh
    """

    def __init__(self, interval_type, size):
        """Create a new Interval.

        Args:
            interval_type : str
                The type of interval. Should be one of :attr:`~music_essentials.interval.Interval.NAMED_INTERVAL_TYPES`.
            distance : int
                The size of the interval. Should be positive.

        Returns:
            Interval
                A new interval of the given type and size.

        Raises:
            ValueError
                If an invalid interval type, size, or combination of type and size is provided.
        
        Examples:
            >>> i = Interval('M', 3)
            >>> print(i)
            M4
            >>> i = Interval('dim', 13)
            >>> print(i)
            dim13
            >>> i = Interval('i', 6)
            ValueError: Unsupported interval type specified: i
            >>> i = Interval('m', -1)
            ValueError: Expected interval distance to be positive (provided -1)
            >>> i = Interval('M', 5)
            ValueError: Impossible interval specific (provided M5)
        """
        if interval_type not in Interval.NAMED_INTERVAL_TYPES:
            raise ValueError('Unsupported interval type specified: ' + str(interval_type))

        try:
            int(size) # test if distance value is a number
        except:
            raise ValueError('Expected integer for interval distance (provided ' + str(size) + ')')
        if '.' in str(size): # check that the distance number doesn't have a decimal place
            raise ValueError('Expected integer for interval distance (provided ' + str(size) + ')')
        if int(size) <= 0:
            raise ValueError('Expected interval distance to be positive (provided ' + str(size) + ')')

        # convert interval to base (i.e., non-compound equivalent)
        interval_string = str(interval_type)
        if int(size) >= 8:
            base_size = int(size) - 7
            while (base_size >= 8):
                base_size -= 7
            interval_string += str(base_size)
        else:
            interval_string += str(size)

        # check if interval is possible (e.g., M4 is not a valid interval - it's P4)
        if interval_string not in Interval.VALID_INTERVAL_TYPES:
            raise ValueError('Impossible interval specific (provided ' + str(interval_type) + str(size) + ')')

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
                
                The interval type should be one of :attr:`~music_essentials.interval.Interval.NAMED_INTERVAL_TYPES`.

                The size of the interval should be positive.

        Returns:
            Interval
                A new interval of the given type and size.

        Raises:
            ValueError
                If an invalid interval type, size, or combination of type and size is provided.
        
        Examples:
            >>> i = Interval.from_interval_string('M3')
            >>> print(i)
            M4
            >>> i = Interval.from_interval_string('dim13')
            >>> print(i)
            dim13
            >>> i = Interval.from_interval_string('i6')
            ValueError: Unsupported interval type specified: i
            >>> i = Interval.from_interval_string('m-1')
            ValueError: Expected interval distance to be positive (provided -1)
            >>> i = Interval.from_interval_string('M5')
            ValueError: Impossible interval specific (provided M5)
        """
        for i in Interval.NAMED_INTERVAL_TYPES:
            if interval_string.startswith(i):
                interval_type = i
                size = interval_string.replace(i, '')

                return cls(interval_type, size)

        raise ValueError('Invalid interval string ' + str(interval_string))

    def __str__(self):
        """Create a string representation of the interval in the form ``<interval type><size>``
        
        Can be used as an interval string argument for :attr:`~music_essentials.interval.Interval.from_interval_string()`.
        
        Examples:
            >>> i = Interval.from_interval_string('m7')
            >>> print(i)
            m7
        """
        return self.interval_type + str(self.size)


if __name__ == '__main__':
    i = Interval('m', 3)
    print(i)

    i = Interval.from_interval_string('dim5')
    print(i)