# Docling Pipeline Options Reference

This document provides a comprehensive list of the `PdfPipelineOptions` available in Docling to customize the conversion process.

## Core Options

| Option | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `do_ocr` | `bool` | `True` | Enables OCR for scanned pages or images. |
| `do_table_structure` | `bool` | `True` | Enables advanced table structure recognition (TableFormer). |
| `do_code_enrichment` | `bool` | `False` | Enables advanced parsing and language detection for code blocks. |
| `do_formula_enrichment` | `bool` | `False` | Analyzes formulas and extracts them as LaTeX. |
| `do_picture_classification` | `bool` | `False` | Classifies images (e.g., as a chart, diagram, or photo). |
| `do_picture_description` | `bool` | `False` | Generates text descriptions/captions for images. |
| `generate_picture_images` | `bool` | `False` | Renders and saves the actual image bits from the PDF (required for enrichment). |

## OCR Configuration (`ocr_options`)

- **Pluggable Engines**: You can choose between `EasyOcrOptions`, `TesseractOcrOptions`, or `RapidOcrOptions`.
- **`force_full_page_ocr`**: Set to `True` to ignore existing text layers and OCR everything (useful for problematic PDFs).

## Table Extraction (`table_structure_options`)

| Option | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `mode` | `TableFormerMode` | `FAST` | `FAST` for speed, `ACCURATE` for high-fidelity extraction of complex tables. |
| `do_cell_matching` | `bool` | `True` | Matches recognized table cells back to the underlying PDF characters. |

## Advanced & Hardware

- **`accelerator_options`**: Configuration for GPU (CUDA/MPS) or CPU optimization settings.
- **`enable_remote_services`**: `bool` (Default: `False`). Set to `True` if you use external API-based plugins.
- **`artifacts_path`**: Path to pre-downloaded model weights (useful for offline/air-gapped environments).
- **`batch_size`**: Number of pages processed in parallel.
- **`scale`**: Scaling factor for rendering pages (default usually 2.0).
- **`picture_area_threshold`**: Minimum area for an element to be considered a "picture".

## Usage in `extractor.py`

In your current implementation, we have enabled:
- `do_table_structure` (Mode: `ACCURATE`)
- `do_ocr`
- `generate_picture_images` (To enable our Cloudflare enrichment feature)
