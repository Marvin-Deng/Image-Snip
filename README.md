# Text Extractor Snipping Tool

A snipping tool app that extracts text from screenshots using PyQt5 and Pytesseract. This application allows you to select a portion of your screen and automatically extracts any text within that area, making it an invaluable tool for quickly capturing and utilizing text from any application or website.

## Usage Instructions
- Clicking `Capture` loads the snipping tool. Drag it across the section of your screen you want to capture. This automatically saves the image into `test.png` and copies it into your clipboard.
- Clicking `Save` allows you to save the image into a folder.
- Clicking `Extract` will display the text from the image underneath the buttons. This will extract the text from any image named `test.png` in your project's root directory.

## Prerequisites

You need to have Python 3.6 or higher. You'll also need to install Tesseract, an OCR engine used by Pytesseract to extract text from images.

## Installing [Pytesseract](https://pyimagesearch.com/2021/08/16/installing-tesseract-pytesseract-and-python-ocr-packages-on-your-system/)

Tesseract OCR needs to be installed separately as it's an external dependency used by the Pytesseract library. Installation instructions vary by operating system:

### Mac

```bash
brew install tesseract
```

### Ubuntu

```bash
sudo apt install tesseract-ocr
```

### Windows:

Download the binary [here](https://github.com/UB-Mannheim/tesseract/wiki)

After installing, make sure to add the path of the exectuable into `extract_text()` inside `main.py()`

Example: `path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"`

## Setup

Create a virtual environment
```python
python -m venv venv
venv/Scripts/activate
```

Install libraries
```python
pip install requirements.txt 
```

## Running
```python
python main.py
```

