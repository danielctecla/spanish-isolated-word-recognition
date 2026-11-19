"""Remuestreo a 16 kHz con filtro anti-aliasing."""

from math import gcd

import numpy as np
from scipy.signal import resample_poly

TARGET_SAMPLE_RATE = 16_000


def resample(signal: np.ndarray, orig_sr: int, target_sr: int = TARGET_SAMPLE_RATE) -> np.ndarray:
    """Cambia la frecuencia de muestreo de `orig_sr` a `target_sr`.

    Quedarse con 1 de cada 3 muestras de 48 kHz doblaría hacia abajo todo lo que hay por encima de
    8 kHz (aliasing). resample_poly aplica antes un pasa-bajas FIR con corte en el Nyquist de la
    frecuencia destino (8 kHz para 16 kHz), así que el anti-aliasing va incluido.
    """
    signal = np.asarray(signal, dtype=np.float64)
    if orig_sr == target_sr:
        return signal
    divisor = gcd(orig_sr, target_sr)
    return resample_poly(signal, target_sr // divisor, orig_sr // divisor)
