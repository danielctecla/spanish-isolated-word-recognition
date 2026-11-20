"""Encadena los pasos de preprocesamiento."""

import numpy as np

from asr.frontend.preprocessing.dc_offset import remove_dc
from asr.frontend.preprocessing.mono import to_mono
from asr.frontend.preprocessing.normalize import normalize
from asr.frontend.preprocessing.resample import TARGET_SAMPLE_RATE, resample


def preprocess(signal: np.ndarray, sample_rate: int, target_sr: int = TARGET_SAMPLE_RATE) -> tuple[np.ndarray, int]:
    """Mono -> quitar offset DC -> remuestrear -> normalizar. Devuelve (señal, frecuencia de muestreo)."""
    signal = to_mono(signal)
    signal = remove_dc(signal, sample_rate)
    signal = resample(signal, sample_rate, target_sr)
    signal = normalize(signal)
    return signal, target_sr
