"""Eliminación del offset DC con un pasa-altas."""

import numpy as np
from scipy.signal import butter, sosfiltfilt

CUTOFF_HZ = 20.0
ORDER = 4
# El transitorio de un pasa-altas a 20 Hz dura ~50 ms. Con el relleno por defecto de scipy
# (unas pocas muestras) deformaría los extremos de clips de 1 s, así que se rellenan 100 ms.
PAD_SECONDS = 0.1


def remove_dc(signal: np.ndarray, sample_rate: int, cutoff_hz: float = CUTOFF_HZ, order: int = ORDER) -> np.ndarray:
    """Pasa-altas Butterworth de fase cero: quita el DC y las derivas lentas sin desplazar la señal.

    El corte de 20 Hz queda por debajo de la voz (la F0 masculina empieza en ~80 Hz). Al filtrar
    hacia delante y hacia atrás, la atenuación en `cutoff_hz` es de -6 dB en lugar de -3 dB.
    """
    signal = np.asarray(signal, dtype=np.float64)
    sos = butter(order, cutoff_hz, btype="highpass", fs=sample_rate, output="sos")
    padlen = min(len(signal) - 1, int(PAD_SECONDS * sample_rate))
    return sosfiltfilt(sos, signal, padlen=padlen)
