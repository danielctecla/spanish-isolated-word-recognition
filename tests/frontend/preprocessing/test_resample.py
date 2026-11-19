import numpy as np
import pytest

from asr.frontend.preprocessing.resample import resample


def rms(x):
    return np.sqrt(np.mean(x**2))


def tone(freq, sample_rate):
    return np.sin(2 * np.pi * freq * np.arange(sample_rate) / sample_rate)


@pytest.mark.parametrize("orig_sr", [8_000, 22_050, 44_100, 48_000])
def test_one_second_becomes_16000_samples(orig_sr):
    assert len(resample(np.zeros(orig_sr), orig_sr)) == 16_000


def test_same_rate_unchanged():
    signal = tone(1_000, 16_000)
    np.testing.assert_array_equal(resample(signal, 16_000), signal)


def test_keeps_voice_band():
    assert rms(resample(tone(1_000, 48_000), 48_000)) == pytest.approx(rms(tone(1_000, 48_000)), rel=0.01)


def test_anti_aliasing():
    # Un tono de 12 kHz no cabe a 16 kHz (Nyquist = 8 kHz).
    high = tone(12_000, 48_000)
    # Quedarse con 1 de cada 3 muestras lo dobla a 4 kHz con toda su energía...
    assert rms(high[::3]) == pytest.approx(rms(high), rel=0.01)
    # ...mientras que el pasa-bajas previo lo elimina.
    assert rms(resample(high, 48_000)) < 0.01 * rms(high)
