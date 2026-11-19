"""Carga de MSWC en español (formato WAV) desde Hugging Face."""

import io
from pathlib import Path

import numpy as np
import soundfile as sf
from datasets import Audio, load_dataset

REPO_ID = "MLCommons/ml_spoken_words"
CONFIG = "es_wav"
# La caché va dentro del proyecto (data/cache, ignorada por git) y no en ~/.cache.
CACHE_DIR = Path(__file__).resolve().parents[3] / "data" / "cache"


def load_mswc(split="train", streaming=True, cache_dir=CACHE_DIR):
    """Devuelve un split de MSWC en español con el audio sin decodificar.

    split: "train", "validation" o "test".
    streaming: True lee los .tar.gz al vuelo sin guardarlos; False descarga el split entero a `cache_dir`.
    """
    dataset = load_dataset(
        REPO_ID,
        CONFIG,
        split=split,
        streaming=streaming,
        trust_remote_code=True,
        cache_dir=str(cache_dir),
    )
    return dataset.cast_column("audio", Audio(decode=False))


def decode_audio(example) -> tuple[np.ndarray, int]:
    """Decodifica el WAV de un ejemplo: devuelve (señal de forma (muestras, canales), frecuencia de muestreo)."""
    signal, sample_rate = sf.read(io.BytesIO(example["audio"]["bytes"]), always_2d=True)
    return signal, sample_rate
