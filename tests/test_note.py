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
    with pytest.raises(TypeError):
        n = Note(7, 4, 'b')

def test_manual_note_creation_invalid_octave():
    with pytest.raises(TypeError):
        n = Note('A', 'y', '##')

def test_manual_note_creation_incorrect_octave_decimal():
    with pytest.raises(TypeError):
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
    with pytest.raises(TypeError):
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
    with pytest.raises(TypeError):
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
    with pytest.raises(TypeError):
        n1.is_enharmonic(3)

def test_enharmonic_notes_wrong_parameter_type_str():
    n1 = Note.from_note_string('C4')
    with pytest.raises(TypeError):
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
    with pytest.raises(TypeError):
        n1 == 1

def test_equality_reject_float():
    n1 = Note.from_note_string('G5')
    with pytest.raises(TypeError):
        n1 == 5.2

def test_equality_reject_str():
    n1 = Note.from_note_string('G5')
    with pytest.raises(TypeError):
        n1 == 'o'

def test_enharmonic_inequality():
    n1 = Note.from_note_string('C5#')
    n2 = Note.from_note_string('D5b')
    assert n1 != n2

def test_inequality_reject_int():
    n1 = Note.from_note_string('G5')
    with pytest.raises(TypeError):
        n1 != 1

def test_inequality_reject_float():
    n1 = Note.from_note_string('G5')
    with pytest.raises(TypeError):
        n1 != 5.2

def test_inequality_reject_str():
    n1 = Note.from_note_string('G5')
    with pytest.raises(TypeError):
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
    with pytest.raises(TypeError):
        n1 < 1

def test_less_than_reject_float():
    n1 = Note.from_note_string('G5')
    with pytest.raises(TypeError):
        n1 < 5.2

def test_less_than_reject_str():
    n1 = Note.from_note_string('G5')
    with pytest.raises(TypeError):
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
    with pytest.raises(TypeError):
        n1 > 1

def test_greater_than_reject_float():
    n1 = Note.from_note_string('G5')
    with pytest.raises(TypeError):
        n1 > 5.2

def test_greater_than_reject_str():
    n1 = Note.from_note_string('G5')
    with pytest.raises(TypeError):
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
    with pytest.raises(TypeError):
        n1 <= 1

def test_less_than_or_equal_reject_float():
    n1 = Note.from_note_string('G5')
    with pytest.raises(TypeError):
        n1 <= 5.2

def test_less_than_or_equal_reject_str():
    n1 = Note.from_note_string('G5')
    with pytest.raises(TypeError):
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
    with pytest.raises(TypeError):
        n1 >= 1

def test_greater_than_or_equal_reject_float():
    n1 = Note.from_note_string('G5')
    with pytest.raises(TypeError):
        n1 >= 5.2

def test_greater_than_or_equal_reject_str():
    n1 = Note.from_note_string('G5')
    with pytest.raises(TypeError):
        n1 >= 'o'

# Test __str__
def test_simple_note_to_str():
    n1 = Note.from_note_string('G5')
    assert n1.__str__() == 'G5'

def test_note_to_str_flat():
    n1 = Note.from_note_string('G5b')
    assert n1.__str__() == 'G5b'

def test_note_to_str_double_flat():
    n1 = Note.from_note_string('G5bb')
    assert n1.__str__() == 'G5bb'

def test_note_to_str_sharp():
    n1 = Note.from_note_string('G5#')
    assert n1.__str__() == 'G5#'

def test_note_to_str_double_sharp():
    n1 = Note.from_note_string('G5##')
    assert n1.__str__() == 'G5##'

# Test note creation from MIDI note number
def test_midi_num_str():
    with pytest.raises(TypeError):
        n = Note.from_midi_num('sldfkj')

def test_midi_num_float():
    with pytest.raises(TypeError):
        n = Note.from_midi_num(15.7)

def test_low_midi_num():
    with pytest.raises(ValueError):
        n = Note.from_midi_num(-1)

def test_high_midi_num():
    with pytest.raises(ValueError):
        n = Note.from_midi_num(128)

def test_midi_num_0():
    n1 = Note.from_midi_num(0)
    n2 = Note.from_note_string('C-1')
    assert n1 == n2

def test_midi_num_1():
    n1 = Note.from_midi_num(1)
    n2 = Note.from_note_string('C-1#')
    assert n1 == n2

def test_midi_num_2():
    n1 = Note.from_midi_num(2)
    n2 = Note.from_note_string('D-1')
    assert n1 == n2

