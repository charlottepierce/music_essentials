import pytest

from music_essentials import Note, Scale

# Test building of major scales
def test_scale_builder_c_maj():
    s = Scale.build_scale(Note('C', 4), 'major')
    expected = [
        Note('C', 4),
        Note('D', 4),
        Note('E', 4),
        Note('F', 4),
        Note('G', 4),
        Note('A', 4),
        Note('B', 4),
        Note('C', 5)
    ]
    assert s == expected

def test_scale_builder_c_sharp_maj():
    s = Scale.build_scale(Note('C', 4, '#'), 'maj')
    expected = [
        Note('C', 4, '#'),
        Note('D', 4, '#'),
        Note('E', 4, '#'),
        Note('F', 4, '#'),
        Note('G', 4, '#'),
        Note('A', 4, '#'),
        Note('B', 4, '#'),
        Note('C', 5, '#')
    ]
    assert s == expected

def test_scale_builder_d_flat_maj():
    s = Scale.build_scale(Note('D', 4, 'b'), 'major')
    expected = [
        Note('D', 4, 'b'),
        Note('E', 4, 'b'),
        Note('F', 4),
        Note('G', 4, 'b'),
        Note('A', 4, 'b'),
        Note('B', 4, 'b'),
        Note('C', 5),
        Note('D', 5, 'b')
    ]
    assert s == expected

def test_scale_builder_d_maj():
    s = Scale.build_scale(Note('D', 4), 'maj')
    expected = [
        Note('D', 4),
        Note('E', 4),
        Note('F', 4, '#'),
        Note('G', 4),
        Note('A', 4),
        Note('B', 4),
        Note('C', 5, '#'),
        Note('D', 5)
    ]
    assert s == expected

def test_scale_builder_d_sharp_maj():
    s = Scale.build_scale(Note('D', 4, '#'), 'major')
    expected = [
        Note('D', 4, '#'),
        Note('E', 4, '#'),
        Note('F', 4, '##'),
        Note('G', 4, '#'),
        Note('A', 4, '#'),
        Note('B', 4, '#'),
        Note('C', 5, '##'),
        Note('D', 5, '#')
    ]
    assert s == expected

def test_scale_builder_e_flat_maj():
    s = Scale.build_scale(Note('E', 4, 'b'), 'major')
    expected = [
        Note('E', 4, 'b'),
        Note('F', 4),
        Note('G', 4),
        Note('A', 4, 'b'),
        Note('B', 4, 'b'),
        Note('C', 5),
        Note('D', 5),
        Note('E', 5, 'b')
    ]
    assert s == expected

def test_scale_builder_e_maj():
    s = Scale.build_scale(Note('E', 4), 'maj')
    expected = [
        Note('E', 4),
        Note('F', 4, '#'),
        Note('G', 4, '#'),
        Note('A', 4),
        Note('B', 4),
        Note('C', 5, '#'),
        Note('D', 5, '#'),
        Note('E', 5)
    ]
    assert s == expected

def test_scale_builder_e_sharp_maj():
    s = Scale.build_scale(Note('E', 4, '#'), 'major')
    expected = [
        Note('E', 4, '#'),
        Note('F', 4, '##'),
        Note('G', 4, '##'),
        Note('A', 4, '#'),
        Note('B', 4, '#'),
        Note('C', 5, '##'),
        Note('D', 5, '##'),
        Note('E', 5, '#')
    ]
    assert s == expected

def test_scale_builder_f_flat_maj():
    s = Scale.build_scale(Note('F', 4, 'b'), 'maj')
    expected = [
        Note('F', 4, 'b'),
        Note('G', 4, 'b'),
        Note('A', 4, 'b'),
        Note('B', 4, 'bb'),
        Note('C', 5, 'b'),
        Note('D', 5, 'b'),
        Note('E', 5, 'b'),
        Note('F', 5, 'b')
    ]
    assert s == expected

def test_scale_builder_f_maj():
    s = Scale.build_scale(Note('F', 4), 'major')
    expected = [
        Note('F', 4),
        Note('G', 4),
        Note('A', 4),
        Note('B', 4, 'b'),
        Note('C', 5),
        Note('D', 5),
        Note('E', 5),
        Note('F', 5)
    ]
    assert s == expected

def test_scale_builder_f_sharp_maj():
    s = Scale.build_scale(Note('F', 4, '#'), 'maj')
    expected = [
        Note('F', 4, '#'),
        Note('G', 4, '#'),
        Note('A', 4, '#'),
        Note('B', 4),
        Note('C', 5, '#'),
        Note('D', 5, '#'),
        Note('E', 5, '#'),
        Note('F', 5, '#')
    ]
    assert s == expected

