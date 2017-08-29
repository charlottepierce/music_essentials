import pytest

from music_essentials import Chord, Note

# Test constructor
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

# Test retrieval of root note
def test_root_one_note():
    c = Chord(Note.from_note_string('C4'))
    root = Note.from_note_string('C4')
    assert c.root() == root

def test_root_two_notes():
    c = Chord(Note.from_note_string('C4'))
    c.add_note(Note.from_note_string('E4'))
    root = Note.from_note_string('C4')
    assert c.root() == root

def test_root_insert_under():
    c = Chord(Note.from_note_string('C4'))
    c.add_note(Note.from_note_string('B3'))
    root = Note.from_note_string('B3')
    assert c.root() == root

def test_root_insert_under_same_pitch():
    c = Chord(Note.from_note_string('C4'))
    c.add_note(Note.from_note_string('C4b'))
    root = Note.from_note_string('C4b')
    assert c.root() == root