def test_midi_num_3():
    n1 = Note.from_midi_num(3)
    n2 = Note.from_note_string('D-1#')
    assert n1 == n2

def test_midi_num_4():
    n1 = Note.from_midi_num(4)
    n2 = Note.from_note_string('E-1')
    assert n1 == n2

def test_midi_num_5():
    n1 = Note.from_midi_num(5)
    n2 = Note.from_note_string('F-1')
    assert n1 == n2

def test_midi_num_6():
    n1 = Note.from_midi_num(6)
    n2 = Note.from_note_string('F-1#')
    assert n1 == n2

def test_midi_num_7():
    n1 = Note.from_midi_num(7)
    n2 = Note.from_note_string('G-1')
    assert n1 == n2

def test_midi_num_8():
    n1 = Note.from_midi_num(8)
    n2 = Note.from_note_string('G-1#')
    assert n1 == n2

def test_midi_num_9():
    n1 = Note.from_midi_num(9)
    n2 = Note.from_note_string('A-1')
    assert n1 == n2

def test_midi_num_10():
    n1 = Note.from_midi_num(10)
    n2 = Note.from_note_string('A-1#')
    assert n1 == n2

def test_midi_num_11():
    n1 = Note.from_midi_num(11)
    n2 = Note.from_note_string('B-1')
    assert n1 == n2

def test_midi_num_12():
    n1 = Note.from_midi_num(12)
    n2 = Note.from_note_string('C0')
    assert n1 == n2

def test_midi_num_13():
    n1 = Note.from_midi_num(13)
    n2 = Note.from_note_string('C0#')
    assert n1 == n2

def test_midi_num_14():
    n1 = Note.from_midi_num(14)
    n2 = Note.from_note_string('D0')
    assert n1 == n2

def test_midi_num_15():
    n1 = Note.from_midi_num(15)
    n2 = Note.from_note_string('D0#')
    assert n1 == n2

def test_midi_num_16():
    n1 = Note.from_midi_num(16)
    n2 = Note.from_note_string('E0')
    assert n1 == n2

def test_midi_num_17():
    n1 = Note.from_midi_num(17)
    n2 = Note.from_note_string('F0')
    assert n1 == n2

def test_midi_num_18():
    n1 = Note.from_midi_num(18)
    n2 = Note.from_note_string('F0#')
    assert n1 == n2

def test_midi_num_19():
    n1 = Note.from_midi_num(19)
    n2 = Note.from_note_string('G0')
    assert n1 == n2

def test_midi_num_20():
    n1 = Note.from_midi_num(20)
    n2 = Note.from_note_string('G0#')
    assert n1 == n2

def test_midi_num_21():
    n1 = Note.from_midi_num(21)
    n2 = Note.from_note_string('A0')
    assert n1 == n2

def test_midi_num_22():
    n1 = Note.from_midi_num(22)
    n2 = Note.from_note_string('A0#')
    assert n1 == n2

def test_midi_num_23():
    n1 = Note.from_midi_num(23)
    n2 = Note.from_note_string('B0')
    assert n1 == n2

def test_midi_num_24():
    n1 = Note.from_midi_num(24)
    n2 = Note.from_note_string('C1')
    assert n1 == n2

def test_midi_num_25():
    n1 = Note.from_midi_num(25)
    n2 = Note.from_note_string('C1#')
    assert n1 == n2

def test_midi_num_26():
    n1 = Note.from_midi_num(26)
    n2 = Note.from_note_string('D1')
    assert n1 == n2

def test_midi_num_27():
    n1 = Note.from_midi_num(27)
    n2 = Note.from_note_string('D1#')
    assert n1 == n2

def test_midi_num_28():
    n1 = Note.from_midi_num(28)
    n2 = Note.from_note_string('E1')
    assert n1 == n2

def test_midi_num_29():
    n1 = Note.from_midi_num(29)
    n2 = Note.from_note_string('F1')
    assert n1 == n2

def test_midi_num_30():
    n1 = Note.from_midi_num(30)
    n2 = Note.from_note_string('F1#')
    assert n1 == n2

def test_midi_num_31():
    n1 = Note.from_midi_num(31)
    n2 = Note.from_note_string('G1')
    assert n1 == n2

def test_midi_num_32():
    n1 = Note.from_midi_num(32)
    n2 = Note.from_note_string('G1#')
    assert n1 == n2

def test_midi_num_33():
    n1 = Note.from_midi_num(33)
    n2 = Note.from_note_string('A1')
    assert n1 == n2

