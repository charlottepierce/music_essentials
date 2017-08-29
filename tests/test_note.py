import pytest

from music_essentials import Note

# Manual note creation - correct values
def test_manual_note_creation_correct_pitch_uppercase():
    n = Note('A', 4, 'bb')
    assert n.pitch == 'A'

def test_manual_note_creation_correct_pitch_lowercase():
    n = Note('b', 4, 'b')
    assert n.pitch == 'B'

def test_manual_note_creation_correct_octave():
    n = Note('A', 4, '##')
    assert n.octave == 4

def test_manual_note_creation_correct_accidentals():
    n = Note('A', 4, '#')
    assert n.accidental == '#'

def test_manual_note_creation_no_accidentals():
    n = Note('A', 4)
    assert n.accidental is None

def test_manual_note_creation_neg_octave():
    n = Note('C', -1)
    assert n.octave == -1

# Note creation from note string - correct values
def test_note_creation_correct_pitch_uppercase():
    n = Note.from_note_string('A4bb')
    assert n.pitch == 'A'

def test_note_creation_correct_pitch_lowercase():
    n = Note.from_note_string('b4b')
    assert n.pitch == 'B'

def test_note_creation_correct_octave():
    n = Note.from_note_string('A4##')
    assert n.octave == 4

def test_note_creation_correct_accidentals():
    n = Note.from_note_string('A4#')
    assert n.accidental == '#'

def test_note_creation_no_accidentals():
    n = Note.from_note_string('A4')
    assert n.accidental is None

def test_note_creation_neg_octave():
    n = Note.from_note_string('C-1')
    assert n.octave == -1

# Manual note creation - invalid values
def test_manual_note_creation_incorrect_pitch_uppercase():
    with pytest.raises(ValueError):
        n = Note('X', 4, 'bb')

def test_manual_note_creation_incorrect_pitch_lowercase():
    with pytest.raises(ValueError):
        n = Note('p', 4, 'b')

def test_manual_note_creation_incorrect_pitch_integer():
    with pytest.raises(ValueError):
        n = Note(7, 4, 'b')

def test_manual_note_creation_invalid_octave():
    with pytest.raises(ValueError):
        n = Note('A', 'y', '##')

def test_manual_note_creation_incorrect_octave_decimal():
    with pytest.raises(ValueError):
        n = Note('A', 5.5, '##')

def test_manual_note_creation_incorrect_octave_low():
    with pytest.raises(ValueError):
        n = Note('A', -2, '##')

def test_manual_note_creation_incorrect_octave_high():
    with pytest.raises(ValueError):
        n = Note('A', 10, '##')
    
def test_manual_note_creation_incorrect_accidentals_too_many():
    with pytest.raises(ValueError):
        n = Note('A', 4, '###')

def test_manual_note_creation_incorrect_accidentals_wrong_symbols():
    with pytest.raises(ValueError):
        n = Note('A', 4, '*')

def test_manual_note_creation_midi_num_low():
    with pytest.raises(ValueError):
        n = Note('C', -1, 'b')

def test_manual_note_creation_midi_num_high():
    with pytest.raises(ValueError):
        n = Note('A', 9, 'b')

# Note creation from note string - invalid values
def test_note_creation_incorrect_pitch_uppercase():
    with pytest.raises(ValueError):
        n = Note.from_note_string('X4bb')

def test_note_creation_incorrect_pitch_lowercase():
    with pytest.raises(ValueError):
        n = Note.from_note_string('p4b')

def test_note_creation_invalid_octave():
    with pytest.raises(ValueError):
        n = Note.from_note_string('Ay##')

def test_note_creation_incorrect_octave_decimal():
    with pytest.raises(ValueError):
        n = Note.from_note_string('A5.5##')

def test_note_creation_incorrect_octave_low():
    with pytest.raises(ValueError):
        n = Note.from_note_string('A-2##')

def test_note_creation_incorrect_octave_high():
    with pytest.raises(ValueError):
        n = Note.from_note_string('A10##')
    
def test_note_creation_incorrect_accidentals_too_many():
    with pytest.raises(ValueError):
        n = Note.from_note_string('A4###')

def test_note_creation_incorrect_accidentals_wrong_symbols():
    with pytest.raises(ValueError):
        n = Note.from_note_string('A4*')

def test_note_creation_no_pitch():
    with pytest.raises(ValueError):
        n = Note.from_note_string('4bb')

def test_note_creation_no_octave():
    with pytest.raises(ValueError):
        n = Note.from_note_string('C#')

def test_note_creation_midi_num_low():
    with pytest.raises(ValueError):
        n = Note.from_note_string('C-1b')

def test_note_creation_midi_num_high():
    with pytest.raises(ValueError):
        n = Note.from_note_string('A9b')

# Test detection of enharmonic notes
def test_enharmonic_notes_wrong_parameter_type_int():
    n1 = Note.from_note_string('C4')
    with pytest.raises(ValueError):
        n1.is_enharmonic(3)

def test_enharmonic_notes_wrong_parameter_type_str():
    n1 = Note.from_note_string('C4')
    with pytest.raises(ValueError):
        n1.is_enharmonic('hello')

def test_enharmonic_notes_identical():
    n1 = Note.from_note_string('G5##')
    n2 = Note.from_note_string('G5##')
    assert n1.is_enharmonic(n2) == True

def test_enharmonic_notes_flat_to_sharp():
    n1 = Note.from_note_string('G5#')
    n2 = Note.from_note_string('A5b')
    assert n1.is_enharmonic(n2) == True

def test_enharmonic_notes_different_octaves():
    n1 = Note.from_note_string('B5#')
    n2 = Note.from_note_string('C6')
    assert n1.is_enharmonic(n2) == True

