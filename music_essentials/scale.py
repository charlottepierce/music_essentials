# TODO: specify number of octaves
# TODO: specify direction
# TODO: add natural minor

from .interval import Interval, _TONE, _SEMITONE, _TONE_AND_HALF

class Scale(object):
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
        # TODO: docstring (does support building of theoretical scales, as long as the result doesn't contain any accidentals above double sharps/flats)
        # TODO: validation (and tests for validation)
        scale_pattern = Scale._SCALE_PATTERNS[scale_type]
        scale = [tonic]
        for diff in scale_pattern:
            new = scale[-1] + diff
            scale.append(new)

        return scale