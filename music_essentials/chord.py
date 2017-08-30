# TODO: instantiate chord with multiple notes
# TODO: add_note support note string

from .note import Note
from .scale import Scale
from .interval import Interval

class Chord(object):
    """Representation of group of notes that are played together."""

    _MAJOR = ('M3', 'm3')
    _MINOR = ('m3', 'M3')
    
    _CHORD_PATTERNS = {
        'major': _MAJOR,
        'maj': _MAJOR,
        'minor': _MINOR,
        'min': _MINOR
    }

    _CHORD_NUM_SCALE_INDEX = {
        'I' : 0,
        'II' : 1,
        'III': 2,
        'IV': 3,
        'V': 4,
        'VI': 5,
        'VII': 6,
        'VIII': 7}

    def __init__(self, root_note):
        """Create a new Chord.

        Once the Chord has been created, additional notes can be added using 
        :attr:`~music_essentials.chord.Chord.add_note`
        
        Args:
            root_note: :attr:`~music_essentials.note.Note`
                The first note to add to the chord.

        Returns:
            :attr:`~music_essentials.chord.Chord`
                A new chord object, with a single note added.

        Raises:
            `TypeError: <https://docs.python.org/2/library/exceptions.html#exceptions.TypeError>`_
                If anything but an instance of :attr:`~music_essentials.note.Note` is provided for `root_note`.
        
        Examples:
            >>> c = Chord(Note.from_note_string('C4'))
            >>> print(c)
            C4
            >>> c = Chord(Note.from_note_string('C4'))
            >>> c.add_note(Note.from_note_string('E4'))
            >>> print(c)
            C4+E4
            >>> c = Chord(5.5)
            Expected Note for root note, got '5.5'
        """
        if not isinstance(root_note, Note):
            raise TypeError('Expected Note for root note, got \'' + str(root_note) + '\'')

        self.notes = [root_note]

    @classmethod
    def build_chord(cls, tonic_key, chord_number, chord_type, base=None):
        # TODO: docstring
        # TODO: tests
        # TODO: validation
        s = Scale.build_scale(tonic_key, chord_type)
        root = s[Chord._CHORD_NUM_SCALE_INDEX[chord_number]]
        cls = Chord(root)
        for interval_str in Chord._CHORD_PATTERNS[chord_type]:
            i = Interval.from_interval_string(interval_str)
            cls.add_note(cls.notes[-1] + i)

        if base:
            b = s[Chord._CHORD_NUM_SCALE_INDEX[base]]
            if b in cls.notes:
                b.octave -= 1
            cls.notes.insert(0, b)

        return cls
    
    def root(self):
        """Get the root (i.e., lowest) note of the chord.
        
        Returns:
            :attr:`~music_essentials.note.Note`
                The lowest note of the chord.
        
        Examples:
            >>> c = Chord(Note.from_note_string('E4'))
            >>> print(c.root())
            E4
            >>> c = Chord(Note.from_note_string('E4'))
            >>> c.add_note(Note.from_note_string('D4'))
            >>> print(c.root())
            D4
        """
        return self.notes[0]

    def add_note(self, new_note):
        """Add another note to the chord.
        
        Args:
            new_note : :attr:`~music_essentials.note.Note`
                The note to add.

        Raises:
            `TypeError: <https://docs.python.org/2/library/exceptions.html#exceptions.TypeError>`_
                If `new_note` is not an instance of :attr:`~music_essentials.note.Note`.

        Examples:
            >>> c = Chord(Note.from_note_string('C4'))
            >>> c.add_note(Note.from_note_string('E4'))
            >>> print(c)
            C4+E4
            >>> c = Chord(Note.from_note_string('G4'))
            >>> c.add_note(Note.from_note_string('E4'))
            >>> c.add_note(Note.from_note_string('D4'))
            >>> print(c)
            D4+E4+G4
        """
        if not isinstance(new_note, Note):
            raise TypeError('Expected Note for new note, got \'' + str(new_note + '\''))

        if new_note < self.root():
            self.notes.insert(0, new_note)
            return

        for i in range(len(self.notes) - 1):
            if (new_note >= self.notes[i]) and (new_note < self.notes[i + 1]):
                self.notes.insert(i + 1, new_note)
                return

        self.notes.append(new_note)
    
    def __str__(self):
        """Get a string representation of the chord.
        
        Returns:
            str
                A string representation of the chord, in the form ``<note_1>+<note_2>+...+<note_n>``.
        """
        out = ''
        for n in self.notes:
            out += n.__str__() + '+'
        out = out [:-1]
        
        return out