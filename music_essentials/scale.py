# TODO: specify number of octaves
# TODO: specify direction

from .note import Note
from .interval import Interval

class Scale(object):
    """Static class methods for building lists of notes according to pre-defined patterns."""
    _MAJOR            = ('M2', 'M3', 'P4', 'P5', 'M6', 'M7', 'P8')
    _HARMONIC_MINOR   = ('M2', 'm3', 'P4', 'P5', 'm6', 'M7', 'P8')
    _NATURAL_MINOR    = ('M2', 'm3', 'P4', 'P5', 'm6', 'm7', 'P8')
    _MELODIC_MINOR    = ('M2', 'm3', 'P4', 'P5', 'M6', 'M7', 'P8')
    _DORIAN           = ('M2', 'm3', 'P4', 'P5', 'M6', 'm7', 'P8')
    _LOCRIAN          = ('m2', 'm3', 'P4', 'dim5', 'm6', 'm7', 'P8')
    _LYDIAN           = ('M2', 'M3', 'aug4', 'P5', 'M6', 'M7', 'P8')
    _MIXOLYDIAN       = ('M2', 'M3', 'P4', 'P5', 'M6', 'm7', 'P8')
    _PHRYGIAN         = ('m2', 'm3', 'P4', 'P5', 'm6', 'm7', 'P8')
    _MAJOR_PENTATONIC = ('M2', 'M3', 'P5', 'M6', 'P8')
    _MINOR_PENTATONIC = ('m3', 'P4', 'P5', 'm7', 'P8')

    _SCALE_PATTERNS = {
        'major'            : _MAJOR,
        'maj'              : _MAJOR,
        'minor'            : _HARMONIC_MINOR,
        'min'              : _HARMONIC_MINOR,
        'natural minor'    : _NATURAL_MINOR,
        'nat min'          : _NATURAL_MINOR,
        'melodic minor'    : _MELODIC_MINOR,
        'dorian'           : _DORIAN,
        'locrian'          : _LOCRIAN,
        'lydian'           : _LYDIAN,
        'mixolydian'       : _MIXOLYDIAN,
        'phrygian'         : _PHRYGIAN,
        'major pentatonic' : _MAJOR_PENTATONIC,
        'minor pentatonic' : _MINOR_PENTATONIC,
    }

    @classmethod
    def build_scale(cls, tonic, scale_type):
        """Build a scale.

        The scale will be built from the provided tonic, for one ascending octave.
        If building the scale will result in creating an invalid note (e.g., a note
        for which there is no MIDI number), the program will crash.

        Args:
            tonic : :attr:`~music_essentials.note.Note`
                The tonic note of the scale.
            
            scale_type : str
                The type of scale to build. Supported scale types are:

                * 'major'/'maj': major scale
                * 'minor'/'min': harmonic minor scale
                * 'natural minor'/'nat min': natural minor scale

        Returns:
            list
                The notes in the specified scale, in ascending order.

        Raises:
            `ValueError: <https://docs.python.org/2/library/exceptions.html#exceptions.ValueError>`_
                If an scale type is provided.

            `TypeError: <https://docs.python.org/2/library/exceptions.html#exceptions.TypeError>`_
                If the tonic is not a :attr:`~music_essentials.note.Note`., or scale type is not a string.
        """
        if not isinstance(tonic, Note):
            raise TypeError('Expected Note for tonic, got ' + str(tonic))
        if not isinstance(scale_type, str):
            raise TypeError('Expected string for scale type, got ' + str(scale_type))
        if scale_type not in Scale._SCALE_PATTERNS.keys():
            raise ValueError('Unknown scale type \'' + str(scale_type) + '\'')

        scale_pattern = Scale._SCALE_PATTERNS[scale_type]
        scale = [tonic]
        for diff in scale_pattern:
            new = scale[0] + Interval.from_interval_string(diff)
            scale.append(new)

        return scale