def test_midi_num_34():
    n1 = Note.from_midi_num(34)
    n2 = Note.from_note_string('A1#')
    assert n1 == n2

def test_midi_num_35():
    n1 = Note.from_midi_num(35)
    n2 = Note.from_note_string('B1')
    assert n1 == n2

def test_midi_num_36():
    n1 = Note.from_midi_num(36)
    n2 = Note.from_note_string('C2')
    assert n1 == n2

def test_midi_num_37():
    n1 = Note.from_midi_num(37)
    n2 = Note.from_note_string('C2#')
    assert n1 == n2

def test_midi_num_38():
    n1 = Note.from_midi_num(38)
    n2 = Note.from_note_string('D2')
    assert n1 == n2

def test_midi_num_39():
    n1 = Note.from_midi_num(39)
    n2 = Note.from_note_string('D2#')
    assert n1 == n2

def test_midi_num_40():
    n1 = Note.from_midi_num(40)
    n2 = Note.from_note_string('E2')
    assert n1 == n2

def test_midi_num_41():
    n1 = Note.from_midi_num(41)
    n2 = Note.from_note_string('F2')
    assert n1 == n2

def test_midi_num_42():
    n1 = Note.from_midi_num(42)
    n2 = Note.from_note_string('F2#')
    assert n1 == n2

def test_midi_num_43():
    n1 = Note.from_midi_num(43)
    n2 = Note.from_note_string('G2')
    assert n1 == n2

def test_midi_num_44():
    n1 = Note.from_midi_num(44)
    n2 = Note.from_note_string('G2#')
    assert n1 == n2

def test_midi_num_45():
    n1 = Note.from_midi_num(45)
    n2 = Note.from_note_string('A2')
    assert n1 == n2

def test_midi_num_46():
    n1 = Note.from_midi_num(46)
    n2 = Note.from_note_string('A2#')
    assert n1 == n2

def test_midi_num_47():
    n1 = Note.from_midi_num(47)
    n2 = Note.from_note_string('B2')
    assert n1 == n2

def test_midi_num_48():
    n1 = Note.from_midi_num(48)
    n2 = Note.from_note_string('C3')
    assert n1 == n2

def test_midi_num_49():
    n1 = Note.from_midi_num(49)
    n2 = Note.from_note_string('C3#')
    assert n1 == n2

def test_midi_num_50():
    n1 = Note.from_midi_num(50)
    n2 = Note.from_note_string('D3')
    assert n1 == n2

def test_midi_num_51():
    n1 = Note.from_midi_num(51)
    n2 = Note.from_note_string('D3#')
    assert n1 == n2

def test_midi_num_52():
    n1 = Note.from_midi_num(52)
    n2 = Note.from_note_string('E3')
    assert n1 == n2

def test_midi_num_53():
    n1 = Note.from_midi_num(53)
    n2 = Note.from_note_string('F3')
    assert n1 == n2

def test_midi_num_54():
    n1 = Note.from_midi_num(54)
    n2 = Note.from_note_string('F3#')
    assert n1 == n2

def test_midi_num_55():
    n1 = Note.from_midi_num(55)
    n2 = Note.from_note_string('G3')
    assert n1 == n2

def test_midi_num_56():
    n1 = Note.from_midi_num(56)
    n2 = Note.from_note_string('G3#')
    assert n1 == n2

def test_midi_num_57():
    n1 = Note.from_midi_num(57)
    n2 = Note.from_note_string('A3')
    assert n1 == n2

def test_midi_num_58():
    n1 = Note.from_midi_num(58)
    n2 = Note.from_note_string('A3#')
    assert n1 == n2

def test_midi_num_59():
    n1 = Note.from_midi_num(59)
    n2 = Note.from_note_string('B3')
    assert n1 == n2

def test_midi_num_60():
    n1 = Note.from_midi_num(60)
    n2 = Note.from_note_string('C4')
    assert n1 == n2

def test_midi_num_61():
    n1 = Note.from_midi_num(61)
    n2 = Note.from_note_string('C4#')
    assert n1 == n2

def test_midi_num_62():
    n1 = Note.from_midi_num(62)
    n2 = Note.from_note_string('D4')
    assert n1 == n2

def test_midi_num_63():
    n1 = Note.from_midi_num(63)
    n2 = Note.from_note_string('D4#')
    assert n1 == n2

def test_midi_num_64():
    n1 = Note.from_midi_num(64)
    n2 = Note.from_note_string('E4')
    assert n1 == n2

