#!/usr/bin/env python3
# The code is ugly but functional, didnt have the time for a cleanup :/
import zipfile
import subprocess
import os
import sys
from lxml import etree
from PIL import Image
from io import BytesIO
import shutil
import fitz  # PyMuPDF
import cv2
import numpy as np
from docx import Document


docx_filename = 'Envelope.docx'


def getData(split, string):
    data = input(string)
    if data:
        return split + data
    return ''


def tel(split, string):
    number = getData(split, string).replace(split, '').replace(' ', '')
    if not len(number) or number == '':
        return split
    return split + 'Tel-' + number


zin = zipfile.ZipFile (docx_filename, 'r')
zout = zipfile.ZipFile (f'Envelope_new.docx', 'w')
new_buf = ''
for item in zin.infolist():
    buffer = zin.read(item.filename)
    if (item.filename == 'word/document.xml'):
        res = buffer.decode("utf-8")
        split = res.split('Blank')
        new_buf += getData(split[0], 'Enter Receiver Name: ')
        new_buf += getData(split[1], 'Enter Receiver Address: ')
        new_buf += getData(split[2], 'Enter Receiver Secondary Address: ')
        new_buf += getData(split[3], 'Enter Receiver Tertiary Address: ')
        new_buf += getData(split[4], 'Enter Receiver Postal Code and City: ')
        new_buf += getData(split[5], 'Enter Receiver Country: ')
        new_buf += tel(split[6], 'Enter Receiver Phone Number: ')
        new_buf += split[7]
        new_buf += split[8]
        # replace empty lines
        new_buf = new_buf.replace('<w:p><w:pPr><w:pStyle w:val="4"/><w:bidi w:val="0"/><w:rPr><w:sz w:val="28"/><w:szCs w:val="28"/><w:lang w:val="en-US"/></w:rPr></w:pPr><w:r><w:rPr><w:sz w:val="28"/><w:szCs w:val="28"/><w:lang w:val="en-US"/></w:rPr><w:t></w:t></w:r></w:p>', '')
        new_buffer = new_buf.encode("utf-8")
        zout.writestr(item, new_buffer)
    else:
        zout.writestr(item, buffer)
zout.close()
zin.close()

subprocess.run(f'rm {docx_filename}')
subprocess.run(f'mv Envelope_new.docx {docx_filename}')

# Extract stamp from pdf
if len(sys.argv) < 2:
    exit()

pdf = sys.argv[1]


def crop_image_by_pixels(pdf_file_path, output_image_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_file_path)
    # Assuming there is only one page
    page = pdf_document[0]
    # Set the DPI for rendering (adjust as needed)
    dpi = 600  # You can change this to the desired DPI
    # Render the page to an image with the specified DPI
    image = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72))
    # Convert the image to a grayscale Pillow image
    pil_image = Image.frombytes("RGB", [image.width, image.height], image.samples)
    # Convert the grayscale image to a NumPy array
    gray_image = np.array(pil_image.convert("L"))
    # Threshold the image to create a binary mask
    _, binary_mask = cv2.threshold(gray_image, 1, 255, cv2.THRESH_BINARY)
    # Find the coordinates of the outermost black markers
    top, bottom, left, right = None, None, None, None
    # Find top coordinate
    for i in range(binary_mask.shape[0]):
        if np.any(binary_mask[i, :] == 0):
            top = i
            break
    # Find bottom coordinate
    for i in range(binary_mask.shape[0] - 1, -1, -1):
        if np.any(binary_mask[i, :] == 0):
            bottom = i
            break
    # Find left coordinate
    for i in range(binary_mask.shape[1]):
        if np.any(binary_mask[:, i] == 0):
            left = i
            break
    # Find right coordinate
    for i in range(binary_mask.shape[1] - 1, -1, -1):
        if np.any(binary_mask[:, i] == 0):
            right = i
            break
    if top is not None and bottom is not None and left is not None and right is not None:
        # Crop the image to the outer black markers
        cropped_image = gray_image[top+60:bottom-60, left+60:right-60]
        # Save the cropped image as a PNG file
        cv2.imwrite(output_image_path, cropped_image)
        print(f'Saved cropped image as {output_image_path}')
    else:
        print('No outer black markers found.')


image_path = 'stamp.png'
crop_image_by_pixels(pdf, image_path)



# Function to resize an image and return its binary content
def get_image_data(image_path):
    img = Image.open(image_path)
    output_buffer = BytesIO()
    img.save(output_buffer, format="PNG")
    return output_buffer.getvalue()


# Replace image
# Function to update the image in a new DOCX copy
def update_image_in_new_docx(docx_path, image_data):
    with zipfile.ZipFile(docx_path, 'w', zipfile.ZIP_DEFLATED) as new_zip_archive:
        with zipfile.ZipFile(docx_filename, 'r') as orig_zip_archive:
            for item in orig_zip_archive.infolist():
                if item.filename != 'word/media/image2.png':
                    new_zip_archive.writestr(item, orig_zip_archive.read(item.filename))
        new_zip_archive.writestr('word/media/image2.png', image_data)


image_data = get_image_data(image_path)

new_docx_path = "new_Envelope.docx"
update_image_in_new_docx(new_docx_path, image_data)

# Replace the original DOCX file with the new DOCX file
shutil.move(new_docx_path, docx_filename)

print(f'Replaced image in Envelope.docx with the resized image.')

# Resize image
def update_image_properties(docx_file, target_image_index):
    doc = Document(docx_file)

    if 0 <= target_image_index < len(doc.inline_shapes):
        # Get the inline shape at the specified index
        inline_shape = doc.inline_shapes[target_image_index]

        # Get the aspect ratio of the existing image
        existing_image_data = get_image_data(image_path)  # Replace with the actual path to the existing image
        existing_img = Image.open(BytesIO(existing_image_data))
        existing_width, existing_height = existing_img.size
        aspect_ratio = existing_width / existing_height

        # Set the width to 296 pixels and calculate the height based on aspect ratio
        inline_shape.height = 1000000  # Width in EMUs (1 inch = 9144000 EMUs)
        inline_shape.width = int(100 * aspect_ratio * 10000)  # Height in EMUs

        # Save the modified document
        doc.save(docx_file)
        print(f'Updated image properties in {docx_file} for the specified image.')
    else:
        print(f'Invalid image index: {target_image_index}')


update_image_properties(docx_filename, 1)

# Cleanup
subprocess.run(f'rm {image_path}')