import numpy as np
import pytest

from asr.frontend.preprocessing.dc_offset import remove_dc


@pytest.mark.parametrize("sample_rate", [16_000, 44_100, 48_000])
def test_removes_offset_and_keeps_voice_band(sample_rate):
    t = np.arange(sample_rate) / sample_rate
    tone = 0.5 * np.sin(2 * np.pi * 200 * t)

    filtered = remove_dc(tone + 0.3, sample_rate)

    assert abs(filtered.mean()) < 1e-3
    # Incluye los extremos: el relleno evita que el transitorio deforme el clip.
    assert np.abs(filtered - tone).max() < 0.05