def test_scale_builder_g_flat_maj():
    s = Scale.build_scale(Note('G', 4, 'b'), 'major')
    expected = [
        Note('G', 4, 'b'),
        Note('A', 4, 'b'),
        Note('B', 4, 'b'),
        Note('C', 5, 'b'),
        Note('D', 5, 'b'),
        Note('E', 5, 'b'),
        Note('F', 5),
        Note('G', 5, 'b')
    ]
    assert s == expected

def test_scale_builder_g_maj():
    s = Scale.build_scale(Note('G', 4), 'maj')
    expected = [
        Note('G', 4),
        Note('A', 4),
        Note('B', 4),
        Note('C', 5),
        Note('D', 5),
        Note('E', 5),
        Note('F', 5, '#'),
        Note('G', 5)
    ]
    assert s == expected

def test_scale_builder_g_sharp_maj():
    s = Scale.build_scale(Note('G', 4, '#'), 'major')
    expected = [
        Note('G', 4, '#'),
        Note('A', 4, '#'),
        Note('B', 4, '#'),
        Note('C', 5, '#'),
        Note('D', 5, '#'),
        Note('E', 5, '#'),
        Note('F', 5, '##'),
        Note('G', 5, '#')
    ]
    assert s == expected

def test_scale_builder_a_flat_maj():
    s = Scale.build_scale(Note('A', 4, 'b'), 'maj')
    expected = [
        Note('A', 4, 'b'),
        Note('B', 4, 'b'),
        Note('C', 5),
        Note('D', 5, 'b'),
        Note('E', 5, 'b'),
        Note('F', 5),
        Note('G', 5),
        Note('A', 5, 'b')
    ]
    assert s == expected
    
def test_scale_builder_a_maj():
    s = Scale.build_scale(Note('A', 4), 'major')
    expected = [
        Note('A', 4),
        Note('B', 4),
        Note('C', 5, '#'),
        Note('D', 5),
        Note('E', 5),
        Note('F', 5, '#'),
        Note('G', 5, '#'),
        Note('A', 5)
    ]
    assert s == expected

def test_scale_builder_a_sharp_maj():
    s = Scale.build_scale(Note('A', 4, '#'), 'maj')
    expected = [
        Note('A', 4, '#'),
        Note('B', 4, '#'),
        Note('C', 5, '##'),
        Note('D', 5, '#'),
        Note('E', 5, '#'),
        Note('F', 5, '##'),
        Note('G', 5, '##'),
        Note('A', 5, '#')
    ]
    assert s == expected

def test_scale_builder_b_flat_maj():
    s = Scale.build_scale(Note('B', 4, 'b'), 'major')
    expected = [
        Note('B', 4, 'b'),
        Note('C', 5),
        Note('D', 5),
        Note('E', 5, 'b'),
        Note('F', 5),
        Note('G', 5),
        Note('A', 5),
        Note('B', 5, 'b')
    ]
    assert s == expected

def test_scale_builder_b_maj():
    s = Scale.build_scale(Note('B', 4), 'maj')
    expected = [
        Note('B', 4),
        Note('C', 5, '#'),
        Note('D', 5, '#'),
        Note('E', 5),
        Note('F', 5, '#'),
        Note('G', 5, '#'),
        Note('A', 5, '#'),
        Note('B', 5)
    ]
    assert s == expected

def test_scale_builder_b_sharp_maj():
    s = Scale.build_scale(Note('B', 4, '#'), 'major')
    expected = [
        Note('B', 4, '#'),
        Note('C', 5, '##'),
        Note('D', 5, '##'),
        Note('E', 5, '#'),
        Note('F', 5, '##'),
        Note('G', 5, '##'),
        Note('A', 5, '##'),
        Note('B', 5, '#')
    ]
    assert s == expected

def test_scale_builder_c_flat_maj():
    s = Scale.build_scale(Note('C', 5, 'b'), 'maj')
    expected = [
        Note('C', 5, 'b'),
        Note('D', 5, 'b'),
        Note('E', 5, 'b'),
        Note('F', 5, 'b'),
        Note('G', 5, 'b'),
        Note('A', 5, 'b'),
        Note('B', 5, 'b'),
        Note('C', 6, 'b')
    ]
    assert s == expected

