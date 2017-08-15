# TODO: test if method to convert Note to a MIDI note number works

import pytest

from music_essentials import Note

def test_midi_0():
    n = Note.from_note_string('C-1')
    mid = n.midi_note_number()
    assert mid == 0

def test_midi_1_sharp():
    n = Note.from_note_string('C-1#')
    mid = n.midi_note_number()
    assert mid == 1

def test_midi_1_flat():
    n = Note.from_note_string('D-1b')
    mid = n.midi_note_number()
    assert mid == 1

def test_midi_2():
    n = Note.from_note_string('D-1')
    mid = n.midi_note_number()
    assert mid == 2

def test_midi_3_sharp():
    n = Note.from_note_string('D-1#')
    mid = n.midi_note_number()
    assert mid == 3

def test_midi_3_flat():
    n = Note.from_note_string('E-1b')
    mid = n.midi_note_number()
    assert mid == 3

def test_midi_4():
    n = Note.from_note_string('E-1')
    mid = n.midi_note_number()
    assert mid == 4

def test_midi_5():
    n = Note.from_note_string('F-1')
    mid = n.midi_note_number()
    assert mid == 5

def test_midi_6_sharp():
    n = Note.from_note_string('F-1#')
    mid = n.midi_note_number()
    assert mid == 6

def test_midi_6_flat():
    n = Note.from_note_string('G-1b')
    mid = n.midi_note_number()
    assert mid == 6

def test_midi_7():
    n = Note.from_note_string('G-1')
    mid = n.midi_note_number()
    assert mid == 7

def test_midi_8_sharp():
    n = Note.from_note_string('G-1#')
    mid = n.midi_note_number()
    assert mid == 8

def test_midi_8_flat():
    n = Note.from_note_string('A-1b')
    mid = n.midi_note_number()
    assert mid == 8

def test_midi_9():
    n = Note.from_note_string('A-1')
    mid = n.midi_note_number()
    assert mid == 9

def test_midi_10_sharp():
    n = Note.from_note_string('A-1#')
    mid = n.midi_note_number()
    assert mid == 10

def test_midi_10_flat():
    n = Note.from_note_string('B-1b')
    mid = n.midi_note_number()
    assert mid == 10

def test_midi_11():
    n = Note.from_note_string('B-1')
    mid = n.midi_note_number()
    assert mid == 11