"""
Fallback OCR Processor - Works without Tesseract
Returns extracted text or mock data for cloud deployment
"""
import os
import cv2
import numpy as np
from PIL import Image
from typing import Dict

class FallbackOCRProcessor:
    """Fallback OCR that works without system dependencies"""
    
    def __init__(self):
        print("[INFO] Using Fallback OCR Processor (no external dependencies)")
        self.available = True
    
    def is_available(self):
        """Always available - no external dependencies"""
        return True
    
    def get_available_methods(self):
        """Get available methods"""
        return ['fallback']
    
    def extract_text(self, image_path: str, force_method: str = None) -> Dict:
        """
        Extract text from image using fallback method
        In production, this would use an API call or model
        """
        try:
            # Read image to validate it exists
            img = cv2.imread(image_path)
            if img is None:
                return {
                    'text': '',
                    'confidence': 0.0,
                    'method': 'fallback',
                    'error': 'Could not read image file'
                }
            
            # Get image dimensions
            height, width = img.shape[:2]
            
            # Return message indicating OCR service needs setup
            text = (
                "OCR service not available on this deployment.\n\n"
                f"Image details: {width}x{height} pixels\n"
                "Image file loaded successfully.\n\n"
                "To enable text extraction:\n"
                "1. Upgrade to a paid Render instance, or\n"
                "2. Use Google Cloud Vision API (paid), or\n"
                "3. Use OCR.space API (free tier available)\n\n"
                "For demo purposes, upload an image and this message will confirm receipt."
            )
            
            return {
                'text': text,
                'confidence': 0.5,
                'method': 'fallback',
                'text_type': 'system_message',
                'word_count': len(text.split()),
                'image_size': f'{width}x{height}'
            }
            
        except Exception as e:
            return {
                'text': '',
                'confidence': 0.0,
                'method': 'fallback',
                'error': str(e)
            }
    
    def detect_text_type(self, image_path: str) -> str:
        """Detect text type"""
        return 'system'