# Test building of harmonic minor scales
def test_scale_builder_c_min():
    s = Scale.build_scale(Note('C', 4), 'minor')
    expected = [
        Note('C', 4),
        Note('D', 4),
        Note('E', 4, 'b'),
        Note('F', 4),
        Note('G', 4),
        Note('A', 4, 'b'),
        Note('B', 4),
        Note('C', 5)
    ]
    assert s == expected

def test_scale_builder_c_sharp_min():
    s = Scale.build_scale(Note('C', 4, '#'), 'min')
    expected = [
        Note('C', 4, '#'),
        Note('D', 4, '#'),
        Note('E', 4),
        Note('F', 4, '#'),
        Note('G', 4, '#'),
        Note('A', 4),
        Note('B', 4, '#'),
        Note('C', 5, '#')
    ]
    assert s == expected

def test_scale_builder_d_flat_min():
    s = Scale.build_scale(Note('D', 4, 'b'), 'minor')
    expected = [
        Note('D', 4, 'b'),
        Note('E', 4, 'b'),
        Note('F', 4, 'b'),
        Note('G', 4, 'b'),
        Note('A', 4, 'b'),
        Note('B', 4, 'bb'),
        Note('C', 5),
        Note('D', 5, 'b')
    ]
    assert s == expected

def test_scale_builder_d_min():
    s = Scale.build_scale(Note('D', 4), 'min')
    expected = [
        Note('D', 4),
        Note('E', 4),
        Note('F', 4),
        Note('G', 4),
        Note('A', 4),
        Note('B', 4, 'b'),
        Note('C', 5, '#'),
        Note('D', 5)
    ]
    assert s == expected

def test_scale_builder_d_sharp_min():
    s = Scale.build_scale(Note('D', 4, '#'), 'minor')
    expected = [
        Note('D', 4, '#'),
        Note('E', 4, '#'),
        Note('F', 4, '#'),
        Note('G', 4, '#'),
        Note('A', 4, '#'),
        Note('B', 4),
        Note('C', 5, '##'),
        Note('D', 5, '#')
    ]
    assert s == expected

def test_scale_builder_e_flat_min():
    s = Scale.build_scale(Note('E', 4, 'b'), 'min')
    expected = [
        Note('E', 4, 'b'),
        Note('F', 4),
        Note('G', 4, 'b'),
        Note('A', 4, 'b'),
        Note('B', 4, 'b'),
        Note('C', 5, 'b'),
        Note('D', 5),
        Note('E', 5, 'b')
    ]
    assert s == expected

def test_scale_builder_e_min():
    s = Scale.build_scale(Note('E', 4), 'minor')
    expected = [
        Note('E', 4),
        Note('F', 4, '#'),
        Note('G', 4),
        Note('A', 4),
        Note('B', 4),
        Note('C', 5),
        Note('D', 5, '#'),
        Note('E', 5)
    ]
    assert s == expected

def test_scale_builder_e_sharp_min():
    s = Scale.build_scale(Note('E', 4, '#'), 'min')
    expected = [
        Note('E', 4, '#'),
        Note('F', 4, '##'),
        Note('G', 4, '#'),
        Note('A', 4, '#'),
        Note('B', 4, '#'),
        Note('C', 5, '#'),
        Note('D', 5, '##'),
        Note('E', 5, '#')
    ]
    assert s == expected

def test_scale_builder_f_flat_min():
    s = Scale.build_scale(Note('F', 4, 'b'), 'minor')
    expected = [
        Note('F', 4, 'b'),
        Note('G', 4, 'b'),
        Note('A', 4, 'bb'),
        Note('B', 4, 'bb'),
        Note('C', 5, 'b'),
        Note('D', 5, 'bb'),
        Note('E', 5, 'b'),
        Note('F', 5, 'b')
    ]
    assert s == expected

def test_scale_builder_f_min():
    s = Scale.build_scale(Note('F', 4), 'min')
    expected = [
        Note('F', 4),
        Note('G', 4),
        Note('A', 4, 'b'),
        Note('B', 4, 'b'),
        Note('C', 5),
        Note('D', 5, 'b'),
        Note('E', 5),
        Note('F', 5)
    ]
    assert s == expected

def test_scale_builder_f_sharp_min():
    s = Scale.build_scale(Note('F', 4, '#'), 'minor')
    expected = [
        Note('F', 4, '#'),
        Note('G', 4, '#'),
        Note('A', 4),
        Note('B', 4),
        Note('C', 5, '#'),
        Note('D', 5),
        Note('E', 5, '#'),
        Note('F', 5, '#')
    ]
    assert s == expected

