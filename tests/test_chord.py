import pytest

from music_essentials import Chord, Note

def test_correct_note_list_length():
    c = Chord(Note.from_note_string('C4'))
    assert len(c.notes) == 1

def test_correct_note_list():
    c = Chord(Note.from_note_string('C4'))
    assert c.notes == [Note.from_note_string('C4')]

def test_incorrect_root_int():
    with pytest.raises(ValueError):
        c = Chord(1)

def test_incorrect_root_float():
    with pytest.raises(ValueError):
        c = Chord(7.2)

def test_incorrect_root_str():
    with pytest.raises(ValueError):
        c = Chord('A note!')