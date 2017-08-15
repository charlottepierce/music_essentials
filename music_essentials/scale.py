from .interval import Interval, TONE, SEMITONE, TONE_AND_HALF

class Scale(object):
    MAJOR = (TONE, TONE, SEMITONE, TONE, TONE, TONE, SEMITONE)
    MINOR = (TONE, SEMITONE, TONE, TONE, SEMITONE, TONE_AND_HALF, SEMITONE)

    @classmethod
    def build_scale(cls, tonic, scale_type):
        scale = [tonic]
        for diff in scale_type:
            new = scale[-1] + diff
            scale.append(new)

        return scale