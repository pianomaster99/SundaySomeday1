from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

PIXEL_THRESHOLD = 130

def clean_image_data(image_data):
    for i in range(len(image_data)):
        for j in range(len(image_data[i])):
            image_data[i][j] = 255 - image_data[i][j]
            if image_data[i][j] < PIXEL_THRESHOLD:
                image_data[i][j]= 0

def jpg_to_64x64(filename):
    image_data = Image.open(filename)
    image_data = image_data.convert("L")
    image_data = image_data.resize((64, 64))
    image_data = np.array(image_data)
    image_data = np.rot90(image_data, k=-1)
    clean_image_data(image_data)
    return image_data