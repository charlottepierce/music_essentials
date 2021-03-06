import random
import math

from .interval import Interval

class Note(object):
    """A single note, defined by a pitch, octave, and (optional) accidentals."""

    VALID_PITCHES = ('C', 'D', 'E', 'F', 'G', 'A', 'B')
    """List of valid pitch characters."""

    VALID_ACCIDENTALS = ('#', '##', 'b', 'bb', None)
    """List of valid accidental representors."""

    def __init__(self, pitch, octave, accidental=None, random_instance=random.Random()):
        """Create a new Note.

        Args:
            pitch : str
                The pitch of the note. Should be one of :attr:`~music_essentials.note.Note.VALID_PITCHES`, but can
                be upper or lower case.
            octave : int
                The octave of the note. Should be in the range [-1, 9].

        Kwags:
            accidental : str (default `None`)
                The accidental to apply to the note. Should be one of :attr:`~music_essentials.note.Note.VALID_ACCIDENTALS`.

            duration : float (default `None`)
                The duration of the note, in terms of how many would fit into one bar in common time.
                For example, a semibreve has a duration of 1; a quaver has a duration of 8.

            dotted : boolean (default `False`)
                If true, the duration of the note is multiplied by 1.5.

        Returns:
            :attr:`~music_essentials.note.Note`
                A new note with the given pitch, octave, and accidental.

        Raises:
            `ValueError: <https://docs.python.org/2/library/exceptions.html#exceptions.ValueError>`_
                If an invalid pitch, octave, or accidental is provided.

            `TypeError: <https://docs.python.org/2/library/exceptions.html#exceptions.TypeError>`_
                If an incorrect type of value is given for pitch, octave, or accidental.

        Examples:
            >>> n = Note('A', 4, '##')
            >>> print(n)
            A4##
            >>> n = Note('d', 7)
            >>> print(n)
            D7
            >>> n = Note('x', 6)
            ValueError: Invalid pitch: x
        """
        if not isinstance(pitch, str):
            raise TypeError('Expected string for pitch, got: ' + str(pitch))
        if pitch.upper() not in Note.VALID_PITCHES:
            raise ValueError('Invalid pitch: ' + str(pitch))

        try:
            int(octave) # test if octave value is a number
        except:
            raise TypeError('Expected integer for octave, got: ' + str(octave))
        if '.' in str(octave): # check that the number doesn't have a decimal place
            raise TypeError('Expected integer for octave, got ' + str(octave))
        if (int(octave) < -1) or (int(octave) > 9):
            raise ValueError('Octave needs to be in the range [-1, 9], got: ' + str(octave))

        if accidental is not None:
            if accidental.lower() not in Note.VALID_ACCIDENTALS:
                raise ValueError('Invalid accidental: ' + str(accidental))

        self.pitch = pitch.upper()
        self.octave = int(octave)
        self.accidental = accidental
        self.is_rest = False
        self.random_instance = random_instance

        if accidental is not None:
            self.accidental = self.accidental.lower()

        if (self.midi_note_number() < 0) or (self.midi_note_number() > 127):
            raise ValueError('Invalid Note parameters \'' + str(self.pitch) + str(self.octave) + str(self.accidental) + '\', results in MIDI note number: ' + str(self.midi_note_number()))

    @classmethod
    def from_note_string(cls, note_string, random_instance=random.Random()):
        """Create a new Note.

        Processes the note string then uses the constructor :attr:`~music_essentials.note.Note.__init__()`.
        If the note string is 'r', a :attr:`~music_essentials.note.Rest` is returned.

        Args:
            note_string : str
                A string representing the note to create. Should be in the form:
                    ``<pitch><octave><accidental>``

                The pitch of the note should be one of :attr:`~music_essentials.note.Note.VALID_PITCHES`, but can
                be upper or lower case.

                The octave of the note should be in the range ``[-1, 9]``.

                The accidental is optional, but if used should be one of :attr:`~music_essentials.note.Note.VALID_ACCIDENTALS`.

        Returns:
            :attr:`~music_essentials.note.Note`
                A new note with the given pitch, octave, and accidental.

        Raises:
            `ValueError: <https://docs.python.org/2/library/exceptions.html#exceptions.ValueError>`_
                If an invalid pitch, octave, or accidental is provided.

            `TypeError: <https://docs.python.org/2/library/exceptions.html#exceptions.TypeError>`_
                If the provided note string is not a string.

        Examples:
            >>> n = Note.from_note_string('A4##')
            >>> print(n)
            A4##
            >>> n = Note.from_note_string('d7')
            >>> print(n)
            D7
            >>> n = Note.from_note_string('x6')
            ValueError: Invalid pitch: x
        """
        if not isinstance(note_string, str):
            raise TypeError('Expected string for note string, got \'' + str(note_string + '\''))

        if note_string == 'r':
            return Rest()

        pitch = note_string[0]
        octave = note_string[1]
        accidental = note_string[2:]

        if octave == '-':
            # interval is negative - offset octave and accidental variables
            octave = note_string[1:3]
            accidental = note_string[3:]

        if len(accidental) == 0:
            accidental = None

        return cls(pitch, octave, accidental, random_instance)

    @classmethod
    def from_midi_num(cls, midi_num, random_instance=random.Random()):
        """Create a new note.
        
        Uses the provided MIDI number to set the note parameters.
        
        Args:
            midi_num : int
                A number in the range [0, 127] representing a Note.

        Returns:
            :attr:`~music_essentials.note.Note`
                A new note with a pitch, octave, and accidental corresponding to the
                given MIDI note number.
        """
        try:
            int(midi_num) # test if octave value is a number
        except:
            raise TypeError('Expected integer for MIDI number, got: ' + str(midi_num))
        if '.' in str(midi_num): # check that the number doesn't have a decimal place
            raise TypeError('Expected integer for MIDI number, got ' + str(midi_num))
        if (int(midi_num) < 0) or (int(midi_num) > 127):
            raise ValueError('MIDI number needs to be in the range [0, 127], got: ' + str(midi_num))

        # key = midi_num % 12; val = (pitch, accidental)
        pitch_accidental_mappings = {
            0 : ('C', None),
            1 : ('C', '#'),
            2 : ('D', None),
            3 : ('D', '#'),
            4 : ('E', None),
            5 : ('F', None),
            6 : ('F', '#'),
            7 : ('G', None),
            8 : ('G', '#'),
            9 : ('A', None),
            10 : ('A', '#'),
            11 : ('B', None)
        }

        octave = int(math.floor(midi_num / 12) - 1)
        pitch, accidental = pitch_accidental_mappings[midi_num % 12]
        return cls(pitch, octave, accidental, random_instance)

    @classmethod
    def random_note(cls, lowest_midi_num=0, highest_midi_num=127, method='rand', chance_for_rest=0.01, random_instance=random.Random()):
        """Create and return a random Note within the MIDI note
        number range [lowest_midi_num, highest_midi_num].

        Args:
            lowest_midi_num : int (default 0)
                The lowest MIDI number allowed.

            highest_midi_num : int (default 127)
                The highest MIDI number allowed.

            method : str (default 'rand')
                The method of random selection to use.
                If 'rand', a uniform distribution will be used.
                If 'gauss', a gaussian distribution will be used.

        Returns:
            :attr:`~music_essentials.note.Note`
                A new note with a randomly selected pitch, octave, and accidental.
        """

        if random_instance.random() <= chance_for_rest:
            return Rest()

        midi_num = -1
        if method == 'rand':
            midi_num = random_instance.randrange(lowest_midi_num, highest_midi_num + 1)
        elif method == 'gauss':
            mean = lowest_midi_num + math.floor(((highest_midi_num - lowest_midi_num) / 2))
            std_dev = math.floor((mean - lowest_midi_num) / 3)
            while (midi_num < lowest_midi_num) or (midi_num > highest_midi_num):
                midi_num = round(random_instance.gauss(mean, std_dev))

        return cls.from_midi_num(midi_num)

    def midi_note_number(self):
        """Get the MIDI note number equivalent to this pitch.

        Assumes that middle C corresponds to the MIDI note number 60, as
        described on `Wikipedia: <https://en.wikipedia.org/wiki/Scientific_pitch_notation#Table_of_note_frequencies>`_.

        Returns:
            int
                The MIDI note number representing this pitch.

        Examples:
            >>> n = Note.from_note_string('C-1')
            >>> print(n.midi_note_number())
            0
            >>> n = Note.from_note_string('G9')
            >>> print(n.midi_note_number())
            127
            >>> n = Note.from_note_string('B0b')
            >>> print(n.midi_note_number())
            22
        """
        # calculate number based on octave and pitch
        midi_num = self.octave * 12
        midi_num += Note.VALID_PITCHES.index(self.pitch) * 2
        if self.pitch not in ('C', 'D', 'E'):
            midi_num -= 1
        midi_num += 12

        # adjust for accidentals
        if self.accidental is not None:
            midi_num -= self.accidental.count('b')
            midi_num += self.accidental.count('#')

        return midi_num

    def __add__(self, other):
        """Calculate and return the note found when adding an interval to this note.

        Args:
            other : :attr:`~music_essentials.interval.Interval`
                The interval to add to this note.

        Returns:
            :attr:`~music_essentials.note.Note`
                The new note that comes from adding the provided interval to this note.

        Raises:
            `TypeError: <https://docs.python.org/2/library/exceptions.html#exceptions.TypeError>`_
                If the object to add is not an :attr:`~music_essentials.interval.Interval`.

        Examples:
            >>> n = Note.from_note_string('C4')
            >>> i = Interval.from_interval_string('M2')
            >>> print(n + i)
            D4
            >>> n = Note.from_note_string('C4')
            >>> i = Interval.from_interval_string('m14')
            >>> print(n + i)
            B5b
            >>> n = Note.from_note_string('C4')
            >>> i = Interval.from_interval_string('aug13')
            >>> print(n + i)
            A5#
        """
        if not isinstance(other, Interval):
            raise TypeError('unsupported operand type(s) for +: \'Note\' and \'' + str(other.__class__.__name__) + '\'')

        # calculate new pitch
        note_pitch_idx = Note.VALID_PITCHES.index(self.pitch)
        pitch_diff = (other.size % 7) - 1
        if (note_pitch_idx + pitch_diff) > (len(Note.VALID_PITCHES) - 1):
            pitch_diff = -7 + pitch_diff
        new_pitch = Note.VALID_PITCHES[note_pitch_idx + pitch_diff]

        # calculate new octave
        base_size = int(other.size)
        octave_diff = 0
        is_compound = False
        while (base_size >= 8):
            base_size -= 7
            octave_diff += 1
            is_compound = True
        if Note.VALID_PITCHES.index(new_pitch) < Note.VALID_PITCHES.index(self.pitch):
            octave_diff += 1
        new_octave = self.octave + octave_diff

        # find appropriate accidental
        goal_semitone_diff = octave_diff * 12
        if not is_compound and octave_diff > 0:
            goal_semitone_diff -= 12
        if base_size in Interval._PERFECT_INTERVALS_SEMITONES.keys():
            goal_semitone_diff += Interval._PERFECT_INTERVALS_SEMITONES[base_size]
            if other.interval_type == 'dim':
                goal_semitone_diff -= 1
            elif other.interval_type == 'aug':
                goal_semitone_diff += 1
        elif base_size in Interval._MAJOR_INTERVALS_SEMITONES.keys():
            goal_semitone_diff += Interval._MAJOR_INTERVALS_SEMITONES[base_size]
            if other.interval_type == 'dim':
                goal_semitone_diff -= 2
            elif other.interval_type == 'm':
                goal_semitone_diff -= 1
            elif other.interval_type == 'aug':
                goal_semitone_diff += 1

        for a in Note.VALID_ACCIDENTALS:
            new_note = Note(new_pitch, new_octave, a)
            diff = new_note.midi_note_number() - self.midi_note_number()

            if diff == goal_semitone_diff:
                return new_note

        raise RuntimeError('FATAL ERROR: Could not complete note + interval operation: ' + str(self) + ' + ' + str(other))

    def is_enharmonic(self, other):
        """Check if two notes are `enharmonic <https://en.wikipedia.org/wiki/Enharmonic>`_.
        
        Args:
            other : :attr:`~music_essentials.note.Note`
                The note to compare this to.
        
        Returns:
            bool
                True if the two notes represent the same pitch, otherwise false.

        Raises:
            `ValueError: <https://docs.python.org/2/library/exceptions.html#exceptions.ValueError>`_
                If anything other than a :attr:`~music_essentials.note.Note` is given to compare to.

            `TypeError: <https://docs.python.org/2/library/exceptions.html#exceptions.TypeError>`_
                If the object to compare to is not a :attr:`~music_essentials.note.Note`.

        Examples:
            >>> n1 = Note('C', 4)
            >>> n2 = Note('D', 4)
            >>> n1.is_enharmonic(n2)
            False
            >>> n1 = Note('C', 4, '#')
            >>> n2 = Note('D', 4, 'b')
            >>> n1.is_enharmonic(n2)
            True
            >>> n1 = Note('F', 4)
            >>> n2 = Note('E', 4, '#')
            >>> n1.is_enharmonic(n2)
            True
            >>> n1 = Note('F', 4)
            >>> n2 = Note('G', 4, 'bb')
            >>> n1.is_enharmonic(n2)
            True
        """
        if not isinstance(other, Note) or (isinstance(other, Rest) or isinstance(self, Rest)):
            raise TypeError('Can not determine whether ' + str(self) + ' and ' + str(other) + ' are enharmonic')

        return self.midi_note_number() == other.midi_note_number()

    def __eq__(self, other):
        """Check if this note is equal to another note.

        Does not consider `enharmonic notes <https://en.wikipedia.org/wiki/Enharmonic>`_ to be equal.
        
        Args:
            other : :attr:`~music_essentials.note.Note`
                The note to compare this note to.

        Returns:
            bool
                True if the notes have the same pitch, octave, and accidentals; otherwise false.

        Raises:
            `TypeError: <https://docs.python.org/2/library/exceptions.html#exceptions.TypeError>`_
                If the object to compare to is not a :attr:`~music_essentials.note.Note`.

        Examples:
            >>> n1 = Note.from_note_string('C4')
            >>> n2 = Note('C', 4)
            >>> n1 == n2
            True
            >>> n1 = Note.from_note_string('C4#')
            >>> n2 = Note.from_note_string('D4b')
            >>> n1 == n2
            False        
        """

        if not isinstance(other, Note) or (isinstance(other, Rest) or isinstance(self, Rest)):
            raise TypeError('Can not check equality between Note and \'' + str(other) + '\'')

        return (self.pitch == other.pitch) and (self.octave == other.octave) and (self.accidental == other.accidental)

    def __ne__(self, other):
        """Check if this note is note equal to another note.

        Does not consider `enharmonic notes <https://en.wikipedia.org/wiki/Enharmonic>`_ to be equal.
        
        Args:
            other : :attr:`~music_essentials.note.Note`
                The note to compare this note to.

        Returns:
            bool
                True if the notes do not have the same pitch, octave, and accidentals; otherwise false.

        Raises:
            `TypeError: <https://docs.python.org/2/library/exceptions.html#exceptions.TypeError>`_
                If the object to compare to is not a :attr:`~music_essentials.note.Note`.

        Examples:
            >>> n1 = Note.from_note_string('C4')
            >>> n2 = Note('C', 4)
            >>> n1 != n2
            False
            >>> n1 = Note.from_note_string('C4#')
            >>> n2 = Note.from_note_string('D4b')
            >>> n1 != n2
            True    
        """
        return not self.__eq__(other)

    def __lt__(self, other):
        """Check if this note is less than another note.

        Does not consider `enharmonic notes <https://en.wikipedia.org/wiki/Enharmonic>`_ to be equal.
        If two notes are enharmonic, the note with the lower written pitch is considered lower.
        
        Args:
            other : :attr:`~music_essentials.note.Note`
                The note to compare this note to.

        Returns:
            bool
                True if this note is less than the other, otherwise false.

        Raises:
            `TypeError: <https://docs.python.org/2/library/exceptions.html#exceptions.TypeError>`_
                If the object to compare to is not a :attr:`~music_essentials.note.Note`.

        Examples:
            >>> n1 = Note.from_note_string('C4')
            >>> n2 = Note('C', 4)
            >>> n1 < n2
            False
            >>> n1 = Note.from_note_string('D4')
            >>> n2 = Note.from_note_string('G4')
            >>> n1 < n2
            True
            >>> n2 < n1
            False    
        """
        if not isinstance(other, Note) or (isinstance(other, Rest) or isinstance(self, Rest)):
            raise TypeError('Can not check equality between Note and \'' + str(other) + '\'')

        if self.__eq__(other):
            return False

        if self.is_enharmonic(other):
            if self.octave != other.octave:
                return self.octave < other.octave
            return Note.VALID_PITCHES.index(self.pitch) < Note.VALID_PITCHES.index(other.pitch)

        return self.midi_note_number() < other.midi_note_number()

    def __gt__(self, other):
        """Check if this note is greater than another note.

        Does not consider `enharmonic notes <https://en.wikipedia.org/wiki/Enharmonic>`_ to be equal.
        If two notes are enharmonic, the note with the higher written pitch is considered higher.
        
        Args:
            other : :attr:`~music_essentials.note.Note`
                The note to compare this note to.

        Returns:
            bool
                True if this note is greater than the other, otherwise false.

        Raises:
            `TypeError: <https://docs.python.org/2/library/exceptions.html#exceptions.TypeError>`_
                If the object to compare to is not a :attr:`~music_essentials.note.Note`.

        Examples:
            >>> n1 = Note.from_note_string('C4')
            >>> n2 = Note('C', 4)
            >>> n1 > n2
            False
            >>> n1 = Note.from_note_string('D4')
            >>> n2 = Note.from_note_string('G4')
            >>> n1 > n2
            False
            >>> n2 > n1
            True 
        """
        if not isinstance(other, Note) or (isinstance(other, Rest) or isinstance(self, Rest)):
            raise TypeError('Can not check equality between Note and \'' + str(other) + '\'')

        if self.__eq__(other):
            return False

        if self.is_enharmonic(other):
            if self.octave != other.octave:
                return self.octave > other.octave
            return Note.VALID_PITCHES.index(self.pitch) > Note.VALID_PITCHES.index(other.pitch)

        return self.midi_note_number() > other.midi_note_number()

    def __le__(self, other):
        """Check if this note is less than or equal to another note.
        
        Args:
            other : :attr:`~music_essentials.note.Note`
                The note to compare this note to.

        Returns:
            bool
                True if this note is less than or equal to the other, otherwise false.

        Raises:
            `TypeError: <https://docs.python.org/2/library/exceptions.html#exceptions.TypeError>`_
                If the object to compare to is not a :attr:`~music_essentials.note.Note`.

        Examples:
            >>> n1 = Note.from_note_string('C4')
            >>> n2 = Note('C', 4)
            >>> n1 < n2
            True
            >>> n1 = Note.from_note_string('D4')
            >>> n2 = Note.from_note_string('G4')
            >>> n1 < n2
            True
            >>> n2 < n1
            False    
        """
        return not self.__gt__(other)

    def __ge__(self, other):
        """Check if this note is greater than or equal to another note.
        
        Args:
            other : :attr:`~music_essentials.note.Note`
                The note to compare this note to.

        Returns:
            bool
                True if this note is greater than or equal to the other, otherwise false.

        Raises:
            `TypeError: <https://docs.python.org/2/library/exceptions.html#exceptions.TypeError>`_
                If the object to compare to is not a :attr:`~music_essentials.note.Note`.

        Examples:
            >>> n1 = Note.from_note_string('C4')
            >>> n2 = Note('C', 4)
            >>> n1 > n2
            True
            >>> n1 = Note.from_note_string('D4')
            >>> n2 = Note.from_note_string('G4')
            >>> n1 > n2
            False
            >>> n2 > n1
            True 
        """
        return not self.__lt__(other)

    def __str__(self):
        """Create a string representation of the note in the form ``<pitch><octave><accidental>``.

        Can be used as a note string argument for :attr:`~music_essentials.note.Note.from_note_string()`.

        Examples:
            >>> n = Note('B', 9, '#')
            >>> print(n)
            B9#
            >>> n = Note('g', 7)
            >>> print(n)
            G7
            >>> n = Note('D', 3, 'B')
            >>> print(n)
            D3b
        """
        s = self.pitch + str(self.octave)
        if self.accidental is not None:
            s += self.accidental

        return s


class Rest(Note):
    """A single note, defined as a period of silence."""

    def __init__(self):
        """Create a rest note. Sets the note's pitch, octave, and accidental as `None`."""
        self.pitch = None
        self.octave = None
        self.accidental = None
        self.is_rest = True

    def midi_note_number(self):
        """Override the MIDI note number method from the parent class.

        Returns -1 to indicate that a rest has no MIDI note number.
        """

        return -1

    def __str__(self):
        """Create a string representation of the rest.
        
        Examples:
            >>> r = Rest()
            >>> print(r)
            r
        """

        return 'r'
