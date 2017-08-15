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

def test_midi_12():
    n = Note.from_note_string('C0')
    mid = n.midi_note_number()
    assert mid == 12

def test_midi_13_sharp():
    n = Note.from_note_string('C0#')
    mid = n.midi_note_number()
    assert mid == 13

def test_midi_13_flat():
    n = Note.from_note_string('D0b')
    mid = n.midi_note_number()
    assert mid == 13

def test_midi_14():
    n = Note.from_note_string('D0')
    mid = n.midi_note_number()
    assert mid == 14

def test_midi_15_sharp():
    n = Note.from_note_string('D0#')
    mid = n.midi_note_number()
    assert mid == 15

def test_midi_15_flat():
    n = Note.from_note_string('E0b')
    mid = n.midi_note_number()
    assert mid == 15

def test_midi_16():
    n = Note.from_note_string('E0')
    mid = n.midi_note_number()
    assert mid == 16

def test_midi_17():
    n = Note.from_note_string('F0')
    mid = n.midi_note_number()
    assert mid == 17

def test_midi_18_sharp():
    n = Note.from_note_string('F0#')
    mid = n.midi_note_number()
    assert mid == 18

def test_midi_18_flat():
    n = Note.from_note_string('G0b')
    mid = n.midi_note_number()
    assert mid == 18

def test_midi_19():
    n = Note.from_note_string('G0')
    mid = n.midi_note_number()
    assert mid == 19

def test_midi_20_sharp():
    n = Note.from_note_string('G0#')
    mid = n.midi_note_number()
    assert mid == 20

def test_midi_20_flat():
    n = Note.from_note_string('A0b')
    mid = n.midi_note_number()
    assert mid == 20

def test_midi_21():
    n = Note.from_note_string('A0')
    mid = n.midi_note_number()
    assert mid == 21

def test_midi_22_sharp():
    n = Note.from_note_string('A0#')
    mid = n.midi_note_number()
    assert mid == 22

def test_midi_22_flat():
    n = Note.from_note_string('B0b')
    mid = n.midi_note_number()
    assert mid == 22

def test_midi_23():
    n = Note.from_note_string('B0')
    mid = n.midi_note_number()
    assert mid == 23

def test_midi_120():
    n = Note.from_note_string('C9')
    mid = n.midi_note_number()
    assert mid == 120

def test_midi_127():
    n = Note.from_note_string('G9')
    mid = n.midi_note_number()
    assert mid == 127

def test_midi_127_flat():
    n = Note.from_note_string('A9bb')
    mid = n.midi_note_number()
    assert mid == 127

def test_midi_127_double_sharp():
    n = Note.from_note_string('F9##')
    mid = n.midi_note_number()
    assert mid == 127