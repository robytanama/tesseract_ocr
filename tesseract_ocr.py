# Library imports
import cv2
import pytesseract
import numpy as np
from pdf2image import convert_from_path

# Self-defined classes imports
import preprocessor
import imageboxer

# Converting PDF to PNG when necessary
pages = convert_from_path('documents/Invoice.pdf')
image_counter = 1

# In the case of multiple pages
for page in pages:
    filename = "page_" + str(image_counter) + ".png"
    page.save('images/' + filename, 'PNG')
    image_counter = image_counter + 1

# Initialize tools
img = cv2.imread('images/page_1.png') # Path to image file
pre_processor = preprocessor.preprocessor() # Pre-processor
image_boxer = imageboxer.imageboxer()

# Process from image to string and print out
preprocessed_image = pre_processor.pre_process(img)
boxed_image = image_boxer.box_image(img)
output = pytesseract.image_to_string(preprocessed_image)
print(output)

# Save preprocessed images for debugging
cv2.imwrite("generated/preprocessed_image.png", preprocessed_image)
cv2.imwrite("generated/boxed_image.png", boxed_image)
cv2.waitKey(0)