def test_enharmonic_notes_different_pitches():
    n1 = Note.from_note_string('G5')
    n2 = Note.from_note_string('A5bb')
    assert n1.is_enharmonic(n2) == True

def test_non_enharmonic_notes():
    n1 = Note.from_note_string('G5')
    n2 = Note.from_note_string('G5b')
    assert n1.is_enharmonic(n2) == False

# Test __eq__ and __ne__
def test_simple_equality():
    n1 = Note.from_note_string('G5')
    n2 = Note.from_note_string('G5')
    assert n1 == n2

def test_equality_reject_int():
    n1 = Note.from_note_string('G5')
    with pytest.raises(ValueError):
        n1 == 1

def test_equality_reject_float():
    n1 = Note.from_note_string('G5')
    with pytest.raises(ValueError):
        n1 == 5.2

def test_equality_reject_str():
    n1 = Note.from_note_string('G5')
    with pytest.raises(ValueError):
        n1 == 'o'

def test_enharmonic_inequality():
    n1 = Note.from_note_string('C5#')
    n2 = Note.from_note_string('D5b')
    assert n1 != n2

def test_inequality_reject_int():
    n1 = Note.from_note_string('G5')
    with pytest.raises(ValueError):
        n1 != 1

def test_inequality_reject_float():
    n1 = Note.from_note_string('G5')
    with pytest.raises(ValueError):
        n1 != 5.2

def test_inequality_reject_str():
    n1 = Note.from_note_string('G5')
    with pytest.raises(ValueError):
        n1 != 'o'

# Test __lt__
def test_simple_less_than():
    n1 = Note.from_note_string('C5')
    n2 = Note.from_note_string('D5')
    assert n1 < n2

def test_less_than_over_octave():
    n1 = Note.from_note_string('B4')
    n2 = Note.from_note_string('C5')
    assert n1 < n2

def test_enharmonic_less_than():
    n1 = Note.from_note_string('C5#')
    n2 = Note.from_note_string('D5b')
    assert n1 < n2

def test_less_than_reject_int():
    n1 = Note.from_note_string('G5')
    with pytest.raises(ValueError):
        n1 < 1

def test_less_than_reject_float():
    n1 = Note.from_note_string('G5')
    with pytest.raises(ValueError):
        n1 < 5.2

def test_less_than_reject_str():
    n1 = Note.from_note_string('G5')
    with pytest.raises(ValueError):
        n1 < 'o'

# Test __gt__
def test_simple_greater_than():
    n1 = Note.from_note_string('D5')
    n2 = Note.from_note_string('C5')
    assert n1 > n2

def test_greater_than_over_octave():
    n1 = Note.from_note_string('C5')
    n2 = Note.from_note_string('B4')
    assert n1 > n2

def test_enharmonic_greater_than():
    n1 = Note.from_note_string('D5b')
    n2 = Note.from_note_string('C5#')
    assert n1 > n2

def test_greater_than_reject_int():
    n1 = Note.from_note_string('G5')
    with pytest.raises(ValueError):
        n1 > 1

def test_greater_than_reject_float():
    n1 = Note.from_note_string('G5')
    with pytest.raises(ValueError):
        n1 > 5.2

def test_greater_than_reject_str():
    n1 = Note.from_note_string('G5')
    with pytest.raises(ValueError):
        n1 > 'o'

# Test __le__
def test_less_than_or_equal():
    n1 = Note.from_note_string('C5')
    n2 = Note.from_note_string('C5')
    assert n1 <= n2

def test_simple_less_than_or_equal():
    n1 = Note.from_note_string('C5')
    n2 = Note.from_note_string('D5')
    assert n1 <= n2

def test_less_than_over_octave_or_equal():
    n1 = Note.from_note_string('B4')
    n2 = Note.from_note_string('C5')
    assert n1 <= n2

def test_enharmonic_less_than_or_equal():
    n1 = Note.from_note_string('C5#')
    n2 = Note.from_note_string('D5b')
    assert n1 <= n2

def test_less_than_or_equal_reject_int():
    n1 = Note.from_note_string('G5')
    with pytest.raises(ValueError):
        n1 <= 1

def test_less_than_or_equal_reject_float():
    n1 = Note.from_note_string('G5')
    with pytest.raises(ValueError):
        n1 <= 5.2

def test_less_than_or_equal_reject_str():
    n1 = Note.from_note_string('G5')
    with pytest.raises(ValueError):
        n1 <= 'o'

# Test __ge__
def test_greater_than_or_equal():
    n1 = Note.from_note_string('D5')
    n2 = Note.from_note_string('D5')
    assert n1 >= n2

def test_simple_greater_than_or_equal():
    n1 = Note.from_note_string('D5')
    n2 = Note.from_note_string('C5')
    assert n1 >= n2

def test_greater_than_or_equal_over_octave():
    n1 = Note.from_note_string('C5')
    n2 = Note.from_note_string('B4')
    assert n1 >= n2

def test_enharmonic_greater_than_or_equal():
    n1 = Note.from_note_string('D5b')
    n2 = Note.from_note_string('C5#')
    assert n1 >= n2

def test_greater_than_or_equal_reject_int():
    n1 = Note.from_note_string('G5')
    with pytest.raises(ValueError):
        n1 >= 1

def test_greater_than_or_equal_reject_float():
    n1 = Note.from_note_string('G5')
    with pytest.raises(ValueError):
        n1 >= 5.2

def test_greater_than_or_equal_reject_str():
    n1 = Note.from_note_string('G5')
    with pytest.raises(ValueError):
        n1 >= 'o'