def test_scale_builder_g_flat_min():
    s = Scale.build_scale(Note('G', 4, 'b'), 'min')
    expected = [
        Note('G', 4, 'b'),
        Note('A', 4, 'b'),
        Note('B', 4, 'bb'),
        Note('C', 5, 'b'),
        Note('D', 5, 'b'),
        Note('E', 5, 'bb'),
        Note('F', 5),
        Note('G', 5, 'b')
    ]
    assert s == expected

def test_scale_builder_g_min():
    s = Scale.build_scale(Note('G', 4), 'minor')
    expected = [
        Note('G', 4),
        Note('A', 4),
        Note('B', 4, 'b'),
        Note('C', 5),
        Note('D', 5),
        Note('E', 5, 'b'),
        Note('F', 5, '#'),
        Note('G', 5)
    ]
    assert s == expected

def test_scale_builder_g_sharp_min():
    s = Scale.build_scale(Note('G', 4, '#'), 'min')
    expected = [
        Note('G', 4, '#'),
        Note('A', 4, '#'),
        Note('B', 4),
        Note('C', 5, '#'),
        Note('D', 5, '#'),
        Note('E', 5),
        Note('F', 5, '##'),
        Note('G', 5, '#')
    ]
    assert s == expected

def test_scale_builder_a_flat_min():
    s = Scale.build_scale(Note('A', 4, 'b'), 'minor')
    expected = [
        Note('A', 4, 'b'),
        Note('B', 4, 'b'),
        Note('C', 5, 'b'),
        Note('D', 5, 'b'),
        Note('E', 5, 'b'),
        Note('F', 5, 'b'),
        Note('G', 5),
        Note('A', 5, 'b')
    ]
    assert s == expected

def test_scale_builder_a_min():
    s = Scale.build_scale(Note('A', 4), 'min')
    expected = [
        Note('A', 4),
        Note('B', 4),
        Note('C', 5),
        Note('D', 5),
        Note('E', 5),
        Note('F', 5),
        Note('G', 5, '#'),
        Note('A', 5)
    ]
    assert s == expected

def test_scale_builder_a_sharp_min():
    s = Scale.build_scale(Note('A', 4, '#'), 'minor')
    expected = [
        Note('A', 4, '#'),
        Note('B', 4, '#'),
        Note('C', 5, '#'),
        Note('D', 5, '#'),
        Note('E', 5, '#'),
        Note('F', 5, '#'),
        Note('G', 5, '##'),
        Note('A', 5, '#')
    ]
    assert s == expected

def test_scale_builder_b_flat_min():
    s = Scale.build_scale(Note('B', 4, 'b'), 'min')
    expected = [
        Note('B', 4, 'b'),
        Note('C', 5),
        Note('D', 5, 'b'),
        Note('E', 5, 'b'),
        Note('F', 5),
        Note('G', 5, 'b'),
        Note('A', 5),
        Note('B', 5, 'b')
    ]
    assert s == expected

def test_scale_builder_b_min():
    s = Scale.build_scale(Note('B', 4), 'minor')
    expected = [
        Note('B', 4),
        Note('C', 5, '#'),
        Note('D', 5),
        Note('E', 5),
        Note('F', 5, '#'),
        Note('G', 5),
        Note('A', 5, '#'),
        Note('B', 5)
    ]
    assert s == expected

def test_scale_builder_b_sharp_min():
    s = Scale.build_scale(Note('B', 4, '#'), 'min')
    expected = [
        Note('B', 4, '#'),
        Note('C', 5, '##'),
        Note('D', 5, '#'),
        Note('E', 5, '#'),
        Note('F', 5, '##'),
        Note('G', 5, '#'),
        Note('A', 5, '##'),
        Note('B', 5, '#')
    ]
    assert s == expected

def test_scale_builder_c_flat_min():
    s = Scale.build_scale(Note('C', 5, 'b'), 'minor')
    expected = [
        Note('C', 5, 'b'),
        Note('D', 5, 'b'),
        Note('E', 5, 'bb'),
        Note('F', 5, 'b'),
        Note('G', 5, 'b'),
        Note('A', 5, 'bb'),
        Note('B', 5, 'b'),
        Note('C', 6, 'b')
    ]
    assert s == expected

