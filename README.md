# Welcome to pdf_bboxes!

Hi! This is a python CLI program which takes a **PDF** as an input and provides bounding boxes over each word on all pages of the PDF in a nice and clean **json format**. 

**Note:** This program only accepts 'Text PDFs' and not 'Image or Scanned PDFs'.

## Usage 
This program can be used on any computer-generated PDFs, be it **Invoices**, **Research Papers**, **e-books**, etc. Its output can be used to make datasets for machine learning algorithms like GCN (Graph Convolutional Network) or other ML algorithms. 


## Installation

    pip install -r requirements.txt

## How to run?

In order to run this program, you need to pass 3 mandatory arguments:
```
  --input INPUT         Path of a PDF file.
  --output_format {json,csv,img}
                        'json' for JSON, 'csv' for CSV, 'img' for images with
                        bounding boxes; for all the pages of PDF.
  --output_folder OUTPUT_FOLDER
                        Output folder path.
```

### Syntax/Examples : 

To get output as a JSON file :

    python pdf_bboxes.py --input '/home/gautam/Desktop/python/ocr/SEAGATE.PDF' --output_format 'json' --output_folder '/home/gautam/Desktop/python/ocr/abcd/'

To get output as a CSV file :

    python pdf_bboxes.py --input '/home/gautam/Desktop/python/ocr/SEAGATE.PDF' --output_format 'csv' --output_folder '/home/gautam/Desktop/python/ocr/abcd/'

To get output as Images of each page of the PDF having  bounding boxes over each word and recognized text over the bounding boxes :

    python pdf_bboxes.py --input '/home/gautam/Desktop/python/ocr/SEAGATE.PDF' --output_format 'img' --output_folder '/home/gautam/Desktop/python/ocr/abcd/'

Output JSON file and Images will be found in the **output_folder** you passed as an argument.


Blog - https://www.devzoneoriginal.com/2021/01/draw-bounding-boxes-over-each-word-on.html