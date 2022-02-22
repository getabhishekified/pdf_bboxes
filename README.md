# Welcome to pdf_bboxes!

Hi! This is a **ubuntu** based python CLI program which takes a **PDF** as an input and provides bounding boxes over each word on all pages of the PDF in **json**, **csv**, and **image representation** of bboxes drawn over words with recognized 'text'. 

**Note:** This program only accepts 'Text PDFs' and not 'Image or Scanned PDFs'. It currently works on Ubuntu only. 

## Usage 
This program can be used on any computer-generated PDFs, be it **Invoices**, **Research Papers**, **e-books**, etc. Its output can be used to make datasets for machine learning algorithms like GCN (Graph Convolutional Network) or other ML algorithms. 

![Sample Output](/output/sample1.pdf_chars.csv-0.jpg)

## Installation (Ubuntu)

    pip3 install -r requirements.txt
    apt-get install poppler-utils

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

    python3 pdf_bboxes.py --input '/home/gautam/Desktop/python/ocr/input/sample.pdf' --output_format 'json' --output_folder '/home/gautam/Desktop/python/ocr/output/'

To get output as a CSV file :

    python3 pdf_bboxes.py --input '/home/gautam/Desktop/python/ocr/input/sample.pdf' --output_format 'csv' --output_folder '/home/gautam/Desktop/python/ocr/output/'

To get output as Images of each page of the PDF having  bounding boxes over each word and recognized text over the bounding boxes :

    python3 pdf_bboxes.py --input '/home/gautam/Desktop/python/ocr/input/sample.pdf' --output_format 'img' --output_folder '/home/gautam/Desktop/python/ocr/output/'

Output JSON file and Images will be found in the **output_folder** you passed as an argument.


Blog - https://www.devzoneoriginal.com/2021/01/draw-bounding-boxes-over-each-word-on.html