def test_midi_num_65():
    n1 = Note.from_midi_num(65)
    n2 = Note.from_note_string('F4')
    assert n1 == n2

def test_midi_num_66():
    n1 = Note.from_midi_num(66)
    n2 = Note.from_note_string('F4#')
    assert n1 == n2

def test_midi_num_67():
    n1 = Note.from_midi_num(67)
    n2 = Note.from_note_string('G4')
    assert n1 == n2

def test_midi_num_68():
    n1 = Note.from_midi_num(68)
    n2 = Note.from_note_string('G4#')
    assert n1 == n2

def test_midi_num_69():
    n1 = Note.from_midi_num(69)
    n2 = Note.from_note_string('A4')
    assert n1 == n2

def test_midi_num_70():
    n1 = Note.from_midi_num(70)
    n2 = Note.from_note_string('A4#')
    assert n1 == n2

def test_midi_num_71():
    n1 = Note.from_midi_num(71)
    n2 = Note.from_note_string('B4')
    assert n1 == n2

def test_midi_num_72():
    n1 = Note.from_midi_num(72)
    n2 = Note.from_note_string('C5')
    assert n1 == n2

def test_midi_num_73():
    n1 = Note.from_midi_num(73)
    n2 = Note.from_note_string('C5#')
    assert n1 == n2

def test_midi_num_74():
    n1 = Note.from_midi_num(74)
    n2 = Note.from_note_string('D5')
    assert n1 == n2

def test_midi_num_75():
    n1 = Note.from_midi_num(75)
    n2 = Note.from_note_string('D5#')
    assert n1 == n2

def test_midi_num_76():
    n1 = Note.from_midi_num(76)
    n2 = Note.from_note_string('E5')
    assert n1 == n2

def test_midi_num_77():
    n1 = Note.from_midi_num(77)
    n2 = Note.from_note_string('F5')
    assert n1 == n2

def test_midi_num_78():
    n1 = Note.from_midi_num(78)
    n2 = Note.from_note_string('F5#')
    assert n1 == n2

def test_midi_num_79():
    n1 = Note.from_midi_num(79)
    n2 = Note.from_note_string('G5')
    assert n1 == n2

def test_midi_num_80():
    n1 = Note.from_midi_num(80)
    n2 = Note.from_note_string('G5#')
    assert n1 == n2

def test_midi_num_81():
    n1 = Note.from_midi_num(81)
    n2 = Note.from_note_string('A5')
    assert n1 == n2

def test_midi_num_82():
    n1 = Note.from_midi_num(82)
    n2 = Note.from_note_string('A5#')
    assert n1 == n2

def test_midi_num_83():
    n1 = Note.from_midi_num(83)
    n2 = Note.from_note_string('B5')
    assert n1 == n2

def test_midi_num_84():
    n1 = Note.from_midi_num(84)
    n2 = Note.from_note_string('C6')
    assert n1 == n2

def test_midi_num_85():
    n1 = Note.from_midi_num(85)
    n2 = Note.from_note_string('C6#')
    assert n1 == n2

def test_midi_num_86():
    n1 = Note.from_midi_num(86)
    n2 = Note.from_note_string('D6')
    assert n1 == n2

def test_midi_num_87():
    n1 = Note.from_midi_num(87)
    n2 = Note.from_note_string('D6#')
    assert n1 == n2

def test_midi_num_88():
    n1 = Note.from_midi_num(88)
    n2 = Note.from_note_string('E6')
    assert n1 == n2

def test_midi_num_89():
    n1 = Note.from_midi_num(89)
    n2 = Note.from_note_string('F6')
    assert n1 == n2

def test_midi_num_90():
    n1 = Note.from_midi_num(90)
    n2 = Note.from_note_string('F6#')
    assert n1 == n2

def test_midi_num_91():
    n1 = Note.from_midi_num(91)
    n2 = Note.from_note_string('G6')
    assert n1 == n2

def test_midi_num_92():
    n1 = Note.from_midi_num(92)
    n2 = Note.from_note_string('G6#')
    assert n1 == n2

def test_midi_num_93():
    n1 = Note.from_midi_num(93)
    n2 = Note.from_note_string('A6')
    assert n1 == n2

def test_midi_num_94():
    n1 = Note.from_midi_num(94)
    n2 = Note.from_note_string('A6#')
    assert n1 == n2

def test_midi_num_95():
    n1 = Note.from_midi_num(95)
    n2 = Note.from_note_string('B6')
    assert n1 == n2

def test_midi_num_96():
    n1 = Note.from_midi_num(96)
    n2 = Note.from_note_string('C7')
    assert n1 == n2

