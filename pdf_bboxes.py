import argparse
import os
from helper import extract_chars, group_chars_into_words, convert_words_csv_to_json, populate_boxes_on_pdf, create_csv_file

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, dest='input', required=True, help="Path of a PDF file.")
parser.add_argument('--output_format', choices=['json','csv', 'img'], dest='output_format', required=True, help="'json' for JSON, 'csv' for CSV, 'img' for images with bounding boxes; for all the pages of PDF.")
parser.add_argument('--output_folder', type=str, dest='output_folder', required=True, help="Output folder path.")

args = parser.parse_args()
filepath = args.input
output_dir = args.output_folder

#extracting filename from filepath
file_start_pos = filepath.rfind("/")
filename = filepath[file_start_pos+1:]

#creating output directory if does not exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
char_output_dir = "char_output_dir/"
words_output_dir = "words_output_dir/"
if not os.path.exists(char_output_dir):
    os.makedirs(char_output_dir)
if not os.path.exists(words_output_dir):
    os.makedirs(words_output_dir)

#extracting characters from pdf
file_start_pos = filepath.rfind("/")
char_filename = filepath[file_start_pos+1:]
char_filepath = extract_chars(filepath, char_filename)

#joining characters to make words
file_start_pos = char_filepath.rfind("/")
word_filename = char_filepath[file_start_pos+1:]
word_filepath = group_chars_into_words(char_filepath, word_filename)

#parsing result into a python list to make a JSON like structure
result = convert_words_csv_to_json(filepath, word_filepath)


if args.output_format == 'img':
	#testing the above structure to populate bounding boxes on pdf pages
	populate_boxes_on_pdf(filepath, word_filename, result, output_dir)
elif args.output_format == 'json':
	#writing result in a file
	file_start_pos = word_filepath.rfind("/")
	word_filename = word_filepath[file_start_pos+1:]
	f = open(output_dir+word_filename+".json","w+")
	f.write(str(result))
	f.close()
elif args.output_format == 'csv':
	#create a csv file
	create_csv_file(result, output_dir+filename)
