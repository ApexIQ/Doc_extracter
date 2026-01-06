import shutil
import os
from pathlib import Path
from tempfile import NamedTemporaryFile
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse

from app.core.extractor import DoclingExtractor

app = FastAPI(
    title="Docling Document Extractor", 
    description="API to extract layout and content from documents using native Docling features."
)

# Initialize the extractor
extractor = DoclingExtractor()

@app.post("/extract")
async def extract_document(file: UploadFile = File(...)):
    """
    Endpoint to extract content from an uploaded document.
    
    Returns:
    - JSON object containing 'markdown' text (with tables) and 'structured_data'.
    """
    temp_file_path = None
    try:
        # 1. Save upload file to a temporary file
        suffix = Path(file.filename).suffix
        with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(file.file, tmp)
            temp_file_path = Path(tmp.name)
        
        # 2. Process the document
        result = extractor.process_document(temp_file_path)
        
        return JSONResponse(content=result)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        # 3. Cleanup
        if temp_file_path and temp_file_path.exists():
            os.remove(temp_file_path)

@app.get("/")
def read_root():
    return {"message": "Docling Extractor API is running. use /extract to process documents."}
