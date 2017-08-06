class Note(object):
    VALID_PITCHES = ('C', 'D', 'E', 'F', 'G', 'A', 'B')
    VALID_ACCIDENTALS = ('#', '##', 'b', 'bb')

    def __init__(self, pitch, octave, accidental=None):
        if not isinstance(pitch, str):
            raise ValueError('Expected string for pitch - (provided ' + str(pitch) + ')')
        if pitch.upper() not in Note.VALID_PITCHES:
            raise ValueError('Invalid pitch: ' + str(pitch))

        try:
            int(octave) # test if octave value is a number
        except:
            raise ValueError('Expected integer for octave - (provided ' + str(octave) + ')')
        if '.' in str(octave): # check that the number doesn't have a decimal place
            raise ValueError('Expected integer for octave - (provided ' + str(octave) + ')')
        if (int(octave) < -1) or (int(octave) > 9):
            raise ValueError('Octave needs to be in the range [-1, 9] - (provided ' + str(octave) + ')')

        if accidental is not None:
            if not isinstance(accidental, str):
                raise ValueError('Expected string for accidental - provided ' + str(accidental) + ')')
            if accidental.lower() not in Note.VALID_ACCIDENTALS:
                raise ValueError('Invalid accidental: ' + str(accidental))

        self.pitch = pitch.upper()
        self.octave = int(octave)
        self.accidental = accidental

        if accidental is not None:
            self.accidental = self.accidental.lower()

    @classmethod
    def from_note_string(cls, note_string):
        pitch = note_string[0]
        octave = note_string[1]
        accidental = note_string[2:]

        if len(accidental) == 0:
            accidental = None

        return cls(pitch, octave, accidental)

    def __str__(self):
        s = self.pitch + str(self.octave)
        if self.accidental is not None:
            s += self.accidental
        
        return s


if __name__ == '__main__':
    n = Note('A', 4, accidental='b')
    print(n)

    n = Note.from_note_string('A4#')
    print(n)