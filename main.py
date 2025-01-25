import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import logging
import os
from concurrent.futures import ThreadPoolExecutor

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def preprocess_image(image):
    """Preprocess image to improve OCR accuracy (e.g., convert to grayscale)."""
    return image.convert('L')  # Convert to grayscale

def perform_ocr_on_page(image, lang):
    """Perform OCR on a single page."""
    try:
        preprocessed_image = preprocess_image(image)
        return pytesseract.image_to_string(preprocessed_image, lang=lang)
    except Exception as e:
        logging.error(f"Error during OCR on page: {e}")
        return ""

def ocr_from_scanned_pdf(file_path, lang='eng', page_range=None):
    try:
        logging.info(f"Converting PDF to images: {file_path}")
        images = convert_from_path(
            file_path,
            first_page=page_range[0] if page_range else None,
            last_page=page_range[1] if page_range else None
        )

        logging.info(f"Performing OCR on {len(images)} pages.")
        text = ""

        with ThreadPoolExecutor() as executor:
            ocr_results = executor.map(lambda img: perform_ocr_on_page(img, lang), images)
            text = "\n".join(ocr_results)

        return text
    except Exception as e:
        logging.error(f"Error during OCR process: {e}")
        return None

def save_text_to_file(text, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(text)
        logging.info(f"Text successfully saved to {output_file}")
    except Exception as e:
        logging.error(f"Error while saving text to file: {e}")

# Example usage
if __name__ == "__main__":
    file_path = r'D:\development\CDIT_Project\img14.pdf'  # Replace with your PDF file path
    lang = 'eng+mal'
    page_range = (1, 3)  # Example page range, adjust as needed

    # Perform OCR and get the extracted text
    text = ocr_from_scanned_pdf(file_path, lang=lang, page_range=page_range)
    
    if text:
        # Save the extracted text to a text file
        output_file = r'D:\development\CDIT_Project\output.txt'  # Adjust the path as needed
        save_text_to_file(text, output_file)
    else:
        logging.error("OCR process failed.")