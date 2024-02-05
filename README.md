# Text Extractor Snipping Tool

A snipping tool app that extracts text from screenshots using PyQt5 and Pytesseract. This application allows you to select a portion of your screen and automatically extracts any text within that area, making it an invaluable tool for quickly capturing and utilizing text from any application or website.

## Prerequisites

You need to have Python 3.6 or higher. You'll also need to install Tesseract, an OCR engine used by Pytesseract to extract text from images.

## Installing [pytesseract](https://pyimagesearch.com/2021/08/16/installing-tesseract-pytesseract-and-python-ocr-packages-on-your-system/)

Tesseract OCR needs to be installed separately as it's an external dependency used by the Pytesseract library. Installation instructions vary by operating system:

###Mac

```bash
brew install tesseract
```

### Ubuntu

```bash
`sudo apt install tesseract-ocr`
```

### Windows:

Download the binary [here](https://github.com/UB-Mannheim/tesseract/wiki)

After installing, add the path of the exectuable into `extract_text()` inside `main.py()`
Example: `path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"`

## Setup

Create a virtual environment
```python
`python -m venv venv`
`venv/Scripts/activate`
```

Install libraries
```python
`pip install requirements.txt `
```

## Running
```python
`python main.py`
```

