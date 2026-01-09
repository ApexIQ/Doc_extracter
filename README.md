# Docling Document Extractor

A FastAPI-based application that extracts layout, tables, and content from documents (PDFs) using native [Docling](https://github.com/DS4SD/docling) features.

## Features

- **Advanced Table Extraction**: Uses `TableFormer` in `ACCURATE` mode for high-fidelity table structure recognition.
- **OCR Support**: Built-in OCR for scanned documents and images.
- **Image Analysis**: Automatic classification and description of figures and images.
- **Markdown Export**: Converts documents to Markdown with embedded table structures and image captions.
- **Structured Data**: Provides access to the underlying structured data model of the document.

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd Doc_extracter
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Open `.env` and configure your credentials if using cloud-based features (e.g., specific enrichment services).
   *Note: logic for loading `.env` is not currently in `main.py`, so you may need to export these variables in your shell or use `python-dotenv` if required by underlying libraries.*

## Usage

### Starting the Server

Run the FastAPI server using `uvicorn`:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

### Using the Client

A simple client script is provided to test the extraction:

```bash
python client_example.py <path_to_document.pdf>
```

**Example:**
```bash
python client_example.py sample.pdf
```

### API Documentation

#### `POST /extract`

Extracts content from an uploaded document.

- **Request**: `multipart/form-data` with a `file` field.
- **Response**: JSON object containing:
  - `markdown`: The extracted text in Markdown format.
  - `structured_data`: The raw structured data from Docling.

Visit `http://127.0.0.1:8000/docs` for the interactive Swagger UI.
