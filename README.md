# CDIT_Team2_Internship

# OCR for Malayalam Characters

This project focuses on developing an Optical Character Recognition (OCR) system for recognizing both **handwritten** and **printed** Malayalam text from scanned PDF documents. The work is split into two parts:

1. **OCR for Handwritten Malayalam Characters**
2. **OCR for Printed Malayalam and English Text**

---

## 🔍 Project Overview

### 1. OCR for Handwritten Malayalam Characters

This module focuses on recognizing individual Malayalam characters from handwritten inputs. Key stages in this pipeline include:

- **Document Preprocessing**
- **Text Segmentation**
- **Character Recognition using Deep Learning**

#### Highlights:
- Achieved **91% accuracy** at the character level.
- Word/sentence recognition is feasible only with consistent spacing.
- Built a minimalistic and scalable OCR system for handwritten character-level recognition.
- Paves the way for digitization and automated data entry from handwritten documents.

---

### 2. OCR for Printed Malayalam and English Text

This module deals with the recognition of printed Malayalam (and English) text from scanned PDFs using a hybrid approach combining:

- **Tesseract OCR**
- **Deep Learning-based Preprocessing Techniques**

#### Key Techniques:
- PDF to Image conversion
- Grayscale and binary image preprocessing
- Multi-threaded and language-optimized OCR execution

#### Highlights:
- Parallelized OCR pipeline to enhance performance
- Improved recognition accuracy over traditional OCR tools
- Effective for multilingual documents

---

## 🛠️ Tech Stack

- **Python**
- **OpenCV**
- **Tesseract OCR**
- **TensorFlow / Keras**
- **Pillow**
- **NumPy**
- **PDF2Image**
- **Matplotlib** (for visualization)

---

## 🚀 Features

- Robust recognition of handwritten Malayalam characters
- Dual-language OCR system for printed Malayalam and English
- Optimized for document digitization workflows
- Scalable and minimalistic system architecture

---

## 📂 Project Structure
📦 CDIT_Team2_Internship/
  **├── handwritten_ocr/ 🌿 main**
  **│   ├── Code/**
  **│   ├── Dataset/**
  **│   ├── model/**
  **│   ├── Testing the Model/**
  **│   └── README.md**
  **└── printed_ocr/ 🌿 Printed-Documents**
      **├── main.py**
      **└── README.md**
