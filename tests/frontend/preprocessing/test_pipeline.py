import numpy as np

from asr.frontend.preprocessing.pipeline import preprocess


def test_stereo_48k_with_offset():
    t = np.arange(48_000) / 48_000
    voice = 0.5 * np.sin(2 * np.pi * 300 * t)
    stereo = np.column_stack([voice + 0.2, voice + 0.4])

    signal, sample_rate = preprocess(stereo, 48_000)

    assert sample_rate == 16_000
    assert signal.shape == (16_000,)
    assert abs(signal.mean()) < 1e-3
