import numpy as np

from asr.frontend.preprocessing.normalize import normalize


def test_peak_becomes_one():
    signal = 0.2 * np.sin(np.linspace(0, 20, 1_000))
    assert np.abs(normalize(signal)).max() == 1.0


def test_same_word_at_different_volumes_matches():
    signal = np.sin(np.linspace(0, 20, 1_000))
    np.testing.assert_allclose(normalize(0.1 * signal), normalize(0.8 * signal))


def test_silence_unchanged():
    np.testing.assert_array_equal(normalize(np.zeros(100)), np.zeros(100))
