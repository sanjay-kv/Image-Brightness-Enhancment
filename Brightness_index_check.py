import os
from PIL import Image, ImageStat
import numpy as np
import requests
from io import BytesIO
import math
import openpyxl

def calculate_brightness(image_path):
    # read image
    original_image = Image.open(image_path)

    # calculate brightness index
    brightness_index = ImageStat.Stat(original_image).mean[0]
    return brightness_index

# input directory
input_dir = 'input'

# create Excel workbook and sheet
wb = openpyxl.Workbook()
ws = wb.active

# add header row
ws.append(["Filename", "Brightness"])

# get list of input filenames
input_filenames = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]

# iterate over input images
for i, filename in enumerate(input_filenames):
    try:
        # calculate brightness
        brightness = calculate_brightness(os.path.join(input_dir, filename))
        
        # append filename and brightness to Excel sheet
        ws.append([filename, brightness])
        
        # print filename and brightness
        print("Filename:", filename)
        print("Brightness:", brightness)
        print("------------------------------------")
    except:
        # print error message
        print("Error processing file:", filename)

# save Excel workbook
wb.save("brightness.xlsx")
