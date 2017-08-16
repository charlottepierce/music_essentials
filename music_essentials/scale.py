# TODO: specify number of octaves
# TODO: specify direction
# TODO: add natural minor

from .interval import Interval, _TONE, _SEMITONE, _TONE_AND_HALF

class Scale(object):
    MAJOR = (_TONE, _TONE, _SEMITONE, _TONE, _TONE, _TONE, _SEMITONE)
    HARMONIC_MINOR = (_TONE, _SEMITONE, _TONE, _TONE, _SEMITONE, _TONE_AND_HALF, _SEMITONE)

    @classmethod
    def build_scale(cls, tonic, scale_type):
        # TODO: docstring (does support building of theoretical scales, as long as the result doesn't contain any accidentals above double sharps/flats)
        # TODO: validation (and tests for validation)
        scale = [tonic]
        for diff in scale_type:
            new = scale[-1] + diff
            scale.append(new)

        return scale