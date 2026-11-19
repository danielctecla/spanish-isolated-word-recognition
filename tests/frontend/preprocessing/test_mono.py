import numpy as np
import pytest

from asr.frontend.preprocessing.mono import to_mono


def test_stereo_averages_channels():
    stereo = np.column_stack([np.full(100, 1.0), np.full(100, 3.0)])
    np.testing.assert_allclose(to_mono(stereo), np.full(100, 2.0))


def test_mono_unchanged():
    signal = np.linspace(-1, 1, 100)
    np.testing.assert_array_equal(to_mono(signal), signal)


def test_rejects_3d():
    with pytest.raises(ValueError):
        to_mono(np.zeros((10, 2, 2)))
