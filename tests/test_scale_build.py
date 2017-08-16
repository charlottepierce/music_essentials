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
# Test building of natural minor scales