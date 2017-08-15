from .interval import Interval, _TONE, _SEMITONE, _TONE_AND_HALF

class Scale(object):
    MAJOR = (_TONE, _TONE, _SEMITONE, _TONE, _TONE, _TONE, _SEMITONE)
    MINOR = (_TONE, _SEMITONE, _TONE, _TONE, _SEMITONE, _TONE_AND_HALF, _SEMITONE)

    @classmethod
    def build_scale(cls, tonic, scale_type):
        scale = [tonic]
        for diff in scale_type:
            new = scale[-1] + diff
            scale.append(new)

        return scale