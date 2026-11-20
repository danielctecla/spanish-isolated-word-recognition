"""Normalización de la señal."""

import numpy as np

TARGET_PEAK = 1.0


def normalize(signal: np.ndarray, target_peak: float = TARGET_PEAK) -> np.ndarray:
    """Escala la señal para que su pico absoluto valga `target_peak`.

    Así la misma palabra dicha más fuerte o más bajo, o grabada con otro micrófono, queda en la
    misma escala. Una señal en silencio total se devuelve tal cual.
    """
    signal = np.asarray(signal, dtype=np.float64)
    peak = np.abs(signal).max(initial=0.0)
    if peak == 0:
        return signal
    return signal * (target_peak / peak)
