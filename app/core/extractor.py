import logging
from pathlib import Path
from typing import Any, Dict

from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions, TableFormerMode
from docling.datamodel.document import DoclingDocument

logger = logging.getLogger(__name__)

class DoclingExtractor:
    """
    A class to handle document extraction using the docling library.
    Configured to use native AI features for layout and image understanding.
    """

    def __init__(self):
        # Configure pipeline options for PDF processing
        pipeline_options = PdfPipelineOptions()
        
        # 1. Table Structure: Set to Accurate mode to ensure tables are preserved well.
        pipeline_options.do_table_structure = True
        pipeline_options.table_structure_options.mode = TableFormerMode.ACCURATE
        
        # 2. OCR: Enabled for scanned content.
        pipeline_options.do_ocr = True 
        
        # 3. Native Enrichment Features (per user request)
        # These use docling's internal models (e.g., for classifying figures and describing images)
        pipeline_options.do_picture_classification = True
        pipeline_options.do_picture_description = True
        
        # Note: export_to_markdown() by default handles tables and enriched image captions.

        self.converter = DocumentConverter(
            format_options={
                InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
            }
        )

    def process_document(self, file_path: Path) -> Dict[str, Any]:
        """
        Process a document and return its extracted content and structure.
        """
        try:
            logger.info(f"Starting conversion for: {file_path}")
            
            # The conversion process includes layout analysis, OCR, and picture description.
            result = self.converter.convert(file_path)
            doc: DoclingDocument = result.document
            
            # Export to Markdown: 
            # This will include tables in markdown format and image descriptions as text.
            markdown_content = doc.export_to_markdown()
            
            # Export basic structured data (dict)
            structured_data = doc.export_to_dict()
            
            return {
                "markdown": markdown_content,
                "structured_data": structured_data
            }

        except Exception as e:
            logger.error(f"Error processing document {file_path}: {e}")
            raise e
