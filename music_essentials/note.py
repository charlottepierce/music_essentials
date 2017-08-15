# TODO: method to get vextab representation
# TODO: comparison between two notes: e.g., note1 < note2 = true/false

from .interval import Interval

class Note(object):
    """A single note, defined by a pitch, octave, and (optional) accidentals."""

    VALID_PITCHES = ('C', 'D', 'E', 'F', 'G', 'A', 'B')
    """List of valid pitch characters."""

    VALID_ACCIDENTALS = ('#', '##', 'b', 'bb')
    """List of valid accidental representors."""

    def __init__(self, pitch, octave, accidental=None):
        """Create a new Note.

        Args:
            pitch : str
                The pitch of the note. Should be one of :attr:`~music_essentials.note.Note.VALID_PITCHES`, but can
                be upper or lower case.
            octave : int
                The octave of the note. Should be in the range [-1, 9].

        Kwags:
            accidental : str (default None)
                The accidental to apply to the note. Should be one of :attr:`~music_essentials.note.Note.VALID_ACCIDENTALS`.

        Returns:
            Note
                A new note with the given pitch, octave, and accidental.

        Raises:
            ValueError
                If an invalid pitch, octave, or accidental is provided.
        
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
            raise ValueError('Expected string for pitch, got: ' + str(pitch))
        if pitch.upper() not in Note.VALID_PITCHES:
            raise ValueError('Invalid pitch: ' + str(pitch))

        try:
            int(octave) # test if octave value is a number
        except:
            raise ValueError('Expected integer for octave, got: ' + str(octave))
        if '.' in str(octave): # check that the number doesn't have a decimal place
            raise ValueError('Expected integer for octave, got ' + str(octave))
        if (int(octave) < -1) or (int(octave) > 9):
            raise ValueError('Octave needs to be in the range [-1, 9], got: ' + str(octave))

        if accidental is not None:
            if accidental.lower() not in Note.VALID_ACCIDENTALS:
                raise ValueError('Invalid accidental: ' + str(accidental))

        self.pitch = pitch.upper()
        self.octave = int(octave)
        self.accidental = accidental

        if accidental is not None:
            self.accidental = self.accidental.lower()

        if (self.midi_note_number() < 0) or (self.midi_note_number() > 127):
            raise ValueError('Invalid Note parameters, results in MIDI note number: ' + str(self.midi_note_number()))

    @classmethod
    def from_note_string(cls, note_string):
        """Create a new Note.

        Processes the note string then uses the constructor :attr:`~music_essentials.note.Note.__init__()`

        Args:
            note_string : str
                A string representing the note to create. Should be in the form:
                    ``<pitch><octave><accidental>``
                
                The pitch of the note should be one of :attr:`~music_essentials.note.Note.VALID_PITCHES`, but can
                be upper or lower case.

                The octave of the note should be in the range ``[-1, 9]``.

                The accidental is optional, but if used should be one of :attr:`~music_essentials.note.Note.VALID_ACCIDENTALS`.

        Returns:
            Note
                A new note with the given pitch, octave, and accidental.

        Raises:
            ValueError
                If an invalid pitch, octave, or accidental is provided.
        
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
        pitch = note_string[0]
        octave = note_string[1]
        accidental = note_string[2:]

        if octave == '-':
            # interval is negative - offset octave and accidental variables
            octave = note_string[1:3]
            accidental = note_string[3:]

        if len(accidental) == 0:
            accidental = None

        return cls(pitch, octave, accidental)

    def __add__(self, other):
        # TODO: docstring
        if not isinstance(other, Interval):
            raise TypeError('unsupported operand type(s) for +: \'Note\' and \'' + str(other.__class__.__name__) + '\'')

        print('Adding ' + str(self) + ' and ' + str(other))
        
        # calculate new pitch
        note_pitch_idx = Note.VALID_PITCHES.index(self.pitch)
        pitch_diff = (other.size % 7) - 1
        if (note_pitch_idx + pitch_diff) > (len(Note.VALID_PITCHES) - 1):
            pitch_diff = -7 + pitch_diff
        new_pitch = Note.VALID_PITCHES[note_pitch_idx + pitch_diff]
        
        # calculate new octave
        octave_diff = 0
        if other.size > 7:
            octave_diff = (other.size / 8)
        elif Note.VALID_PITCHES.index(new_pitch) < note_pitch_idx:
            octave_diff += 1
        new_octave = int(self.octave + octave_diff)

        # TODO: finish this
        # calculate new accidentals (if any)
        new_accidentals = self.accidental # notes from perfect intervals have the same accidentals

    def midi_note_number(self):
        # TODO: docstring
        """Assumes middle C is MIDI note number 60."""
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


if __name__ == '__main__':
    n = Note.from_note_string('C4')
    i = Interval.from_interval_string('P12')

    print('Result: ' + str(n + i))