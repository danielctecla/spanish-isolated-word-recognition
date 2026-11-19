# Reconocimiento de palabras aisladas en español

Sistema de reconocimiento de voz construido por módulos, uno detrás de otro.

## Pipeline

```
Corpus público (MSWC es) ─┐
Dataset propio (equipo) ──┤
                          ▼
        Parte frontal acústica
          Preprocesamiento: 16 kHz, ruido, normalizar
          ├─ MFCC + Δ + ΔΔ
          └─ Log-mel
                          ▼
        Modelo acústico P(O|W):  DTW · HMM-GMM · MLP
                          ▼
  Léxico ──►  Decodificador argmax P(O|W)·P(W)  ◄── Modelo de lenguaje (uniforme)
                          ▼
        Evaluación: WER, WRR, accuracy
```

## Estructura

| Ruta | Contenido |
|---|---|
| `data/raw/mswc_es/` | Corpus público MSWC en español (sin modificar) |
| `data/raw/own/` | Grabaciones del equipo (sin modificar) |
| `data/processed/` | Audio preprocesado (16 kHz, sin ruido, normalizado) |
| `data/features/mfcc/`, `data/features/logmel/` | Características extraídas |
| `data/splits/` | Particiones train / val / test |
| `src/asr/data/` | Carga de los dos corpus |
| `src/asr/frontend/preprocessing/` | Remuestreo, ruido, normalización |
| `src/asr/frontend/features/` | MFCC + Δ + ΔΔ y log-mel |
| `src/asr/acoustic_models/` | `dtw/`, `hmm_gmm/`, `mlp/` |
| `src/asr/lexicon/` | Lista de las N palabras |
| `src/asr/language_model/` | P(W) |
| `src/asr/decoder/` | argmax P(O\|W)·P(W) |
| `src/asr/evaluation/` | WER, WRR, accuracy |
| `configs/` | Parámetros de cada módulo |
| `scripts/` | Puntos de entrada (ejecutar cada etapa) |
| `notebooks/` | Exploración y análisis |
| `tests/` | Pruebas, con la misma estructura que `src/asr/` |
| `models/` | Modelos entrenados |
| `reports/` | Resultados y figuras |
| `docs/` | Documentación |

## Uso

Requiere [uv](https://docs.astral.sh/uv/). El proyecto usa Python 3.12 porque MSWC se carga con un script de Hugging Face que solo funciona con `datasets<4`.

```bash
uv sync                     # crea .venv e instala dependencias
uv run --group dev pytest   # pruebas
```

MSWC (`MLCommons/ml_spoken_words`, configuración `es_wav`) se lee en streaming por defecto, sin guardarlo en disco. Si se descarga (`streaming=False`), la caché va a `data/cache/` (~15 GB comprimidos el español completo).

## Estado

- [ ] Preprocesamiento: ~~mono~~, ~~offset DC~~, ~~16 kHz~~, ruido, normalizar
- [ ] Extracción de características
- [ ] Modelos acústicos
- [ ] Léxico, modelo de lenguaje y decodificador
- [ ] Evaluación
