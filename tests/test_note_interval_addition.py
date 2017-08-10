import pytest

from music_essentials import Note, Interval

# Simple additions
def test_valid_addition_simple_major_second():
    n = Note.from_note_string('C4')
    i = Interval.from_interval_string('M2')
    res = n + 1
    assert (res.pitch == 'D') and (res.octave == 4) and (res.accidental == None)

def test_valid_addition_simple_major_fifth():
    n = Note.from_note_string('C4')
    i = Interval.from_interval_string('P5')
    res = n + 1
    assert (res.pitch == 'G') and (res.octave == 4) and (res.accidental == None)

def test_valid_addition_simple_minor_third():
    n = Note.from_note_string('C4')
    i = Interval.from_interval_string('m3')
    res = n + 1
    assert (res.pitch == 'E') and (res.octave == 4) and (res.accidental == 'b')

def test_valid_addition_simple_minor_seventh():
    n = Note.from_note_string('C4')
    i = Interval.from_interval_string('m7')
    res = n + 1
    assert (res.pitch == 'B') and (res.octave == 4) and (res.accidental == 'b')

def test_valid_addition_simple_unison():
    n = Note.from_note_string('C4')
    i = Interval.from_interval_string('P1')
    res = n + 1
    assert (res.pitch == 'C') and (res.octave == 4) and (res.accidental == None)

def test_valid_addition_simple_octave():
    n = Note.from_note_string('C4')
    i = Interval.from_interval_string('P8')
    res = n + 1
    assert (res.pitch == 'C') and (res.octave == 5) and (res.accidental == None)

# Compound additions
def test_valid_addition_compound_major():
    n = Note.from_note_string('C4')
    i = Interval.from_interval_string('M10')
    res = n + 1
    assert (res.pitch == 'E') and (res.octave == 5) and (res.accidental == None)

def test_valid_addition_compound_minor():
    n = Note.from_note_string('C4')
    i = Interval.from_interval_string('m14')
    res = n + 1
    assert (res.pitch == 'B') and (res.octave == 5) and (res.accidental == 'b')

def test_valid_addition_compound_augmented():
    n = Note.from_note_string('C4')
    i = Interval.from_interval_string('aug13')
    res = n + 1
    assert (res.pitch == 'A') and (res.octave == 5) and (res.accidental == '#')

def test_valid_addition_compound_diminished():
    n = Note.from_note_string('C4')
    i = Interval.from_interval_string('dim14')
    res = n + 1
    assert (res.pitch == 'B') and (res.octave == 5) and (res.accidental == 'bb')

def test_valid_addition_compound_diminished_octave():
    n = Note.from_note_string('C4')
    i = Interval.from_interval_string('dim8')
    res = n + 1
    assert (res.pitch == 'C') and (res.octave == 5) and (res.accidental == 'b')