# Test building of natural minor scales
def test_scale_builder_c_nat_minj():
    s = Scale.build_scale(Note('C', 4), 'natural minor')
    expected = [
        Note('C', 4),
        Note('D', 4),
        Note('E', 4, 'b'),
        Note('F', 4),
        Note('G', 4),
        Note('A', 4, 'b'),
        Note('B', 4, 'b'),
        Note('C', 5)
    ]
    assert s == expected

def test_scale_builder_c_sharp_nat_minj():
    s = Scale.build_scale(Note('C', 4, '#'), 'nat min')
    expected = [
        Note('C', 4, '#'),
        Note('D', 4, '#'),
        Note('E', 4),
        Note('F', 4, '#'),
        Note('G', 4, '#'),
        Note('A', 4),
        Note('B', 4),
        Note('C', 5, '#')
    ]
    assert s == expected

def test_scale_builder_d_flat_nat_min():
    s = Scale.build_scale(Note('D', 4, 'b'), 'natural minor')
    expected = [
        Note('D', 4, 'b'),
        Note('E', 4, 'b'),
        Note('F', 4, 'b'),
        Note('G', 4, 'b'),
        Note('A', 4, 'b'),
        Note('B', 4, 'bb'),
        Note('C', 5, 'b'),
        Note('D', 5, 'b')
    ]
    assert s == expected

def test_scale_builder_d_nat_min():
    s = Scale.build_scale(Note('D', 4), 'nat min')
    expected = [
        Note('D', 4),
        Note('E', 4),
        Note('F', 4),
        Note('G', 4),
        Note('A', 4),
        Note('B', 4, 'b'),
        Note('C', 5),
        Note('D', 5)
    ]
    assert s == expected

def test_scale_builder_d_sharp_nat_min():
    s = Scale.build_scale(Note('D', 4, '#'), 'natural minor')
    expected = [
        Note('D', 4, '#'),
        Note('E', 4, '#'),
        Note('F', 4, '#'),
        Note('G', 4, '#'),
        Note('A', 4, '#'),
        Note('B', 4),
        Note('C', 5, '#'),
        Note('D', 5, '#')
    ]
    assert s == expected

def test_scale_builder_e_flat_nat_min():
    s = Scale.build_scale(Note('E', 4, 'b'), 'nat min')
    expected = [
        Note('E', 4, 'b'),
        Note('F', 4),
        Note('G', 4, 'b'),
        Note('A', 4, 'b'),
        Note('B', 4, 'b'),
        Note('C', 5, 'b'),
        Note('D', 5, 'b'),
        Note('E', 5, 'b')
    ]
    assert s == expected

def test_scale_builder_e_nat_min():
    s = Scale.build_scale(Note('E', 4), 'natural minor')
    expected = [
        Note('E', 4),
        Note('F', 4, '#'),
        Note('G', 4),
        Note('A', 4),
        Note('B', 4),
        Note('C', 5),
        Note('D', 5),
        Note('E', 5)
    ]
    assert s == expected

def test_scale_builder_e_sharp_nat_min():
    s = Scale.build_scale(Note('E', 4, '#'), 'nat min')
    expected = [
        Note('E', 4, '#'),
        Note('F', 4, '##'),
        Note('G', 4, '#'),
        Note('A', 4, '#'),
        Note('B', 4, '#'),
        Note('C', 5, '#'),
        Note('D', 5, '#'),
        Note('E', 5, '#')
    ]
    assert s == expected

def test_scale_builder_f_flat_nat_min():
    s = Scale.build_scale(Note('F', 4, 'b'), 'natural minor')
    expected = [
        Note('F', 4, 'b'),
        Note('G', 4, 'b'),
        Note('A', 4, 'bb'),
        Note('B', 4, 'bb'),
        Note('C', 5, 'b'),
        Note('D', 5, 'bb'),
        Note('E', 5, 'bb'),
        Note('F', 5, 'b')
    ]
    assert s == expected

def test_scale_builder_f_nat_min():
    s = Scale.build_scale(Note('F', 4), 'nat min')
    expected = [
        Note('F', 4),
        Note('G', 4),
        Note('A', 4, 'b'),
        Note('B', 4, 'b'),
        Note('C', 5),
        Note('D', 5, 'b'),
        Note('E', 5, 'b'),
        Note('F', 5)
    ]
    assert s == expected

def test_scale_builder_f_sharp_nat_min():
    s = Scale.build_scale(Note('F', 4, '#'), 'natural minor')
    expected = [
        Note('F', 4, '#'),
        Note('G', 4, '#'),
        Note('A', 4),
        Note('B', 4),
        Note('C', 5, '#'),
        Note('D', 5),
        Note('E', 5),
        Note('F', 5, '#')
    ]
    assert s == expected

