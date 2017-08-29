import pytest

from music_essentials import Note, Scale

def test_non_note_tonic_str():
    with pytest.raises(TypeError):
        Scale.build_scale('dlsfk', 'major')

def test_non_note_tonic_int():
    with pytest.raises(TypeError):
        Scale.build_scale(1, 'major')

def test_unsupported_scale_type():
    with pytest.raises(ValueError):
        Scale.build_scale(Note('C', 4), 'scale')