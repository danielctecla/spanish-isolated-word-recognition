"""Conversión a mono."""

import numpy as np


def to_mono(signal: np.ndarray) -> np.ndarray:
    """Promedia los canales de una señal (muestras, canales). Una señal 1-D se devuelve tal cual."""
    signal = np.asarray(signal, dtype=np.float64)
    if signal.ndim == 1:
        return signal
    if signal.ndim == 2:
        return signal.mean(axis=1)
    raise ValueError(f"se esperaba una señal 1-D o (muestras, canales), no de {signal.ndim} dimensiones")