def test_scale_builder_g_flat_nat_min():
    s = Scale.build_scale(Note('G', 4, 'b'), 'nat min')
    expected = [
        Note('G', 4, 'b'),
        Note('A', 4, 'b'),
        Note('B', 4, 'bb'),
        Note('C', 5, 'b'),
        Note('D', 5, 'b'),
        Note('E', 5, 'bb'),
        Note('F', 5, 'b'),
        Note('G', 5, 'b')
    ]
    assert s == expected

def test_scale_builder_g_nat_min():
    s = Scale.build_scale(Note('G', 4), 'natural minor')
    expected = [
        Note('G', 4),
        Note('A', 4),
        Note('B', 4, 'b'),
        Note('C', 5),
        Note('D', 5),
        Note('E', 5, 'b'),
        Note('F', 5),
        Note('G', 5)
    ]
    assert s == expected

def test_scale_builder_g_sharp_nat_min():
    s = Scale.build_scale(Note('G', 4, '#'), 'nat min')
    expected = [
        Note('G', 4, '#'),
        Note('A', 4, '#'),
        Note('B', 4),
        Note('C', 5, '#'),
        Note('D', 5, '#'),
        Note('E', 5),
        Note('F', 5, '#'),
        Note('G', 5, '#')
    ]
    assert s == expected

def test_scale_builder_a_flat_nat_min():
    s = Scale.build_scale(Note('A', 4, 'b'), 'natural minor')
    expected = [
        Note('A', 4, 'b'),
        Note('B', 4, 'b'),
        Note('C', 5, 'b'),
        Note('D', 5, 'b'),
        Note('E', 5, 'b'),
        Note('F', 5, 'b'),
        Note('G', 5, 'b'),
        Note('A', 5, 'b')
    ]
    assert s == expected

def test_scale_builder_a_nat_min():
    s = Scale.build_scale(Note('A', 4), 'nat min')
    expected = [
        Note('A', 4),
        Note('B', 4),
        Note('C', 5),
        Note('D', 5),
        Note('E', 5),
        Note('F', 5),
        Note('G', 5),
        Note('A', 5)
    ]
    assert s == expected

def test_scale_builder_a_sharp_nat_min():
    s = Scale.build_scale(Note('A', 4, '#'), 'natural minor')
    expected = [
        Note('A', 4, '#'),
        Note('B', 4, '#'),
        Note('C', 5, '#'),
        Note('D', 5, '#'),
        Note('E', 5, '#'),
        Note('F', 5, '#'),
        Note('G', 5, '#'),
        Note('A', 5, '#')
    ]
    assert s == expected

def test_scale_builder_b_flat_nat_min():
    s = Scale.build_scale(Note('B', 4, 'b'), 'nat min')
    expected = [
        Note('B', 4, 'b'),
        Note('C', 5),
        Note('D', 5, 'b'),
        Note('E', 5, 'b'),
        Note('F', 5),
        Note('G', 5, 'b'),
        Note('A', 5, 'b'),
        Note('B', 5, 'b')
    ]
    assert s == expected

def test_scale_builder_b_nat_min():
    s = Scale.build_scale(Note('B', 4), 'natural minor')
    expected = [
        Note('B', 4),
        Note('C', 5, '#'),
        Note('D', 5),
        Note('E', 5),
        Note('F', 5, '#'),
        Note('G', 5),
        Note('A', 5),
        Note('B', 5)
    ]
    assert s == expected

def test_scale_builder_b_sharp_nat_min():
    s = Scale.build_scale(Note('B', 4, '#'), 'nat min')
    expected = [
        Note('B', 4, '#'),
        Note('C', 5, '##'),
        Note('D', 5, '#'),
        Note('E', 5, '#'),
        Note('F', 5, '##'),
        Note('G', 5, '#'),
        Note('A', 5, '#'),
        Note('B', 5, '#')
    ]
    assert s == expected

def test_scale_builder_c_flat_nat_min():
    s = Scale.build_scale(Note('C', 5, 'b'), 'natural minor')
    expected = [
        Note('C', 5, 'b'),
        Note('D', 5, 'b'),
        Note('E', 5, 'bb'),
        Note('F', 5, 'b'),
        Note('G', 5, 'b'),
        Note('A', 5, 'bb'),
        Note('B', 5, 'bb'),
        Note('C', 6, 'b')
    ]
    assert s == expected