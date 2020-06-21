from PIL import Image
import sys
import os

#grab the first and second arguement with sys

input_folder = sys.argv[1]
output_folder = sys.argv[2]

#check if new exist or # NOTE:

if os.path.exists(output_folder) == False:
    os.makedirs(output_folder)

#loop through the folder and convert to png
try:
    for filename in os.listdir(input_folder):
        img = Image.open(f'{input_folder}\\{filename}')

        #to make thumbnails of the pics
        #img.thumbnail((500,500))

        
        clean_name = os.path.splitext(filename)[0]
        img.save(f'{output_folder}\\{clean_name}.png','png')
except Exception as e:
    print(e)
