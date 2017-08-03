class Note(object):
    def __init__(self, pitch, octave, accidental=None):
        self.pitch = pitch.upper()
        self.octave = octave
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