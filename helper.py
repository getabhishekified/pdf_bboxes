import subprocess as subp
import csv
from pdf2image import convert_from_path
import cv2
import numpy as np
from PyPDF2 import PdfFileReader

char_output_dir = "char_output_dir/"
words_output_dir = "words_output_dir/"

def extract_chars(filepath, filename):
	output_filepath = char_output_dir+filename+"_chars.csv"
	pdfplumber_cmd = "pdfplumber --types char < '"+filepath+"' > '"+output_filepath+"'"
	subp.check_call(pdfplumber_cmd, shell=True)
	return output_filepath

def group_chars_into_words(filepath, filename):
	output_filepath = words_output_dir+filename+"_words.csv"
	coalesce_cmd = "python coalesce_words.py '"+filepath+"' > '"+output_filepath+"'"
	subp.check_call(coalesce_cmd, shell=True)
	return output_filepath

def convert_words_csv_to_json(pdf_filepath, words_csv_filepath):
	#reading PDF Pages
	fp = open(pdf_filepath, 'rb')
	pdf = PdfFileReader(fp)

	with open(words_csv_filepath) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		output_list = []
		line_count = 0
		page_number = '1'
		bboxes_list=[]
		for row in csv_reader:
			if line_count > 0:
				if page_number == row[3]:
					scaleFactor = 2.777
					bbox_dict = {
					"word" : row[5],
					"startX" : (float(row[13])) * scaleFactor,
					"startY" : (float(pdf.getPage(int(page_number)-1).mediaBox[3]) - float(row[11])) * scaleFactor,
					"endX" : (float(row[14]) + 1) * scaleFactor,
					"endY" : (float(pdf.getPage(int(page_number)-1).mediaBox[3]) - float(row[12])) * scaleFactor
					}
				else:
					#inserting page details
					page_dict = {
						"page_no" : page_number,
						"bboxes" : bboxes_list,
						"image_url": "todo"
					}
					output_list.append(page_dict)

					#initializing for new page
					bboxes_list=[]
					page_number = row[3]

					scaleFactor = 2.777
					bbox_dict = {
					"word" : row[5],
					"startX" : (float(row[13])) * scaleFactor,
					"startY" : (float(pdf.getPage(int(page_number)-1).mediaBox[3]) - float(row[11])) * scaleFactor,
					"endX" : (float(row[14]) + 1) * scaleFactor,
					"endY" : (float(pdf.getPage(int(page_number)-1).mediaBox[3]) - float(row[12])) * scaleFactor
					}
				bboxes_list.append(bbox_dict)

			line_count += 1

		#inserting last page details
		page_dict = {
					"page_no" : page_number,
					"bboxes" : bboxes_list,
					"image_url": "todo"
				}
		output_list.append(page_dict)

		return output_list

def populate_boxes_on_pdf(filepath, filename, result, img_output_dir):
	images = convert_from_path(filepath)

	for page in result:
		page_no = int(page["page_no"]) - 1

		image = images[page_no]
		image = np.uint8(image)

		bboxes = page["bboxes"]
		for bbox in bboxes:
			x0 = int(float(bbox["startX"]))
			y0 = int(float(bbox["startY"]))
			x1 = int(float(bbox["endX"]))
			y1 = int(float(bbox["endY"]))
			# drawing bboxes over each word
			image = cv2.rectangle(image, (int(x0),int(y0)), (int(x1),int(y1)), (0, 255, 0), 1)

			# writing text on image
			# font 
			font = cv2.FONT_HERSHEY_SIMPLEX 
			# fontScale
			fontScale = 0.5
			# Blue color in BGR 
			color = (255, 0, 0) 
			# Line thickness of 2 px 
			thickness = 1
			# Using cv2.putText() method 
			image = cv2.putText(image, bbox["word"], (x0,y0-6), font,  
							   fontScale, color, thickness, cv2.LINE_AA) 

		cv2.imwrite(img_output_dir+"/"+filename+"-"+str(page_no)+".jpg", image)

def create_csv_file(result, csv_out_filepath):
	for page in result:
		page_no = int(page["page_no"]) - 1
		bboxes = page["bboxes"]

		#csv params
		rows = []

		for bbox in bboxes:
			xmin = int(float(bbox["startX"]))
			ymin = int(float(bbox["startY"]))
			xmax = int(float(bbox["endX"]))
			ymax = int(float(bbox["endY"]))
			Object = bbox["word"]

			row = [xmin, ymin, xmax, ymax, Object]
			rows.append(row)
		
		#writing into the csv file
		with open(csv_out_filepath+str(page_no)+".csv", 'w+') as csv_file:
				fieldnames = ['xmin', 'ymin', 'xmax', 'ymax', 'Object']
				writer = csv.writer(csv_file)
				writer.writerow(fieldnames)
				writer.writerows(rows)
				csv_file.close()