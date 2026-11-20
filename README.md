# Reconocimiento de palabras aisladas en español

Sistema que reconoce palabras sueltas en español, construido módulo a módulo:

**preprocesamiento → características (MFCC, log-mel) → modelo acústico (DTW, HMM-GMM, MLP) → decodificador → evaluación (WER, WRR, accuracy)**

## Datos

- [MSWC](https://huggingface.co/datasets/MLCommons/ml_spoken_words) en español (`es_wav`), leído en streaming desde Hugging Face.
- Grabaciones propias del equipo.

## Instalación

Requiere [uv](https://docs.astral.sh/uv/) y Python 3.12.

```bash
uv sync
uv run --group dev pytest
```

## Estado

- [x] Preprocesamiento: mono, offset DC, remuestreo a 16 kHz, normalización
- [ ] Preprocesamiento: ruido
- [ ] Características
- [ ] Modelos acústicos
- [ ] Decodificador
- [ ] Evaluación
