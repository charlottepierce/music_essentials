# TODO: specify number of octaves
# TODO: specify direction

from .note import Note
from .interval import Interval, _TONE, _SEMITONE, _TONE_AND_HALF

class Scale(object):
    """Static class methods for building lists of notes according to pre-defined patterns."""
    _MAJOR = (_TONE, _TONE, _SEMITONE, _TONE, _TONE, _TONE, _SEMITONE)
    _HARMONIC_MINOR = (_TONE, _SEMITONE, _TONE, _TONE, _SEMITONE, _TONE_AND_HALF, _SEMITONE)
    _NATURAL_MINOR = (_TONE, _SEMITONE, _TONE, _TONE, _SEMITONE, _TONE, _TONE)

    _SCALE_PATTERNS = {
        'major': _MAJOR,
        'maj': _MAJOR,
        'minor': _HARMONIC_MINOR,
        'min': _HARMONIC_MINOR,
        'natural minor': _NATURAL_MINOR,
        'nat min' : _NATURAL_MINOR
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
                If an invalid tonic or scale type is provided.
        """
        if not isinstance(tonic, Note):
            raise ValueError('Expected Note for tonic, got ' + str(tonic))
        if scale_type not in Scale._SCALE_PATTERNS.keys():
            raise ValueError('Unknown scale type \'' + str(scale_type + '\''))

        scale_pattern = Scale._SCALE_PATTERNS[scale_type]
        scale = [tonic]
        for diff in scale_pattern:
            new = scale[-1] + diff
            scale.append(new)

        return scale