def test_midi_num_97():
    n1 = Note.from_midi_num(97)
    n2 = Note.from_note_string('C7#')
    assert n1 == n2

def test_midi_num_98():
    n1 = Note.from_midi_num(98)
    n2 = Note.from_note_string('D7')
    assert n1 == n2

def test_midi_num_99():
    n1 = Note.from_midi_num(99)
    n2 = Note.from_note_string('D7#')
    assert n1 == n2

def test_midi_num_100():
    n1 = Note.from_midi_num(100)
    n2 = Note.from_note_string('E7')
    assert n1 == n2

def test_midi_num_101():
    n1 = Note.from_midi_num(101)
    n2 = Note.from_note_string('F7')
    assert n1 == n2

def test_midi_num_102():
    n1 = Note.from_midi_num(102)
    n2 = Note.from_note_string('F7#')
    assert n1 == n2

def test_midi_num_103():
    n1 = Note.from_midi_num(103)
    n2 = Note.from_note_string('G7')
    assert n1 == n2

def test_midi_num_104():
    n1 = Note.from_midi_num(104)
    n2 = Note.from_note_string('G7#')
    assert n1 == n2

def test_midi_num_105():
    n1 = Note.from_midi_num(105)
    n2 = Note.from_note_string('A7')
    assert n1 == n2

def test_midi_num_106():
    n1 = Note.from_midi_num(106)
    n2 = Note.from_note_string('A7#')
    assert n1 == n2

def test_midi_num_107():
    n1 = Note.from_midi_num(107)
    n2 = Note.from_note_string('B7')
    assert n1 == n2

def test_midi_num_108():
    n1 = Note.from_midi_num(108)
    n2 = Note.from_note_string('C8')
    assert n1 == n2

def test_midi_num_109():
    n1 = Note.from_midi_num(109)
    n2 = Note.from_note_string('C8#')
    assert n1 == n2

def test_midi_num_110():
    n1 = Note.from_midi_num(110)
    n2 = Note.from_note_string('D8')
    assert n1 == n2

def test_midi_num_111():
    n1 = Note.from_midi_num(111)
    n2 = Note.from_note_string('D8#')
    assert n1 == n2

def test_midi_num_112():
    n1 = Note.from_midi_num(112)
    n2 = Note.from_note_string('E8')
    assert n1 == n2

def test_midi_num_113():
    n1 = Note.from_midi_num(113)
    n2 = Note.from_note_string('F8')
    assert n1 == n2

def test_midi_num_114():
    n1 = Note.from_midi_num(114)
    n2 = Note.from_note_string('F8#')
    assert n1 == n2

def test_midi_num_115():
    n1 = Note.from_midi_num(115)
    n2 = Note.from_note_string('G8')
    assert n1 == n2

def test_midi_num_116():
    n1 = Note.from_midi_num(116)
    n2 = Note.from_note_string('G8#')
    assert n1 == n2

def test_midi_num_117():
    n1 = Note.from_midi_num(117)
    n2 = Note.from_note_string('A8')
    assert n1 == n2

def test_midi_num_118():
    n1 = Note.from_midi_num(118)
    n2 = Note.from_note_string('A8#')
    assert n1 == n2

def test_midi_num_119():
    n1 = Note.from_midi_num(119)
    n2 = Note.from_note_string('B8')
    assert n1 == n2

def test_midi_num_120():
    n1 = Note.from_midi_num(120)
    n2 = Note.from_note_string('C9')
    assert n1 == n2

def test_midi_num_121():
    n1 = Note.from_midi_num(121)
    n2 = Note.from_note_string('C9#')
    assert n1 == n2

def test_midi_num_122():
    n1 = Note.from_midi_num(122)
    n2 = Note.from_note_string('D9')
    assert n1 == n2

def test_midi_num_123():
    n1 = Note.from_midi_num(123)
    n2 = Note.from_note_string('D9#')
    assert n1 == n2

def test_midi_num_124():
    n1 = Note.from_midi_num(124)
    n2 = Note.from_note_string('E9')
    assert n1 == n2

def test_midi_num_125():
    n1 = Note.from_midi_num(125)
    n2 = Note.from_note_string('F9')
    assert n1 == n2

def test_midi_num_126():
    n1 = Note.from_midi_num(126)
    n2 = Note.from_note_string('F9#')
    assert n1 == n2

def test_midi_num_127():
    n1 = Note.from_midi_num(127)
    n2 = Note.from_note_string('G9')
    assert n1 == n2